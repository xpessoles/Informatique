#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = "Xavier PESSOLES"

# EXERCICE 15
# Question 1 
# ==========
def f_sigma(n,t):
    return (np.cos(n*t))**3-(np.sin(n*t))**3

x = np.linspace(0,10,1000)
y = f_sigma(1,x)

for i in range(4):
    x = np.linspace(0,10,1000)
    y = f_sigma(i,x)
    plt.plot(y*np.cos(x),y*np.sin(x),label=str(i))

plt.legend()
plt.axis("equal")    
plt.show()