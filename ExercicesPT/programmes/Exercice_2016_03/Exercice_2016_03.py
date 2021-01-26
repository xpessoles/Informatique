import random as r
import numpy as np
import matplotlib.pyplot as plt

#Q1
 #Modification du programme (il manque l'initialisation )

def ordonner(L):
    if len(L) == 0 :
        return([])
    if len == 1 :
        return(L)
    if len(L) == 2 :
        if L[1]<=L[0] :
            return(L)
        else :
            return([L[1],L[0]])
    if len(L) >= 3 :
        n = 1
        e0 = L[0]
        Linf,Lsup = [],[]
        for ei in L[1:]:
          if ei == e0 :
              n+= 1
          elif ei < e0  :
              Linf.append(ei)
          else :
              Lsup.append(ei)

        return(ordonner(Linf)+ n *[e0] + ordonner (Lsup))

#Ordonner permet de classer la liste L par ordre croissant

#Q2

def less(z1,z2):
    """ Renvoie True si Re(z1)<Re(z2) ou (Re(z1)=Re(z2) et Im(z1) < Im (z2) """
    B = (((z1.real) < (z2.real)) or ((z1.real) == (z2.real) and (z1.imag < z2.imag)))

    return(B)

#print(less(1+2j,1+3j))
#True

#Q3

def ordonnerdansc(L):
    """ Ordonner la liste L d'après la méthode de la liste ordonner, en s'appuyant sur l'ordonnancement de la fonction less """
    if len(L) == 0 :
        return([])
    if len(L) == 1 :
        return(L)
    if len(L) == 2 :
         if less(L[1],L[0]) :
             return(L)
         else :
             return([L[1],L[0]])
    if len(L) >= 3 :
        n = 1
        e0 = L[0]
        Linf,Lsup = [],[]
        for ei in L[1:]:
             if ei == e0 :
                 n+= 1
             elif less(ei,e0) :
                 Linf.append(ei)
             else :
                 Lsup.append(ei)
        
        return(ordonnerdansc(Linf) + n *[e0] + ordonnerdansc(Lsup))
    
#Q3
L = []
for i in range(11):
    a = r.randint(-10,10)
    b = r.randint(-10,10)
    L.append(a+b*1j)


#print (L)
#print(ordonnerdansc(L))

#[(-3-5j), (-2+0j), (9-6j), (4+1j), (-2+2j), (2-1j), (2-4j), (-5-1j), (3+9j), (-5+6j), (-7-9j)]
#[(-7-9j), (-5-1j), (-5+6j), (-3-5j), (-2+0j), (-2+2j), (2-4j), (2-1j), (3+9j), (4+1j), (9-6j)]


#Q4

Lpi = []

for a in range(-100,100):
    Lpi.append((20+ np.cos(10*a*np.pi/100))*np.exp((a*np.pi/100)*1j))

Lpi = ordonnerdansc(Lpi)

Lpir = []
Lpiim =[]

for z in Lpi :
        Lpir.append(z.real)
        Lpiim.append(z.imag)
        
plt.plot(Lpir,Lpiim,'o',label = 'Lpi')

plt.xlabel('Re()')
plt.ylabel('Im()')

plt.legend()
plt.show()
