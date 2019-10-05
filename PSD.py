import numpy as np 
import matplotlib.pyplot as plt 
from scipy.fftpack import fft
from scipy.signal import welch 

sr = 60000
s = np.loadtxt('Registro1Act1.txt')

l = 256
tr = 25
index = np.concatenate((np.arange(0, len(s[:,2])-l, l), np.delete((np.arange(0, len(s[:,2])-l, l)-(l*(tr/100))),0))).astype(int)
epochs = np.array([s[i:i+l,2] for i in index])

w = np.linspace(0, sr, l)
mfft = (np.abs(fft(epochs)))
mfft = (1/len(epochs[:,2]))*np.sum(mfft, axis=0)

plt.plot(w[0:int(len(mfft)/2)], mfft[0:int(len(mfft)/2)])
plt.show()



