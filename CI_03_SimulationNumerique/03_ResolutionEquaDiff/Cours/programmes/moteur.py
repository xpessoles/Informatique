# -*- coding: utf-8 -*-
"""
@author: Xavier Pessoles
"""

import numpy as np
import matplotlib.pyplot as plt
from math import exp


ti=0
tf=8
pas=0.3
omega_0=0

def omega_n(ti,tf,pas,omega_0):
    res=[]
    temps=[ti]
    res=[omega_0]
    for i in range(1,int((tf-ti)/pas)):
        res.append(pas*1+res[i-1]*(1-pas))
        temps.append(ti+i*pas)
    return temps,res
        
def omega_t(ti,tf,pas):
    pas=pas/100
    res=[]
    temps=[ti]
    res=[0]
    for i in range(1,int((tf-ti)/pas)):
        res.append(1-exp(-i*pas))
        temps.append(ti+i*pas)
    return temps,res

temps,omegan=omega_n(ti,tf,pas,omega_0)
temps2,omegat=omega_t(ti,tf,pas)

plt.plot(temps,omegan,linewidth=3,marker='v')
plt.plot(temps2,omegat,linewidth=3)

plt.grid(True, which="both", linestyle="dotted")
plt.legend(["Solution approchée","Solution exacte"],loc='lower right', fancybox=True, shadow=True, prop=dict(size=10))
#plt.xlabel("Temps en $s$")
#plt.ylabel("Position en $m$")
#plt.axis([0,xf,-1.2,1.2])
plt.show()
