import matplotlib.pyplot as plt
from collections import deque
import random as random

### question 1
def creer_graphe(n:int,p:int)->dict:
    G={}
    def estDansGrille(i,j):
        return i>=0 and i<n and j>=0 and j<p
    for i in range(n):
        for j in range(p):
            L=[]
            for s in [(i+1,j),(i-1,j),(i,j+1),(i,j-1)]:
                if estDansGrille(s[0],s[1]):
                    L.append(s)
            G[(i,j)]=L
    return G

# >>> creer_graphe(2,2)
# {(0, 0): [(1, 0), (0, 1)], (0, 1): [(1, 1), (0, 0)], (1, 0): [(0, 0), (1, 1)], (1, 1): [(0, 1), (1, 0)]}


### question 2
def get_sommets(G:dict)->(list,list):
    les_x,les_y=[],[]
    for cle in G.keys():
        les_y.append(cle[0]) # les lignes donnent les y
        les_x.append(cle[1]) # les colonnes donnent les x
    return les_x,les_y

# >>> get_sommets(G)
# ([0, 0, 1, 1], [0, 1, 0, 1])


### question 3
def trace_sommets(G:dict)->None:
    les_x,les_y=get_sommets(G)
    plt.plot(les_x,les_y,'ro')
    plt.axis('equal')
    plt.show()


### question 4
def get_aretes(G:dict)->list:
    A=[]
    for cle in G.keys():
        for s in G[cle]:
            if not [cle,s] in A and not [s,cle] in A:
                A.append([cle,s])
    return A

# >>> get_aretes(G)
# [[(0, 0), (1, 0)], [(0, 0), (0, 1)], [(0, 1), (1, 1)], [(1, 0), (1, 1)]]

### question 5
def trace_aretes(G:dict)->None:
    A=get_aretes(G)
    for a in A:
        plt.plot([a[0][1],a[1][1]],[a[0][0],a[1][0]],'b')
        plt.axis('equal')
    plt.show()


### question 6
def trace_graphe(G:dict)->None:
    plt.figure()
    A=get_aretes(G)
    for a in A:
        plt.plot([a[0][1],a[1][1]],[a[0][0],a[1][0]],'b')
        plt.axis('equal')
    les_x,les_y=get_sommets(G)
    plt.plot(les_x,les_y,'ro')
    plt.axis('equal')
    plt.show()  
    #trace_aretes(G)
    #trace_sommets(G)

### generation du labyrinthe
### question 7
def ajouter_arete(G:dict,s1:tuple,s2:tuple)->None:
    if not s1 in G.keys():
        G[s1]=[s2]
    if not s2 in G.keys():
        G[s2]=[s1]
    if not s2 in G[s1]:
        G[s1].append(s2)
    if not s1 in G[s2]:
        G[s2].append(s1)
    #return G

G={}
ajouter_arete(G,(0,0),(0,1))
print (G)

### parcours en largeur (arbre couvrant)
def explorationLargeur(G:dict, s1:tuple)->dict:
    visited = {}
    for s in G.keys():
        visited[s] = False
    file=deque()
    file.append(s1)
    visited[s1]= True
    sommetsExplores={}
    while not len(file)==0:
        r=file.popleft()
        if not r in sommetsExplores.keys():
            sommetsExplores[r]=[]
        for rr in G[r]:
            if not visited[rr]:
                file.append(rr)
                visited[rr] = True
                sommetsExplores[r].append(rr)
    return sommetsExplores

def explorationLargeur2(G:dict, s1:tuple)->dict:
    visited = {}
    for s in G.keys():
        visited[s] = False
    file=deque()
    file.append(s1)
    visited[s1]= True
    sommetsExplores={}
    while not len(file)==0:
        r=file.popleft()
        for rr in G[r]:
            if not visited[rr]:
                file.append(rr)
                visited[rr] = True
                ajouter_arete(sommetsExplores,r,rr)
    return sommetsExplores

trace_graphe(explorationLargeur2(creer_graphe(5,8),(0,0)))

# >>> explorationLargeur(creer_graphe(5,8),(0,0),(3,7))
# {(0, 0): [(1, 0), (0, 1)], (1, 0): [(2, 0), (1, 1)], (0, 1): [(0, 2)], (2, 0): [(3, 0), (2, 1)], (1, 1): [(1, 2)], (0, 2): [(0, 3)], (3, 0): [(4, 0), (3, 1)], (2, 1): [(2, 2)], (1, 2): [(1, 3)], (0, 3): [(0, 4)], (4, 0): [(4, 1)], (3, 1): [(3, 2)], (2, 2): [(2, 3)], (1, 3): [(1, 4)], (0, 4): [(0, 5)], (4, 1): [(4, 2)], (3, 2): [(3, 3)], (2, 3): [(2, 4)], (1, 4): [(1, 5)], (0, 5): [(0, 6)], (4, 2): [(4, 3)], (3, 3): [(3, 4)], (2, 4): [(2, 5)], (1, 5): [(1, 6)], (0, 6): [(0, 7)], (4, 3): [(4, 4)], (3, 4): [(3, 5)], (2, 5): [(2, 6)], (1, 6): [(1, 7)], (0, 7): [], (4, 4): [(4, 5)], (3, 5): [(3, 6)], (2, 6): [(2, 7)], (1, 7): [], (4, 5): [(4, 6)], (3, 6): [(3, 7)]}


def explorationProfondeur(G:dict, s1:tuple)->dict:
    visited = {}
    for s in G.keys():
        visited[s] = False
    pile=[s1]
    visited[s1] = True
    sommetsExplores={}
    while not len(pile)==0:
        s=pile.pop()
        c=0
        i=0
        while c==0 and i<len(G[s]):
            if not visited[G[s][i]]:
                c=1
                pile.append(G[s][i])
                visited[G[s][i]]=True
                # je ne prends que le dernier celui que je dépile
                ajouter_arete(sommetsExplores,s,G[s][i])
            i+=1
    return sommetsExplores

trace_graphe(explorationProfondeur(creer_graphe(5,8),(0,0)))
# {(0, 0): [(0, 1)], (0, 1): [(0, 2)], (0, 2): [(0, 3)], (0, 3): [(0, 4)], (0, 4): [(0, 5)], (0, 5): [(0, 6)], (0, 6): [(0, 7)], (0, 7): [(1, 7)], (1, 7): [(1, 6)], (1, 6): [(1, 5)], (1, 5): [(1, 4)], (1, 4): [(1, 3)], (1, 3): [(1, 2)], (1, 2): [(1, 1)], (1, 1): [(1, 0)], (1, 0): [(2, 0)], (2, 0): [(2, 1)], (2, 1): [(2, 2)], (2, 2): [(2, 3)], (2, 3): [(2, 4)], (2, 4): [(2, 5)], (2, 5): [(2, 6)], (2, 6): [(2, 7)], (2, 7): [(3, 7)]}


### on réalise un arbre couvrant par un parcours en largeur et par un parcours en profondeur

def labyrinthe_largeur(G:dict, s1:tuple)->dict:
    visited = {}
    for s in G.keys():
        visited[s] = False
    file=deque()
    file.append(s1)
    visited[s1]= True
    sommetsExplores={}
    while not len(file)==0:
        r=file.popleft()
        random.shuffle(G[r])
        for rr in G[r]:
            if not visited[rr]:
                file.append(rr)
                visited[rr] = True
                ajouter_arete(sommetsExplores,r,rr)
    return sommetsExplores

trace_graphe(labyrinthe_largeur(creer_graphe(5,8),(0,0)))

### attention à la construction du dictionnaire labyrinthe, les sommets en bout de chemin n'ont pas de voisins, à modifier
def grapheConforme(G:dict):
    for cle in G.keys():
        for c,v in G.items():
            if cle in v and not c in G[cle]:
                G[cle].append(c)
            for e in v:
                if not e in G.keys():
                    G[e]=c

# attention, ne fonctionne pas, utiliser ajouter_aretes() à la fin uniquement
def arbre_profondeur(G:dict, s1:tuple)->dict:
    # dictionnaire des sommets visités
    visited = {}
    for s in G.keys():
        visited[s] = False
    # pile avec le premier sommet
    pile=[s1] #
    visited[s1] = True
    # sommets explorés et les arètes
    sommetsExplores={}
    while not len(pile)==0:
        s=pile.pop()
        if not s in sommetsExplores.keys():
            pile.append(s) # on remet le sommet dans la pile tant que tous les voisins n'ont pas été vus
        c=0
        i=0
        random.shuffle(G[s])
        while c==0 and i<len(G[s]):
            if not visited[G[s][i]]: # on ne cherche qu'un seul voisin
                c=1
                pile.append(G[s][i])
                visited[G[s][i]]=True
                # je ne prends que le dernier celui que je dépile
                ajouter_arete(sommetsExplores,s,G[s][i])
            i+=1
        # si s n'a plus de voisin, on redescend
    return sommetsExplores


### ok, renvoie un graphe complet
def arbre_profondeur3(G:dict, s1:tuple)->dict:
    # dictionnaire des sommets visités
    visited = {}
    for s in G.keys():
        visited[s] = False
    # pile avec le premier sommet
    pile=[s1] #
    visited[s1] = True
    # sommets explorés et les arètes
    sommetsExplores={}
    while not len(pile)==0:
        s=pile.pop()
        if not s in sommetsExplores.keys():
            sommetsExplores[s]=[]
            pile.append(s) # on remet le sommet dans la pile tant que tous les voisins n'ont pas été vus
        c=0
        i=0
        #random.shuffle(G[s])
        while c==0 and i<len(G[s]):
            if not visited[G[s][i]]: # on ne cherche qu'un seul voisin
                c=1
                pile.append(G[s][i])
                visited[G[s][i]]=True
                sommetsExplores[s].append(G[s][i]) # je ne prends que le dernier celui que je dépile
            i+=1
        # si s n'a plus de voisin, on redescend
    # pour les sommets, mettre tous les voisins du labyrinthe
    # on pourrait utiliser ajouter_aretes()
    for c,v in sommetsExplores.items():
        for e in v:
            ajouter_arete(sommetsExplores,e,c)
    return sommetsExplores

# avec grapheConforme()
def arbre_profondeur2(G:dict, s1:tuple)->dict:
    # dictionnaire des sommets visités
    visited = {}
    for s in G.keys():
        visited[s] = False
    # pile avec le premier sommet
    pile=[s1] #
    visited[s1] = True
    # sommets explorés et les arètes
    sommetsExplores={}
    while not len(pile)==0:
        s=pile.pop()
        if not s in sommetsExplores.keys():
            sommetsExplores[s]=[]
            pile.append(s) # on remet le sommet dans la pile tant que tous les voisins n'ont pas été vus
        c=0
        i=0
        random.shuffle(G[s])
        while c==0 and i<len(G[s]):
            if not visited[G[s][i]]: # on ne cherche qu'un seul voisin
                c=1
                pile.append(G[s][i])
                visited[G[s][i]]=True
                sommetsExplores[s].append(G[s][i]) # je ne prends que le dernier celui que je dépile
                # ajouter_arete(sommetsExplores,s,G[s][i])
            i+=1
        # si s n'a plus de voisin, on redescend
    # pour les sommets, mettre tous les voisins du labyrinthe
    # on pourrait utiliser ajouter_aretes()
    grapheConforme(sommetsExplores)
    return sommetsExplores


### question 11 le parcours du labyrinthe
# labyrinthe à partir de l'arbre couvrant en profondeur
labyrinthe=arbre_profondeur3(creer_graphe(5,6),(0,0))
trace_graphe(labyrinthe)

def parcours_largeur(G,s1,s2)->list:
    visited = {}
    for s in G.keys():
        visited[s] = False
    file=deque()
    file.append(s1)
    visited[s1]= True
    L=[]
    while not visited[s2]:
        r=file.popleft()
        L.append(r)
        c=0
        for rr in G[r]:
            # tant qu'il y a des voisins non vus, on les met dans la file
            if not visited[rr]:
                c=1
                file.append(rr)
                visited[rr] = True
        if c==0 and not visited[s2]: # cul de sac, il faut dépiler L
            t=L.pop()
            # enlever les sommets restant de la file
    L.append(s2)
    # dans L il y a des sommets inutiles
    # verification du chemin si deux sommets consécutifs ne sont pas voisins, enlever le premier
    L2=[s2]
    L.pop()
    while len(L)>0:
        sommet=L.pop()
        if sommet in G[L2[0]]:
            L2=[sommet]+L2
    return L2

L=parcours_largeur(labyrinthe,(0,0),(4,5))


def parcours_profondeur(G:dict, s1:tuple, s2:tuple)->dict:
    # dictionnaire des sommets visités
    visited = {}
    for s in G.keys():
        visited[s] = False
    # pile avec le premier sommet, ce sera le chemin
    pile=[s1] #
    visited[s1] = True
    while not visited[s2]:
        s=pile.pop()
        pile.append(s)
        c=0 # variable pour test si encore des voisins
        i=0 # index des voisins
        while c==0 and i<len(G[s]):
            if not visited[G[s][i]]: # on ne cherche qu'un seul voisin
                c=1
                pile.append(G[s][i])
                visited[G[s][i]]=True
            i+=1
        # si s n'a plus de voisin, on redescend
        if c==0 and not visited[s2]:
            pile.pop()
    return pile


L2=parcours_profondeur(labyrinthe,(0,0),(4,5))

def trace_parcours(labyrinthe:dict,L:list):
    trace_graphe(labyrinthe)
    for i in range(len(L)-1):
        plt.plot([L[i][1],L[i+1][1]],[L[i][0],L[i+1][0]],color='black',linewidth=2.0)
        plt.axis('equal')
    plt.show()


trace_parcours(labyrinthe,L)
trace_parcours(labyrinthe,L2)










