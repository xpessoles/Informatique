import numpy as np
from math import pi,floor,cos,sin
import matplotlib.pyplot as plt
from random import randint


N = 100001
Tf = 10
tps = np.linspace(0,Tf,N)
# Fréquence d'échantillonage
fe = 1000
Te = 1/fe

T = 3 #s
omega = 2*pi/T

# On ajoute du bruit que pour un point sur 10
bruit = np.array([randint(-100,100)/10000 for x in range(N)])
# for i in range (N):
#     if i%10==0 :
#         bruit[i]=bruit[i]
#     else :
#         bruit[i]=0

signal = 0.5*np.sin(omega*tps)+2+bruit
#plt.plot(tps,signal)
sig0 = 0*np.sin(tps)
plt.plot(tps,sig0)


# Echantillonage du signal / bloqueur
TT = Te
signal_ech = [signal[0]]
for i in range(1,len(tps)):
    t = tps[i]
    if t<TT:
        signal_ech.append(signal_ech[-1])
    else :
        TT = TT+Te
        signal_ech.append(signal[i])
plt.plot(tps,signal_ech)

#Quantification
Umin = -5
Umax = 5
Nb = 10 #Nombre de bits

plage = np.linspace(Umin,Umax,2**Nb)

signal_qt = []
for i in range(len(signal_ech)):
    sig = signal_ech[i]
    signal_qt.append(floor((2**Nb)*sig/(Umax-Umin))/(2**Nb) * (Umax-Umin))

plt.plot(tps,signal_qt)
plt.show()

# for i in range(len(signal_ech)):
#     sig = signal_ech[i]
#     for j in range(len(plage)-1):
#         if sig>plage[j] and sig<plage[j+1]:
#             signal_qt.append(plage[j])
#             break

def transf_fourier_freq(sig,k):
    reel=0
    ima = 0
    for i in range(len(sig)):
        reel = reel + sig[i]*cos(-2*pi*k*i/len(sig))
        ima = ima + sig[i]*sin(-2*pi*k*i/len(sig))
    return reel,ima
    

[re,im]=transf_fourier_freq(signal_qt,100)


plt.show()    