# -*- coding: utf-8 -*-
"""
Created on Mon Mar 16 20:40:51 2020

@author: Robert
"""
import scipy.io.wavfile
import numpy as np
from os.path import dirname, join as pjoin
import matplotlib.pyplot as plt

i = 2

filename = "F:\Language_Project\Portuguese\Portuguese ({}).wav".format(i)

rate2, data2 = scipy.io.wavfile.read(filename)

editedData = []
if np.shape(np.shape(data2))[0] > 1:
       for sample in data2:
              editedData.append(sample[0])
#if np.shape(np.shape(data2))[0] > 1:
#       for item in data2:
#              print(item[0])

data3 = data2[:len(data2)][0]

data4 = []



filename = "F:\Language_Project\English\English ({}).wav".format(i)
rate, data = scipy.io.wavfile.read(filename)


sin_data = np.sin(data2)



i = 0
first_sample = True
index = 0

for sample in data2:
       if sample != 0 and first_sample:
              first_sample = False
              index = i
       i += 1             
       print(sample)
       
       
np.mean(lengths)
np.mean(englishLengths)
np.mean(mandarinLengths)
np.mean(portugueseLengths)

np.min(lengths)
np.min(englishLengths)
np.min(mandarinLengths)
np.min(portugueseLengths)

np.std(lengths)
np.std(englishLengths)
np.std(mandarinLengths)
np.std(portugueseLengths)

np.max(lengths)
np.max(englishLengths)
np.max(mandarinLengths)
np.max(portugueseLengths)

np.median(lengths)
np.median(englishLengths)
np.median(mandarinLengths)
np.median(portugueseLengths)

np.quantile(lengths, .25)
np.quantile(englishLengths, .25)
np.quantile(mandarinLengths, .25)
np.quantile(portugueseLengths, .25)

np.quantile(lengths, .75)
np.quantile(englishLengths, .75)
np.quantile(mandarinLengths, .75)
np.quantile(portugueseLengths, .75)