# -*- coding: utf-8 -*-
"""
Created on Tue Apr 25 14:14:15 2023

@author: xavier.pessoles2
"""
from collections import deque
import matplotlib.pyplot as plt
import random

## Question 1 ##
def creer_graphe(p:int, n:int) -> dict:
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

## Question 2 ##
def get_sommets(G:{}) -> ([],[]):
    # On trace les sommets
    les_x,les_y = [],[]
    for sommet in G.keys() : 
        les_x.append(sommet[0])
        les_y.append(sommet[1])
    return les_x,les_y
                

## Question 4 ##
def get_aretes(G):
    edges = []
    for sommet,voisins in G.items():
        for v in voisins : 
            edge = (sommet,v)
            if (sommet,v) not in edges : 
                if (v,sommet) not in edges : 
                    edges.append(edge)
    return edges


## Question 6 ##
def tracer_graphe(G) :
    # On trace les arrêtes    
    edges = get_aretes(G)
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
    
## Question 7 ##
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
        

## Question 8 ##
def parcours_largeur(G,depart) :
    labyrinthe = {}
    predecesseurs = {}
    
    for sommet in G.keys():
        predecesseurs[sommet] = False
    
    file = deque([(depart,depart)])
    
    while len(file) > 0:
        s1,s2 = file.pop()
        if predecesseurs[s1] == False:
            predecesseurs[s1] = s2
            voisins = G[s1]
            for v in voisins:
                file.appendleft((v,s1))
            ajouter_arete(labyrinthe, s1, s2)        
    return labyrinthe
    
   
# G = creer_graphe(10, 8)
# tracer_graphe(G)
# L = parcours_largeur(G)
# tracer_graphe(L)

## Question 9 ##
def parcours_profondeur(G,depart) :
    labyrinthe = {}
    predecesseurs = {}
    
    for sommet in G.keys():
        predecesseurs[sommet] = False
    
    pile = deque([(depart,depart)])
    
    while len(pile) > 0:
        s1,s2 = pile.pop()
        if predecesseurs[s1] == False:
            predecesseurs[s1] = s2
            voisins = G[s1]
            #random.shuffle(voisins)
            for v in voisins:
                pile.append((v,s1))
            ajouter_arete(labyrinthe, s1, s2)        
    return labyrinthe
    
   
# G = creer_graphe(10, 8)
# tracer_graphe(G)
# L = parcours_profondeur(G)
# tracer_graphe(L)

## Question 10 ##
def labyrinthe_largeur(G) :
    labyrinthe = {}
    predecesseurs = {}
    
    for sommet in G.keys():
        predecesseurs[sommet] = False
    
    depart = (0,0)
    
    file = deque([(depart,depart)])
    
    while len(file) > 0:
        s1,s2 = file.pop()
        if predecesseurs[s1] == False:
            predecesseurs[s1] = s2
            voisins = G[s1]
            random.shuffle(voisins)
            for v in voisins:
                file.appendleft((v,s1))
            ajouter_arete(labyrinthe, s1, s2)        
    return labyrinthe
    
   
# G = creer_graphe(10, 8)
# tracer_graphe(G)
# L = labyrinthe_largeur(G)
# tracer_graphe(L)


def labyrinthe_profondeur(G) :
    labyrinthe = {}
    predecesseurs = {}
    
    for sommet in G.keys():
        predecesseurs[sommet] = False
    
    depart = (0,0)
    
    pile = deque([(depart,depart)])
    
    while len(pile) > 0:
        s1,s2 = pile.pop()
        if predecesseurs[s1] == False:
            predecesseurs[s1] = s2
            voisins = G[s1]
            random.shuffle(voisins)
            for v in voisins:
                pile.append((v,s1))
            ajouter_arete(labyrinthe, s1, s2)        
    return labyrinthe
    
   
# G = creer_graphe(10, 8)
# tracer_graphe(G)
# L = labyrinthe_profondeur(G)
# tracer_graphe(L)


## Question 11 ##
def resolution_largeur(G) :
    labyrinthe = {}
    predecesseurs = {}
    
    for sommet in G.keys():
        predecesseurs[sommet] = False
    
    depart = (0,0)
    
    file = deque([(depart,depart)])
    
    while len(file) > 0:
        s1,s2 = file.pop()
        if predecesseurs[s1] == False:
            predecesseurs[s1] = s2
            voisins = G[s1]
            #random.shuffle(voisins)
            for v in voisins:
                file.appendleft((v,s1))
            ajouter_arete(labyrinthe, s1, s2)        
    return predecesseurs


def path(pred, s, v):
    L = []
    while v != s:
        L.append(v)
        v = pred[v]
    L.append(s)
    return L[::-1] # inverse le chemin


#chemin = path(pred, s, v)
def plot_chemin(G,chemin):
    # On trace les arrêtes    
    edges = get_aretes(G)
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
    
    
    for i in range(len(chemin)-1):
        seg_x = [chemin[i][0] , chemin[i+1][0]]
        seg_y = [chemin[i][1] , chemin[i+1][1]]
        plt.plot(seg_x,seg_y,"k")
    plt.show()
    
G = creer_graphe(10, 8)
L = labyrinthe_profondeur(G)

chemin_inv = resolution_largeur(L)
chemin = path(chemin_inv,(0,0),(9,7))
tracer_graphe(L)
plot_chemin(L, chemin)


