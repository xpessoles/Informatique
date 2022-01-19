# -*- coding: utf-8 -*-
"""
Created on Thu Jan 13 10:18:46 2022

@author: xpess
"""

def fonction(x,y = []) :
    if x == [] : 
        return y
    else : 
        z = x.pop(0)
        if z not in y : 
            y.append(z)
        return fonction(x, y)

def supprimer_doublons_liste(L,y = []) :
    """
    Fonction permettant de supprimer les doublons d'une liste.
    Entrée : 
     * L: list(int) : liste d'entiers. 
    Sortie : 
     * list(int) : liste d'entiers ne comportant aucun doublons.
    """
    if x == [] : 
        return y
    else : 
        z = x.pop(0)
        if z not in y : 
            y.append(z)
        return fonction(x, y)

def supprimer_doublons_liste2(L,y = []) :
    """
    

    Parameters
    ----------
    L : TYPE
        DESCRIPTION.
    y : TYPE, optional
        DESCRIPTION. The default is [].

    Returns
    -------
    None.

    """
    return None

def fonction_02(L):
    LL = []
    for elt in L : 
        if elt not in LL : 
            LL.append(elt)
    return LL

def fonction_03_v1(L):
    n = len(L)
    LL = []
    i = 0
    while i<=n :
        x = L[i]
        j=0
        flag = False
        while j<=n:
            if L[j]==x :
                flag == True
            j=j+1
        if flag == True : 
            LL.append(x)
        i=i+1
    return LL

def fonction_03_v2(L):
    n = len(L)
    LL = []
    i = 0
    while i<n :
        x = L[i]
        j=0
        flag = False
        while j<n:
            print(i,j)
            if L[j]==x :
                flag == True
            j=j+1
        if flag == False : 
            LL.append(x)
        i=i+1
    return LL

def addition(a:str,b:str) -> str:
    return a+b

def addition(a:int, b:int) -> int : 
    assert type(a) == int and type(b) == int
    return a+b


def dichotomie(f, a:float , b:float , epsilon:float) -> float :
    """Zéro de f sur [a,b] à epsilon près, par dichotomie
        Préconditions : f(a) * f(b) <= 0
        f continue sur [a,b]
        epsilon > 0"""
    assert (f(a) * f(b) <= 0) and (epsilon > 0)
    c, d = a, b
    fc, fd = f(c), f(d)
    while d - c > 2 * epsilon:
        m = (c + d) / 2.
        fm = f(m)
        if fc * fm <= 0:
            d, fd = m, fm
        else:
            c, fc = m, fm
    return (c + d) / 2.

def ff(x):
    return x*x-2

def produit_scalaire(vecteur1, vecteur2):
    """Renvoie le produit scalaire de deux vecteurs.
    Arguments d'entrée :
        vecteur1 (list[int, float])
        vecteur2 (list[int, float])
    Sortie :
        int ou float
    Renvoie une erreur si les deux listes n'ont pas même longueur.
    """
    if len(vecteur1) != len(vecteur2):
        raise Exception("Les deux vecteurs doivent avoir même dimension !")
    somme = 0
    for i in range(len(vecteur1)):
        somme += vecteur1[i]*vecteur2[i]
    return somme

def test_produit_scalaire():
    assert produit_scalaire([1, 1, 1], [1, 1, 1]) == 3
    assert produit_scalaire([1, 2, 3, 4], [0, 1, 0, 0]) == 2


def dichotomie(f, a:float , b:float , epsilon:float) -> float :
    """Zéro de f sur [a,b] à epsilon près, par dichotomie
        Préconditions : f(a) * f(b) <= 0
        f continue sur [a,b]
        epsilon > 0"""
    if f(a) * f(b) > 0 : 
        raise Exception("f(a) et f(b) sont de même signe")
    elif epsilon < 0 :
        raise Exception("epsilon est négatif")

    c, d = a, b
    fc, fd = f(c), f(d)
    while d - c > 2 * epsilon:
        m = (c + d) / 2.
        fm = f(m)
        if fc * fm <= 0:
            d, fd = m, fm
        else:
            c, fc = m, fm
    return (c + d) / 2.

a = [1, 1, 1]
b = [1, 1, 1]
c = [1,1]
print(dichotomie(ff, 0, 1, 0.00001))
test = [1,2,3,1,2,3,4]