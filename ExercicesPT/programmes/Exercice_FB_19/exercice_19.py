#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = "Xavier PESSOLES"


# EXERCICE 19
# Question 1 
# ==========
import numpy as np
import scipy.integrate as sci
import matplotlib.pyplot as plt

def fonction_PP(X,t,a,b,c,d):
    return [a*X[0]-b*X[0]*X[1],-c*X[1]+d*X[0]*X[1]]

def fonction_PP2(X,t):
    a,b,c,d = 1,1,1,1
    return [a*X[0]-b*X[0]*X[1],-c*X[1]+d*X[0]*X[1]]

# Question 2 
# ==========
# Conditions initiale : 
X0=[1,2]
t = np.linspace(0,20,1000)
res = sci.odeint(fonction_PP2,X0,t)

# Question 3 
# ==========
plt.figure()
plt.plot(t,res[:,0])
plt.plot(t,res[:,1])


# Question 4 
# ==========
plt.figure()
plt.plot(res[:,0],res[:,1])
plt.axis("equal")


plt.show()