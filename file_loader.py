
import scipy.io.wavfile
import numpy as np


#Loop for English
englishWavFiles = []
englishRateFiles = []

for i in range(1, 14735):
       filename = "F:\Language_Project\English\English ({}).wav".format(i)
       rate, data = scipy.io.wavfile.read(filename)


#Loop for Mandarin


for i in range(1, 11148):
       filename = "F:\Language_Project\Mandarin\Mandarin ({}).wav".format(i)
       rate, data = scipy.io.wavfile.read(filename)





#Loop for Portuguese
       
port_wav_files = []
port_rate_files = []
for i in range(1, 1976):
       filename = "F:\Language_Project\Portuguese\Portuguese ({}).wav".format(i)
       rate, data = scipy.io.wavfile.read(filename)
       temp_data, long_enough = audioEditor(data, rate, 1.3)
       if long_enough:
              port_wav_files.append(temp_data)
              port_rate_files.append(rate)
       





#Function to grab part of audio we want
def audioEditor(data, rate, length):
       
       editedData = []
       if np.shape(np.shape(data))[0] > 1:
              for sample in data:
                     editedData.append(sample[0])
       else:
              editedData = np.copy(data)
       #Delete all 0 values at beginning
       i = 0
       for sample in editedData:
              if sample != 0:
                     break
              i += 1
       editedData = editedData[i:]
       if calculateAudioLength(editedData, rate) <= length:
              return editedData, False
       else:
              #chop off everything longer than 1.3 seconds
              num_samples = length * rate
              editedData = editedData[:int(num_samples)]
       return editedData, True


def calculateAudioLength(data, rate):
       
       return len(data) / rate



#Neural Network