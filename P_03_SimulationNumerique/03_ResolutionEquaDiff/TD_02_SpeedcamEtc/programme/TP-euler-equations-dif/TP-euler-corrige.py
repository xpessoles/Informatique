# -*- coding: utf-8 -*-
"""
Created on Sat Jan 11 08:39:21 2014

Informatique commune
Lycée Faidherbe
PCSI-MPSI
"""


#################################################
###Asservissement d'un chariot

#Réponse du chariot à une entrée de tension en échelon (constante)
#Résolution d'une équation différentielle du premier ordre

#Importation des modules
import matplotlib.pyplot as plt
import math


#Définition des paramètres
K_c=0.5
tau_c=1
U_mot=5
pas = 0.5
tmax=6

#Définition d'une fonction abscisse des temps
def liste_temps(tmax,pas):
    '''Renvoie une liste des abscisses en temps 
    à partir du pas et de la borne supérieure des temps'''
    t=0
    temps=[0]
    while t<=(tmax-pas):
        t=t+pas
        temps=temps+[t]
    return (temps)
    
#Définition d'une fonction premier ordre 
def ordre1_euler(k,tau,u,temps):
    ''' Renvoie une liste des ordonnées pour un premier ordre
    soumis à un échelon u de tension 
    pour une liste abscisse des temps fournie'''
    s=0
    sortie=[0]
    for i in range(1,len(temps)):
        f=(k*u-s)/tau
        s=s+f*(temps[i]-temps[i-1])
        sortie=sortie + [s]
    return sortie
    
#réponse analytique d'un premier ordre
def ordre1_th(k,tau,u,temps):
    s=[0]*(len(temps))
    for i in range(len(temps)):
        s[i]=k*u*(1-math.exp(-temps[i]/tau))
    return s
  


#Les tracés 

#Tracé reponse theorique    
x=liste_temps(tmax,0.1)
z=ordre1_th(K_c,tau_c,U_mot,x)
plt.plot(x,z,'-')


#Tracé superposé pour différents pas de temps
marqueurs = ['^', '+', '.', 'x', '*', 'o'] #Les marqueurs
couleurs = ['b', 'g', 'r', 'c', 'm', 'y', 'k', 'w'] #Les couleurs
style = ['-', '--', '-.', ':']
k=0
for i in (0.3,0.5,0.7,1):
    x=liste_temps(tmax,i)
    y=ordre1_euler(K_c,tau_c,U_mot,x)
    plt.plot(x,y,'--',color=couleurs[k],marker=marqueurs[k])
    k=k+1


#Affichage superpose des courbes
plt.show()
  


#Reponse en boucle fermée

#Premier ordre en boucle fermée sans prise en compte de la saturation
def ordre1_BF(ka,k,tau,vc,temps):
    ''' Renvoie une liste des ordonnées pour un premier ordre
    soumis à un échelon u de tension 
    pour une liste abscisse des temps fournie'''
    s=0
    sortie=[0]
    for i in range(1,len(temps)):
        u=ka*(vc-s)
        f=(k*u-s)/tau
        s=s+f*(temps[i]-temps[i-1])
        sortie=sortie + [s]
    return sortie

#Premier ordre en boucle fermée avec prise en compte de la saturation
def ordre1_BFsat(ka,k,tau,vc,umax,temps):
    ''' Renvoie une liste des ordonnées pour un premier ordre
    soumis à un échelon u de tension 
    pour une liste abscisse des temps fournie'''
    s=0
    sortie=[0]
    tension=[0]
    for i in range(1,len(temps)):
        u=ka*(vc-s)
        if u>umax:
            u=umax
        elif u<-umax:
            u=-umax
        f=(k*u-s)/tau
        s=s+f*(temps[i]-temps[i-1])
        sortie=sortie + [s]
        tension = tension +[u]
    return sortie, tension

#Les tracés 
#tracé superposé pour différents pas de temps   

x=liste_temps(5,0.001)
y=ordre1_BF(20,K_c,tau_c,6,x)
z , us =ordre1_BFsat(20,K_c,tau_c,6,12,x)
plt.plot(x,y,'--')
plt.plot(x,z,'--')
plt.plot(x,us,'--')
plt.show()  
  
 


###################################
###Resolution avec les methodes Python

import scipy.integrate
import math
import matplotlib.pyplot as plt

def f(y,t):
    return(-math.exp(t-y))

n=50
a=0
b=1
C=4

x=[a+k*(b-a)/n for k in range(n)]

y=scipy.integrate.odeint(f,math.log(C-1),x)
yvraie=[math.log(C-math.exp(t)) for t in x]

plt.plot(x,y,'*',color='red')
plt.plot(x,yvraie)
plt.show()

#################################################
#Résolution d'une équation différentielle d'ordre 2

#Importation des modules
import matplotlib.pyplot as plt
import math


#Définition des paramètres
K=10
w_0=5
U_mot=5
pas = 0.5
tmax=5


    
#Définition d'une fonction deuxième ordre
#Equation du type 
def ordre2_euler(w_0,xi,K,u,temps):
    ''' Renvoie une liste des ordonnées pour un premier ordre
    soumis à un échelon u de tension 
    pour une liste abscisse des temps fournie'''
    p=0
    v=0
    position=[0]
    vitesse=[0]
    for i in range(1,len(temps)):
        f1=(K*u-p-2*xi*v/w_0)*((w_0)**2)
        f2=v
        v2=v+f1*(temps[i]-temps[i-1])
        p2=p+f2*(temps[i]-temps[i-1])
        position=position + [p2]
        vitesse=vitesse+[v2]
        v=v2
        p=p2
    return position, vitesse
    
#Les tracés 

#Tracé reponse    
x=liste_temps(10,0.01)

#Tracé superposé pour différents pas de temps
marqueurs = ['^', '+', '.', 'x', '*', 'o'] #Les marqueurs
couleurs = ['b', 'g', 'r', 'c', 'm', 'y', 'k', 'w'] #Les couleurs
style = ['-', '--', '-.', ':']
k=0
#Pour différentes valeurs de xi
for i in (0.3,0.69,1,2,5):
    y,z=ordre2_euler(w_0,i,K,U_mot,x)
    plt.plot(x,y,'--',color=couleurs[k],marker=marqueurs[k])
    k=k+1


#Affichage superpose des courbes
plt.show()



###Resolution avec les methodes Python
#Utilisation de integrate.odeint

import scipy.integrate
import numpy

def f(z,t):
    v,p=z
    return((K*u-p-2*xi*v/w_0)*((w_0)**2),v)


xi=0.3
   
x=liste_temps(10,0.01)
z0 = [0,0]
z = scipy.integrate.odeint (f, z0, x)

y=z[:,1] #Pour avoir la deuxième colonne (position, environnement numpy)
plt.plot(x,y,'--',color='r',marker='+')
plt.show()
  
    
    
    
    
        
        