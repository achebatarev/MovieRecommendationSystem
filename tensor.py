
# %%
import numpy as np
import tensorflow as tf
import os
import argparse
from cv2 import cv2


class Inference:
    def __init__(self, weightspath, metaname, ckptname, imagepath):
        self.weightspath = weightspath
        self.metaname = metaname
        self.ckptname = ckptname
        self.imagepath = imagepath
        self.mapping = {'normal': 0, 'pneumonia': 1, 'COVID-19': 2}
        self.inv_mapping = {0: 'normal', 1: 'pneumonia', 2: 'COVID-19'}


    def opperate(self): 
        tf.compat.v1.disable_eager_execution()
        sess = tf.compat.v1.Session()
        tf.compat.v1.get_default_graph()
        saver = tf.compat.v1.train.import_meta_graph(
            os.path.join(self.weightspath, self.metaname))
        saver.restore(sess, os.path.join(self.weightspath, self.ckptname))

        graph = tf.compat.v1.get_default_graph()

        image_tensor = graph.get_tensor_by_name("input_1:0")
        pred_tensor = graph.get_tensor_by_name("dense_3/Softmax:0")

        x = cv2.imread(self.imagepath)
        h, w, c = x.shape
        x = x[int(h/6):, :]
        x = cv2.resize(x, (224, 224))
        x = x.astype('float32') / 255.0
        self.pred = sess.run(pred_tensor, feed_dict={
                        image_tensor: np.expand_dims(x, axis=0)})

    def getPrediction(self):
        return 'Prediction: {}'.format(self.inv_mapping[self.pred.argmax(axis=1)[0]])

    def getConfidence(self):
        return 'Normal: {:.3f}, Pneumonia: {:.3f}, COVID-19: {:.3f}'.format(self.pred[0][0], self.pred[0][1], self.pred[0][2])


#

# %%
# model = Inference('models/COVIDNet-CXR-Large', 'model.meta', 'model-8485', 'images/testImage.jpeg')
# model.opperate()

# print(model.getPrediction() + '\n' + model.getConfidence())