# -*- coding: utf-8 -*-
"""
Created on Sat Jul 10 12:53:24 2021

@author: Lawrence
"""

import numpy as np

from scipy.io.wavfile import write

inputFile ='./Adeptus Mechanicus.htm'
outputFile = './toaster.wav'


try:
    data = open(inputFile, 'rb')
    samples = data.read()
except:
    raise IOError('Error reading from input file')
finally:
    data.close()
    
    
sampleRate = 44100

samples = np.fromstring(samples, dtype = np.uint8)


# interpolate to move some of the frequencies down into the audible range
# without this files just sound like white noise thoughout

# TODO: scalable interpolation to adjust level of downscaling


samples2 = np.zeros(shape = samples.shape)

samples2[:-1] = (samples[:-1]+samples[1:])/2
samples2 = samples2.astype(np.uint8)

megaSamples = np.asarray([samples, samples2])
megaSamples = megaSamples.transpose().flatten()
write(outputFile, sampleRate, megaSamples)