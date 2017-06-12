import numpy as np
import matplotlib.pyplot as plt
from random import randint
from math import pi,floor

# Génération du signal artificiel
nb = 10000
temps = np.linspace(0,10,nb)
aleatoire = [randint(-200,200)/10000*(i%2)*(i%3)*(i%4)*(i%5) for i in range(nb)]
aleatoire  = np.array(aleatoire)
# Signal clair (porteuse)
signal_clair = 10*np.sin(temps*2*pi*5000)*np.exp(-temps/2)*(1-np.exp(-temps))
# Signal bruité
signal = 10*np.sin(temps*2*pi*5000)*np.exp(-temps/2)*(1-np.exp(-temps))+aleatoire


Umin = -4 
Umax = 4
Nq = 10 # 2^Nb niveaux de quantification. 

freq = 4 # Hz
T = 1/freq
TT = T
ech_blo = [signal[0]]
ech = [signal[0]]
tps_ech = [temps[0]]


# Echantillonnnage du signal (Avec 1 ou 2 échantillons par seconde, on récupère rien).
for i in range(1,len(temps)):
    tps = temps[i]
    if tps<TT:
        ech_blo.append(ech[-1])
    else :
        TT = TT+T
        ech_blo.append(signal[i])
        ech.append(signal[i])
        tps_ech.append(temps[i])

plt.plot(temps,signal) # Affichage du signal bruité
#plt.plot(tps_ech,ech) # Affichage du signal échantilloné
#plt.plot(temps,ech_blo) # Affichage du signal échantilloné bloqué


def recherche_niveau(nb,niv):
    # Recherche du nibeau de quantification
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

for s in ech_blo: # Signal bloqué quantifié
#for s in signal: # signal quantifié
    quan.append(recherche_niveau(s,niv))
"""
for i in range(len(ech)):
    if ech[i]>0 :
        quan.append(floor(ech[i]))
    else :
        quan.append(floor(ech[i]))
"""
    
#plt.plot(temps,quan) # Affichage du signal quantifié


      
# Filtrage du signal
tau = 00.001*1/freq
print(1/tau)
h = 1/freq
K=1

res=[quan[0]]
for i in range(1,len(quan)):
    res.append((h*K*quan[i]+tau*res[-1])/(h+tau))

#Moyenne glissante
filtrageg =[]
tempsg = []
fenetre = 1000
for i in range(fenetre-1,len(quan)):
        s = sum(quan[i-fenetre+1:i+1])/fenetre
        filtrageg.append(s)
        tempsg.append(temps[i])


#plt.plot(temps,signal,label = "Signal")
#plt.plot(tps_ech,quan,label="Echantillonage "+str(freq)+ "Hz - Quantification "+str(Nq)+" bits")

# PLOT du signal filtré
plt.plot(temps,res,linewidth=2,label="Pulsation de coupure "+str(1/tau)+" rad/s")


#plt.plot(temps,signal)

#plt.plot(tps_ech[fenetre-1:len(tps_ech)],filtrageg,linewidth=2,label="Moyenne sur "+str(fenetre)+" points")
plt.plot(tempsg,filtrageg,linewidth=2,label="Moyenne sur "+str(fenetre)+" points")
plt.grid()

#plt.legend()
plt.show()



#plt.plot(temps,ech,linewidth=2,label = "Frequence 1000 Hz")
"""
import scipy.fftpack

N = len(quan)
T = 1/freq
yf = scipy.fftpack.fft(quan)
plt.plot(tps_ech,np.abs(yf)*2/N)

plt.legend()
plt.show()
"""