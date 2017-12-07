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

 

freq = 1000 # Hz
T = 1/freq
TT = T
ech_blo = [signal[0]]
ech = [signal[0]]
tps_ech = [temps[0]]


def echant(temps,signal,freq):
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
    return tps_ech,ech,ech_blo

        
def recherche_niveau(nb,niv):
    if nb<niv[0]:
        return niv[0]

    for i in range(len(niv)-1):
        if nb >= niv[i] and nb <=niv[i+1]:
            return niv[i]
    return niv[-1]
        
# Définition des niveaux de quantification
def signal_quan(Umin,Umax,Nq,signal):
    niv = []
    for i in range(2**Nq):
        niv.append(i*(Umax-Umin)/(2**Nq-1)+Umin)
    
    quan = []
    for s in signal:
        quan.append(recherche_niveau(s,niv))
    return quan


"""
for i in range(len(ech)):
    if ech[i]>0 :
        quan.append(floor(ech[i]))
    else :
        quan.append(floor(ech[i]))
"""
      
      

# Filtrage du signal
def filtrage_passe_bas(freq,pas_filtre,signal):
    tau = 1/freq # Coupure du filtre
    h = pas_filtre # Pas du filtre
    K=1
    res=[signal[0]]
    for i in range(1,len(signal)):
        res.append((h*K*signal[i]+tau*res[-1])/(h+tau))
    return res


# Filtrage du signal
def filtrage_passe_haut(freq,pas_filtre,signal):
    tau = 1/freq # Coupure du filtre
    h = pas_filtre # Pas du filtre
    K=1
    res=[signal[0]]
    for i in range(1,len(signal)):
        res.append((K*(signal[i]-signal[i-1])+res[-1]*(tau-h))/tau)
    return res
    
#Moyenne glissante
filtrageg =[]

fenetre = 100
for i in range(fenetre-1,len(quan)):
        s = sum(quan[i-fenetre+1:i+1])/fenetre
        filtrageg.append(s)


plt.grid()



## AFFICHAGE DU SIGNAL CLAIR
#plt.plot(temps,signal_clair)

## AFFICHAGE DU SIGNAL BRUITE
#plt.plot(temps,signal)

## AFFICHAGE DU SIGNAL BRUITE
#plt.plot(temps,signal)

## AFFICHAGE DU SIGNAL ECHANTILLONE
freq = 100
tps_ech,ech,ech_blo = echant(temps,signal,freq)

#plt.plot(temps,ech_blo,label="Signal bloqué")
#plt.plot(tps_ech,ech,label="Signal échantilonné")

## AFFICHAGE DU SIGNAL QUANTIFIE
Umin = -4 
Umax = 4
Nq = 4 # 2^Nb niveaux de quantification.
quan = signal_quan(Umin,Umax,Nq,ech_blo)
#plt.plot(temps,quan,label="Echantillonage "+str(freq)+ "Hz - Quantification "+str(Nq)+" bits")

## AFFICHAGE DU SIGNAL FILTRE PB
f = 1
s_pb= filtrage_passe_bas(1,0.001,signal)
#plt.plot(temps,signal,label="Signal brut")
#plt.plot(temps,s_pb,label="Signal filtré")


## AFFICHAGE DU SIGNAL FILTRE PH
f = .1
s_ph= filtrage_passe_haut(f,0.001,signal)
#plt.plot(temps,signal,label="Signal brut")
plt.plot(temps,s_ph,label="Signal filtré PH")



#plt.plot(tps_ech,res,linewidth=2,label="Pulsation de coupure "+str(1/tau)+" rad/s")

#plt.plot(tps_ech[fenetre-1:len(tps_ech)],filtrageg,linewidth=2,label="Moyenne sur "+str(fenetre)+" points")


#plt.plot(temps,ech,linewidth=2,label = "Frequence 1000 Hz")

import scipy.fftpack

N = len(quan)
T = 1/freq
yf = scipy.fftpack.fft(quan)
#plt.plot(tps_ech,np.abs(yf)*2/N)

plt.legend()
plt.show()