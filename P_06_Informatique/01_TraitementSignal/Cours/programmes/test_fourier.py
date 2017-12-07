import numpy as np
import matplotlib.pyplot as plt
import math as m
temps = np.linspace(0,6,2000)


def fonction_carre(t):
    T,A = 1/2,1
    d,ind_d=T,1
    if t<=d:
        ind_d=1
        d=T
    else : 
        while t>d:
            d=d+T
            ind_d+=1    
    if ind_d%2==0:
        return -A/2
    else :
        return A/2
        
    
carre  = [fonction_carre(t) for t in temps]


def int_rect_dcos(f,T,h,n):
    s = 0
    t=h
    while t<=T:
        s+=f(t)*m.cos(n*t*2*m.pi/T)
        t+=h
    return s*h

def int_rect_dsin(f,T,h,n):
    s = 0
    t=h
    while t<=T:
        s+=f(t)*m.sin(n*t*2*m.pi/T)
        t+=h
    return s*h
    
def coef_fourier(f,T,n):
    h=T/10000
    a=[1/T*int_rect_d(f,T,h)]
    b=[0]
    for i in range(1,n+1):
        a.append(2/T*int_rect_dcos(f,T,h,i))
        b.append(2/T*int_rect_dsin(f,T,h,i))
    
    return a,b
    

def serie_fourier(temps,T,a,b,n):
    s=[]
    for t in temps:
        tmp = a[0]
        for i in range(1,n+1):
            tmp=tmp+a[i]*m.cos(n*t*2*m.pi/T)+b[i]*m.sin(n*t*2*m.pi/T)
        s.append(tmp)
    return s

def coef_carre()
print(int_rect_dcos(f,T,h,i)

T = 1 # Période
n = 4
h=T/10000
print(int_rect_dcos(fonction_carre,T,h,i))

a,b=coef_fourier(fonction_carre,T,n)
sf = serie_fourier(temps,T,a,b,n) 
plt.plot(temps,sf)
            
     