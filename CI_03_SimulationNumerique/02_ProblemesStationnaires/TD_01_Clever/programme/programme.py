# -*- coding: utf-8 -*-
"""
Created on Wed Apr  2 20:01:47 2014

@author: Xavier
"""
from math import radians
from math import sqrt
from math import cos
from math import sin


# Question 1
def lambda1 (x):
    a,b,L = 0.14,0.046,0.49
    res = sqrt(
    pow(L*cos(x-radians(130))+a,2)
    +pow(L*sin(x-radians(130))-b,2) 
    )
    return res


# Question 2 et 3
"""
x = np.linspace(radians(-50),radians(50),1000)
xx,yy=[],[]
for i in range(len(x)):
    xx.append(x[i])
    yy.append(lambda1(x[i]))
plot(xx,yy)
"""
#Solution : -0.401 rad

# Question 4
"""
def f(x):
    return lambda1(x)-0.4

import scipy.optimize as opt
res=opt.newton(f,0)
print(res)
"""

# Question 5
def newton():
    #Condtions d'arret
    epsilon = 1e-10
    maxiter  = 500
    x0 = radians(-50)
    xf = radians(50)
    xm = (xf-x0)/2
    nbiter = 0
    while(abs(x0-xf)>epsilon and nbiter < maxiter):
        nbiter +=1
        if f(xm)>0 :
            xf=xm
            xm = (xf-x0)/2
        else : 
            x0=xm
            xm = (xf-x0)/2
        print(nbiter,xm)
    return xm
print(newton())

