# -*- coding: utf-8 -*-
"""
@author: Xavier PESSOLES
"""
import numpy as np
import matplotlib.pyplot as plt
import random

x = np.linspace(0,5,10000)
T1 = 2 
T2 = .012
K2 = 0.02
K1 = .1
y1 = K1*np.sin(2*np.pi/T1*x)+K1+1
rand = [K2*random.randint(1,1000)/1000 for x in range(10000)]
rand = np.array(rand)
y2 = y1+0.05*np.sin(2*np.pi/T2*x)+rand

T3 = 10
K4=.4
y3=y2+K4*(np.cos(2*np.pi/T3*x))

#plt.plot(x,y1)
#plt.plot(x,y2)
#plt.plot(x,y3)

def filtrePB(e,h,tau):
    s = [e[0]]
    for i in range(1,len(e)):
        s.append((h*e[i]+tau*s[-1])/(h+tau))
    return s



def calculAire(x,y,h):
    #Calcul de l'aire en dessous et en dessus de l'altitude h
    # Séparation des profils
    dx = x[1]-x[0]
    haut = []
    bas = []
    for i in range(len(y)):
        if y[i]>h:
            haut.append(y[i])
            bas.append(h)
        else : 
            haut.append(h)
            bas.append(y[i])
            
    aire_sup = 0.5*(haut[0]+haut[-1])
    aire_inf = 0.5*(bas[0]+bas[-1])

    for i in range(1,len(haut)-1):
        aire_sup = aire_sup+haut[i]
        aire_inf = aire_inf+bas[i]
    
    aire_sup = abs(aire_sup*dx)
    aire_inf = abs(aire_inf*dx)
    return aire_inf,aire_sup

def rechercheh(x,y):
    g = min(y)
    d = max(y)
    ii = 0
    c= (d+g)/2
    a_i,a_s = calculAire(x,y,c)

    while abs(a_i-a_s)>0.00001 and ii<100:
        ii=ii+1
        if a_i>a_s :
            g=c
        else :
            d=c
        c= (d+g)/2
        a_i,a_s = calculAire(x,y,c)
        print(ii,g,d,c,abs(a_i-a_s))
    return c
            
        
    

    
fid = open("mesures.txt","w")
for i in range(len(x)):
    fid.write(str(x[i])+"\t"+str(y2[i])+"\n")

fid.close()

h = 0.0005
tau = .02
s = filtrePB(y2,h,tau)
#plt.plot(x,s)
#plt.plot(x,y2-s)

yr = y2-s
print(calculAire(x,yr,-0.04))
print(rechercheh(x,yr))


"""
plt.axis("equal")
plt.show()
"""