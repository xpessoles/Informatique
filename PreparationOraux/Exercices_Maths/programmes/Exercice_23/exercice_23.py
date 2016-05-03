#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = "Xavier PESSOLES"


# EXERCICE 23
# Question 1 
# ==========
import matplotlib.pyplot as plt
import math
import numpy as np

n=1
N=1000

def solve_eq(N,n,t0,tf):
    x = np.linspace(t0,tf,N)
    h = (tf-t0)/N
    y1=[0]
    y2=[0]
    for i in range(1,N):
        y1.append(h*y2[i-1]+y1[i-1])
        y2.append(h*(math.sin(n*x[i-1])+y1[i-1]-10*y2[i-1])+y2[i-1])
         
    return x,y1
    
for i in range(1,10):
    les_x,les_y = solve_eq(N,i,0,7)
    plt.plot(les_x,les_y)

plt.show()
        
     
    
    
