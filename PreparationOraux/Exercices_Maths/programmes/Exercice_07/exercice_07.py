#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = "Xavier PESSOLES"

# EXERCICE 7

# Import de fonctions

# Question 1 
# ==========
def d(n):
    """
    Retourne la liste de tous les diviseurs de n.
    Entrée : 
     * n(int) : entier.
    Sortie : 
     * L(lst) : liste des diviseurs de n.
    """
    L =[1]
    for nombre in range(2,n+1):
        if n%nombre == 0:
            L.append(nombre)
    return L

print(d(4))
print(d(10))

# Question 2 
# ==========
def DNT_01(n):
    return d(n)[1:-1]

def DNT_02(n):
    L =[]
    for nombre in range(2,n):
        if n%nombre == 0:
            L.append(nombre)
    return L
    
print(DNT_01(4),DNT_02(4))
print(DNT_01(10),DNT_02(10))

# Question 3
# ==========
def sommeCarresDNT_01(n):
    L = DNT_01(n)
    res = [x**2 for x in L]
    return sum(res)

def sommeCarresDNT_02(n):
    L = DNT_01(n)
    res = 0
    for x in L:
        res = res + x*x
    return res
    
def sommeCarresDNT_03(n):
    L = DNT_01(n)
    res = 0
    for i in range(len(L)):
        res = res + L[i]**2
    return res
    
print(sommeCarresDNT_01(15),sommeCarresDNT_02(15),sommeCarresDNT_03(15))

# Question 4
# ==========
from math import sqrt
for i in range(1001):
    if i == sommeCarresDNT_01(i) :
        print(str(i)+"\t"+str(sqrt(i)))

# Conjecture les nombres recherchés sont les carrés des nombres premiers. 
