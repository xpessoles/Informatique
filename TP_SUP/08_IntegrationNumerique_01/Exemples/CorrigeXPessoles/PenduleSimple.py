#! /usr/bin/env python
# -*- coding: utf-8 -*-

from math import sin,sqrt,pi,radians


def fonc_phi(x,T0,theta_0):
    k=sin(theta_0/2)
    val = (2.*T0/pi)*2/(sqrt(1-k*k*sin(x)**2))
    return val

def rectangle_gauche(fonc,T0,theta_0,a,b,nb_echantillons):
    I=0
    pas = abs(b-a)/nb_echantillons
    for i in range(nb_echantillons):
        I=I+pas*fonc(a+i*pas,T0,theta_0)
    return I
        
def rectangle_droite(fonc,T0,theta_0,a,b,nb_echantillons):
    I=0
    pas = abs(b-a)/nb_echantillons
    for i in range(nb_echantillons):
        I=I+pas*fonc(a+(i+1)*pas,T0,theta_0)
    return I

def trapeze(fonc,T0,theta_0,a,b,nb_echantillons):
    I=0
    pas = abs(b-a)/nb_echantillons
    for i in range(nb_echantillons):
        I=I+pas*0.5*(fonc(a+i*pas,T0,theta_0)+fonc(a+(i+1)*pas,T0,theta_0))
    return I

def periode(T0,theta_0,methode):
    nb_echantillons = 1000
    theta_0=radians(theta_0)
    if methode=="trapeze":
        return trapeze(fonc_phi,T0,theta_0,0,theta_0,nb_echantillons)
    elif methode=="rectangle_g":
        return rectangle_gauche(fonc_phi,T0,theta_0,0,theta_0,nb_echantillons)
    elif methode=="rectangle_d":
        return rectangle_droite(fonc_phi,T0,theta_0,0,theta_0,nb_echantillons)
    else :
        return None

def ecartRelatif(T0,T):
    return 100*abs((T-T0)/T0)

L,g =1,9.81
T0 = 2*pi*sqrt(L/g)
theta_0=60
TRg = periode(T0,theta_0,"rectangle_g")
TRd = periode(T0,theta_0,"rectangle_d")
TTr = periode(T0,theta_0,"trapeze")

ListeAngle,ListePeriode,ListeEcartRelatif=[],[],[]
for i in range(1,91):
    ListeAngle.append(i)
    ListePeriode.append(periode(T0,i,"trapeze"))
    ListeEcartRelatif.append(ecartRelatif(T0,periode(T0,i,"trapeze")))

"""
import matplotlib.pyplot as plt
import numpy as np
plt.plot(ListeAngle,ListePeriode,linewidth=3)
plt.plot(ListeAngle,ListeEcartRelatif,linewidth=3)
plt.grid(True, which="both", linestyle="dotted")
plt.show()
"""

print(TRg)
print(TRd)
print(TTr)
print()
print(ecartRelatif(T0,TRg))
print(ecartRelatif(T0,TRd))
print(ecartRelatif(T0,TTr))
