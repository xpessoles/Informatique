#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = "Xavier PESSOLES"


# EXERCICE 18
import numpy as np
import matplotlib.pyplot as plt


# Question 2
# ==========
R=4
r=R/4
m = 1-R/r
theta = np.linspace(0,2*np.pi,1000)
x=(R-r)*np.cos(theta)+r*np.cos(m*theta)
y=(R-r)*np.sin(theta)+r*np.sin(m*theta)
plt.plot(x,y,label="R=4, r=1, m=-3")

# Question 3
# ==========
for p in [1, 5, 10, 100]:
    r=R/p
    m = 1-R/r
    theta = np.linspace(0,2*np.pi,1000)
    x=(R-r)*np.cos(theta)+r*np.cos(m*theta)
    y=(R-r)*np.sin(theta)+r*np.sin(m*theta)
    titre = "R = "+str(R)+ ", r = "+str(r)+ ", m = "+str(m)
    plt.plot(x,y,label=titre)

x=R*np.cos(m*theta)
y=R*np.sin(m*theta)
#plt.plot(x,y)

plt.axis("equal")
#plt.legend()
plt.show()
