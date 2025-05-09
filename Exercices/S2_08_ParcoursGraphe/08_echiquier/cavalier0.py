# -*- coding: utf-8 -*-

## importation des modules
import numpy as np
import matplotlib.pyplot as plt
import networkx as nx

## déclaration des fonctions
def dessinerGraphe(G):
    plt.figure()
    nx.draw(G, with_labels=True, pos=nx.kamada_kawai_layout(G))
    plt.show()

def estDansEch(i, j):
    return 0 <= i < 8 and 0 <= j < 8

def mvtsPossibles(i, j):
    L = []
    for di in [-2, -1, 1, 2]:
        for dj in [-2, -1, 1, 2]:
            if abs(di) + abs(dj) == 3 and estDansEch(i+di, j+dj):
                L.append((i+di, j+dj))
    return L



def codage(i, j):
    return chr(ord('a') + i) + str(j+1)

## programme principal
G = {}
for i in range(8):
    for j in range(8):
        G[(i, j)] = mvtsPossibles(i, j)

Nb_aretes = 0
for c in G.keys():
    Nb_aretes += len(G[c])
print(Nb_aretes/2)

G2 = {}
for i in range(8):
    for j in range(8):
        code = codage(i, j)
        mvts = mvtsPossibles(i, j)
        G2[code] = [codage(i_, j_) for (i_, j_) in mvts]


G_repr = nx.from_dict_of_lists(G2, create_using=nx.Graph)
dessinerGraphe(G_repr)



def bfs(G:dict, s:str) -> None:
    """
    G : graphe sous forme de dictionnaire d'adjacence
    s : sommet du graphe (Chaine de caractere du type "S1").
    """
    visited = {}
    for sommet,voisins in G.items():
        visited[sommet] = False
        # Le premier sommet àvisiter entre dans la file
        file = deque([s])
        while len(file) > 0:
            # On visite la tête de file
            tete = file.pop()
            # On vérifier qu'elle n'a pas été visitée
            if not visited[tete]:
            # Si on l'avait pas visité, maintenant c'est le cas :)
                visited[tete] = True
                # On met les voisins de tete dans la file
                for v in G[tete]:
                    file.appendleft(v)

# G = nx.DiGraph()
# G.add_nodes_from(sommets)
# G.add_edges_from(arcs)
# dessinerGraphe(G)
#
# G1 = nx.from_dict_of_lists(dictAdj(sommets, arcs), create_using=nx.DiGraph)
# dessinerGraphe(G1)
#
# M = np.array(listeDeListes(sommets, arcs))
# G2 = nx.from_numpy_matrix(M, create_using=nx.DiGraph)
# dessinerGraphe(G2)
#
