import numpy as np 
import matplotlib.pyplot as plt 

#Archivos
sg = np.loadtxt('C:\\Users\\Mouzhroq\\Desktop\\Python\\MCIB\\Registro1Act1.txt')
t1 = int(1./sg[1,0])
t2 = int(1.25/sg[1,0])

fig, (ax0, ax1, ax2, ax3) = plt.subplots(nrows=4, sharex=True, constrained_layout=True)
ax0.plot(sg[t1:t2,0], sg[t1:t2,1]); ax0.set(title = 'Respirograma', ylabel='V')
ax1.plot(sg[t1:t2,0], sg[t1:t2,2]); ax1.set(title = 'ECG', ylabel='V')
ax2.plot(sg[t1:t2,0], sg[t1:t2,3]); ax2.set(title = 'EMG', ylabel='V')
ax3.plot(sg[t1:t2,0], sg[t1:t2,4]); ax3.set(title = 'Oximetro', ylabel='V', xlabel='tiempo [min]')

plt.show(block=False)
fig.savefig('C:\\Users\\Mouzhroq\\Desktop\\Python\\MCIB\\p1f1.png')

#Onda Cuadrada
fr = 5
sr = 300
t = np.linspace(0, 1, sr)[np.newaxis]

n = int(input('Numero de armonicos: '))
f = np.linspace(1,2*n-1,n)[:,np.newaxis]

s = (4*np.pi)*np.sum((1/f)*(np.sin(f*2*np.pi*fr*t)), axis=0)

fig, ax = plt.subplots()
ax.plot(t.flatten(),s); ax.set(xlabel='Tiempo [s]' ,ylabel= 'Amplitud', title= 'Aproximación de una señal cuadrada')

plt.show(block=False)
fig.savefig('C:\\Users\\Mouzhroq\\Desktop\\Python\\MCIB\\p1f2.png')

s2 = (8/np.pi**2)*np.sum((1/f**2)*(np.cos(2*np.pi*f*fr*t)), axis=0)
fig, ax = plt.subplots()
ax.plot(t.flatten(), s2); ax.set(xlabel='Tiempo [s]' ,ylabel= 'Amplitud', title= 'Aproximación de una señal triangular')

plt.show()
fig.savefig('C:\\Users\\Mouzhroq\\Desktop\\Python\\MCIB\\p1f3.png')