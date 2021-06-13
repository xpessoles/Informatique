#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = "Xavier PESSOLES"

# EXERCICE 10
import numpy as np
# Question 1
# ==========
R = np.array([[1,2,3],[4,5,6]])
S = np.array([[1,2,3],[4,5,6],[7,8,9]])

# Question 2
# ==========
def test(M):
    """
    Fonction permettant de tester si la
    matrice est carrée et retournant sa taille.
    Entrée : 
     * M(numpy.ndarray) : matrice
    Sortie :
     * 0 si taille non carrée
     * n(int) : taille de M si elle est carrée
    """
    l = M.shape[0]
    c = M.shape[1]
    if l==c :
        return l
    else : 
        return 0

print(test(R))
print(test(S))

# Question 3
# ==========
fid = open("data/ex_006.txt",'r')
M1 = []
for ligne in fid :
    l = ligne.rstrip().split(" ")
    Ligne = [float(x) for x in l]
    M1.append(Ligne)
fid.close()
M1 = np.array(M1)

# Question 4
# ==========
if test(M1)>0:
    valeurs_propres = np.linalg.eig(M1)[0]
    print(valeurs_propres)

# Question 5
# ==========
def dansIntervalle(L,a,b):
    """
    Vérifier que chaque élément de L est dans l'intervalle [a,b]
    Entrées : 
     * L(lst) : liste de nombres
     * a,b(flt) : nombres
    Sortie : 
     * True si chaque élément est dans [a,b]
     * False sinon. 
    """   
    for e in L :
        if e<a or e> b:
            return False
    return True
print(dansIntervalle(valeurs_propres,0,1))