import numpy as np 
import matplotlib.pyplot as plt  
import scipy.signal as sg 

sr = 512
fc = 50
b, a = sg.cheby1(10, 10,fc/sr, btype='lowpass')

w, h = sg.freqz(b, a)
plt.plot(w*sr/np.pi, 20*np.log10(np.abs(h)))
plt.show()
