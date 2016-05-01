#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = "Xavier PESSOLES"

import matplotlib.pyplot as plt
import math

# EXERCICE 22
# Question 1 
# ==========
def fonc(x):
    return math.ln(x)
    
def calc_int_trap(a,b,n):
    pas = (b-a)/n
    I=0
    for i in range(1,n-1):
       I = I+fonc(a+pas*i)
    I = I+0.5*(a+b)
    I = I*pas
    return I