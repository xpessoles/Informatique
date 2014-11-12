#!/usr/bin/python
# -*- coding: utf-8 -*-


import numpy as np
import pylab as pl
import math

# =========================
# Définition des fonctions
# =========================
def calcul_bezier_3(u,p0,p1,p2,p3):
    """Calcul des coordonnées d'un point sur une courbe de Bézier de degré 3.
    Keyword arguments :
    u : coordonnée paramétrique comprise entre 0 et 1
    p0,p1,p2,p3,p4 : tableaux constitués de deux réels
    """

    c=[]

    #Calcul de la coordonnée suivant x de la courbe
    c.append((1-u)*(1-u)*(1-u)*p0[0]
             +3*u*(1-u)*(1-u)*p1[0]
             +3*u*u*(1-u)*p2[0]
             +u*u*u*p3[0])

    #Calcul de la coordonnée suivant y de la courbe
    c.append((1-u)*(1-u)*(1-u)*p0[1]
             +3*u*(1-u)*(1-u)*p1[1]
             +3*u*u*(1-u)*p2[1]
             +u*u*u*p3[1])
    
    return c


def binomiaux(n,i):
    """Calcul des coefficients binomiaux selon la formule $\dfrac{!n}{!(n-i)!i}$

    Keyword arguments :
    n,i : deux entiers

    Retourne un réel
    """
    res = factorielle(n)/(factorielle(n-i)*factorielle(i))
    return res


    
    
def factorielle(n):
    if n==0:
        return 1
    else :
        i=1    
        res=1
        while i<=n:
            res=res*i
            i+=1
        return res

def bernstein(i,n,u):
    """ Calcul des fonctions de Bernstein

    Keyword Arguments :
    i : 
    n : degré du polynome
    u : paramètre
    """

    res=binomiaux(n,i)*(u**i)*((1-u)**(n-i))
    return res

def calcul_bezier_n(u,tab_p):
    """Calcul des coordonnées d'un point sur une courbe de Bézier de degré n.

    Keyword arguments :
    u : coordonnée paramétrique comprise entre 0 et 1
    tab_p : tableaux constitués de tableaux de poles
    
    """

    #Calcul du degré du polynome
    deg = len(tab_p)

    res=[]
    x=0
    y=0
    for i in range(0,deg):
        x=x+bernstein(i,deg-1,u)*tab_p[i][0]
        y=y+bernstein(i,deg-1,u)*tab_p[i][1]

    #Calcul de la coordonnée suivant x de la courbe
    res.append(x)
    res.append(y)

    return res






# SHARK 
"""
a=[0,0];p.append(a);polx.append(a[0]);poly.append(a[1])
a=[40,0];p.append(a);polx.append(a[0]);poly.append(a[1])
a=[0,60];p.append(a);polx.append(a[0]);poly.append(a[1])
a=[80,60];p.append(a);polx.append(a[0]);poly.append(a[1])
a=[80,60];p.append(a);polx.append(a[0]);poly.append(a[1])
a=[80,60];p.append(a);polx.append(a[0]);poly.append(a[1])
a=[80,60];p.append(a);polx.append(a[0]);poly.append(a[1])
a=[80,60];p.append(a);polx.append(a[0]);poly.append(a[1])
a=[80,60];p.append(a);polx.append(a[0]);poly.append(a[1])
a=[0,0];p.append(a);polx.append(a[0]);poly.append(a[1])
a=[80,0];p.append(a);polx.append(a[0]);poly.append(a[1])
#px=[0,40,0,80,0,80]
#py=[0,0,60,60,0,0]
inc = 0.001
"""

# Forme
p=[]
a=[5,5];p.append(a)
a=[15,45];p.append(a)
a=[35,5];p.append(a)
a=[45,45];p.append(a)
px=[5,15,35,45]
py=[5,45,5,45]
inc = 0.001


# Calcul des points de la courbe
x=[]
y=[]
u=0
while u<=1:
    courbe=[]
    courbe.append(calcul_bezier_n(u,p))
    x.append(courbe[0][0])
    y.append(courbe[0][1])
    u += inc

# Affichage avec matplotib
#pl.plot(x,y)
#Affichage du polynome caractéristique
#pl.plot(polx,poly)

fig = plt.figure()
ax = fig.gca()
params = {'legend.fontsize': 8,'legend.linewidth': 1}
plt.rcParams.update(params)
plot(x,y,'r',linewidth=2, label='Courbe de Bézier')
plot(px,py,'b',linewidth=2)
plot(px,py,'bo',linewidth=4, label='Polygone de contrôle (Pôles)')
axis([0,50,0,50])
pl.grid()
#pl.axis('equal')
pl.show()





"""
u=0
xx=[]
yy=[]
while u<=1:
    courbe=[]
    courbe.append(calcul_bezier_3(u,p0,p1,p2,p3))
    xx.append(courbe[0][0])
    yy.append(courbe[0][1])
    u += inc
"""

