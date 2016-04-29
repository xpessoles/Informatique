#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = "Xavier PESSOLES"

import matplotlib.pyplot as plt

# EXERCICE 16
# Question 1 
# ==========

def calcul_un(u0,n,a):
    if n ==0 :
        return u0
    else : 
        un = calcul_un(u0,n-1,a)
        return (1+a*(1-un))*un

def proc(a1,c,a2,u0) :
    a=[]
    un = []
    for i in range (100,201):
        jf=int((a2-a1)/c)
        for j in range(jf+1):
            a.append(a1+j*c)
            un.append(calcul_un(u0,i,a1+j*c))
    return a,un
     
     
"""     
a,u0 = 1,0.5
n = 10
T = [calcul_un(u0,k,a) for k in range(10)]
N = [k for k in range(n)]
plt.plot(N,T)
"""
a,un=proc(2,0.005,3,.5)
plt.plot(a,un,'r.')
a,un=proc(2.84,0.0001,2.86,.5)
plt.plot(a,un,'b*')

plt.show()
