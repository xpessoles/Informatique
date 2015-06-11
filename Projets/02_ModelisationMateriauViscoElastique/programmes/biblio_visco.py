#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__      = "Xavier Pessoles"
__email__ = "xpessoles.ptsi@free.fr"


from math import sin,pi
import numpy as np


def generate_M(n,m):
    """
    Génération de la matrice des masses.
    Entrées : 
     * n,int : nombre d'éléments
     * m,flt : masse d'un élément en kg
    Sortie :
     * array : matrice des masses
    """
    # np.eye renvoie la matrice identité de taille nxn
    return m*np.eye(n,n)

def generate_K(n,k):
    """
    Génération de la matrice des raideurs.
    Entrées : 
     * n,int : nombre d'éléments
     * k,flt : raideur d'un élément en MPa
    Sortie :
     * array : matrice des masses
    """
    # np.eye renvoie la matrice "vide" de taille nxn
    M = np.eye(n,n)
    M[0][0:2]=[2*k,-k]
    M[n-1][n-2:n]=[-k,k]
    for i in range(1,n-1):
        M[i][i-1:i+2]=[-k,2*k,-k]
    return M
    
def generate_C(n,c):
    return generate_K(n,c)
