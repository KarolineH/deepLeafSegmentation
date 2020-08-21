import numpy as np
import tensorflow as tf
class_dict = {0 : 'a', 1 : 'b', 2 : 'c' ,3 : 'd'}






class WeightedSparseCategoricalCrossentropy(tf.keras.losses.Loss):
    def __init__(self, class_weights, name='WeightedCrossentropyLoss'):
        self.unweighted_loss_function = tf.keras.losses.SparseCategoricalCrossentropy(reduction=tf.keras.losses.Reduction.NONE, name = name)
        self.class_weights = class_weights # dictionary of weightings

        super(WeightedSparseCategoricalCrossentropy, self).__init__()

    def __call__(self, y_true, y_pred, sample_weight=None):
        elementwise_unweighted_loss = self.unweighted_loss_function(y_true, y_pred)  # shape (batches, points_per_cloud)
        elementwise_class_penalty = self.class_weights[y_true] # assuming y_true is an array of zero-indexed integers
        import pdb; pdb.set_trace()
        elementwise_weighted_loss = elementwise_class_penalty * elementwise_unweighted_loss
        weighted_loss = tf.math.reduce_mean(elementwise_weighted_loss)

        print('using weighted cross entropy')
        return weighted_loss




y = np.random.randint(4, size=(100,100,1))

import pdb; pdb.set_trace()
labels = np.where(x !=  None, labels, 4)
import pdb; pdb.set_trace()
try2 = tf.where(y.ref() == y.ref(), class_dict[y.ref()], class_dict[y.ref()])

import pdb; pdb.set_trace()
out = tf.map_fn(map_tens, y)
import pdb; pdb.set_trace()
