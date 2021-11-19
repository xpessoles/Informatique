# === Import des modules ===
import numpy as np
import matplotlib.pyplot as plt

from numpy.random import rand
from matplotlib.colors import ListedColormap

# === Fonctions prédéfinies ===
def sauvegarder_grille(grille : list, nom_de_fichier : str) -> None:
    # Echelle Blanc : 0, Noir : 1, Blue : 2
    echelle = ListedColormap(['white','black','aqua'],2)
    plt.matshow(grille,cmap=echelle,vmin=0,vmax=2)
    plt.colorbar()
    plt.savefig(nom_de_fichier)
    return None

def afficher_grille(grille : list) -> None:
    echelle = ListedColormap(['white','black','aqua'],2)
    plt.matshow(grille,cmap=echelle,vmin=0,vmax=2)
    plt.colorbar()
    plt.show()
    return None
# ==============================

##Partie 2 : Choix d'un modèle
# Question 1
def creation_grille_vierge(n:int) -> list :
    '''crée un grille vide (valeur 0) de dimension  n*n sous la forme d'une liste de liste'''
    grille = []
    for i in range (n):
        ligne = []
        for j in range (n):
            ligne.append(0)
        grille.append(ligne)
    return grille

# Question 2
# g = creation_grille_vierge(3)
# afficher_grille(g)

# Question 3
# g = [[1, 0, 1], [0, 1, 0], [1, 0, 1]]
# afficher_grille(g)

# Question 4
def creation_zebreh(n:int) -> list :
    '''crée une grille zébrée horizontalement de taille n*n'''
    grille = []
    for i in range (n):
        ligne = []
        for j in range (n):
            if i%2 == 0 :
                ligne.append(1)
            else :
                ligne.append(0)
        grille.append(ligne)
    return grille

# g = creation_zebreh(3)
# afficher_grille(g)

# Question 5
def creation_zebrev(n:int) -> list :
    '''crée une grille zébrée verticalement de taille n*n'''
    grille = []
    for i in range (n):
        ligne = []
        for j in range (n):
            if j%2 == 0 :
                ligne.append(1)
            else :
                ligne.append(0)
        grille.append(ligne)
    return grille

# g = creation_zebrev(3)
# afficher_grille(g)

# Question 6
def creation_damier(n:int) -> list :
    '''crée une grille de type damier de taille n*n'''
    grille = []
    for i in range (n):
        ligne = []
        for j in range (n):
            if (j%2 == 0 and i%2 == 0) or (j%2 == 1 and i%2 == 1):
                ligne.append(1)
            else :
                ligne.append(0)
        grille.append(ligne)
    return grille

# g = creation_damier(3)
# afficher_grille(g)

# Question 7
def creation_grille(p: float, n: int) -> list :
    '''crée une grille aléatoire pour laquelle chaque case a la probabilité p d'être ouverte'''
    grille = creation_grille_vierge(n)
    for i in range(n) :
        for j in range(n) :
            nb = rand()
            if nb > p :
                grille[i][j] = 1
    return grille


def creation_grille_bis(p: float, n: int) -> list :
    '''crée une grille aléatoire pour laquelle chaque case a la probabilité p d'être ouverte'''
    L=[[1 for i in range(n)] for j in range(n)]

    for i in range (n):
        for j in range(n):
            nb=rand()
            if nb<p:
                L[i][j]=0
    return(L)

# g=creation_grille(0.5,10)
# afficher_grille(g)


##Partie 3 : Percolation
# Question 8
def a_un_voisin_rempli(grille: list,i:int,j:int):
    '''renvoie un booléen indiquant si l'un des voisins est rempli (valeur 2)'''
    test=False
    n=len(grille)
    if j+1<n and grille[i][j+1]==2:
        test=True
    elif j-1>=0 and grille[i][j-1]==2 :
        test=True
    elif i-1>=0 and grille[i-1][j]==2:
        test=True
    elif i+1<n and grille[i+1][j]==2 :
        test=True
    return(test)


# g[1][5]=2
# print(a_un_voisin_rempli(g,4,5))
# print(a_un_voisin_rempli(g,4,4))
# print(a_un_voisin_rempli(g,3,5))
# print(a_un_voisin_rempli(g,8,5))

# Question 9
def percolation_V0(grille : list) -> None:
    '''réalise la percolation en modifiant sur place la grille'''
    #premiere ligne
    n=len(grille)
    for j in range(n):
        if grille[0][j]==0:
            grille[0][j]=2
    #lignes suivantes
    for i in range(1,n):
        for j in range(n):
            if grille[i][j]==0 and a_un_voisin_rempli(grille,i,j):
                grille[i][j]=2



#Q10
def percolation(grille : list) -> None:
    '''réalise la percolation en modifiant sur place la grille'''
    #premiere ligne
    n=len(grille)
    for j in range(n):
        if grille[0][j]==0:
            grille[0][j]=2

    pas_fini=True

    while pas_fini:
        pas_fini=False
        for i in range(1,n):
            for j in range(n):
                if grille[i][j]==0 and a_un_voisin_rempli(grille,i,j):
                    grille[i][j]=2
                    pas_fini=True

# percolation(g)
# afficher_grille(g)


#Q11 : Percolation plus évoluée
def percolation2(grille:list)->None :
    '''réalise la percolation en modifiant sur place la grille'''
    n=len(grille)
    liste_coord=[]
    for j in range(n):
        if grille[0][j]==0:
            liste_coord.append([0,j])
            grille[0][j]=2
    while len(liste_coord)>0:
        i,j=liste_coord[0]
        del(liste_coord[0])
        if j+1<n and grille[i][j+1]==0:
            liste_coord.append([i,j+1])
            grille[i][j+1]=2
        if j-1>=0 and grille[i][j-1]==0 :
            liste_coord.append([i,j-1])
            grille[i][j-1]=2
        if i-1>=0 and grille[i-1][j]==0:
            liste_coord.append([i-1,j])
            grille[i-1][j]=2
        if i+1<n and grille[i+1][j]==0 :
            liste_coord.append([i+1,j])
            grille[i+1][j]=2

#Q12 : Validation de la percolation
g=creation_grille(0.5,10)
afficher_grille(g)
percolation2(g)
afficher_grille(g)


g=creation_grille(0.8,10)
afficher_grille(g)
percolation2(g)
afficher_grille(g)



#Q13
def teste_percolation(p : float, n : int) -> bool:
    '''teste la réussite de la percolation'''
    grille=creation_grille(p,n)
    percolation(grille)
    #afficher_grille(grille)
    j=0
    while j<=n-1 and grille[n-1][j]!=2:
        j=j+1
    return(j<=n-1)

b=teste_percolation(0.9,10)

##Partie 4 : seuil critique
#Q14
def proba(p, k=20, n=128) -> float:
    reussites=0
    for i in range(k):
        if teste_percolation(p, n):
            reussites=reussites+1
    return(reussites/k)


def tracer_proba(n):
    x=np.linspace(0,1,21)
    y=[]
    for p in x:
        y.append(proba(p,20,n))
    plt.clf()
    plt.plot(x,y)
    plt.show()
    return None

#tracer_proba(128)
