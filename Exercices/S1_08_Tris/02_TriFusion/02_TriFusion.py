# -*- coding: utf-8 -*-
"""
Created on Mon Feb 13 14:21:12 2023

@author: xpess
"""

def separe(L: list) -> tuple[list,list]:
    return L[:len(L) // 2], L[len(L) // 2:]

def fusion(L1: list, L2: list) -> list:
    if not L1 or not L2: # si l'une des listes est vide (éventuellement les 2)
        return L1 or L2 # alors on renvoie l'autre (éventuellement vide aussi)
    else:
        a, b = L1[0], L2[0] 
        if a < b : # sinon on compare leurs premiers éléments
            return [a] + fusion(L1[1:], L2) # on place le plus petit en tête et on fusionne le reste
        else:
            return [b] + fusion(L1, L2[1:])
        

def tri_fusion(L: list) -> list:
    if len(L) < 2: # cas d'arrêt
        return L
    L1, L2 = separe(L) # sinon on sépare
    return fusion(tri_fusion(L1), tri_fusion(L2)) # et on fusionne les sous-listes triées