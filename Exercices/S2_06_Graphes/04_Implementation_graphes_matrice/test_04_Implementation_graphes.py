# -*- coding: utf-8 -*-
"""
Created on Thu May 12 15:57:49 2022

@author: xpess
"""


from copy import deepcopy
import implementation_graphes as ref
import implementation_graphes as eleve
#import eleve as eleve

# Création d'une autre matrice d'adjacences
GG = [[0, 1, 2, 3, 4, 5],
      [1, 0, 6, 7, 8, 9],
      [2, 6, 0,-1,-1,-1],
      [3, 7,-1, 0,-1,-1],
      [4, 8,-1,-1,-1,-1],
      [5, 9,-1,-1,-1,-1]]

# Question 1
def test_Q1():
    # On vérifie si les matrices d'adjacences sont les mêmes.
    assert eleve.G == ref.G

def test_Q2_01():
    # On regarde si les voisins de 0 sont les mêmes
    # TODO : les voisins sont pas forcément dans le meme ordre
    assert eleve.voisins(GG,0) == ref.voisins(GG,0)
    
def test_Q2_02():
    # On regarde si les voisins de 2 sont les mêmes
    # TODO : les voisins sont pas forcément dans le meme ordre
    assert eleve.voisins(GG,2) == ref.voisins(GG,2)

def test_Q2_03():
    # On regarde si les voisins de n sont les mêmes
    # TODO : les voisins sont pas forcément dans le meme ordre
    n = len(GG)-1
    assert eleve.voisins(GG,n) == ref.voisins(GG,n)

def test_Q2_04():
    # On regarde si le nombre de voisins est le meme
    for i in range(len(GG)):
        assert len(eleve.voisins(GG,i)) == len(ref.voisins(GG,i))

    
def test_Q3_01():
    # On vérifie que les listes d'arêtes sont identiques
    ea = eleve.aretes(GG)
    ea.sort()
    
    ra = ref.aretes(GG)
    ra.sort()
    assert ea == ra
    
def test_Q5():
    # On vérifie que chacun des sommets du graphe GG ont les mêmes degrés
    for i in range(len(GG)):
        assert eleve.degre(GG,i) == ref.degre(GG,i)
        
def test_Q6_01():
    chemin = [1,2,3]
    assert eleve.longueur(GG, chemin) == ref.longueur(GG, chemin)
    
def test_Q6_02():
    chemin = [4,5]
    assert eleve.longueur(GG, chemin) == ref.longueur(GG, chemin)
    

def test_Q7_01():
    # On ajoute un sommet et on vérifie que les graphes sont les memes
    sommet = [4,3]
    poids = [10,20]
    A = deepcopy(GG)
    B = deepcopy(GG)
    ref.ajout_sommet(A, sommet, poids)
    eleve.ajout_sommet(B, sommet, poids)
    assert A == B
    

def test_Q8_01():
    # On supprime le dernier sommet
    A = deepcopy(GG)
    B = deepcopy(GG)
    ref.supprime_sommet(A, 0)
    eleve.supprime_sommet(B, 0)
    assert A == B
    
def test_Q8_02():
    # On supprime le dernier sommet
    A = deepcopy(GG)
    B = deepcopy(GG)
    n = len(A)-1
    ref.supprime_sommet(A, n)
    eleve.supprime_sommet(B, n)
    assert A == B
    