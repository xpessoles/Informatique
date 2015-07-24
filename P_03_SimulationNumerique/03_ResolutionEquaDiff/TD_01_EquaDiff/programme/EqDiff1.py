# -*- coding: utf-8 -*-
"""
Created on Wed Mar 25 22:28:32 2015

@author: Xavier
"""

import numpy as np 
import matplotlib.pyplot as plt
from scipy.integrate import odeint

ti = 0
tf = 5
nb = 20
tau = 1
texp = [0]
yexp = [1]
h = (tf-ti)/nb
for i in range(nb):
    texp.append(texp[i]+h)
    yexp.append(yexp[i]*(1-h/tau))

timp = [0]
yimp = [1]
for i in range(nb):
    timp.append(timp[i]+h)
    yimp.append(yimp[i]*(tau/(tau+h)))

t = np.linspace(ti,tf,500)
ya = np.exp(-t)

N0 = 1
tn = np.linspace(ti,tf,nb)
def deriv(syst, t):
    N = syst[0]                         # Variable1 N(t)
    dNdt=-N/tau                         # Equation différentielle
    return [dNdt]                       # Dérivées des variables
    
syst_CI=np.array([N0]) 
yn=odeint(deriv,syst_CI,tn)

plt.plot(t,ya,label = "Solution analytique")
plt.plot(texp,yexp,'o',label = "Solution numérique explicite")
plt.plot(timp,yimp,'*',label = "Solution numérique implicite")
plt.plot(tn,yn,'.',label = "Solution numérique SciPy")

plt.legend()
plt.show()