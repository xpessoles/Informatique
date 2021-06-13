from prog import *
import pytest

#Q1

def cor_creation_grille(p, n):
    grille = np.zeros((n, n))
    for i in range(n):
        for j in range(n):
            if rand() < p:
                grille[i][j] = 1.0
    return grille



def test_creation_grille1():
    grille=creationgrille(0.5, 10)
    cor_grille=cor_creation_grille(0.5, 10)
    assert grille.shape == cor_grille.shape

def test_creation_grille2():
    grille=creationgrille(0.5, 10)
    assert grille.max() == 1.0

def test_creation_grille3():
    grille=creationgrille(0.5, 10)
    res=True
    for i in range(10):
        for j in range(10):
            if grille[i,j]!=0.0 and grille[i,j]!=1.0:
                res=False
    assert res == True

def test_creation_grille4():
    grille=creationgrille(0.6, 20)
    cor_grille=cor_creation_grille(0.6, 20)
    assert grille.shape == cor_grille.shape

#Q02

def test_afficher_grille1():
    grille=cor_creation_grille(0.5, 10)
    assert afficher_grille(grille,'testQ02.png') == None

#Q03

def cor_percolation(grille):
    n, p = grille.shape
    lst = []
    for j in range(p):
        if grille[0][j] == 1.: # les cases vides de la première ligne
            grille[0][j] = .5 # sont remplies et ajoutées à lst
            lst.append((0, j))
    while len(lst) > 0:
        (i, j) = lst.pop() # une case est extraite de lst
        if i > 0 and grille[i-1][j] == 1.: # si le voisin haut est vide, il est rempli
            grille[i-1][j] = .5
            lst.append((i-1, j))
        if i < n-1 and grille[i+1][j] == 1.: # si le voisin bas est vide, il est rempli
            grille[i+1][j] = .5
            lst.append((i+1, j))
        if j > 0 and grille[i][j-1] == 1.: # si le voisin gauche est vide, il est rempli
            grille[i][j-1] = .5
            lst.append((i, j-1))
        if j < p - 1 and grille[i][j+1] == 1.: # si le voisin droit est vide, il est rempli
            grille[i][j+1] = .5
            lst.append((i, j+1))

def test_percolation1():
    grille=cor_creation_grille(0.5, 10)
    grille0=np.copy(grille)
    percolation(grille)
    cor_percolation(grille0)
    test_grille=grille0==grille
    res=True
    for i in range(10):
        for j in range(10):
            if test_grille[i,j]!=True:
                res=False
    assert res==True

def test_percolation2():
    grille=cor_creation_grille(0.5, 10)
    assert cor_percolation(grille) == None


#Q05

def cor_teste_percolation(p, n):
    grille = cor_creation_grille(p, n)
    cor_percolation(grille)
    for j in range(n):
        if grille[n-1][j] == .5:
            return(True)
    return(False)

def test_teste_percolation1():
    grille=cor_creation_grille(0.5, 10)
    grille0=np.copy(grille)
    cor_percolation(grille)
    n=10
    res_cor=False
    j=0
    while j<n and grille[n-1][j] != .5:
        j+=1
    if grille[n-1][j-1] == .5:
        res_cor=True
    res=False
    j=0
    while j<n and grille0[n-1][j] != .5:
        j+=1
    if grille0[n-1][j-1] == .5:
        res=True
    assert res==res_cor

#Q06

def cor_proba(p, k, n):
    s = 0
    for i in range(k):
        if cor_teste_percolation(p, n):
            s += 1
    return s/k

def test_proba1():
    res_cor=cor_proba(0.8, 10, 128)
    res=proba(0.8, 10, 128)
    assert res==res_cor

def test_proba2():
    res_cor=cor_proba(0.1, 10, 128)
    res=proba(0.1, 10, 128)
    assert res==res_cor

def test_proba3():
    res_cor=cor_proba(0.7, 10, 128)
    res=proba(0.7, 10, 128)
    assert res==res_cor

def test_proba4():
    res_cor=cor_proba(0.4, 10, 128)
    res=proba(0.4, 10, 128)
    assert res==res_cor

#Q07

def test_tracer_proba():
    assert tracer_proba(20,'testQ07.png') == None




