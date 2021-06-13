# -*- coding: utf-8 -*-
"""
Created on Mon Mar 24 13:10:42 2014

@author: emiliendurif2
"""

#Importation des modules
import scipy as sp
import scipy.integrate as sint
import matplotlib.pyplot as plt


#Définition des fonctions
def f(Y,t):
    vc=8
    vm=1.5    
    dx=vc*(vm*t-Y[0])/(sp.sqrt((vm*t-Y[0])**2+(-Y[1])**2))
    dy=vc*(-Y[1])/(sp.sqrt((vm*t-Y[0])**2+(-Y[1])**2))
    return [dx,dy]



#Programme principal
x0=100
y0=300
t=sp.linspace(0,38,100)
res=sint.odeint(f,[x0,y0],t)

plt.plot(res[:,0],res[:,1])
plt.show()