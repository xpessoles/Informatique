# -*- coding: utf-8 -*-
"""
Created on Wed Jun  9 22:55:28 2021

@author: xpess
"""
import numpy as np
import matplotlib.pyplot as plt
import random

## Question 1 
def lire_fichier(file: str) -> (list,list) :
    fid = open(file,'r')
    data = fid.readlines()
    fid.close()
    les_t = []
    les_n = []
    for ligne in data : 
        l = ligne.split(",")
        les_t.append(float(l[0]))
        les_n.append(float(l[1]))
    return les_t,les_n


## Question 2 
def trace_vagues(file: str) -> None :
    les_t,les_n = lire_fichier(file)
    plt.grid()
    plt.xlabel("Temps (en s.)")
    plt.xlabel("Niveau de vague (en m.)")
    plt.plot(les_t,les_n)
    


# Question 3
def moyenne(liste_niveaux: list) -> float :
    return sum(liste_niveaux)/len(liste_niveaux)

# Question 4
def ind_premier_pzd(liste_niveaux : list) -> int:
    m = moyenne(liste_niveaux)
    n = len(liste_niveaux)
    for i in range (n-1):
        if liste_niveaux[i] > m and liste_niveaux[i+1] < m:
        # if liste_niveaux [i] >= m > liste_niveaux [i+1]:
            return i
    return -1 


# Question 5
def ind_dernier_pzd(liste_niveaux: list) -> int:
    m = moyenne(liste_niveaux)
    position = -2 # Valeur par défaut si jamais on ne trouve rien
    for i in range(len(liste_niveaux)-1):
        if liste_niveaux[i] > m and liste_niveaux[i+1] < m:
            position = i
    return position

# Autre solution
def ind_dernier_pzd_2(liste_niveaux: list) -> int:
    m = moyenne(liste_niveaux)
    for i in range(len(liste_niveaux)-2,-1,-1):
        if liste_niveaux[i] > m and liste_niveaux[i+1] < m:
            return i 
    return -2 


# Question 6
def construction_successeurs(liste_niveaux: list) -> list:
    n = len(liste_niveaux)
    successeurs = []
    m = moyenne(liste_niveaux)
    for i in range(n-1):
        if liste_niveaux[i] > m and liste_niveaux[i+1] < m:
            successeurs.append(i+1)
    return successeurs


# Question 7
def decompose_vagues(liste_niveaux: list) -> list :
    successeurs = construction_successeurs(liste_niveaux)
    vagues = []
    for i in range(len(successeurs)-1):
        deb = successeurs[i]
        fin = successeurs[i+1]
        vagues.append(liste_niveaux[deb:fin])
    return vagues

def decompose_vagues_2(liste_niveaux: list) -> list :
    successeurs = construction_successeurs(liste_niveaux)
    n = len(successeurs)
    return [liste_niveaux[successeurs[i]:successeurs[i+1]] for i in range (n-1)]


# Question 8
def proprietes(liste_niveaux: list, dt: float) -> list :
    vagues = decompose_vagues(liste_niveaux)
    prop = [] 
    # Initialisation
    deb = ind_premier_pzd(liste_niveaux)
    H1 = max(liste_niveaux[:deb]) - min(vagues[0])
    T1 = len(vagues[0]) * dt
    prop.append([H1,T1])
    for i in range(len(vagues)-1):
        Hi = max(vagues[i]) - min(vagues[i+1])
        Ti = len(vagues[i+1]) * dt
        prop.append([Hi,Ti])
    return prop


# Question 9
def H_max(liste_niveaux: list, dt:float) -> float :
    prop = proprietes(liste_niveaux,dt)
    Hmax = 0 
    for p in prop: 
        H,T = p
        if H > Hmax : 
            Hmax = H
    return Hmax 


# Question 10
import statistics as s
def skewness(liste_niveaux,dt):
    prop = proprietes(liste_niveaux,dt)
    liste_hauteurs = [p[0] for p in prop]
    n = len (liste_hauteurs)
    et3=(s.pstdev(liste_hauteurs))**3
    m = moyenne(liste_hauteurs)
    S = 0
    for i in range(n):
        S += (liste_hauteurs[i]-m)
    S=n/(n-1)/(n-2)*S/et3
    return S

def SurfingPorquerolles():
    # Question 1
    les_t, liste_niveaux = lire_fichier("vagues.txt")
    # Question 
    trace_vagues("vagues.txt")
    # Question 3
    print("Question 3 ",moyenne(liste_niveaux))
    print("Question 4 ",ind_premier_pzd(liste_niveaux))
    print("Question 5 ", ind_dernier_pzd(liste_niveaux))
    
    successeurs = construction_successeurs(liste_niveaux)
    print("Question 6 ",print(successeurs))
    
    #print(decompose_vagues(liste_niveaux)==decompose_vagues_2(liste_niveaux))
    vagues = decompose_vagues(liste_niveaux)
    print("Question 7 ",vagues[0])
    
    dt = les_t[1]-les_t[0]
    prop = proprietes(liste_niveaux,dt)
    print("Question 8 ",prop[0])
    
    hmax = H_max(liste_niveaux,dt)
    print("Question 9 ",hmax)
    
    S = skewness(liste_niveaux,dt) 
    print("Question 10 ", S)
    
#SurfingPorquerolles()

        

