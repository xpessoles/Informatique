# -*- coding: utf-8 -*-
"""
Created on Tue Apr 12 23:49:24 2022

@author: xpess
"""

from collections import deque

def bfs(G, s):
    """
    Parcours d'un graphe en largeur

    Parameters
    ----------
    G : graphe sous forme de dictionnaire d'adjacence
    s : sommet du graphe (Chaine de caractere du type "S1").

    Returns
    -------
    None.

    """
    visited = {}
    for sommet,voisins in G.items():
        visited[sommet]=False
    # Le premier sommet à visiter entre dans la file
    q = deque([s])
    while len(q) > 0:
        # On visite la tête de file
        u = q.pop()
        
        # On vérifier qu'elle n'a pas été visitée
        if not visited[u]:
            # Si on l'avait pas visité, maintenant c'est le cas :)
            visited[u] = True
            
            # On met les voisins de u dans la file
            for v in G[u]:
                q.appendleft(v)

graphe = {"S0":["S1"],\
          "S1":["S0","S2","S3","S4","S5"],\
          "S2":["S1","S3"],\
          "S3":["S1","S2","S4"],\
          "S4":["S1","S3","S6"],\
          "S5":["S1"],\
          "S6":["S4"]}


def bfs_pr(G, s):
    visited = {}
    for sommet,voisins in G.items():
        visited[sommet]=False
    q = deque([s])
    while len(q) > 0:
        print('================')
        print(q)
        print(visited)
        u = q.pop()
        print(u)
        if not visited[u]:
            visited[u] = True
            for v in G[u]:
                q.appendleft(v)
        

def bfs_parcours(G, s):
    visited = {}
    for sommet,voisins in G.items():
        visited[sommet]=False
    q = deque([s])
    chemin = []
    while len(q) > 0:
        u = q.pop()
        if not visited[u]:
            chemin.append(u)
            visited[u] = True
            for v in G[u]:
                q.appendleft(v)
    return chemin


def dfs(G, s): 
    visited = {}
    for sommet,voisins in G.items():
        visited[sommet]=False
        
    pile = [s]
    while len(pile) > 0:
        u = pile.pop()
        if not visited[u]:
            visited[u] = True
            for v in G[u]:
                pile.append(v)

def dfs_pr(G, s): 
    visited = {}
    for sommet,voisins in G.items():
        visited[sommet]=False
        
    pile = [s]
    while len(pile) > 0:
        u = pile.pop()
        if not visited[u]:
            visited[u] = True
            print(u)
            for v in G[u]:
                pile.append(v)


graphe2 = {"S0":["S1","S2","S3"],\
          "S1":["S0","S3"],\
          "S2":["S0"],\
          "S3":["S0","S1"]}

                
dfs_pr(graphe2, "S0")
#bfs_pr(graphe, "S0")