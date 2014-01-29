# -*- coding: utf-8 -*-
"""
@author: Xavier Pessoles
"""

import numpy as np
import matplotlib.pyplot as plt
from math import pi
v0 = 360000/3600 # 360 km/h record de Joe Miller
xT = 400
yT = -10
g = 9.81
m = 45.93/1000
dT = 108./1000. #diametre trou
db = 42.67/1000. #diametre balle
def tir_parabolique():
    # Reseau de courbe en tir parabolique
    t = np.linspace(0,8,200)
    alpha = 20*2*pi/360
    plt.plot(v0*np.cos(alpha)*t,
         -0.5*g*t*t+v0*np.sin(alpha)*t
      ,label="$\\alpha = 20^o$",linewidth=3)
    alpha = 30*2*pi/360
    t = np.linspace(0,11,200)
    plt.plot(v0*np.cos(alpha)*t,
         -0.5*g*t*t+v0*np.sin(alpha)*t
      ,label="$\\alpha = 30^o$",linewidth=3)
    alpha = 40*2*pi/360
    t = np.linspace(0,14,200)
    plt.plot(v0*np.cos(alpha)*t,
         -0.5*g*t*t+v0*np.sin(alpha)*t
      ,label="$\\alpha = 40^o$",linewidth=3)

    
    plt.grid(True, which="both", linestyle="dotted")
    plt.legend(loc='lower left', fancybox=True, shadow=True, prop=dict(size=10))
    #plt.xlabel("Temps en $s$")
    #plt.ylabel("Position en $m$")
    #plt.axis([0,xf,-1.2,1.2])
    plt.show()

def courbe_alpha():
    # courbe donnant l'équation a resoudre
    t = np.linspace(0,1.4,200)
    plt.plot(t,
         yT+0.5*g*((xT*xT)/(v0*v0*np.cos(t)*np.cos(t)))-xT*np.tan(t)
      ,label="$f(\\alpha)$ - Trou à 400 m avec un surpolomb de 10 m",linewidth=3)
    plt.grid(True, which="both", linestyle="dotted")
    plt.legend(loc='lower left', fancybox=True, shadow=True, prop=dict(size=10))
    #plt.xlabel("Temps en $s$")
    #plt.ylabel("Position en $m$")
    #plt.axis([0,xf,-1.2,1.2])
    plt.show()


def tir_parabolique(alpha):
    # tir pour un aplha donne
    t = np.linspace(0,4.2,200)
    plt.plot(v0*np.cos(alpha)*t,
         -0.5*g*t*t+v0*np.sin(alpha)*t
      ,label="$\\alpha = 20^o$",linewidth=3)
    
    
    plt.grid(True, which="both", linestyle="dotted")
    plt.legend(loc='lower left', fancybox=True, shadow=True, prop=dict(size=10))
    #plt.xlabel("Temps en $s$")
    #plt.ylabel("Position en $m$")
    #plt.axis([0,xf,-1.2,1.2])
    plt.show()

def fonc(t):
    return yT+0.5*g*((xT*xT)/(v0*v0*np.cos(t)*np.cos(t)))-xT*np.tan(t)

def dichotomie(a,b,epsilon):
    assert fonc(a) * fonc(b) <= 0 and epsilon > 0
    g, d = a, b
    fg, fd = fonc(g), fonc(d)
    i=0
    while (d - g) > 2 * epsilon:
        #print(i)
        i=i+1
        m = (g + d) / 2.
        fm = fonc(m)
        if fg * fm <= 0:
            d, fd = m, fm
        else:
            g, fg = m, fm
    return (g+d)/2,i

def courbe_erreur():
    tt=[]
    tab_op =[]
    for i in range(0,1000) :
        t = 0.000000000001+i*(0.0000001-0.000000000001)/1000
        res,op = dichotomie(0.000000000001,1.,t)
        tt.append(t)
        tab_op.append(op)

    plt.plot(tt,tab_op,label="$Nb op$",linewidth=3)
    plt.grid(True, which="both", linestyle="dotted")
    plt.legend(loc='lower left', fancybox=True, shadow=True, prop=dict(size=10))
    #plt.xlabel("Temps en $s$")
    #plt.ylabel("Position en $m$")
    #plt.axis([0,xf,-1.2,1.2])
    plt.show()
#courbe_erreur()
#tir_parabolique(1.3)
#courbe_alpha()
#tir_parabolique()
res = dichotomie(0.0000000001,1.,0.01)[0]*180/pi
print(res)
tir_parabolique(dichotomie(0.0000000001,1.,0.01)[0])
