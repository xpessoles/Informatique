#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = "Xavier PESSOLES"


# EXERCICE 9
import numpy as np
import matplotlib.pyplot as plt
import turtle

# Question 1 
#============
turtle.hideturtle()
turtle.goto(100,0)
turtle.speed(1)
tortue = turtle.Pen()
"""
t = np.linspace(0,2*np.pi,1000)
x=100*np.cos(t)
y=100*np.sin(t)
for i in range(len(x)):
    tortue.goto(x[i],y[i])
"""

# Question 2 
# ==========
def peano(n) : 
    if n==1 :
        tortue.forward(10)
    else : 
        peano(n-1)
        tortue.left(90)
        peano(n-1)
        tortue.left(-90)
        peano(n-1)
        tortue.left(-90)
        peano(n-1)
        tortue.left(-90)
        peano(n-1)
        tortue.left(90)
        peano(n-1)
        tortue.left(90)
        peano(n-1)
        tortue.left(90)
        peano(n-1)
        tortue.left(-90)
        peano(n-1)
        
peano(4)
turtle.hideturtle()

