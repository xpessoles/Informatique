# -*- coding: utf-8 -*-

import numpy as np
from math import *
import matplotlib.pyplot as plt

temperatureMer=15+273.15
pressionMer=101325
R=287
g=9.81
zMax=47000

masseVolumiqueMer=pressionMer/(R*temperatureMer)

temperature=[temperatureMer]
pression=[pressionMer]
masseVolumique=[masseVolumiqueMer]

for i in range(zMax):
    if i<11000 : ecart=-0.0065
    elif i<20000 : ecart=0
    elif i<32000 : ecart=0.001
    else : ecart=0.0028
    temperature.append(temperature[i]+ecart)

for i in range(zMax):
    pression.append(pression[i]-g*masseVolumique[i])
    masseVolumique.append(pression[i+1]/(R*temperature[i+1]))

listeAltitudes=np.linspace(0,zMax,zMax+1)

plt.figure(1)

plt.plot(listeAltitudes,temperature)
plt.title("Evolution de la température en fonction de l'altitude")
plt.xlabel("altitude (m)")
plt.ylabel("température (K)")
plt.grid(True)

plt.figure(2)

plt.plot(listeAltitudes,masseVolumique)
plt.title("Evolution de la masse volumique en fonction de l'altitude")
plt.xlabel("altitude (m)")
plt.ylabel("masse volumique (kg/m$^{-3}$)")
plt.grid(True)

plt.figure(3)

plt.plot(listeAltitudes,pression)
plt.title("Evolution de la pression en fonction de l'altitude")
plt.xlabel("altitude (m)")
plt.ylabel("pression (Pa)")
plt.grid(True)

plt.show()