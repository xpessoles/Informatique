# -*- coding: utf-8 -*-
"""
Created on Fri May  2 08:08:50 2014

@author: Xavier
"""

import math

R = 20000
C = 0.00000001
tau = R*C
E0 = 5
T = 0.005
pas = T/1000
pas_solve = T/1000
f=1000
A = 1

def charge(E0,tau,T,pas):
    t=[]
    uc=[]
    for i in range(int(T/pas)+1):
        ttmp = i*pas
        t.append(ttmp)
        uc.append(E0*(1-math.exp(-ttmp/tau)))
    return t,uc


def euler_ordre1_echelon(pas_solve,tau,T,E0):
    un=[0]
    t=[0]
    for i in range(1,int(T/pas_solve)+1):
        t.append(i*pas_solve)
        un.append(pas_solve*E0/tau+un[i-1]*(1-pas_solve/tau))
    return t,un
    

def euler_ordre1_sin(pas_solve,tau,T,A,f):
    un=[0]
    t=[0]
    for i in range(1,int(T/pas_solve)+1):
        t.append(i*pas_solve)
        un.append(pas_solve*math.sin(2*math.pi*f*pas_solve*i)/tau+un[i-1]*(1-pas_solve/tau))
    return t,un

def fon_sin(pas,T,A,f):
    un=[0]
    t=[0]
    for i in range(0,int(T/pas)+1):
        t.append(i*pas)
        un.append(A*math.sin(2*math.pi*f*i*pas))
    return t,un
    
tc,uc = charge(E0,tau,T,pas) 
tn,un = euler_ordre1_echelon(pas_solve,tau,T,E0)
tns,uns=euler_ordre1_sin(pas_solve,tau,T,A,10*f)
tsin,fsin=fon_sin(pas,T,A,10*f)

plt.close()
#plt.plot(tn,un)
#plt.plot(tc,uc)
plt.plot(tsin,fsin)
plt.plot(tns,uns)

plt.show()   