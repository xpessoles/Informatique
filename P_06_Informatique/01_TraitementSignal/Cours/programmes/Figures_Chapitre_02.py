import numpy as np
import matplotlib.pyplot as plt
from random import randint
from math import pi,floor
nb = 10000
temps = np.linspace(0,10,nb)
aleatoire = [randint(-200,200)/10000*(i%2)*(i%3)*(i%4)*(i%5) for i in range(nb)]
aleatoire  = np.array(aleatoire)
signal = 10*np.sin(temps*2*pi*5000)*np.exp(-temps/2)*(1-np.exp(-temps))+aleatoire
signal_clair = 10*np.sin(temps*2*pi*5000)*np.exp(-temps/2)*(1-np.exp(-temps))

Umin = -4 
Umax = 4
Nq = 10 # 2^Nb niveaux de quantification. 

freq = 1000 # Hz
T = 1/freq
TT = T
ech_blo = [signal[0]]
ech = [signal[0]]
tps_ech = [temps[0]]

for i in range(1,len(temps)):
    tps = temps[i]
    if tps<TT:
        ech_blo.append(ech[-1])
    else :
        TT = TT+T
        ech_blo.append(signal[i])
        ech.append(signal[i])
        tps_ech.append(temps[i])
        
def recherche_niveau(nb,niv):
    if nb<niv[0]:
        return niv[0]

    for i in range(len(niv)-1):
        if nb >= niv[i] and nb <=niv[i+1]:
            return niv[i]
    return niv[-1]
        
# Définition des niveaux de quantification
niv = []
for i in range(2**Nq):
    niv.append(i*(Umax-Umin)/(2**Nq-1)+Umin)

quan = []
for s in signal:
    quan.append(recherche_niveau(s,niv))


"""
for i in range(len(ech)):
    if ech[i]>0 :
        quan.append(floor(ech[i]))
    else :
        quan.append(floor(ech[i]))
"""
      
      

# Filtrage du signal
tau = 1/freq
h = 1/freq
"""
filtrage=[quan[0]]
for i in range(
"""

plt.grid()
#plt.plot(temps,signal,label = "Signal")
plt.plot(tps_ech,quan,label="Echantillonage "+str(freq)+ "Hz - Quantification "+str(Nq)+" bits")

#plt.plot(temps,ech,linewidth=2,label = "Frequence 1000 Hz")
plt.legend()
plt.show()