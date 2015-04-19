# -*- coding: utf-8 -*-
"""
Created on Fri Apr 17 20:35:52 2015

@author: Xavier
"""

import numpy as np
import matplotlib.pyplot as plt
import math
"""
Dimensions de la poutre : L=1m, b=0,1m, e=0,02m
Masse volumique :rho =7800 kg/m3
Nombre d'éléments de poutres : 200
"""
L,b,e = 1,0.1,0.02
rho = 7800
E = 210 *10**9 #Pa
E=200
eta = 0.001
# Nombre de poutres 
n=200
l = L/n
M = L*b*e*rho
m = M/n
k = E*b*e/l 
c= eta * m 
c=0
m=1
k=1

fmax = 10000 #N
f = 1 #Hz
om = 2*math.pi * f

T=10 # Temps de simu : 0,3 s
h = 10**(-1) # Pas de calcul : en ms 2*10**(-6)

tt,x,v,t = 0,[0],[0],[0]
i=0
ff=[0]
while tt<T:
    tt=tt+h
    x.append(h*v[i]+x[i])
    #v.append((h/m)*fmax*math.sin(om*tt)-(k*h/m)*x[i]+((1-c*h)/m)*v[i])
    v.append((h/m)*fmax-(k*h/m)*x[i]+((1-c*h)/m)*v[i])
    t.append(tt)
    ff.append(fmax*math.sin(om*tt))
    i=i+1
print(m,c,k)
print(len(t),len(x),'.')
plt.plot(t,v,'.')
plt.show()



