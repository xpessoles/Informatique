# -*- coding: utf-8 -*-
"""
Created on Thu May 12 15:57:49 2022

@author: xpess
"""


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
    
def test_Q3_01():
    assert eleve.aretes(G)