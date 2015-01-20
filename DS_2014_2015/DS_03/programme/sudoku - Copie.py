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

x=[]
y=[]
z=0.7

for i in range (1000):
    tom0 = i/100
    x.append(tom0)
    y.append(f_s(tom0,z))
    
plot(x,y)    
    


