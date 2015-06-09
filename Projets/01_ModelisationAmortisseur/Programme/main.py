#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__      = "Xavier Pessoles"
__email__ = "xpessoles.ptsi@free.fr"

import matplotlib.pyplot as plt
import numpy as np
#from biblio import *

# Raideur du ressort en N/m
k = 1000000
# Coefficient d'amortissement en N.s/m
c = 50
# Masse en kg
m = 1000
# Pas de temps en seconde
h = 0.001
# Temps total en s
T = 1
# Initialisation 
x0,v0 = 0,0

import math

def f_sin(A,omega,t):
    """
    Fonction retournant la valeur de a*sin(omega*t).
    Entrées :
     * A,flt : Amplitude du sinus
     * omega,flt : pulsation du sinus
    Sortie :
     res,flt : résultat
    """
    return A*math.sin(omega*t)
    
    
    
def solve_eq(m,k,c,x0,v0,h,T,f):
    """
    Résolution de l'équation différentielle du second ordre pour un système
    masse amortisseur.
    Entrées : 
     * m,flt : masse en kg
     * k,flt : raideur du ressort en N/m
     * c,flt : coefficient d'amortissement en N.s/m
     * x0,flt : position initiale en m
     * v0,flt : vitesse initiale en m/s
     * h,flt : pas de temps de calcul
     * T,flt ; temps de simulation
     * f,lst : liste de valeurs prise par la fonction.
    Sortie : 
     * 
    
    """
    res=[x0,v0]
    t=h
    temps = [0,t]
    i=1
    while t<=T:
        t=t+h
        i=i+1
        res.append((1/(m+k*h*h+c*h))*(h*h*f[i]+res[-1]*(2*m+c*h)-m*res[-2]))
        temps.append(t)
        
    return temps,res

ff = [f_sin(1,1,x) for x in range(int(T/h)+1)]

t,x = solve_eq(m,k,c,x0,v0,h,T,ff)
plt.plot(t,t)
plt.show()
