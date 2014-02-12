# -*- coding: utf-8 -*-
"""
@author: Xavier Pessoles
"""

import numpy as np
import matplotlib.pyplot as plt
from math import pi

x = np.linspace(0,5,200)

def fonc(x):
    return x**2 - 4+x

def dfonc(x):
    return 2*x +1


plt.plot(x,
         fonc(x),
         linewidth=3)

plt.plot(x,
         fonc(0)+dfonc(0)*(x-0),
         "r",
         linewidth=1)
c = 0 - fonc(0)/dfonc(0)

plt.plot([c,c], [0,fonc(c)], "r--")

plt.plot(x,
         fonc(c)+dfonc(c)*(x-c),
         "g",
         linewidth=1)
c = c - fonc(c)/dfonc(c)
plt.plot([c,c], [0,fonc(c)], "g--")


plt.plot(x,
         fonc(c)+dfonc(c)*(x-c),
         "y",
         linewidth=1)

plt.grid(True, which="both", linestyle="dotted")
#plt.legend(loc='lower left', fancybox=True, shadow=True, prop=dict(size=10))
#plt.xlabel("Temps en $s$")
#plt.ylabel("Position en $m$")
#plt.axis([0,xf,-1.2,1.2])
plt.show()
