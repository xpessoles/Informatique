# -*- coding: utf-8 -*-
"""
Created on Wed Apr  2 20:01:47 2014

@author: Xavier
"""
from math import radians
from math import sqrt
from math import cos
from math import sin
from math import log


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

def f(x):
    return lambda1(x)-0.4
"""
import scipy.optimize as opt
res=opt.newton(f,0)
print(res)
"""

# Question 5
def dichotomie(f,a,b,epsilon):
    maxiter  = 500
    x0 = a
    xf = b
    xm = (xf+x0)/2
    nbiter = 0
    tab_res=[[nbiter,xm]]
    while(abs(x0-xf)>epsilon and nbiter < maxiter):
        nbiter +=1
        if f(xm)>0 :
            xf=xm
            xm = (xf+x0)/2
        else : 
            x0=xm
            xm = (xf+x0)/2
        tab_res.append([nbiter,xm])
    return xm,nbiter,tab_res

alpha_i = radians(-50)
alpha_f = radians(50)
epsilon = 1e-10
res_dicho=dichotomie(f,alpha_i,alpha_f,epsilon)
print("Resultat dichotomie : " +str(res_dicho[0])+"  et "+str(res_dicho[1])+" itérations")

#Question 13
def ordre(liste_x) :
    res=[]
    for i in range(2,len(liste_x)):
        tmp = log(abs(liste_x[i][1]-liste_x[i-1][1]))/log(abs(liste_x[i-1][1]-liste_x[i-2][1]))
        res.append([i-2,tmp])
    return res
res_ordre_dicho = ordre(res_dicho[2])


#Question 14
def lambda_prime (x):
    a,b,L = 0.14,0.046,0.49
    num = -a*L*sin(x-radians(130))-b*L*cos(x-radians(130))
    den = lambda1(x)
    return num/den


def newton(f,fprime,xini,epsilon):
    maxiter  = 500
    x1=xini
    x2 = xini + 2*epsilon
    nbiter = 0
    while(abs(x2-x1)>epsilon and nbiter < maxiter):
        # Equation de la tangente y = mx+p
        x1=x2
        nbiter += 1
        m = fprime(x1)
        p = f(x1)-m*x1
        x2 = -p/m
    return x2,nbiter

print(newton(f,lambda_prime,radians(50),epsilon))

def newton2(f,xini,epsilon):
    maxiter  = 500
    x1=xini
    x2 = xini + 2*epsilon
    nbiter = 0
    while(abs(x2-x1)>epsilon and nbiter < maxiter):
        # Equation de la tangente y = mx+p
        x1=x2
        nbiter += 1
        m = (f(x1+epsilon)-f(x1))/epsilon
        p = f(x1)-m*x1
        x2 = -p/m
        
    return x2,nbiter
print(newton2(f,radians(50),epsilon))
