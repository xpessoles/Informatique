#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = "Xavier PESSOLES"

import matplotlib.pyplot as plt
import networkx as nx


# Question 1
# ==========
# Matrices avec des listes
M=[[1,2,4],[0,2,3],[0,1,3,4],[1,2],[0,2]]

# Question 2
# ==========
def voisins_l(M:list, i:int) -> list:
    """
    Entrées : 
      * M(lst) : graphe (liste d'adjacence)
      * i : noeud considéré
    Sortie :
      * v(lst) : liste des voisins
    """
    
    return M[i]

# Question 3
# ===========
def arretes_l(G:list)->list:
    """
    Renvoie la liste des arêtes sous forme de tuples.
    """
    edges = []
    for i in range(len(G)):
        for sommet in G[i]:
            e = (i,sommet)
            e2 = (sommet,i)
            # Pour éviter les doublons
            if (e not in edges) and (e2 not in edges) : 
                edges.append(e)
    
    return edges

            
# Question 4
# ===========
def plot_graphe_l(G):
    edges = arretes_l(G)
    Gx = nx.Graph()
    Gx.add_edges_from(edges)
    nx.draw(Gx,with_labels = True)
    plt.show()
    
# print(voisins(M,0))
# print(voisins(M,1))
# print(voisins(M,2))
# print(voisins(M,3))
# print(voisins(M,4))

# Question 5
# ==========
def degre_l(M,i):
    """
    Entrées : 
      * M(lst) : graphe
      * i : noeud considéré
    Sortie :
      * (int) : nombre de voisins
    """
    return len(M[i])



def ajout_sommet_l(G:list, L:list)-> None :
    # On ajoute le sommet et ses voisins
    index_sommet = len(G)
    G.append(L)
    for s in L : 
        G[s].append(index_sommet)
   


# A REFAIRE CA MARCHE PAS
def supprime_sommet_l(G,i):
    # Suppression des voisins i dans chaque voisins
    for j in range(len(G)):
        if i in G[j] :
            G[j].remove(i)
    #Suppression du sommet
    G.pop(i)
    
        

LL = [4]
# poids = [99]
# plot_graphe(M)
# ajout_sommet(M,LL,poids)
# plot_graphe(M)


              