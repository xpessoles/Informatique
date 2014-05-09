# -*- coding: utf-8 -*-
"""
Created on Fri May  2 08:08:50 2014

@author: Xavier
"""

import math

M = 10
D = 0.0573
L = 630*10**(-6)
R = 4
k = 1/66
ke = 0.0342
kt = ke
J =   47*10**(-7)

a = 2*ke/(D*k)
b = (R/kt)*(M*D*D*k*k/4 + J)*(2/(D*k))
c = (L/kt)*(M*D*D*k*k/4 + J)*(2/(D*k))



def solveEq(Tcalcul,pas,u0):
    v1=[]
    v2=[]
    v1.append(0.)
    v2.append(0.)
    temps = []
    temps.append(0.)
    for i in range (1,int(Tcalcul/pas)+1):
        v2.append(pas*v1[i-1]+v2[i-1])
        v1.append(pas*(u0-a*v2[i-1]-b*v1[i-1])/(c) + v1[i-1])
        temps.append(pas*i)
        
    return v1,v2,temps



from scipy.integrate import odeint

def emeric(v_dv_ddv,t):
    v,dv = v_dv_ddv
    return [dv,(21.3-a*v-b*dv)/(c)]
ttt=linspace(0,0.3,1000)
sol = odeint(emeric, (0, 0), ttt)


t=0.3
p=t/1000
v1,v2,tt = solveEq(t,p,21.3)

plt.plot(tt,v2) # affichage du calcul à la main
#plt.plot(sol) # affichage de la solution Scipy