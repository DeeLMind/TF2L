# -*- coding:utf-8 -*-

"""
@author: DeeLMind
@file: isGPU.py
@time: 2019/6/11 17:00
"""

import tensorflow as tf

try:
    with tf.device("/device:GPU:0"):
        print("Of cource GPU")
except:
    print("NOooO GPU")

