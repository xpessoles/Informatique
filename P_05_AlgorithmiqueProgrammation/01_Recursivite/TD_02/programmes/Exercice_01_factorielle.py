#!/usr/bin/env python
# -*- coding: utf-8 -*-


from math import factorial

# Exercice 1
# ==========


def fact_it(n):
    """
    Calcul de n! de manière itérative
    Entrée : 
     * n(int) : nombre entier naturel
    Sortie 
     * res (int): résultat, nombre entier naturel
    """
    # Vérifie que n est bien positif ou nul
    # On pourrait aussi vérifier que n est bien un integer
    assert (n >= 0),"Nombre négatif" 
    if n==0:
        return 1
    else :
        res = 1
        k=n
        while k>0:
            res=res * k
            k=k-1
        return res
    

def fact_rec(n):
    """
    Calcul de n! de manière récursive
    Entrée : 
     * n(int) : nombre entier naturel
    Sortie 
     * (int): résultat, nombre entier naturel
    """
    if n<2:
        return 1
    else:
        return n*fact_rec(n-1)
        
print(fact_it(1010))
print(factorial(1010)) 

#print(fact_rec(1010))