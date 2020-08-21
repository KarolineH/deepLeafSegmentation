import os
import sys
import datetime
import tensorflow as tf
from tensorflow import keras
from models.sem_seg_model import SEM_SEG_Model

sys.path.insert(0, './')
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'

physical_devices = tf.config.experimental.list_physical_devices('GPU')
tf.config.experimental.set_memory_growth(physical_devices[0], True)

tf.random.set_seed(42) #random samples will be the same for each execution of this program

def load_dataset(in_file, batch_size):

	assert os.path.isfile(in_file), '[error] dataset path not found'

	n_points = 8192
	shuffle_buffer = 1000

	def _extract_fn(data_record):

		in_features = {
			'points': tf.io.FixedLenFeature([n_points * 3], tf.float32),
			'labels': tf.io.FixedLenFeature([n_points], tf.int64)
		}

		return tf.io.parse_single_example(data_record, in_features)

	def _preprocess_fn(sample):

		points = sample['points']
		labels = sample['labels']

		points = tf.reshape(points, (n_points, 3))
		labels = tf.reshape(labels, (n_points, 1))

		shuffle_idx = tf.range(points.shape[0])
		shuffle_idx = tf.random.shuffle(shuffle_idx)
		points = tf.gather(points, shuffle_idx)
		labels = tf.gather(labels, shuffle_idx)

		return points, labels

	dataset = tf.data.TFRecordDataset(in_file)
	import pdb; pdb.set_trace()
	dataset = dataset.shuffle(shuffle_buffer)
	dataset = dataset.map(_extract_fn)
	dataset = dataset.map(_preprocess_fn)
	dataset = dataset.batch(batch_size, drop_remainder=True)

	return dataset

def train():

	model = SEM_SEG_Model(config['batch_size'], config['num_classes'], config['bn'])

	train_ds = load_dataset(config['train_ds'], config['batch_size'])
	val_ds = load_dataset(config['val_ds'], config['batch_size'])



	thingy = list(val_ds.as_numpy_iterator())
	thingy[0][0][:,0:100,:].shape
	model.call(thingy[0][0][:,0:100,:])
	model.call(thingy[0][0][0:1,0:100,:]) # only a single batch, size can be changed

	import pdb; pdb.set_trace()




	callbacks = [
		keras.callbacks.TensorBoard(
			'./logs/{}'.format(config['log_dir']), update_freq=50),
		keras.callbacks.ModelCheckpoint(
			'./logs/{}/model/weights'.format(config['log_dir']), 'val_sparse_categorical_accuracy', save_best_only=True)
	]

	model.build((config['batch_size'], 8192, 3))
	print(model.summary())

	model.compile(
		optimizer=keras.optimizers.Adam(config['lr']),
		loss=keras.losses.SparseCategoricalCrossentropy(),
		metrics=[keras.metrics.SparseCategoricalAccuracy()]
	)

	model.fit(
		train_ds,
		validation_data=val_ds,
		validation_steps=10,
		validation_freq=1,
		callbacks=callbacks,
		epochs=100,
		verbose=1
	)


if __name__ == '__main__':

	config = {
		'train_ds' : 'data/scannet_train.tfrecord',
		'val_ds' : 'data/scannet_val.tfrecord',
		'log_dir' : 'scannet_1',
		'log_freq' : 10,
		'test_freq' : 100,
		'batch_size' : 4,
		'num_classes' : 21,
		'lr' : 0.001,
		'bn' : False,
	}

	train()
