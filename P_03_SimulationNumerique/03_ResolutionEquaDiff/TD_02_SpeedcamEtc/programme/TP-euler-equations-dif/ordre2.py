# -*- coding: utf-8 -*-
"""
Created on Mon Jan 27 14:27:44 2014

@author: SR
"""

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

#Double oscillateurs battement

#Importation des modules
import matplotlib.pyplot as plt
import math



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


def ordre2_bat(k0,k,m,v0,temps):
    ''' Renvoie une liste des ordonnées pour un premier ordre
    soumis à un échelon u de tension 
    pour une liste abscisse des temps fournie'''
    p1=0
    v1=v0
    p2=0
    v2=0
    position1=[0]
    vitesse1=[v0]
    position2=[0]
    vitesse2=[0] 
    for i in range(1,len(temps)):
        fv1=(k*p2-(k0+k)*p1)/m
        fp1=v1
        fv2=(k*p1-(k0+k)*p2)/m
        fp2=v2
        v1plus=v1+fv1*(temps[i]-temps[i-1])
        p1plus=p1+fp1*(temps[i]-temps[i-1])
        v2plus=v2+fv2*(temps[i]-temps[i-1])
        p2plus=p2+fp2*(temps[i]-temps[i-1])        
        position1=position1 + [p1plus]
        vitesse1=vitesse1+[v1plus]
        position2=position2 + [p2plus]
        vitesse2=vitesse2+[v2plus]
        v1=v1plus
        p1=p1plus
        v2=v2plus
        p2=p2plus
    return position1, position2
    
#Tracé reponse    
x=liste_temps(10,0.001)
y,z=ordre2_bat(10,1,0.1,1,x)
plt.plot(x,y,'--',color='r',marker='+')
plt.plot(x,z,'--',color='g',marker='*')


#Affichage superpose des courbes
plt.show()



###################################
###Resolution avec les methodes Python

import scipy.integrate
import math
import matplotlib.pyplot as plt
import numpy

k0=10
k=1
m=0.1


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


def f(z,t):
    v1,p1,v2,p2=z
    return((k*p2-(k0+k)*p1)/m,v1,(k*p1-(k0+k)*p2)/m,v2)


x=liste_temps(10,0.01)
z0 = [1,0,0,0]
z = scipy.integrate.odeint (f, z0, x)

y=z[:,1]
w=z[:,3]

plt.plot(x,y,'--',color='r',marker='+')
plt.plot(x,w,'--',color='g',marker='*')

#Affichage superpose des courbes
plt.show()

