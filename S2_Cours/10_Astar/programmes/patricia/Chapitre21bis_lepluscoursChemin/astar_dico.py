import numpy as np


### l'heuristique avec la méthode de détermination des distances du cours
def heuristique(pt1:tuple,A:tuple)->int:
    '''Calcul de la valeur de l'heuristique avec la méthode du cours,
    14 pour un déplacement diagonal et 10 pour un déplacement sur le côté
    entrées :
    pt1, tuple ou list des coordonnées
    A, tuple ou list des coordonnées
    sortie :
    H : integer, valeur de l'heuristique
    '''
    a=abs(pt1[0]-A[0])
    b=abs(pt1[1]-A[1])
    if a<=b:
        return (a*14+(b-a)*10)
    else:
        return (b*14+(a-b)*10)

# >>> heuristique([2,7],[0,1])
# 68
# >>> heuristique([1,0],[0,1])
# 14
# >>> heuristique([0,5],[0,1])
# 40


### les voisins sont les cases à côté du point considéré en ligne droite ou en diagonale
def estVoisin(M:dict,pt1:tuple):
    l,c=pt1
    voisins=[]
    for i in [-1,0,1]:
        for j in [-1,0,1]:
            if (l+i,c+j) in M:
                voisins.append((l+i,c+j))
    voisins.remove(pt1)
    return voisins

# >>> estVoisin(G,[1,2])
# [[0, 1], [0, 2], [0, 3], [1, 1], [1, 3], [2, 1], [2, 2], [2, 3]]

### on peut calculer la distance entre deux points voisins en dehors de Astar
def distance(pt1:tuple,pt2:tuple):
    '''pt1 et pt2 doivent être voisin en ligne ou en diagonale
    '''
    ligne=0
    colonne=0
    i,j=pt1
    l,c=pt2
    if not i==l:
        ligne=1
    if not j==c:
        colonne=1
    if colonne==ligne:
        return 14
    else:
        return 10

# >>> distance([1,2],[0, 3])
# 14



def Astar(M:dict,depart,fin,visited=[]):
    '''calcul le plus court chemin en partant de départ pour atteindre
    arrivée par l'algorithme de Astar avec un heuristique de distance la plus courte
    entrées :
    M : dict, dictionnaire dont chaque sommet est un couple de coordonnées et sa valeur une liste de 4 éléments : G, H, F et le prédécesseur
    départ : un sommet de M dont on connait les coordonnées
    fin : un sommet de M dont on connait les coordonnées
    sortie : None (ne renvoie rien)
    '''
    if depart not in list(M.keys()):
        raise TypeError('Le sommet de départ n\'est pas dans le graphe')
    if fin not in list(M.keys()):
        raise TypeError('Le sommet d\'arrivée n\'est pas dans le graphe')
    # condition de sortie de la boucle récursive
    if depart==fin:
        # on construit le plus court chemin et on l'affiche
        chemin=[]
        pred=fin
        while pred != None:
            chemin.append(M[pred][-1])
            pred=M[pred][-1]
        chemin.reverse() # on retourne la liste dans le bon ordre
        print ('chemin le plus court :'+str(chemin)+' cout='+str(M[fin][2]))

    else :
        # au premier passage, on initialise le coût à 0
        if visited==[] :
            M[depart][0]=0 # changement
        # on visite les successeurs de depart
        voisins=estVoisin(M,depart) # changement
        for voisin in voisins:
            if voisin not in visited:
                # heuristique
                G = M[depart][0] + distance(depart,voisin)
                H = heuristique(voisin,fin)
                F = G + H

                if F < M[voisin][2]:
                    # les distances calculées
                    M[voisin][0] = G
                    M[voisin][1] = H
                    M[voisin][2] = F
                    # le prédécesseur
                    M[voisin][3] = depart
        # On marque comme "visited"
        visited.append(depart)
        # Une fois que tous les successeurs ont été visités : récursivité
        # On choisit les sommets non visités avec la distance globale la plus courte
        # On ré-exécute récursivement Astar en prenant depart='x'
        not_visited={}
        for k in M.keys():
            if not k in visited :
                not_visited[k] = M[k][2]
        x=min(not_visited, key=not_visited.get)
        Astar(M,x,fin,visited)



# G est une matrice de 1 pour les cases adjacentes visibles et -10 pour les obstacles
G=np.ones((5,9))
G[1,4]=-10
G[1,5]=-10
G[2,4]=-10
G[3,4]=-10

# >>> G
# array([[  1.,   1.,   1.,   1.,   1.,   1.,   1.,   1.,   1.],
       # [  1.,   1.,   1.,   1., -10., -10.,   1.,   1.,   1.],
       # [  1.,   1.,   1.,   1., -10.,   1.,   1.,   1.,   1.],
       # [  1.,   1.,   1.,   1., -10.,   1.,   1.,   1.,   1.],
       # [  1.,   1.,   1.,   1.,   1.,   1.,   1.,   1.,   1.]])

depart = G[3,7]
fin = G[0,1]

M={}
ligne,colonne=G.shape
for i in range(ligne):
    for j in range(colonne):
        if not G[i,j]==-10.0:
            M[i,j]=[np.inf,None,np.inf,None]

# avant traitement
# >>> M
# {(0, 0): [inf, None, inf, None], (0, 1): [inf, None, inf, None], (0, 2): [inf, N
# one, inf, None], (0, 3): [inf, None, inf, None], (0, 4): [inf, None, inf, None],
#  (0, 5): [inf, None, inf, None], (0, 6): [inf, None, inf, None], (0, 7): [inf, N
# one, inf, None], (0, 8): [inf, None, inf, None], (1, 0): [inf, None, inf, None],
#  (1, 1): [inf, None, inf, None], (1, 2): [inf, None, inf, None], (1, 3): [inf, N
# one, inf, None], (1, 6): [inf, None, inf, None], (1, 7): [inf, None, inf, None],
#  (1, 8): [inf, None, inf, None], (2, 0): [inf, None, inf, None], (2, 1): [inf, N
# one, inf, None], (2, 2): [inf, None, inf, None], (2, 3): [inf, None, inf, None],
#  (2, 5): [inf, None, inf, None], (2, 6): [inf, None, inf, None], (2, 7): [inf, N
# one, inf, None], (2, 8): [inf, None, inf, None], (3, 0): [inf, None, inf, None],
#  (3, 1): [inf, None, inf, None], (3, 2): [inf, None, inf, None], (3, 3): [inf, N
# one, inf, None], (3, 5): [inf, None, inf, None], (3, 6): [inf, None, inf, None],
#  (3, 7): [inf, None, inf, None], (3, 8): [inf, None, inf, None], (4, 0): [inf, N
# one, inf, None], (4, 1): [inf, None, inf, None], (4, 2): [inf, None, inf, None],
#  (4, 3): [inf, None, inf, None], (4, 4): [inf, None, inf, None], (4, 5): [inf, N
# one, inf, None], (4, 6): [inf, None, inf, None], (4, 7): [inf, None, inf, None],
#  (4, 8): [inf, None, inf, None]}


Astar(M,(3,7),(0,1),[])
# après traitement
# >>> M
# {(0, 0): [inf, None, inf, None], (0, 1): [78, 0, 78, (0, 2)], (0, 2): [68, 10, 7
# 8, (0, 3)], (0, 3): [58, 20, 78, (0, 4)], (0, 4): [48, 30, 78, (0, 5)], (0, 5):
# [38, 40, 78, (1, 6)], (0, 6): [34, 50, 84, (1, 6)], (0, 7): [38, 60, 98, (1, 6)]
# , (0, 8): [inf, None, inf, None], (1, 0): [inf, None, inf, None], (1, 1): [82, 1
# 0, 92, (0, 2)], (1, 2): [72, 14, 86, (0, 3)], (1, 3): [62, 24, 86, (0, 4)], (1,
# 6): [24, 54, 78, (2, 6)], (1, 7): [28, 64, 92, (2, 6)], (1, 8): [inf, None, inf,
#  None], (2, 0): [inf, None, inf, None], (2, 1): [inf, None, inf, None], (2, 2):
# [inf, None, inf, None], (2, 3): [inf, None, inf, None], (2, 5): [24, 48, 72, (2,
#  6)], (2, 6): [14, 58, 72, (3, 7)], (2, 7): [10, 68, 78, (3, 7)], (2, 8): [14, 7
# 8, 92, (3, 7)], (3, 0): [inf, None, inf, None], (3, 1): [inf, None, inf, None],
# (3, 2): [inf, None, inf, None], (3, 3): [inf, None, inf, None], (3, 5): [20, 52,
#  72, (3, 6)], (3, 6): [10, 62, 72, (3, 7)], (3, 7): [0, None, inf, None], (3, 8)
# : [10, 82, 92, (3, 7)], (4, 0): [inf, None, inf, None], (4, 1): [inf, None, inf,
#  None], (4, 2): [inf, None, inf, None], (4, 3): [inf, None, inf, None], (4, 4):
# [34, 52, 86, (3, 5)], (4, 5): [24, 56, 80, (3, 6)], (4, 6): [14, 66, 80, (3, 7)]
# , (4, 7): [10, 76, 86, (3, 7)], (4, 8): [14, 86, 100, (3, 7)]}






