# -*- coding:utf-8 -*-

"""
@author: DeeLMind
@file: keras-overview.py
@time: 2019/6/11 16:49
"""

import tensorflow as tf
from tensorflow.keras import layers
print(tf.__version__)
print(tf.keras.__version__)

model = tf.keras.Sequential()
model.add(layers.Dense(32, activation='relu'))
model.add(layers.Dense(32, activation='relu'))
model.add(layers.Dense(10, activation='softmax'))
print(model)