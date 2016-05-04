#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = "Xavier PESSOLES"


# EXERCICE 22
# Question 1 
# ==========
import matplotlib.pyplot as plt
import math

I_th = 8*math.log(2)-3

# Question 2
# ==========
def fonc(x):
    return math.log(x)
    
def calc_int_trap(a,b,n):
    res = 0
    pas = (b-a)/n
    x = a+pas
    i=1
    while i<n:
        res = res + fonc(x)
        x = x + pas
        i=i+1
    res = pas*(res+(fonc(a)+fonc(b))/2)
    return res
    
def calc_int_rect_g(a,b,n):
    res = 0
    pas = (b-a)/n
    x = a
    i=0
    while i<n:
        res = res + fonc(x)
        x = x + pas
        i=i+1
    return res*pas

N = [10,20,40,100,200, 400, 500, 600, 700, 800, 900, 1000, 5000, 10000, 20000, 100000]

calc_int_trap(1,4,10)
err_trap = [abs(I_th-calc_int_trap(1,4,n)) for n in N]
err_rect = [abs(I_th-calc_int_rect_g(1,4,n)) for n in N]

plt.loglog(N,err_trap,label = "Erreur trapèze")
plt.loglog(N,err_rect,label = "Erreur rectangle")
plt.legend()
plt.grid()
plt.show()
