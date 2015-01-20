# -*- coding: utf-8 -*-
"""
Created on Mon Jan 12 21:08:25 2015

@author: Xavier
"""
import math

def f_pseudo(t,z,om0):
    return 1-((math.exp(-z*om0*t))/(math.sqrt(1-z*z)))*math.sin(t*om0*math.sqrt(1-z*z)+math.asin(math.sqrt(1-z*z)))

def f_critique(t,om0):
    return 1-(1+t*om0)*math.exp(-om0*t) 

def f_aperiodique(t,z,om0):
    return 1+(math.exp(-t*om0*(z+math.sqrt(z*z+1))))/(2*(z*math.sqrt(z*z-1)+z*z-1))-(math.exp(-t*om0*(z-math.sqrt(z*z+1))))/(2*(z*math.sqrt(z*z-1)-z*z+1))


def f2_pseudo(tom0,z):
    return 1-((math.exp(-z*tom0))/(math.sqrt(1-z*z)))*math.sin(tom0*math.sqrt(1-z*z)+math.asin(math.sqrt(1-z*z)))

def f2_critique(tom0):
    return 1-(1+tom0)*math.exp(-tom0) 
    
def f2_aperiodique(tom0,z):
    return 1+(math.exp(-tom0*(z+math.sqrt(z*z-1))))/(2*(z*math.sqrt(z*z-1)+z*z-1))-(math.exp(-tom0*(z-math.sqrt(z*z-1))))/(2*(z*math.sqrt(z*z-1)-z*z+1))

    
def f_s(tom0,z) :
    if z<0 :
        return None
    elif z<1 :
        return f2_pseudo(tom0,z)
    elif z==1:
        return f2_critique(tom0)
    else : 
        return f2_aperiodique(tom0,z)


def trace_s(z):
    x = []
    y = []
    for i in range(11):
        t = i
        x.append(t)
        y.append(f_s(t,z))
    plot(x,y)

def trace_s(z):
    x = []
    y = []
    n=1000
    for i in range(n+1):
        t = 10*i/n
        x.append(t)
        y.append(f_s(t,z))
    plot(x,y)

# Appels de la fonction trace
trace_s(0.4)
trace_s(0.7)