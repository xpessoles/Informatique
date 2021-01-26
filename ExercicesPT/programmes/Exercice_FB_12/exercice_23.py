#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = "Xavier PESSOLES"


# EXERCICE 23
# Question 1 
# ==========
import matplotlib.pyplot as plt
import math
import numpy as np

import scipy.integrate as spi
n=1
N=10000

def solve_eq(N,n,t0,tf):
    x = np.linspace(t0,tf,N)
    h = (tf-t0)/N
    y1=[0]
    y2=[1]
    for i in range(1,N):
        y1.append(h*y2[i-1]+y1[i-1])
        y2.append(h*(math.sin(n*x[i-1])+y1[i-1]-10*y2[i-1])+y2[i-1])
         
    return x,y1

def solve_syst(N,n,t0,tf):
    t = np.linspace(t0,tf,N)
    A=np.array([[0,1],[1,-10]])
    I=np.array([[1,0],[0,1]])
    X0 = np.array([[0],[1]])
    X = [X0]
    h= (tf-t0)/N
    for i in range(1,N):
        B=np.array([[0],[math.sin(n*t[i])]])
        Xk = np.dot(h*A+I,X0)+h*B
        X.append(Xk)
        X0=Xk
    res = [x[0][0] for x in X]
    return (t,res)

def fonction_f(X,t,n):
   return [X[1],X[0]-10*X[1]+np.sin(n*t)]


les_t=np.linspace(0,7,N)
for i in range(0,8):
    #les_x,les_y = solve_eq(N,i,0,7)
    #plt.plot(les_x,les_y)
    #les_x,les_y = solve_syst(N,i,0,7)
    #plt.plot(les_x,les_y)
    res = spi.odeint(fonction_f,[0,1],les_t,(i,))
    plt.plot(les_t,res[:,0])
plt.show()
    
    
