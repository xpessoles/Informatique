# -*- coding: utf-8 -*-
"""
Created on Fri Jan 30 13:12:56 2015

@author: Xavier
"""

# Exercice 1
def f(x):
    return 4/(1+x**2)

x = []
y = []
for i in range(101):    
    x.append(i/100.)
    y.append(f(x[i]))
#plot(x,y)


a = 0
b = 1
n = 100
pas = (b-a)/n
x = a
somme = 0
for k in range (0,n):
    somme = somme+f(x)*pas
    x=x+pas  
#print("Méthode des rectangles à gauche : "+ str(somme))

x = a
somme = 0
for k in range (0,n):
    x=x+pas
    somme = somme+f(x)*pas
      
#print("Méthode des rectangles à gauche : "+ str(somme))


# Exercice 2

import numpy as np
def f2(x,n):
    return (x/(1+x**n))

def integrale(n,nb):
    a = 0
    b = 1
    pas = (b-a)/nb
    x = a+pas
    somme = 0
    for i in range(nb):
        somme = somme + f2(x,n)*pas
        x = pas + x
    return somme

xx=[]
yy=[]
for i in range(0,100,1):
    xx.append(i)
    yy.append(integrale(i,1000))

for i in range(10):
    xx=np.linspace(0,1,100)
    for j in xx :
        yy.append(f(j,i))
    plt.plot(xx,yy)      

