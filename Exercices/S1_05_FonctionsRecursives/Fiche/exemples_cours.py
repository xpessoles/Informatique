# -*- coding: utf-8 -*-
"""
Created on Mon Jul 19 11:29:06 2021

@author: xpessoles
"""

def fact_it(n : int) -> int :
    res = 1
    for i in range (1,n+1): # ou range(n)
        res = res*i
    return res

def fact_rec(n : int) -> int :
    if n == 0 : 
        return 1
    else : 
        return n * fact_rec(n-1) # Récursion
    
def un_rec (n : int) -> float :
    if n == 1 :
        return 1
    else : 
        return (un_rec(n-1)+6)/(un_rec(n-1)+2)

def un_it (n : int) -> float :
    if n == 1 :
        return 1
    else : 
        u = 1
        for i in range(2,n+1):
            u = (u+6)/(u+2)
        return u
    

def appartient_dicho(e : int , t : list) -> bool:
    """Renvoie un booléen indiquant si e est dans t
    Préconditions : t est un tableau de nombres trié par ordre croissant e est un nombre"""
    g = 0 # Limite gauche de la tranche où l'on recherche e
    d = len(t)-1 # Limite droite de la tranche où l'on recherche e
    while g <= d: # La tranche où l'on cherche e n'est pas vide
        m = (g+d)//2 # Milieu de la tranche où l'on recherche e
        pivot = t[m]
        if e == pivot: # On a trouvé e
            return True
        elif e < pivot:
            d = m-1 # On recherche e dans la partie gauche de la tranche
        else:
            g = m+1 # On recherche e dans la partie droite de la tranche
    return False

def appartient_dicho_rec(e : int , t : list) -> bool:
    """Renvoie un booléen indiquant si e est dans t
    Préconditions : t est un tableau de nombres trié par ordre croissant e est un nombre"""
    g = 0 # Limite gauche de la tranche où l'on recherche e
    d = len(t)-1 # Limite droite de la tranche où l'on recherche e
    while g <= d: # La tranche où l'on cherche e n'est pas vide
        m = (g+d)//2 # Milieu de la tranche où l'on recherche e
        pivot = t[m]
        if e == pivot: # On a trouvé e
            return True
        elif e < pivot:
            d = m-1 # On recherche e dans la partie gauche de la tranche
            appartient_dicho_rec(e,t[g:d])
        else:
            g = m+1 # On recherche e dans la partie droite de la tranche
            appartient_dicho_rec(e,t[g:d])
    return False
