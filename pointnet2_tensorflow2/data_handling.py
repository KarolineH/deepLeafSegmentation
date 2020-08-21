import tensorflow as tf
from tensorflow import keras
import open3d as o3d
import pdb
import numpy as np
from models.sem_seg_model import SEM_SEG_Model

# currently the poinclouds are numpy arrays
# 480x480x3
# 480x480 string labels
# order is column by column through the world space, so starting at top left to bottom left and then slowly across to the right

# What I need:
# Make labels into numeric values

# some dummy data
data = np.random.rand(1080,1080,3)
labels = np.random.randint(5, size=(1080,1080,1))
#unroll the point clouds into 1 dimension
data = data.reshape(data.shape[0] * data.shape[1], data.shape[2])
labels = labels.reshape(labels.shape[0] * labels.shape[1], labels.shape[2])
# stack multiple examples to a whole set
inp = np.stack((data,data,data))
outp = np.stack((labels,labels,labels))
weirdin = (tf.convert_to_tensor(inp),tf.convert_to_tensor(outp))
dataset = tf.data.Dataset.from_tensor_slices(weirdin)
batches = dataset.batch(3, drop_remainder=True)

pdb.set_trace()

model = SEM_SEG_Model(2, 5)
callbacks = [
    keras.callbacks.TensorBoard(
        './logs/{}'.format('scannet_1'), update_freq=50),
    keras.callbacks.ModelCheckpoint(
        './logs/{}/model/weights'.format('scannet_1'), 'val_sparse_categorical_accuracy', save_best_only=True)
]

model.build((1, 1166400, 3))
print(model.summary())

model.compile(
    optimizer=keras.optimizers.Adam(0.001),
    loss=keras.losses.SparseCategoricalCrossentropy(),
    metrics=[keras.metrics.SparseCategoricalAccuracy()]
)

model.fit(
    batches,
    batch_size=1,
    validation_data=None,
    validation_steps=10,
    validation_freq=1,
    callbacks=callbacks,
    epochs=100,
    verbose=1
)

pdb.set_trace()



pcd = o3d.io.read_point_cloud("./synth_data/split_clouds/1_1.ply")
#print(np.asarray(pcd.points))
o3d.visualization.draw_geometries([pcd], zoom=0.3412,
                                  front=[0.4257, -0.2125, -0.8795],
                                  lookat=[2.6172, 2.0475, 1.532],
                                  up=[-0.0694, -0.9768, 0.2024])
pdb.set_trace()
