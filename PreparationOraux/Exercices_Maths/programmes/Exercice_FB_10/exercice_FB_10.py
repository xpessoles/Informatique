#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = "Frederic Butin"


# EXERCICE 10 FB
import numpy as np
import matplotlib.pyplot as plt
import turtle

# Question 1 
# ==========
turtle.hideturtle()
turtle.speed(10);
tortue = turtle.Pen()

def koch (n):
    if n==1 : 
        tortue.forward(5)
    else : 
        koch(n-1);
        tortue.left(60)
        koch(n-1);
        tortue.left(-120)
        koch(n-1);
        tortue.left(60)
        koch(n-1)
        

def flocon(n):
    tortue.clear()
    koch(n)
    tortue.left(-120)
    koch(n)
    tortue.left(-120)
    koch(n)
    tortue.hideturtle()

flocon(2)