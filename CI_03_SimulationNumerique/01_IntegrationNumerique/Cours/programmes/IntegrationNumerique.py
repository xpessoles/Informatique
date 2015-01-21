# -*- coding: utf-8 -*-
"""
Created on Wed Jan 21 21:38:08 2015

@author: Xavier
"""

from math import sqrt
def f(x):
    return math.sqrt(1-x*x)


def rect_gauche(f,a,b,nb):
    res = 0
    pas = (b-a)/nb
    for i in range(nb):
        x = i*pas
        res = res+f(x)*pas
    return res

print(4*rect_gauche(f,0,1,10000))
        