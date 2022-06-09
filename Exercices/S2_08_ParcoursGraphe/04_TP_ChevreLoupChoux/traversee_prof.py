# -*- coding: utf-8 -*-

## importation des modules
from collections import deque

## déclaration graphe sous forme d'un dictionnaire d'adjacence

G = {
    'PLCX': ['LX'], 'PCX': ['X', 'C'], 'PLX': ['LX', 'X', 'L'],
    'LX': ['PLCX', 'PLX'], 'X': ['PCX', 'PLX'], 'PLC': ['C', 'L'],
    'PC': ['C', ''], 'C': ['PCX', 'PLC', 'PC'], 'L': ['PLX', 'PLC'], '': ['PC']}

## déclaration des fonctions

def parcoursProfondeur(G):
    def explorationProfondeur(s):
        parcouru[s] = True
        for ss in G[s]: # G[s] liste des successeurs de s dans G
            if not parcouru[ss]:
                explorationProfondeur(ss) # appel récursif
    parcouru = {}   # dictionnaire de booléens pour le marquage
    for s in G.keys(): # Itération sur les clés de G (dictionnaire de listes)
        parcouru[s] = False # initialisation du marquage
    for r in G.keys(): # Itération sur les clés de G (dictionnaire de listes)
        if not parcouru[r]:
            explorationProfondeur(r)

def parcoursLargeur(G):
    def explorationLargeur(r):
        f = deque() # initialisation d'une deque vide
        f.append(r)
        parcouru[r] = True
        while f:    # Vrai tant que f est non-vide
            s = f.popleft()
            for ss in G[s]: # G[s] liste des successeurs de s dans G
                if not parcouru[ss]:
                    f.append(ss)
                    parcouru[ss] = True
    parcouru = {}   # dictionnaire de booléens pour le marquage
    for s in G.keys(): # Itération sur les clés de G (dictionnaire de listes)
        parcouru[s] = False # initialisation du marquage
    for r in G.keys(): # Itération sur les clés de G (dictionnaire de listes)
        if not parcouru[r]:
            explorationLargeur(r)

def existence_chemin(G, dep, arr):
    def explorationProfondeur(s):
        parcouru[s] = True
        for ss in G[s]: # G[s] liste des successeurs de s dans G
            if ss == arr:
                return True
            if not parcouru[ss]:
                res = explorationProfondeur(ss) # appel récursif
                if res == True:
                    return True
        return False
    parcouru = {}   # dictionnaire de booléens pour le marquage
    for s in G.keys(): # Itération sur les clés de G (dictionnaire de listes)
        parcouru[s] = False # initialisation du marquage
    if dep == arr:
        return True
    res = explorationProfondeur(dep)
    return res

def trouver_chemin(G, dep, arr):
    def explorationProfondeur(s):
        parcouru[s] = True
        for ss in G[s]: # G[s] liste des successeurs de s dans G
            if ss == arr:
                predecesseur[ss] = s
                return True
            if not parcouru[ss]:
                res = explorationProfondeur(ss) # appel récursif
                predecesseur[ss] = s
                if res == True:
                    return True
        return False
    parcouru = {}   # dictionnaire de booléens pour le marquage
    for s in G.keys(): # Itération sur les clés de G (dictionnaire de listes)
        parcouru[s] = False # initialisation du marquage
    predecesseur = {}
    explorationProfondeur(dep)
    # reconstruction du chemin
    f = deque([arr])
    sommet = arr
    while sommet != dep:
        sommet = predecesseur[sommet]
        f.appendleft(sommet)
    return list(f)



## programme principal
parcoursProfondeur(G)
parcoursLargeur(G)

print(existence_chemin(G, 'PLCX', ''))
print(trouver_chemin(G, 'PLCX', ''))