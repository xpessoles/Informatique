# -*- coding: utf-8 -*-
"""
Created on Mon Jan 12 21:08:25 2015

@author: Xavier
"""
import math

def f_pseudo(t,z,om0):
    return 1-((math.exp(-z*om0*t))/(math.sqrt(1-z*z)))*math.sin(t*om0*math.sqrt(1-z*z)+math.asin(math.sqrt(1-z*z)))

def f_critique(t,om0):
    """
    Fonction permettant de calculer s(t) dans le cas ou z>1. 
    Entrées :
        * t, flt : le temps en secondes
        * om0, flt : la pulsation en rad.s-1
    Sortie : 
        * res, flt : s(t). Ici, sans unité.
    """
    res = 1-(1+t*om0)*math.exp(-om0*t) 
    return res


def f_aperiodique(t,z,om0):
    return 1+(math.exp(-t*om0*(z+math.sqrt(z*z+1))))/(2*(z*math.sqrt(z*z-1)+z*z-1))-(math.exp(-t*om0*(z-math.sqrt(z*z+1))))/(2*(z*math.sqrt(z*z-1)-z*z+1))


def f2_pseudo(tom0,z):
    return 1-((math.exp(-z*tom0))/(math.sqrt(1-z*z)))*math.sin(tom0*math.sqrt(1-z*z)+math.asin(math.sqrt(1-z*z)))

def f2_critique(tom0):
    return 1-(1+tom0)*math.exp(-tom0) 
    
def f2_aperiodique(tom0,z):
    return 1+(math.exp(-tom0*(z+math.sqrt(z*z-1))))/(2*(z*math.sqrt(z*z-1)+z*z-1))-(math.exp(-tom0*(z-math.sqrt(z*z-1))))/(2*(z*math.sqrt(z*z-1)-z*z+1))

    
def f_s(tom0,z) :
    """
    Fonction permettant de calculer la réponse indicielle d'un système du second ordre. 
    Entrées : 
        * tom0, flt : temps de réponse réduit
        * z, flt : coefficient d'amortissement
    Sortie : 
        * s(tom0,z)
    """
    if z<0 :
        return None
    elif z<1 :
        return f2_pseudo(tom0,z)
    elif z==1:
        return f2_critique(tom0)
    else : 
        return f2_aperiodique(tom0,z)


def trace_s(z):
    x = []
    y = []
    for i in range(11):
        t = i
        x.append(t)
        y.append(f_s(t,z))
    plot(x,y)

def trace_s(z):
    x = []
    y = []
    n=1000
    for i in range(n+1):
        t = 10*i/n
        x.append(t)
        y.append(f_s(t,z))
    plot(x,y)

# Appels de la fonction trace
#trace_s(0.4)
#trace_s(0.7)


def is_in_strip(x):
    """
    Fonction permettant de savoir si une valeur est dans la bande des + ou - 5% de la valeur finale.
    Entrée : 
        x, flt : réel
    Sortie : 
        True si la valeur est dans la bande à + ou - 5%
        False si la valeur n'est pas dans la bande à + ou - 5%
    """
    if x>.95 and x<1.05:
        return True
    else:
        return False

def calcul_tom0(z,tom0=500):
    """
    Recherche du temps de réponse à 5%
    Entrées : 
       * z, flt : coefficient d'amortissement
       * tom0 (flt, optionnel) : si non précisé, on calcule le temps de réponse en partant de tom0 = 500
    Sortie : 
       * tom0 (flt) : temps de réponse à 5%
    """
    pas_tom0=0.05
    x = f_s(tom0,z) 
    if z<0.7:
        while is_in_strip(x) :
            tom0  = tom0 - pas_tom0
            x = f_s(tom0,z)
        tom0=tom0+pas_tom0
    else :
        while not is_in_strip(x) :
            tom0  = tom0 + pas_tom0 
            x = f_s(tom0,z)
        tom0=tom0-pas_tom0
    return tom0


def mystere(nb,tab):
    """ 
    Entrées : 
        * nb,int -- nombre entier
        * tab,list -- liste de nombres entiers triés
    Sorties : 
        * 
    """
    g, d = 0, len(tab)-1
    while g <= d:
        m = (g + d) // 2
        print(m)
        if tab[m] == nb:
            return m
        if tab[m] < nb:
            g = m+1
        else:
            d = m-1
    return None
#mystere(4,[1,2,3,4,5,6,7,8,9])

xx,yy = [],[]
n = 1000
z = 0.01
tom0 = 500
pasz = 0.001
while z<=100:
    #print(z)
    if z<0.7:
        tom0=calcul_tom0(z,tom0)
    else :
        tom0=calcul_tom0(z,0)
  
    if z<0.1:
        pasz = 0.001
    elif z<1:
        pasz = 0.01
    elif z<10:
        pasz = 0.1
    else :
        pasz = 1
    print(z,pasz)
    xx.append(z)
    yy.append(tom0)
    z=z+pasz


"""
import matplotlib.pyplot as plt
import numpy as np

plt.plot(xx,yy,label="Temps de réponse réduit $tr \\omega_0$")
plt.xlabel("Coefficient d'amortissement $\\xi$")
plt.ylabel("Temps de réponse réduit $tr \\omega_0$")
plt.title("Temps de réponse réduit d'un système du 2nd ordre")
plt.legend()
plt.loglog()
plt.grid(which="major",axis="x",linewidth=1.5, linestyle='-')
plt.grid(which="major",axis="y",linewidth=1.5, linestyle='-')
plt.grid(which="minor",axis="x",linewidth=0.75, linestyle='-', color='0.75')
plt.grid(which="minor",axis="y",linewidth=0.75, linestyle='-', color='0.75')
"""
