# -*- coding: utf-8 -*-
"""
Created on Sun May 29 18:11:32 2022

@author: xpess
"""
from collections import deque

G1 = {"0":["1","4"],
      "1":["0","2","5","6"],
      "2":["3","6"],
      "3":["2","7"],
      "4":["5"],
      "5":[],
      "6":["7"],
      "7":["6"]}

def parcours_largeur(g,s:str) -> None :
    """
    Parcours en largeur d'un graphe défini par dictionnaire
    d'adjacence

    Parameters
    ----------
    g : dict
        grahe.
    s : str
        sommet de départ.

    Returns
    -------
    None 

    """
    # On défini le dictionnaire permettant gérant les visites des sommets
    visited = {}
    for key,value in g.items():
        visited[key]=False
    
    file = deque([s])
    while len(file) > 0:
        u = file.pop()
        # On vérifie que le sommet n'a pas été visité
        if not visited[u]:
            # Si on l'avait pas visité, maintenant c'est le cas :)
            visited[u] = True
            # On met les voisins de u dans la file
            for v in g[u]:
                file.appendleft(v)

def parcours_largeur_distances(g,s:str) :

    visited = {}
    distances = {}
    for key,value in g.items():
        visited[key]=False
        distances[key]=float("inf")
    
    # Initialisation de la distance de départ
    distances[s]=0
    
    file = deque([s])
    while len(file) > 0:
        u = file.pop()
        if not visited[u]:
            visited[u] = True
            for v in g[u]:
                if distances[v]==float('inf'):
                    file.appendleft(v)
                    distances[v]=1+distances[u]
    return distances
    