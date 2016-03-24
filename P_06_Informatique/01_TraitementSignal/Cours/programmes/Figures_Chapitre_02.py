import numpy as np
import matplotlib.pyplot as plt
from random import randint
from math import pi,floor
nb = 10000
temps = np.linspace(0,10,nb)
aleatoire = [randint(-200,200)/10000*(i%2)*(i%3)*(i%4)*(i%5) for i in range(nb)]
aleatoire  = np.array(aleatoire)
signal = 10*np.sin(temps*2*pi*5000)*np.exp(-temps/2)*(1-np.exp(-temps))+aleatoire



freq = 1000 # Hz
T = 1/freq
TT = T
ech = [signal[0]]
for i in range(1,len(temps)):
    tps = temps[i]
    if tps<TT:
        ech.append(ech[-1])
    else :
        TT = TT+T
        ech.append(signal[i])

quan = []
for i in range(len(ech)):
    if ech[i]>0 :
        quan.append(floor(ech[i]))
    else :
        quan.append(floor(ech[i]))
        
plt.grid()
#plt.plot(temps,signal,label = "Signal")
#plt.plot(temps,quan)

plt.plot(temps,ech,linewidth=2,label = "Frequence 1000 Hz")
plt.legend()
plt.show()