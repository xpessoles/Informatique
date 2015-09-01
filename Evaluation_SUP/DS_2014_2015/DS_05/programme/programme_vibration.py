# -*- coding: utf-8 -*-
"""
Created on Fri Apr 17 20:35:52 2015

@author: Xavier
"""

import numpy as np
import matplotlib.pyplot as plt
import math
"""
Dimensions de la poutre : L=1m, b=0,1m, e=0,02m
Masse volumique :rho =7800 kg/m3
Nombre d'éléments de poutres : 200
"""
L,b,e = 1,0.1,0.02
rho = 7800
E = 210 *10**9 #Pa
eta = 0.001
# Nombre de poutres 
n=200
l = L/n
M = L*b*e*rho
m = M/n
k = E*b*e/l 
c= eta * m 

k=20000
c = 10

print(c,k,m)
fmax = 1 #N
f = 1 #Hz
om = 2*math.pi * f

T=0.1 # Temps de simu : 0,3 s
#h = 10**(-3) # Pas de calcul : en ms 2*10**(-6)
h=T/2000


def euler_explicite():
    # Solution explicite
    tt_exp,x_exp,v_exp,t_exp = 0,[0],[0],[0]
    i=0
    ff_exp=[0]
    print("Calcul explicite")
    while tt_exp<T:
        tt_exp=tt_exp+h
        x_exp.append(h*v_exp[i]+x_exp[i])
        #v.append((h/m)*fmax*math.sin(om*tt)-(k*h/m)*x[i]+((1-c*h)/m)*v[i])
        v_exp.append((h/m)*fmax-(k*h/m)*x_exp[i]+(1-c*h/m)*v_exp[i])
        t_exp.append(tt_exp)
        ff_exp.append(fmax*math.sin(om*tt_exp))
        i=i+1
    print("Fin calcul explicite")
    return t_expl,x_exp


def euler_implicite():
    # Solution implicite
    tt_imp,x_imp,v_imp,t_imp = 0,[0],[0],[0]
    i=0
    ff_imp=[0]
    print("Calcul implicite")
    while tt_imp<T:
        tt_imp=tt_imp+h
        x_imp.append(((m+c*h)/(m+c*h+h*h+k))*(x_imp[i]+(h/(m+c*h))*(h*fmax-m*v_imp[i])))
        v_imp.append((x_imp[i+1]-x_imp[i])/h)
        t_imp.append(tt_imp)
        ff_imp.append(fmax*math.sin(om*tt_exp))
        i=i+1
    print("Fin calcul implicite")
    return t_imp,x_imp



def f_omega(Tsimu,h,fmax,fsign):
   """
   Entrées :
       * Tsimu (flt) : temps de la simulation en seconde
       * h (flt) : pas de temps de a simulation
       * fmax (flt) : amplitude du signal (en Newton)
       * fsign (flt) : fréquence du signal (en Hertz)
   Sortie : 
       * F (list) : liste des valeurs de la fonction f_n (t)= fmax sin (omega *t)
   """
   omega  = 2*math.pi*fsign
   t=0 
   F = []
   while t<Tsimu :
       F.append(fmax*math.sin(omega*t))
       t=t+h
       #print(t)
   return F
    

def generate_tridiagonale(n,c,k):
    T=[]
    for i in range (n):
        ligne=[]
        for j in range (n):
            ligne.append(0.0)
        T.append(ligne)
    
    for i in range(n):
        T[i][i]=k
    for i in range(n-1):
        T[i][i+1]=c
    for i in range(1,n):
        T[i][i-1]=c
    return T
    
T = generate_tridiagonale(4,1.0,2.0)
D = generate_tridiagonale(4,0,0)
for i in range(len(T)):
    print(T[i][:])

print()
print(T[0][:])
for i in range(len(T)):
    D[0][i]=T[0][i]
for i in range(1,len(T)):
    coef = T[i][i-1]/T[i-1][i-1]
    #print(coef)
    for k in range(len(T)):
        T[i][k]=T[i][k]-(coef)*T[i-1][k]
    #print(T[i])
    
print()
for i in range(len(T)):
    print(T[i][:])
# print(len(t),len(x),'.')
# plt.plot(t_imp,x_imp,'.')
# plt.plot(t_exp,x_exp,'.')
#plt.plot(F)
plt.show()



