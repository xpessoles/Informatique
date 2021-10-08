# -*- coding: utf-8 -*-
"""
Created on Sat Feb 20 16:46:03 2021

@author: David
"""

Fichier = open("CoMax.txt",'r')
data = []

for k in range(2):
    Fichier.readline()

temps=[]; q_exp=[]
for lu in Fichier:
    ligne = lu.split("\t")
    temps.append(float(ligne[1]))
    q_exp.append(float(ligne[2]))

import numpy as np
temps = np.array(temps)
q_exp = np.array(q_exp)
X_exp = (q_exp-q_exp[0])*(3.41/1000)

import matplotlib.pyplot as plt

plt.figure(1)
plt.plot(temps,X_exp,'b+',label="points exp.")
plt.legend()
plt.xlabel('t [s]'); plt.ylabel('x [mm]')
plt.title("Evolution de la position de l'axe en fonction du temps")

"""Donnees"""
Acmax = 2.83; Vmax = 0.68
t1 = Vmax/Acmax; t2 = 2*t1
X1 = Vmax**2/(2*Acmax)

def Loi_Vitesse(t):
    global t1, Vmax, Acmax
    if 0<=t<t1:
        v=Acmax*t
    elif t1<=t<=t2:
        v=Vmax - Acmax*(t-t1)
    else:
        print("erreur")
    return v

def Loi_Position(t):
    global t1, Vmax, Acmax
    if 0<=t<t1:
        x=(Acmax/2)*t**2
    elif t1<=t<=t2:
        x=X1 + Vmax*(t-t1) - (Acmax/2)*(t-t1)**2
    else:
        print("erreur")
    return x

n = len(temps)
X_th = np.zeros(n); V_th = np.zeros(n)
for i in range(n):
    X_th[i] = 1000*Loi_Position(temps[i])
    V_th[i] = Loi_Vitesse(temps[i])

plt.plot(temps,X_th,'g',label="pos. commande")
plt.legend()

plt.figure(2)
plt.plot(temps,V_th,'g',label="vitesse theorique")
plt.legend()
plt.xlabel('t [s]'); plt.ylabel('v [m/s]')
plt.title("Evolution de la vitesse de l'axe en fonction du temps")

def Calcul_ecarts(T1,T2):
    return 100*abs((T1-T2)/T2)

Delta_X = Calcul_ecarts(X_exp[1:n],X_th[1:n])

plt.figure(3)
plt.bar([i for i in range(1,n)],Delta_X,color=[0.5,0,1])


def Calculs_stats(T):
    n = np.shape(T)[0]
    #Moyenne :
    moy_T = np.sum(T)/n
    #Médianne :
    T_trie = np.sort(T)
    if n==0:
        med_T = 0
    elif n%2==0:
        med_T = (T_trie[n//2]+T_trie[n//2-1])/2
    else:
        med_T = T_trie[n//2]
    #Ecart type :
    sigma_T = np.sqrt(np.sum((T - moy_T)**2)/n)
    
    return (moy_T, med_T, sigma_T)

(a,b,c) = Calculs_stats(Delta_X)

print(np.mean(Delta_X))
print(np.median(Delta_X))
print(np.std(Delta_X))

plt.show()


