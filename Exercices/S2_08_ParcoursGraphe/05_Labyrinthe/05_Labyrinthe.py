# -*- coding: utf-8 -*-
"""
Created on Tue Apr 25 14:14:15 2023

@author: xavier.pessoles2
"""
from collections import deque
import matplotlib.pyplot as plt
import random

def creer_graphe(n:int, p:int):
    # n : lignes
    # p : colonnes
    G = {}
    sommets = []
    for i in range(n):
        for j in range(p):
            sommets.append((j,i))
    
    for sommet in sommets : 
        (i,j) = sommet
        voisins = [(i+1,j),(i,j+1),(i-1,j),(i,j-1)]
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
    plt.plot(les_x,les_y,".",color="royalblue")
    
    plt.grid()
    plt.axis("equal")
    plt.show()
    



def ajouter_arete(G,s1,s2):
    
    # s1 et s2 ne sont pas dans G
    if (s1 not in G) and (s2 not in G) :     
        G[s1]=[s2]
        G[s2]=[s1]
    
    # s1 est dans G, s2 n'est pas dans G,
    elif (s1 in G) and (s2 not in G) :
        G[s2]=[s1]
        G[s1].append(s2)
    
    # s1 n'est pas dans G, s1 est dans G,
    elif (s1 not in G) and (s2 in G) :
        G[s1]=[s2]
        G[s2].append(s1)
    else : 
        G[s2].append(s1)
        G[s1].append(s2)
        
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
            #random.shuffle(voisins)
            for v in voisins:
                file.appendleft(v)
                if v not in laby :
                    ajouter_arete(laby, tete, v)
        
                
    return laby


# Parcours de graphe en profondeur
def dfs(G,s) -> None:
    """
    G : graphe sous forme de dictionnaire d'adjacence
    s : sommet du graphe (Chaine de caractere du type "S1").
    """
    laby = {}
    visited = {}
    for sommet,voisins in G.items():
        visited[sommet] = False
    # Le premier sommet à visiter entre dans la file
    pile = deque([s])
    while len(pile) > 0:
        # On visite la tête de file
        tete = pile.pop()
        # On vérifier qu'elle n'a pas été visitée
        if not visited[tete]:
            # Si on l'avait pas visité, maintenant c'est le cas :)
            visited[tete] = True
            # On met les voisins de tete dans la file
            voisins = G[tete]
            #random.shuffle(voisins)
            for v in voisins:
                pile.append(v)
                if v not in laby :
                    ajouter_arete(laby, tete, v)
        
                
    return laby

def labyrinthe(G,s) -> None:
    """
    G : graphe sous forme de dictionnaire d'adjacence
    s : sommet du graphe (Chaine de caractere du type "S1").
    """
    laby = {}
    visited = {}
    for sommet,voisins in G.items():
        visited[sommet] = False
    # Le premier sommet à visiter entre dans la file
    pile = deque([s])
    while len(pile) > 0:
        # On visite la tête de file
        tete = pile.pop()
        # On vérifier qu'elle n'a pas été visitée
        if not visited[tete]:
            # Si on l'avait pas visité, maintenant c'est le cas :)
            visited[tete] = True
            # On met les voisins de tete dans la file
            voisins = G[tete]
            random.shuffle(voisins)
            for v in voisins:
                pile.append(v)
                if v not in laby :
                    ajouter_arete(laby, tete, v)
        
                
    return laby

l,c = 8,10
G = creer_graphe(l,c)
tracer_graphe(G)
laby = bfs(G,(0,0))
tracer_graphe(laby)

labyrinthe = labyrinthe(G,(0,0))
tracer_graphe(labyrinthe)
