# -*- coding: utf-8 -*-
"""
Created on Wed Mar 25 22:28:32 2015

@author: Xavier
"""
import math
import numpy as np 
import matplotlib.pyplot as plt
from scipy.integrate import odeint

ti = 0
tf = 5
nb = 50
h = (tf-ti)/nb
Q = 1
om0 = 2*math.pi
x0=[1]
x1=[0]
tt = [0]
for i in range(nb):
    tt.append(tt[i]+h)
    x0.append(h*x1[i]+x0[i])
    x1.append(x1[i]-(h*om0/Q)*x1[i]-h*om0*om0*x0[i])


def deriv(syst, t):
    x = syst[0]                         # Variable1 x
    v = syst[1]                         # Variable2 v
    dxdt = v                            # Equation différentielle 1
    dvdt = -om0/Q*v-om0**2*x      # Equation différentielle 2
    return [dxdt,dvdt]                  # Dérivées des variables

# Paramètres d'intégration
t = np.linspace(ti,tf,nb)

# Conditions initiales et résolution
xi=1
vi=0
syst_CI=np.array([xi,vi])                  # Tableau des CI
Sols=odeint(deriv,syst_CI,t)            # Résolution numérique des équations différentielles

# Récupération des solutions
x = Sols[:, 0]
v = Sols[:, 1]

plt.plot(tt,x0,'o',label="Euler explicite")
plt.plot(t,x,'*',label="Solution SciPy")
plt.legend()
plt.show()