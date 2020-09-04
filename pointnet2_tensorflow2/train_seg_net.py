import pickle
import os
import sys
import tensorflow as tf
import numpy as np
from tensorflow import keras
from models.sem_seg_model import SEM_SEG_Model
import warnings
import copy
import open3d as o3d
from sklearn.metrics import roc_curve, roc_auc_score, confusion_matrix
from matplotlib import pyplot
import seaborn

def initialise(dataset_name, directory, num_classes, reload):
    sys.path.insert(0, './')
    os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'

    physical_devices = tf.config.experimental.list_physical_devices('GPU')
    tf.config.experimental.set_memory_growth(physical_devices[0], True)

    tf.random.set_seed(42) #random samples will be the same for each execution of this program
    tfr_path = os.path.join(directory, 'tf_records', '{}_0.tfrecord'.format(dataset_name))
    if reload == True or not os.path.isfile(tfr_path):
        inpath = os.path.join(directory, 'partial_cloud_pickles_{}'.format(dataset_name))
        write_dataset_to_tfrecord(inpath,tfr_path, dataset_name, num_classes)

def write_dataset_to_tfrecord(inpath, outpath, dataset_name, num_classes):
    # Adapted from https://stackoverflow.com/questions/61720708/how-do-you-save-a-tensorflow-dataset-to-a-file
    prevalence = np.zeros(num_classes)
    ds = None
    num_files = 10
    # loop and count the prevalence of all classes
    for i in range(1,num_files+1):
        label_string = "%d.0_labels.pickle" %i
        label_file = os.path.join(inpath, label_string)
        labels = pickle.load(open(label_file,"rb")) # read data
        labels = np.where(labels !=  None, labels, 4) # replace None values with a new category 4
        for i, elem in enumerate(prevalence):
            num = list(labels.flatten()).count(i)
            prevalence[i] += num # count the prevalence of each class seperately
    class_weights = 1 - (prevalence / sum(prevalence))

    # loop and load all split files
    for i in range(1,num_files+1):
        cloud_string = "%d.0_partial_clouds.pickle" %i
        label_string = "%d.0_labels.pickle" %i
        cloud_file = os.path.join(inpath, cloud_string)
        label_file = os.path.join(inpath, label_string)

        cloud = pickle.load(open(cloud_file,"rb"))
        if np.any(cloud == None):
            warnings.warn("Warning...........There are empty [None] points in an imported point cloud.")
        labels = pickle.load(open(label_file,"rb"))
        labels = np.where(labels !=  None, labels, 4)

        weights = class_weights[labels.astype(int)]
        weights = np.array(weights, dtype = object)
        part_ds = tf.data.Dataset.from_tensor_slices((tf.convert_to_tensor(cloud.astype(np.float32)),tf.convert_to_tensor(labels.astype(np.int32)),tf.convert_to_tensor(weights.astype(np.float32))))

        if ds is None:
            ds = part_ds
        else:
            ds = ds.concatenate(part_ds)

    for i, _ in enumerate(ds.element_spec):
        ds_i = ds.map(lambda *args: args[i]).map(tf.io.serialize_tensor)
        outpath_short = os.path.dirname(outpath)
        outfile = os.path.join(outpath_short, '{}_{}.tfrecord'.format(dataset_name, i))
        writer = tf.data.experimental.TFRecordWriter(outfile)
        writer.write(ds_i)

    print('Dataset has been created from raw data source and stored in tfrecord files')

def load_dataset(directory, name, batch_size, nr_points):
    # Read dataset from tfrecords
    # Adapted from https://stackoverflow.com/questions/61720708/how-do-you-save-a-tensorflow-dataset-to-a-file
    parts = []
    def read_map_cloud(x):
        read_tensor = tf.io.parse_tensor(x, tf.float32)
        read_tensor.set_shape((nr_points,3))
        return read_tensor
    def read_map_labels(x):
        read_tensor = tf.io.parse_tensor(x, tf.int32)
        read_tensor.set_shape((nr_points,1))
        return read_tensor
    def read_map_weights(x):
        read_tensor = tf.io.parse_tensor(x, tf.float32)
        read_tensor.set_shape((nr_points,1))
        return read_tensor
    cloud_path = os.path.join(directory, 'tf_records', '{}_{}.tfrecord'.format(name, 0))
    label_path = os.path.join(directory, 'tf_records', '{}_{}.tfrecord'.format(name, 1))
    weight_path = os.path.join(directory, 'tf_records', '{}_{}.tfrecord'.format(name, 2))

    cloud_part = tf.data.TFRecordDataset(cloud_path).map(read_map_cloud)
    label_part = tf.data.TFRecordDataset(label_path).map(read_map_labels)
    weight_part = tf.data.TFRecordDataset(weight_path).map(read_map_weights)

    parts.append(cloud_part)
    parts.append(label_part)
    parts.append(weight_part)
    ds = tf.data.Dataset.zip(tuple(parts))
    print("Dataset has been loaded successfully")
    return ds

def preprocess_data(ds, batch_size):
    # Make sure all sets have both small and medium sized plant examples
    medium_plants = ds.take(750)
    small_plants = ds.skip(750)
    # Split into train, val, test
    train_size = 1052
    val_size = 224
    test_size = 224

    train_m = medium_plants.take(int(train_size/2))
    val_m = medium_plants.skip(int(train_size/2))
    test_m = val_m.take(int(test_size/2))
    val_m = val_m.skip(int(test_size/2))

    train_s = small_plants.take(int(train_size/2))
    val_s = small_plants.skip(int(train_size/2))
    test_s = val_s.take(int(test_size/2))
    val_s = val_s.skip(int(test_size/2))

    train_data = train_m.concatenate(train_s)
    val_data = val_m.concatenate(val_s)
    test_data = test_m.concatenate(test_s)

    # shuffle order of examples
    shuffle_buffer = 5000
    train_data.shuffle(shuffle_buffer)
    val_data.shuffle(shuffle_buffer)
    test_data.shuffle(shuffle_buffer)

    # Shuffle the order of point within each point cloud?

    # Batch
    train_data = train_data.batch(batch_size, drop_remainder=True)
    val_data = val_data.batch(batch_size, drop_remainder=True)
    return train_data, val_data, test_data

class UpdatedMeanIoU(tf.keras.metrics.MeanIoU):
    # Adapted from https://stackoverflow.com/questions/61824470/dimensions-mismatch-error-when-using-tf-metrics-meaniou-with-sparsecategorical
    def __init__(self,
               y_true=None,
               y_pred=None,
               num_classes=None,
               name=None,
               dtype=None):
       super(UpdatedMeanIoU, self).__init__(num_classes = num_classes,name=name, dtype=dtype)

    def update_state(self, y_true, y_pred, sample_weight=None):
        y_pred = tf.math.argmax(y_pred, axis=-1)
        return super().update_state(y_true, y_pred, sample_weight)

# class WeightedSparseCategoricalCrossentropy(tf.keras.losses.Loss):
#     def init(self, class_weights):
#         self.unweighted_loss_function = tf.keras.losses.SparseCategoricalCrossentropy(reduction=tf.keras.losses.Reduction.NONE)
#         self.class_weights = class_weights # dictionary of weightings
#
#         super(WeightedSparseCategoricalCrossentropy, self).init()
#     def __init__(self, class_weights):
#         self.unweighted_loss_function = tf.keras.losses.SparseCategoricalCrossentropy(reduction=None)
#         self.class_weights = class_weights
#
#         super(WeightedSparseCategoricalCrossentropy, self).__init__()
#
#     def __call__(self, y_true, y_pred, sample_weight=None):
#         elementwise_unweighted_loss = self.unweighted_loss_function(y_true, y_pred)
#         elementwise_class_penalty = self.class_weights[y_true] # assuming y_true is an array of zero-indexed integers
#
#         elementwise_weighted_loss = elementwise_class_penalty * elementwise_unweighted_loss
#         weighted_loss = tf.math.reduce_sum(elementwise_weighted_loss, axis=None)
#         return weighted_loss


def train(train_ds, val_ds, epochs, num_classes, resume_training):
    model = SEM_SEG_Model(config['batch_size'], config['num_classes'], config['bn'])
    logdir = './logs/{}/model/weights'.format(config['log_dir'])
    cppath = logdir + "/saved-model-{epoch:02d}"

    callbacks = [
    keras.callbacks.TensorBoard(
    './logs/{}'.format(config['log_dir']), update_freq=25),
    keras.callbacks.ModelCheckpoint(cppath, save_best_only=False),
    ]

    model.build((config['batch_size'], 57600, 3))
    print(model.summary())

    model.compile(
    optimizer=keras.optimizers.Adam(config['lr']),
    loss=keras.losses.SparseCategoricalCrossentropy(),
    metrics=[keras.metrics.SparseCategoricalAccuracy(), UpdatedMeanIoU(num_classes = num_classes)]
    )

    if resume_training == True:
        model.load_weights(logdir)

    model.fit(
    train_ds,
    validation_data=val_ds,
    validation_steps=10,
    validation_freq=1,
    callbacks=callbacks,
    initial_epoch=config['starting_epoch'],
    epochs=epochs,
    verbose=1
    )

def test_net(test_set):
    model_nr = 250
    model = SEM_SEG_Model(config['batch_size'], config['num_classes'], config['bn'])
    logdir = './logs/{}/model/weights'.format(config['log_dir'])
    model.build((config['batch_size'], 57600, 3))
    model.compile(
    optimizer=keras.optimizers.Adam(config['lr']),
    loss=keras.losses.SparseCategoricalCrossentropy(),
    metrics=[keras.metrics.SparseCategoricalAccuracy(), UpdatedMeanIoU(num_classes = config['num_classes'])]
    )
    save_string = logdir + "/saved-model-{}".format(model_nr)
    model.load_weights(save_string)
    test_batched = test_set.batch(8, drop_remainder=True)

    pred = model.predict(test_batched)

    #results = model.evaluate(test_batched)
    #precision_recall_curve(pred, test_batched)
    calc_confusion_matrix(pred, test_batched)

def visualise_predictions(path, dataset):
    model = SEM_SEG_Model(config['batch_size'], config['num_classes'], config['bn'])
    model.build((config['batch_size'], 57600, 3))
    model.load_weights(path)

    batch = next(iter(dataset))
    cloud_nr = 0
    example = np.expand_dims(batch[0][cloud_nr,:,:], axis=0)
    prediction = model.call(example)
    pred_labels = np.argmax(prediction[0,:,:],axis=1)
    true_labels = batch[1][cloud_nr,:,:]

    rgb_codes = np.array([(0, 255, 0),(255, 0, 0),(0, 0, 0),(0, 0, 255),(0, 255, 255)])
    pcd = o3d.geometry.PointCloud()
    xyz = np.squeeze(example)
    pcd.points = o3d.utility.Vector3dVector(xyz)
    pcd.colors = o3d.utility.Vector3dVector(rgb_codes[pred_labels])
    pcd_truth = copy.deepcopy(pcd)
    pcd_truth.colors =  o3d.utility.Vector3dVector(rgb_codes[np.squeeze(true_labels)])

    o3d.visualization.draw_geometries([pcd])

    o3d.visualization.draw_geometries([pcd_truth])

def calc_confusion_matrix(pred, dataset):
    for i,batch in enumerate(dataset):
        if i == 0:
            true_labels = batch[1]
        else:
            true_labels = np.concatenate((true_labels, batch[1]), axis=0)

    single_predictions = tf.math.argmax(pred, axis=-1).numpy()
    labels = np.squeeze(true_labels)
    cm = confusion_matrix(single_predictions.flatten(), labels.flatten())
    seaborn.heatmap(cf_matrix, annot=True)
    import pdb; pdb.set_trace()

def precision_recall_curve(pred, dataset):
    true_labels = None
    for i,batch in enumerate(dataset):
        if i == 0:
            true_labels = batch[1]
        else:
            true_labels = np.concatenate((true_labels, batch[1]), axis=0)

    leaf_probability = pred[:,:,1]
    binary_true_labels = np.squeeze(np.where(true_labels == 1, 1, 0))
    fpr, tpr, thresholds = roc_curve(binary_true_labels.flatten(), leaf_probability.flatten())
    auc = roc_auc_score(binary_true_labels.flatten(), leaf_probability.flatten())

    pyplot.plot(fpr, tpr, marker='.', label='PointNet++')
    pyplot.plot(range(0,2), range(0,2), linestyle='--', label='No Skill')
    # axis labels
    pyplot.xlabel('False Positive Rate')
    pyplot.ylabel('True Positive Rate')
    # show the legend
    pyplot.legend()
    pyplot.title("Precision-Recall metric for point-wise binary segmentation (leaf vs. non-leaf)")
    # show the plot
    pyplot.show()

if __name__ == '__main__':

    config = {
        'dataset_name' : 'lowres',
        'reload_data' : False,
        'data_directory' : os.path.join(os.path.expanduser('~'), 'Desktop', 'project', 'deepLeaveSegmentation', 'synth_data'),
        'train_dim' : 57600,
        'log_dir' : 'sem_seg_final_long',
        'log_freq' : 10,
        'test_freq' : 100,
        'batch_size' : 8,
        'num_classes' : 4,
        'lr' : 0.001,
        'bn' : False, # batch normalisation?
        'epochs': 250,
        'load_weights': False,
        'starting_epoch': 0
        }

    initialise(config['dataset_name'], config['data_directory'], config['num_classes'], config['reload_data'])
    data = load_dataset(config['data_directory'], config['dataset_name'], config['batch_size'], config['train_dim'])
    train_ds, val_ds, test_ds = preprocess_data(data, config['batch_size'])
    #train(train_ds, val_ds, config['epochs'], config['num_classes'], config['load_weights'])
    #visualise_predictions('./logs/sem_seg_multiclass_0.001_retry/model/weights', val_ds)
    #precision_recall_curve('./logs/sem_seg_multiclass_0.001_retry/model/weights', val_ds)
    test_net(test_ds)
