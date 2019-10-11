import numpy as np 
import matplotlib.pyplot as plt 

time = np.linspace(0,1,320)
s = np.sin(2*np.pi*time*12)+np.sin(2*np.pi*time*17.5)+(5*time+2.5)

fig, ax = plt.subplots()
ax.plot(time,s)
#plt.show()

l=100
t= 50
index=np.array([0, l])
while index[-1]+l<len(s):
    index= np.append(index, np.array([index[-1]-l*(t/100), index[-1]-l*(t/100)+l]) )
index = np.array(np.sort(np.delete(index, -1))).astype(int)
epochs = np.array([s[i:i+l] for i in index])
for i in range (len(index)):
    x = np.append(time[index[i]:index[i]+l], np.ones(l)).reshape(2,l)
    y = epochs[i,:]
    w = np.dot(np.dot(np.linalg.inv(np.dot(x, x.T)), x), y.T)
    epochs[i,:] = epochs[i,:]-(w[0]*time[index[i]:index[i]+l]+w[1])

filt = epochs[0,:]
for i in range (1, len(epochs[:,0])):
    filt = np.append(filt, epochs[i, int(len(filt)-index[i])::])

x = np.append(time[index[-1]+l::], np.ones(len(time[index[-1]+l::]))).reshape(2,len(time[index[-1]+l::]))
y = s[index[-1]+l::]
w = np.dot(np.dot(np.linalg.inv(np.dot(x, x.T)), x), y.T)
filt = np.append(filt, s[index[-1]+l::]-(w[0]*time[index[-1]+l::]+w[1]))

plt.figure()
plt.plot(filt)
plt.show()