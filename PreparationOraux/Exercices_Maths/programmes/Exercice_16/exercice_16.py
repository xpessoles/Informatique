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

a,u0 = 1,0.5
n = 10
T = [calcul_un(u0,k,a) for k in range(10)]
N = [k for k in range(n)]
plt.plot(N,T)