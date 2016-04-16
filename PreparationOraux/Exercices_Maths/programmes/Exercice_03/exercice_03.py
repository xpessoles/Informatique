#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = "Xavier PESSOLES"

# Import des bibliothèques
import matplotlib.pyplot as plt

# Question 1
# ==========
# Matrices avec des listes
M=[[0,9,3,-1,7],[9,0,1,8,-1],[3,1,0,4,2],[-1,8,4,0,-1],[7,-1,2,-1,0]]

# Question 2 & 3
# ==============
def voisins(M,i):
    """
    Entrées : 
      * M(lst) : graphe
      * i : noeud considéré
    Sortie :
      * v(lst) : liste des voisins
    """
    v = []
    # On cherche les voisins sur une ligne 
    # (on pourrait le faire sur une colonne)
    for j in range(len(M[i])):
        if M[i][j]>0:
            v.append(j)
    return v
    
# print(voisins(M,0))
# print(voisins(M,1))
# print(voisins(M,2))
# print(voisins(M,3))
# print(voisins(M,4))

# Question 4
# ==========
def degre(M,i):
    """
    Entrées : 
      * M(lst) : graphe
      * i : noeud considéré
    Sortie :
      * (int) : nomnbre de voisins
    """
    return len(voisins(M,i))

# Question 5
# ==========
