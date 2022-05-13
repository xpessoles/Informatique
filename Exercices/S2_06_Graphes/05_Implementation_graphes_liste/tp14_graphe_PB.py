import networkx as nx
import matplotlib.pyplot as plt

### question 1
G=[[1,2,4],[2,3,0],[0,1,3,4],[1,2],[0,2]]


### question 2
def voisins_l(G:list, i:int)->list:
    '''Fonction qui renvoie un élément de la liste G
    '''
    return G[i]


### question 3
def aretes_l(G:list)->list:
    '''Fonction qui construit à partir d'une liste d'adjacence la liste des arêtes sans doublon
    entrée :
    G : list, liste d'adjacence
    sortie :
    L : list, liste des couples de sommets voisins
    '''
    L=[]
    for i in range(len(G)):
        for j in range(len(G[i])):
            if i<G[i][j]:
                L.append((i,G[i][j]))
    return L

### question 4
def plot_graphe_l(G):
    Gx=nx.Graph()
    edges=aretes_l(G)
    Gx.add_edges_from(edges)
    nx.draw(Gx,with_labels = True)
    plt.show()


plt.figure('graphe non pondéré')
plot_graphe_l(G)


### question 5
def degre_l(G:list,i:int)->int:
    '''fonction qui renvoie la longueur de la liste d'indice i
    '''
    return len(G[i])


### question 6
# (ce n'est pas simplement ajouter une liste L à G, il faut ajouter le nouveau sommet à la liste des voisins)

def ajout_sommet_l(G,L):
    '''fonction qui renvoie la liste G avec un élément L ajouté
    '''
    n=len(G)
    for element in L:
        G[element].append(len(G))
    G.append(L)

ajout_sommet_l(G,[0,1])
# >>> G
# [[1, 2, 4, 5], [2, 3, 0, 5], [0, 1, 3, 4], [1, 2], [0, 2], [0, 1]]
plt.figure('graphe non pondéré + un sommet')
plot_graphe_l(G)


### question 7
# (ce n'est pas simplement supprimer la liste G[i], il faut enlever la référence du sommet dans les voisins)

def supprime_sommet_l(G,i):
    '''fonction supprime l'élément de G à l'indice i
    entrées :
    G : list, la liste d'adjacence
    i : int, un indice de la liste
    sortie :
    ne renvoie rien et fonctionne avec effet de bord
    '''
    L=G[i]  # liste des voisins de i à supprimer
    for j in L: # pour chaque voisin
        G[j].remove(i) # supprime le sommet i de la liste des voisins
    G[i]=[] # pour l'affichage... pour avoir bien le sommet supprimé (autrement décale la numérotation)

# >>> supprime_sommet_l(G,5)
# >>> G
# [[1, 2, 4], [2, 3, 0], [0, 1, 3, 4], [1, 2], [0, 2]]
# >>> supprime_sommet_l(G,1)
# >>> G
# [[2, 4], [0, 3, 4], [2], [0, 2]]


### exercice 2
### question 8
MG=[[0,9,3,-1,7],[9,0,1,8,-1],[3,1,0,4,2],[-1,8,4,0,-1],[7,-1,2,-1,0]]


### question 9
def voisins(G,i):
    '''Recherche les voisins du sommet i à partir de la matrice d'adjacence et les renvoie sous forme de liste
    '''
    L=[]
    for j in range(len(G)):
        if not G[i][j]==0 and not G[i][j]==-1:
            L.append(j)
    return L

# >>> voisins(MG,1)
# [0, 2, 3]


### question 10
def aretes(G:list)->list:
    L=[]
    for i in range(len(G)):
        for j in range(i+1,len(G)):
            if not G[i][j]==0 and not G[i][j]==-1:
                L.append((i,j))
    return L


### pour aller plus loin, mettre le poids de chaque arête
def aretes2(G:list)->list:
    L=[]
    for i in range(len(G)):
        for j in range(i+1,len(G)):
            if not G[i][j]==0 and not G[i][j]==-1:
                L.append((i,j,{'weight':G[i][j]}))
    return L

# >>> aretes2(MG)
# [(0, 1, {'weight': 9}), (0, 2, {'weight': 3}), (0, 4, {'weight': 7}), (1, 2, {'weight': 1}), (1, 3, {'weight': 8}), (2, 3, {'weight': 4}), (2, 4, {'weight': 2})]

### question 11
def plot_graphe(G):
    Gx=nx.Graph()
    edges=aretes(G)
    Gx.add_edges_from(edges)
    nx.draw(Gx,with_labels = True)
    plt.show()


plt.figure('graphe pondéré')
plot_graphe(MG)


### pour aller plus loin, mettre le poids de chaque arête
def aretes2(G:list)->list:
    L=[]
    for i in range(len(G)):
        for j in range(i+1,len(G)):
            if not G[i][j]==0 and not G[i][j]==-1:
                L.append((i,j,{'weight':G[i][j]}))
    return L

# >>> aretes2(MG)
# [(0, 1, {'weight': 9}), (0, 2, {'weight': 3}), (0, 4, {'weight': 7}), (1, 2, {'weight': 1}), (1, 3, {'weight': 8}), (2, 3, {'weight': 4}), (2, 4, {'weight': 2})]
def plot_graphe_pondere(G):
    Gx=nx.Graph()
    edge=aretes2(G)
    for element in edge:
        Gx.add_edges_from([(element[0],element[1])], weight=element[2]['weight'])

    edge_labels=dict([((u,v,),d['weight'])
                    for u,v,d in Gx.edges(data=True)])

    #commande pour tracer le graphe
    pos=nx.circular_layout(Gx)
    nx.draw_networkx_edge_labels(Gx,pos,edge_labels=edge_labels)
    nx.draw(Gx,pos, with_labels=True)
    plt.show()

def plot_graphe_pondere_oriente(G):
    Gx=nx.DiGraph() # simple modification pour passer d'un graphe non orienté à un graphe orienté
    edge=aretes2(G)
    for element in edge:
        Gx.add_edges_from([(element[0],element[1])], weight=element[2]['weight'])

    edge_labels=dict([((u,v,),d['weight'])
                    for u,v,d in Gx.edges(data=True)])

    #commande pour tracer le graphe
    pos=nx.circular_layout(Gx)
    nx.draw_networkx_edge_labels(Gx,pos,edge_labels=edge_labels)
    nx.draw(Gx,pos, with_labels=True)
    plt.show()





### question 12
def degre(G,i):
    s=0
    for j in range(len(G[i])):
        if not G[i][j]==0 and not G[i][j]==-1:
            s+=1
    return s


### question 13
def longueur(G,L):
    s=0
    for i in range(len(L)-1):
        if not G[L[i]][L[i+1]]==-1:
            s=s+G[L[i]][L[i+1]]
        else:
            return -1
    return s

# >>> longueur(MG,[0,2,3])
# 7
# >>> longueur(MG,[0,4,2,1])
# 10
# >>> longueur(MG,[4,0,3])
# -1

### question 14
def ajout_sommet(M:list,L:list,poids:list):
    '''fonction qui renvoie la matrice d'adjacence avec un sommet supplémentaire
    '''
    n=len(M)
    # on construit la dernière ligne
    ligne=[-1]*(n)+[0]
    for i in range(len(L)):
        ligne[L[i]]=poids[i]
    M.append(ligne)
    # travail sur la dernière colonne
    for j in range(len(ligne)-1):
        M[j].append(ligne[j])

### question 15
# >>> ajout_sommet(MG,[1,4],[6,5])
# >>> MG
# [[0, 9, 3, -1, 7, -1], [9, 0, 1, 8, -1, 6], [3, 1, 0, 4, 2, -1], [-1, 8, 4, 0, -1, -1], [7, -1, 2, -1, 0, 5], [-1, 6, -1, -1, 5, 0]]

### question 16
def supprime_sommet(M:list,i:int):
    '''supprime la colonne i et la ligne i de la matrice carrée M
    '''
    for j in range(len(M)):
        M[j].pop(i)
    M.pop(i)

# >>> MG
# [[0, 9, 3, -1, 7], [9, 0, 1, 8, -1], [3, 1, 0, 4, 2], [-1, 8, 4, 0, -1], [7, -1, 2, -1, 0]]
# >>> supprime_sommet(MG,2)
# >>> MG
# [[0, 9, -1, 7], [9, 0, 8, -1], [-1, 8, 0, -1], [7, -1, -1, 0]]

### question 17
def from_list_to_matrix(G:list)->list:
    '''Construit une matrice d'adjacence à partir d'une liste d'adjacence avec 0 et 1
    '''
    M=[]
    for i in range(len(G)):
        L=[0]*len(G)
        for element in G[i]:
            L[element]=1
        M.append(L)
    return M

# >>> from_list_to_matrix(G)
# [[0, 1, 1, 0, 1, 1], [1, 0, 1, 1, 0, 1], [1, 1, 0, 1, 1, 0], [0, 1, 1, 0, 0, 0], [1, 0, 1, 0, 0, 0], [1, 1, 0, 0, 0, 0]]

### question 18
def from_matrix_to_list(M:list)->list:
    '''Construit une liste d'adjacence à partir d'une matrice d'adjacence avec 0 et 1
    '''
    G=M[:]
    for i in range(len(G)):
        for j in range(len(G)):
            if G[i][j]==0:
                G[i][j]='autre'
            else:
                G[i][j]=j
        G[i]=list(set(G[i])) # enlève les doublons
        G[i].remove('autre')
    return G

# >>> G
# [[1, 2, 4, 5], [2, 3, 0, 5], [0, 1, 3, 4], [1, 2], [0, 2], [0, 1]]
# >>> from_list_to_matrix(G)
# [[0, 1, 1, 0, 1, 1], [1, 0, 1, 1, 0, 1], [1, 1, 0, 1, 1, 0], [0, 1, 1, 0, 0, 0], [1, 0, 1, 0, 0, 0], [1, 1, 0, 0, 0, 0]]
# >>> from_matrix_to_list([[0, 1, 1, 0, 1, 1], [1, 0, 1, 1, 0, 1], [1, 1, 0, 1, 1, 0], [0, 1, 1, 0, 0, 0], [1, 0, 1, 0, 0, 0], [1, 1, 0, 0, 0, 0]])
# [[1, 2, 4, 5], [0, 3, 2, 5], [0, 1, 3, 4], [1, 2], [0, 2], [0, 1]]







