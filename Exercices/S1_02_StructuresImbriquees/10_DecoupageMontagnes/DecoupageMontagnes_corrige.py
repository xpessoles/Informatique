# -*- coding: utf-8 -*-
"""
@author: xpessoles@lamartin.fr
"""
# === Import des Modules ===
import math as m
import random as rd
import numpy as np
import matplotlib.pyplot as plt

# === Génération d'un profil de montagne ===
les_x = np.linspace(-1.1,1.3,1000)
les_y1 = 0.6366 * np.cos(6.2813*les_x-np.pi/2)
les_y2 = 0.2122 * np.cos(18.85*les_x-np.pi/2)
les_y = les_y1+les_y2-0.4*les_x*les_x

les_x = np.linspace(0,60*14,1000)
les_y = 800*les_y + 1500
alt = les_y

# plt.ylabel("Altitude [m]")
# plt.plot(les_x,les_y,label = "Profil")
# plt.legend()
# plt.grid()
# plt.show()

# ==========================================

def plus_haut(L:list) -> float :
    maxi = L[0]
    for el in L :
        if el>maxi :
            maxi = el
    return maxi

def plus_haut_indice(L:list) -> float :
    m = 0
    for i in range(len(L)):
        if L[i]>L[m] :
            m = i
    return m

def deniveles(alt:list) -> list:
    pos,neg = 0,0
    for i in range(1,len(alt)) :
        delta = alt[i]-alt[i-1]
        if  delta > 0:
            pos = pos + delta
        else :
            neg = neg + delta
    return [pos,neg]

def moyenne(alt:list):
    somme = 0
    for a in alt :
        somme = somme + a
    return somme/len(alt)

def indice_premier_PNM(alt:list):
    m = moyenne(alt)
    indice = -1
    for i in range(len(alt)-1):
        if alt[i]<m and alt[i+1]>m:
            return i
    return indice



def indices_PNM(alt:list):
    m = moyenne(alt)
    les_PNM = []
    for i in range(len(alt)-1):
        if alt[i]<m and alt[i+1]>m:
            les_PNM.append(i)
    return les_PNM


def liste_alt_min(alt:list):
    les_PNM = indices_PNM(alt)
    les_min = []
    for i in range(len(les_PNM)-1):
        mini = les_PNM[i]
        for j in range(les_PNM[i],les_PNM[i+1]):
            if alt[j]<alt[mini]:
                mini = j
        les_min.append(mini)
    return les_min

def creer_montagnes(alt):
    pam = liste_alt_min(alt)
    montagnes = []
    mont = []
    for i in range(0,pam[0]):
        mont.append(alt[i])
    montagnes.append(mont)
    for i in range(len(pam)-1):
        mont = []
        for j in range(pam[i],pam[i+1]):
            mont.append(alt[j])
        montagnes.append(mont)
    mont = []
    for i in range(pam[-1],len(alt)):
        mont.append(alt[i])
    montagnes.append(mont)
    return montagnes

pam = liste_alt_min(alt)
les_x1 = les_x[0:pam[0]]
les_x2 = les_x[pam[0]:pam[1]]
les_x3 = les_x[pam[1]:]
m = creer_montagnes(alt)
plt.plot(les_x1,m[0])
plt.plot(les_x2,m[1])
plt.plot(les_x3,m[2])
plt.show()