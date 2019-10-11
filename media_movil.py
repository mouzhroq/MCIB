import numpy as np 
import matplotlib.pyplot as plt 

t = np.linspace(0,1,320)
s = np.sin(2*np.pi*t*12)+np.sin(2*np.pi*t*17.5)

fig, ax = plt.subplots()
ax.plot(t,s)
#plt.show()

l = 50
t = 10
index=np.array([0, l])
while index[-1]+l<len(s):
    index= np.append(index, np.array([index[-1]-l*(t/100), index[-1]-l*(t/100)+l]) )
index = np.array(np.sort(np.delete(index, -1))).astype(int)

epochs = np.array([s[i:i+l] for i in index])
m = np.mean(epochs, axis=1)
ti = epochs-m[:,np.newaxis]
filt = ti[0,:]
for i in range (1, ti.shape[0]):
    filt = np.append(filt, ti[i, int(len(filt)-index[i])::])
filt = np.append(filt, s[index[-1]+l::]-np.mean(s[index[-1]+l::]))

plt.figure()
plt.plot(filt)
plt.show()