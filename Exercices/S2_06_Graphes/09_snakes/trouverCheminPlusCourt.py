import matplotlib.pyplot as plt
import networkx as nx
from collections import deque

dSeE = {  1: 38,  4: 14,  9: 31, 17:  7, 21: 42, 28: 84, 51: 67, 54: 34,
         62: 19, 64: 60, 71: 91, 80: 99, 87: 24, 93: 73, 95: 75, 98: 79}

def position(case):
    j = (case-1) // 10
    i = (case-1) % 10
    if j % 2 == 1: # j impair
        i = 9 - i
    return i, j

def caseFuture(case):
    if case in dSeE.keys():
        return dSeE[case]
    else:
        return case

def avanceCase(case, de, choix):
    if case + de <= 100:
        return caseFuture(case + de)
    else:
        if choix == 'r':
            case_ = 100 - (case+de)%100
            return caseFuture(case_)
        elif choix == 'i':
            return case
        elif choix == 'q':
            return 100

def casesAccessibles(case):
    cases = []
    for de in range(1, 7):
        cases.append(avanceCase(case, de, 'i'))
    return cases

def eliminationDoublon(L):
    res = []
    for elt in L:
        if elt not in L:
            res.append(elt)
    return res

def eliminationDoublon(L):
    res = []
    d = {}
    for elt in L:
        d[elt] = None
    for elt in d:
        res.append(elt)
    return res

def chemin(G, depart, arrivee):
    predecesseur = {}
    file = deque([depart])
    predecesseur[depart] = None
    while file:
        sommet = file.popleft()
        for successeurDeSommet in G[sommet]:
            if successeurDeSommet not in predecesseur.keys():
                file.append(successeurDeSommet)
                predecesseur[successeurDeSommet] = sommet
    return arrivee in predecesseur

def chemin(G, depart, arrivee):
    predecesseur = {}
    file = deque([depart])
    predecesseur[depart] = None
    while file:
        sommet = file.popleft()
        for successeurDeSommet in G[sommet]:
            if successeurDeSommet not in predecesseur.keys():
                file.append(successeurDeSommet)
                predecesseur[successeurDeSommet] = sommet
    if depart == arrivee:
        return [depart]
    elif arrivee not in predecesseur:
        return []
    else:
        L = deque()
        sommet = arrivee
        while sommet != None:
            L.appendleft(sommet)
            sommet = predecesseur[sommet]
        return list(L)

def partieOptimale():
    return chemin(G, 0, 100)

G = {}
for case in range(100):
    if case not in dSeE.keys():
        G[case] = eliminationDoublon(casesAccessibles(case))
G[100] = []

