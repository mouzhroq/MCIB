import numpy as np 
import matplotlib.pyplot as plt 
from scipy.fftpack import fft
import scipy.signal.windows as win 

sr = 320
t = np.linspace(0, 1, sr)
s = np.sin(2*np.pi*12*t)+np.sin(2*np.pi*17.5*t)

fig, ax = plt.subplots()
ax.plot(t, s)

plt.show(block=False)

fft1 = np.abs(fft(s))
fft1 = 20*np.log10(fft1)
w = win.hamming(sr)
fft2 = np.abs(fft(s*w))
fft2 = 20*np.log10(fft2)
fig, ax = plt.subplots()
ax.plot(fft1[0:int(sr/2)])
ax.plot(fft2[0:int(sr/2)])

plt.show()
