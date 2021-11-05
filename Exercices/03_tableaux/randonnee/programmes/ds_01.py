# -*- coding: utf-8 -*-
"""
Created on Wed Oct 27 21:54:13 2021

@author: xpess
"""

lat = [45.461516, 45.461448, 45.461383, 45.461641, 45.461534, 45.461595, 45.461562]
long = [6.44461, 6.444426, 6.444239, 6.444035, 6.443879, 6.4437, 6.443521]
alt = [1315.221, 1315.702, 1316.182, 1316.663, 1319.144, 1317.634, 1318.105]
tps = [1597496965, 1597496980, 1597496995, 1597496710, 1597496725, 1597496740, 1597496755]

import math as m
import random as rd

def conversion(L:list) -> list : 
    tab = []
    for el in L : 
        tab.append(m.radians(el))
    return tab

latr = conversion(lat)
longr = conversion(long)

def plus_haut_index(L:list) -> float :
    m = 0
    for i in range(len(L)):
        if L[i]>L[m] :
            m = i  
    return m

def coords_plus_haut(alt:list, long:list, lat:list)-> list :
    m = plus_haut_index(alt)
    return[lat[m],long[m]]

def deniveles(alt:list) -> list:
    pos,neg = 0,0
    for i in range(1,len(alt)) : 
        delta = alt[i]-alt[i-1]
        if  delta > 0: 
            pos = pos + delta
        else : 
            neg = neg + delta
    return [pos,neg]


#### 
# Création d'un profil d'altitude
import numpy as np
import matplotlib.pyplot as plt
les_x = np.linspace(-1.1,1.3,1000)

les_y1 = 0.6366 * np.cos(6.2813*les_x-np.pi/2)
les_y2 = 0.2122 * np.cos(18.85*les_x-np.pi/2)
les_y = les_y1+les_y2-0.4*les_x*les_x


les_x = np.linspace(0,60*14,1000)
les_y = 800*les_y + 1500
plt.xlabel("Temps [min]")
plt.ylabel("Altitude [m]")
plt.plot(les_x,les_y,label = "Profil")
plt.legend()

#plt.plot(les_x,-les_x*les_x)
plt.grid()

plt.savefig("fig_01.png")


alt = [e for e in les_y]
def moyenne(alt:list):
    somme = 0
    for a in alt : 
        somme = somme + a
    return somme/len(alt)  

m = moyenne(alt)
les_m = [m for i in range(len(alt))]
plt.plot(les_x,les_m,label = "Valeur moyenne")
plt.legend()
plt.savefig("fig_02.png")

def indice_premier_PNM(alt:list):
    m = moyenne(alt)
    indice = -1
    for i in range(len(alt)-1):
        if alt[i]<m and alt[i+1]>m:
            return i
    return indice


prems = indice_premier_PNM(alt)


def indices_PNM(alt:list):
    m = moyenne(alt)
    les_PNM = []
    for i in range(len(alt)-1):
        if alt[i]<m and alt[i+1]>m:
            les_PNM.append(i)
    return les_PNM

les_PNM = indices_PNM(alt)

x_PNM = [les_x[i] for i in les_PNM]
y_PNM = [alt[i] for i in les_PNM]
plt.plot(x_PNM,y_PNM,'or',label = "PNM")
plt.legend()
plt.plot(les_x[prems],alt[prems],'sg',label = "Premier PNM")
plt.legend()
plt.savefig("fig_03.png")

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

les_min = liste_alt_min(alt)
            
x_min = [les_x[i] for i in les_min]
y_min = [alt[i] for i in les_min]
plt.plot(x_min,y_min,'ok',label = "PAM")
plt.legend()
plt.savefig("fig_04.png")


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

def creer_montagnes2(alt,les_x):
    pam = list_alt_min(alt)
    montagnes = []
    mont = []
    les_t = []
    t = []
    for i in range(0,pam[0]):
        mont.append(alt[i])
        t.append(les_x[i])
    
    montagnes.append(mont)
    les_t.append(t)
    
    for i in range(len(pam)-1):
        mont = []
        t = []
        for j in range(pam[i],pam[i+1]):
            mont.append(alt[j])
            t.append(les_x[j])
        montagnes.append(mont)
        les_t.append(t)
    mont = []
    t=[]
    for i in range(pam[-1],len(alt)):
        mont.append(alt[i])
        t.append(les_x[i])
    montagnes.append(mont)
    les_t.append(t)
    return montagnes,les_t

montagnes,ts = creer_montagnes2(alt,les_x)

plt.clf()
plt.grid()
plt.plot(ts[0],montagnes[0],linestyle = 'solid',label = 'Montagne 1')
plt.plot(ts[1],montagnes[1],linestyle = 'dotted',label = 'Montagne 2')
plt.plot(ts[2],montagnes[2],linestyle = 'dashed',label = 'Montagne 3')
plt.legend()
plt.savefig("fig_05.png")
"""for i in range(len(montagnes)):
    plt.plot(ts[i],montagnes[i])
"""




"""
def distance_totale(alt:list, long:list, lat:list)-> float :
    D = 0
    for i in range(1,len(alt)):
        c1  = [alt[i-1],lat[i-1],long[i-1]]
        c2  = [alt[i],lat[i],long[i]]
        D = D + distance(c1,c2)
    return D"""


def voisins(p:list) -> list :
    x = p[0]
    y = p[1]
    v = [[x+1,y],[x,y+1],[x-1,y],[x,y-1]]
    return v

def positions_possibles(p:list, atteints:list)-> list :
    possibles = []
    voi = voisins(p)
    for v in voi : 
        if v not in atteints: 
            possibles.append(v)
    return possibles

def genere_chemin_naif(n:int) : 
    chemin = [[0,0]]
    while len(chemin)<n :
        possibles = (chemin[-1],chemin)
        if len(possibles) == 0 : 
            return None 
        else : 
            chemin.append(rd.choice(possibles))
    return chemin