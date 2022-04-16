#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = "Xavier PESSOLES"

import matplotlib.pyplot as plt
import networkx as nx


# Question 1
# ==========
# Matrices avec des listes
M=[[0,9,3,-1,7],[9,0,1,8,-1],[3,1,0,4,2],[-1,8,4,0,-1],[7,-1,2,-1,0]]

# Question 2 & 3
# ==============
def voisins(M:list, i:int) -> list:
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

# Question 3
# ===========
def arretes(G:list)->list:
    """
    Renvoie la liste des arêtes sous forme de tuples.
    """
    # Il suffit de travailler sur le triangle supérieur
    nb_l = len(G)
    nb_c = len(G[0])
    edges = []
    for i in range(0,nb_l):
        for j in range (i+1,nb_c):
            if G[i][j] >0 :
                edges.append((i,j))
    return edges
            
# Question 4
# ===========
def plot_graphe(G):
    edges = arretes(G)
    Gx = nx.Graph()
    Gx.add_edges_from(edges)
    nx.draw(Gx,with_labels = True)
    plt.show()
plot_graphe(M)
    
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

def longueur(M,chemin):
    l = 0
    for i in range(len(chemin)-1):
        if M[chemin[i]][chemin[i+1]]<0:
            return -1
        else :
            l=l+M[chemin[i]][chemin[i+1]]
    return l
    
chemin = [1,2,3,1,4]
print(longueur(M,chemin))
        
chemin = [0,4,2,1,0]
print(longueur(M,chemin))
