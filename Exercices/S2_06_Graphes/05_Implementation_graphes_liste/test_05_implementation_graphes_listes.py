# -*- coding: utf-8 -*-
"""
Created on Thu May 12 15:57:49 2022

@author: xpess
"""


from copy import deepcopy
import implementation_graphes_listes as ref
import implementation_graphes_listes as eleve
#import tp14_graphe_PB as eleve

#import eleve as eleve

# Création d'une liste d'adjacences
GG = [[1,2,3,4],[0,2],[0,1,3,4],[0,2,4],[0,2,3]]

# Question 1
def test_Q1():
    # On vérifie si les matrices d'adjacences sont les mêmes.
    assert eleve.G == ref.G

def test_Q2_01():
    # On regarde si les voisins de 0 sont les mêmes
    # TODO : les voisins sont pas forcément dans le meme ordre
    assert eleve.voisins_l(GG,0) == ref.voisins_l(GG,0)
    
def test_Q2_02():
    # On regarde si les voisins de 2 sont les mêmes
    # TODO : les voisins sont pas forcément dans le meme ordre
    assert eleve.voisins_l(GG,2) == ref.voisins_l(GG,2)

def test_Q2_03():
    # On regarde si les voisins de n sont les mêmes
    # TODO : les voisins sont pas forcément dans le meme ordre
    n = len(GG)-1
    assert eleve.voisins_l(GG,n) == ref.voisins_l(GG,n)

def test_Q2_04():
    # On regarde si le nombre de voisins est le meme
    for i in range(len(GG)):
        assert len(eleve.voisins_l(GG,i)) == len(ref.voisins_l(GG,i))

    
def test_Q3_01():
    # On vérifie que les listes d'arêtes sont identiques
    ea = eleve.aretes_l(GG)
    ea.sort()
    
    ra = ref.aretes_l(GG)
    ra.sort()
    assert ea == ra
    
def test_Q5():
    # On vérifie que chacun des sommets du graphe GG ont les mêmes degrés
    for i in range(len(GG)):
        assert eleve.degre_l(GG,i) == ref.degre_l(GG,i)

def test_Q6_01():
    # On ajoute un sommet et on vérifie que les graphes sont les memes
    sommet = [1,2]
    A = deepcopy(GG)
    B = deepcopy(GG)
    ref.ajout_sommet_l(A, sommet)
    eleve.ajout_sommet_l(B, sommet)
    assert A == B
    

def test_Q7_01():
    # On supprime le premier sommet à
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
    
def test_Q8_03():
    # On supprime le sommet 1
    A = deepcopy(GG)
    B = deepcopy(GG)

    ref.supprime_sommet(A, 1)
    eleve.supprime_sommet(B, 1)
    assert A == B

