# -*- coding: utf-8 -*-
"""
Created on Mon Mar 16 20:40:51 2020

@author: Robert
"""
import scipy.io.wavfile
import numpy as np
from os.path import dirname, join as pjoin
import matplotlib.pyplot as plt

filename = "F:\Language_Project\Portuguese\wavs\Portuguese (11).wav"

rate2, data2 = scipy.io.wavfile.read(filename)

sin_data = np.sin(data2)

length = data2.shape[0] / rate2

i = 0
first_sample = True
index = 0

for sample in data2:
       if sample != 0 and first_sample:
              first_sample = False
              index = i
       i += 1             
       print(sample)