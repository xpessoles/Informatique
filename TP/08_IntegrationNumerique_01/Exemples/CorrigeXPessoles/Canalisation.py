# -*- coding: utf-8 -*-
#! /usr/bin/env python

global D
D=2.8*10**(-7)
global T0
T0 =278
global T1
T1=258
global tf
tf=10

from math import pi,exp

def erf(x,nb):
    """
    x : borne supérieure de l'intégrale
    nb : nombre d'échantillons
    """
    if x>=0:
        return trapeze(fexp,0,x,nb)
    else :
        return None

def fexp(u):
    return (2/math.pi)*exp(-u*u)

def trapeze(f,a,b,nb):
    res = 0
    pas = abs(b-a)/nb
    for i in range(nb):
        x0 = a+pas*i
        x1 = a+pas*(i+1)
        res = res + (x1-x0)*0.5*(f(x0)+f(x1))
    return res


def temp(z,t):
  
    res = T1+(T0-T1)*erf(z/(math.sqrt(D*t)),1000)
    return res 
z = 1 #m
t = 10 * 24 * 3600
print(temp(z,t)-273.15)
""" 
#
"""


