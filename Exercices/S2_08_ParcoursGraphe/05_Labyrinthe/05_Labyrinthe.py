# -*- coding: utf-8 -*-
"""
Created on Tue Apr 25 14:14:15 2023

@author: xavier.pessoles2
"""
from collections import deque
import matplotlib.pyplot as plt
import random

def creer_graphe(n:int, p:int):
    G = {}
    sommets = []
    for i in range(p):
        for j in range(n):
            sommets.append((i,j))
    
    for sommet in sommets : 
        (i,j) = sommet
        voisins = [(i+1,j),(i-1,j),(i,j+1),(i,j-1)]
        # On vérifie que les voisins sont dans les sommets
        vv = []
        for v in voisins : 
            if v in sommets : 
                vv.append(v)
                
        G[sommet]=vv
    return G
                
    
def get_edges(G):
    edges = []
    for sommet,voisins in G.items():
        for v in voisins : 
            edge = (sommet,v)
            if (sommet,v) not in edges : 
                if (v,sommet) not in edges : 
                    edges.append(edge)
    return edges
    

def tracer_graphe(G) :
    # On trace les arrêtes    
    edges = get_edges(G)
    for edge in edges : 
        x = [edge[0][0],edge[1][0]]
        y = [edge[0][1],edge[1][1]]
        plt.plot(x,y,'lightcoral')
    
    # On trace les sommets
    les_x,les_y = [],[]
    for sommet in G.keys() : 
        les_x.append(sommet[0])
        les_y.append(sommet[1])
    plt.plot(les_x,les_y,"o",color="royalblue")
    
    plt.grid()
    plt.axis("equal")
    plt.show()
    



def ajouter_arete(G,s1,s2):
   
    if (s1 not in G) or (s2 not in G) :     # Ou bien s1 et s2 ne sont pas dans G
        G[s1]=[s2]
        G[s2]=[s1]
    # Ou bien ils y sont tous les 2
    else : 
        if s2 not in G[s1] :
            G[s1].append(s2)
            G[s2].append(s1)
# Parcours de graphe en largeur
def bfs(G,s) -> None:
    """
    G : graphe sous forme de dictionnaire d'adjacence
    s : sommet du graphe (Chaine de caractere du type "S1").
    """
    laby = {}
    visited = {}
    for sommet,voisins in G.items():
        visited[sommet] = False
    # Le premier sommet à visiter entre dans la file
    file = deque([s])
    while len(file) > 0:
        # On visite la tête de file
        tete = file.pop()
        # On vérifier qu'elle n'a pas été visitée
        if not visited[tete]:
            # Si on l'avait pas visité, maintenant c'est le cas :)
            visited[tete] = True
            
            # On met les voisins de tete dans la file
            voisins = G[tete]
            random.shuffle(voisins)
            for v in voisins:
                file.appendleft(v)
                ajouter_arete(laby, tete, v)
                
    return laby
G = creer_graphe(5,10)
tracer_graphe(G)
laby = bfs(G,(0,0))
tracer_graphe(laby)