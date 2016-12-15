# -*- coding: utf-8 -*-
"""
@author: Xavier PESSOLES
"""
import numpy as np
import matplotlib.pyplot as plt


def calculAire(x,y,h):
    """
    Pour un profil (x,y), détermination de l'aire en dessus et en dessous 
    de l'altitude h
    """
    dx = x[1]-x[0]
    haut = []
    bas = []
    for i in range(len(y)):
        if y[i]>h:
            haut.append(y[i])
            bas.append(h)
        else : 
            haut.append(h)
            bas.append(y[i])
            
    aire_sup = 0.5*(haut[0]+haut[-1])
    aire_inf = 0.5*(bas[0]+bas[-1])

    for i in range(1,len(haut)-1):
        aire_sup = aire_sup+haut[i]
        aire_inf = aire_inf+bas[i]
    
    aire_sup = abs(aire_sup*dx)
    aire_inf = abs(aire_inf*dx)
    return aire_inf,aire_sup

def rechercheh(x,y):
    """
    Recherche de l'altitude de la ligne moyenne
    """
    g = min(y)
    d = max(y)
    ii = 0
    c= (d+g)/2
    a_i,a_s = calculAire(x,y,c)

    while abs(a_i-a_s)>0.00001 and ii<100:
        ii=ii+1
        if a_i>a_s :
            g=c
        else :
            d=c
        c= (d+g)/2
        a_i,a_s = calculAire(x,y,c)
        print(ii,g,d,c,abs(a_i-a_s))
    return c
            
def filtrePB(e,h,tau):
    s = [e[0]]
    for i in range(1,len(e)):
        s.append((h*e[i]+tau*s[-1])/(h+tau))
    return s


# Fonction principale
# ====================

# Ouverture du fichier
x=[]
y=[]
fid = open("data/mesures.txt","r")
for ligne in fid : 
    ligne = ligne.split("\t")
    x.append(float(ligne[0]))
    y.append(float(ligne[1]))
fid.close()
plt.plot(x,y)


# Filtrage du signal
h = 0.0005
tau = 1

# Récupération du défaut d'ondulation
y_o = filtrePB(y,h,tau)
#Récuparétion du profil de rugosité
y_r = y2-s
plt.plot(x,y_o)
plt.plot(x,y_r)



plt.axis("equal")
plt.show()
