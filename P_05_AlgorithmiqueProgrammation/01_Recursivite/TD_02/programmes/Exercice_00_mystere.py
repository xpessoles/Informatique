#!/usr/bin/env python
# -*- coding: utf-8 -*-

def mystere(L):
    """
    Ceci est la fonction mystère, saurez-vous trouver son but ?
    Entrée : 
        * L(list) : liste de nombres entiers ou réels
    Sortie : 
        * ??? 
    """
    n = len(L)
    if n==0 :
        return (none)
    elif n==1 :
        return (L[0])
    else :
        x = mystere(L[0:n-1])
        if x<=L[-1] :
            return (x)
        else : 
            return (L[-1])
