#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = "Xavier PESSOLES"

# EXERCICE 12

b,w = 0.5,6
# Question 1 
# ==========
import numpy as np
def fonc_p(t):
    return [np.cos(t)+b*np.cos(w*t),np.sin(t)+b*np.sin(w*t)]

def fonc_v(t):
    return [-np.sin(t)-b*w*np.sin(w*t),np.cos(t)+b*w*np.cos(w*t)]

def fonc_a(t):
    return [-np.cos(t)-b*w*w*np.cos(w*t),-np.sin(t)-b*w*w*np.sin(w*t)]
    
    
# Question 2
# ==========
L=np.linspace(-np.pi,np.pi,200)

# Question 3
# ==========
import matplotlib.pyplot as plt
p = fonc_p(L)
#plt.plot(p[0],p[1])
#plt.axis("equal")
#plt.show()
   
# Question 4
# ==========
def fonc_d(t):
    xp,yp = fonc_v(t)
    xpp,ypp = fonc_a(t)
    return (xp**2 + yp**2)/(xp*ypp-yp*xpp)

def fonc_c(t):
    fd = fonc_d(t)
    x,y = fonc_p(t)
    xp,yp = fonc_v(t)
    return [x-fd*yp,y+fd*xp]

# Question 5
# ==========
les_xc  = []
les_yc  = []
c = fonc_c(L)
#plt.plot(c[0],c[1])

# Question 6
# ==========
from math import sqrt
def distance(p):
    """
    Calcule la longueur du profil p.
    Entrée : 
     * p(lst) : liste [les_x,les_y]
    Sortie : 
     * L(flt) : longueur du profil.
    """
    L=0
    for i in range(len(p[0])-1):
        x0 = p[0][i]
        y0 = p[1][i]
        x1 = p[0][i+1]
        y1 = p[1][i+1]
        L = L+ sqrt((x1-x0)**2+(y1-y0)**2)
    return L

les_dt = []
les_dist = []
for i in range(10,2000,1) :
    dt = 2*np.pi/i
    L=np.linspace(-np.pi,np.pi,i)
    p = fonc_p(L)
    d = distance(p)
    les_dt.append(dt)
    les_dist.append(d)
    
    
plt.plot(les_dt,les_dist)
plt.show()       