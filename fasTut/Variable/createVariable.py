# -*- coding:utf-8 -*-

"""
@author: DeeLMind
@file: createVariable.py
@time: 2019/6/11 16:57
"""

import tensorflow as tf

o23 = tf.Variable(tf.ones([2,3]))
print(o23)

c = tf.Variable(2)
print(c.value())