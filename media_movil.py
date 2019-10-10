import numpy as np 
import matplotlib.pyplot as plt 

t = np.linspace(0,1,320)
s = np.sin(2*np.pi*t*12)+np.sin(2*np.pi*t*17.5)

fig, ax = plt.subplots()
ax.plot(t,s)
#plt.show()

l = 100
t = 25
x = np.arange(0, len(s)-l, l-1)
y = np.delete((np.arange(0, len(s)-l, l-1)-(l*(t/100))),0)
index = np.empty(len(x)+len(y)).astype(int)
index[::2] = x
index[1::2] = y

epochs = np.array([s[i:i+l] for i in index])
m = np.mean(epochs, axis=1)
ti = epochs-m[:,np.newaxis]
filt = ti[0,:]
for i in range (1, ti.shape[0]):
    filt = np.append(filt, ti[i, int(l*(t/100))::])

print(filt.shape)
# mf = np.mean(s[index[-1]::])
# ti = 