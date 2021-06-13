# -*- coding: utf-8 -*-
"""
Created on Tue Mar  4 20:44:11 2014

@author: ericguichet
"""

# importation des modules

from scipy.integrate import odeint
import numpy as np
import matplotlib.pyplot as plt

# declaration des fonctions

def F(X,t):
    vm=1.5
    vc=8.0
    vecteur_CM=np.array([vm*t-X[0],-X[1]])
    return vc*vecteur_CM/np.linalg.norm(vecteur_CM)

# programme principal

X0=np.array([100,300])
t=np.linspace(0,38,100)
X=odeint(F,X0,t)
plt.axis([0,100,0,300])
plt.plot(X[:,0],X[:,1])
plt.savefig('trajectoire_du_chien.png')
plt.show()
