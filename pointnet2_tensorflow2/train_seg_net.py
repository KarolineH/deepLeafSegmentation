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
from scipy import io

def initialise(dataset_name, directory, num_classes, reload, numfiles):
    sys.path.insert(0, './')
    os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'

    physical_devices = tf.config.experimental.list_physical_devices('GPU')
    tf.config.experimental.set_memory_growth(physical_devices[0], True)

    tf.random.set_seed(42) #random samples will be the same for each execution of this program
    tfr_path = os.path.join(directory, 'tf_records', '{}_0.tfrecord'.format(dataset_name))
    if reload == True or not os.path.isfile(tfr_path):
        inpath = os.path.join(directory, 'partial_cloud_pickles_{}'.format(dataset_name))
        write_dataset_to_tfrecord(inpath,tfr_path, dataset_name, num_classes, num_files = numfiles)

def write_dataset_to_tfrecord(inpath, outpath, dataset_name, num_classes, num_files = 10):
    # Adapted from https://stackoverflow.com/questions/61720708/how-do-you-save-a-tensorflow-dataset-to-a-file
    prevalence = np.zeros(num_classes)
    ds = None
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
    model_nr = 120
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
    test_batched = test_set.batch(config['batch_size'], drop_remainder=True)
    pred = model.predict(test_batched)

    #results = model.evaluate(test_batched)
    import pdb; pdb.set_trace()
    #print("test set metrics: " + results)
    precision_recall_curve(pred, test_batched)
    calc_confusion_matrix(pred, test_batched)

def real_world_data_test():
    matr = io.loadmat('testcloud_realcrop.mat')
    pc = matr['single_example']
    pc_model_format = np.expand_dims(pc, axis=0)
    ds = tf.data.Dataset.from_tensor_slices((tf.convert_to_tensor(pc_model_format.astype(np.float32))))
    batchds = ds.batch(1, drop_remainder=True)

    model_nr = 120
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

    pred = model.predict(batchds)
    pred_labels = np.argmax(pred[0,:,:],axis=1)
    pcd = o3d.geometry.PointCloud()
    pcd.points = o3d.utility.Vector3dVector(pc)
    rgb_codes = np.array([(0.271, 0.372, 0.631),(0.94, 0.94, 0.114),(1, 1, 1),(0.835,0.345,0.243), (0,0,0)])
    pcd.colors = o3d.utility.Vector3dVector(rgb_codes[pred_labels])
    o3d.io.write_point_cloud("cloud_vis/realworld_pred_cloud.pcd", pcd)

def visualise_predictions(dataset, cloudnr):
    model_nr = 120
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
    test_batched = dataset.batch(config['batch_size'], drop_remainder=True)

    batch = next(iter(test_batched))
    cloud_nr = cloudnr
    example = np.expand_dims(batch[0][cloud_nr,:,:], axis=0)
    prediction = model.call(example)
    pred_labels = np.argmax(prediction[0,:,:],axis=1)
    true_labels = batch[1][cloud_nr,:,:]

    rgb_codes = np.array([(0.271, 0.372, 0.631),(0.94, 0.94, 0.114),(1, 1, 1),(0.835,0.345,0.243), (0,0,0)])
    pcd = o3d.geometry.PointCloud()
    xyz = np.squeeze(example)
    pcd.points = o3d.utility.Vector3dVector(xyz)
    pcd.colors = o3d.utility.Vector3dVector(rgb_codes[pred_labels])
    pcd_truth = copy.deepcopy(pcd)
    pcd_truth.colors =  o3d.utility.Vector3dVector(rgb_codes[np.squeeze(true_labels)])

    import pdb; pdb.set_trace()
    o3d.io.write_point_cloud("cloud_vis/{}_pred_cloud.pcd".format(config['dataset_name']), pcd)
    o3d.io.write_point_cloud("cloud_vis/{}_truth_cloud.pcd".format(config['dataset_name']), pcd_truth)

    #o3d.visualization.draw_geometries([pcd])
    #o3d.visualization.draw_geometries([pcd_truth])

    error_vector = np.where(pred_labels == np.squeeze(true_labels), 4, 0)
    error_pcd = copy.deepcopy(pcd)
    error_pcd.colors = o3d.utility.Vector3dVector(rgb_codes[error_vector])
    o3d.io.write_point_cloud("cloud_vis/{}_error_cloud.pcd".format(config['dataset_name']), error_pcd)
    #o3d.visualization.draw_geometries([pcd])
    import pdb; pdb.set_trace()

def calc_confusion_matrix(pred, dataset):
    for i,batch in enumerate(dataset):
        if i == 0:
            true_labels = batch[1]
        else:
            true_labels = np.concatenate((true_labels, batch[1]), axis=0)

    single_predictions = tf.math.argmax(pred, axis=-1).numpy()
    labels = np.squeeze(true_labels)
    cm = confusion_matrix(labels.flatten(), single_predictions.flatten())
    seaborn.heatmap(cm, annot=True)
    # Frequency table for all (mis-)classifications
    # true label in rows, predicted label in columns
    # diagonals over all is the same as categorial accuracy
    # binary accuracy per class is calculated per row
    binary_accuracies = []
    ious = []
    for i, label_class in enumerate(cm):
        binary_accuracies.append(label_class[i] / sum(label_class))

        ious.append(cm[i,i] / (sum(cm[i]) + sum(cm[:,i]) - cm[i,i]))
    import pdb; pdb.set_trace()
    print("Binary classification accuracies per class: " + binary_accuracies)
    print("Intersection over union per class: " + ious)
    print("Confusion matrix (ground truth labels in rows): " + cm)

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
    import pdb; pdb.set_trace()

    pyplot.plot(fpr, tpr, marker='.', label='PointNet++', markersize = 3)
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
        'num_files' : 10,
        'reload_data' : False,
        'data_directory' : os.path.join(os.path.expanduser('~'), 'Desktop', 'project', 'deepLeafSegmentation', 'synth_data'),
        'train_dim' : 57600,
        'log_dir' : 'sem_seg_final_long',
        'log_freq' : 10,
        'test_freq' : 100,
        'batch_size' : 1,
        'num_classes' : 4,
        'lr' : 0.001,
        'bn' : False, # batch normalisation?
        'epochs': 250,
        'load_weights': False,
        'starting_epoch': 0
        }

    initialise(config['dataset_name'], config['data_directory'], config['num_classes'], config['reload_data'], numfiles = config['num_files'])
    #data = load_dataset(config['data_directory'], config['dataset_name'], config['batch_size'], config['train_dim'])
    #train_ds, val_ds, test_ds = preprocess_data(data, config['batch_size'])
    #train(train_ds, val_ds, config['epochs'], config['num_classes'], config['load_weights'])
    #visualise_predictions(test_ds, cloudnr = 3) # or test set here
    #test_net(test_ds)
    real_world_data_test()
