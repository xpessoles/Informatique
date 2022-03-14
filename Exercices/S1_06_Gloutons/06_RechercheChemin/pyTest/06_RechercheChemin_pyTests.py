# -*- coding: utf-8 -*-
"""
Created on Thu Jan  6 15:55:01 2022

@author: xpess
@author Serge Bays https://mathematice.fr/fichier.php?menu=pcsi&adr=pcsi_tp06a.pdf&vid=6

"""

import RechercheCheminCorrige as ref
import RechercheCheminEleve as eleve
#import RechercheCheminCorrige as eleve


from random import randint
import math as m
import numpy as np

nbpoints, dim = 20, 20
def points(n, c):
    liste = []
    while len(liste) < n:
        x = randint(-c, c)
        y = randint(-c, c)
        if [x, y] not in liste:
            liste.append([x, y])
    return liste

depart = (randint(-dim, dim), randint(-dim, dim))
pts = points(nbpoints, dim)


def test_Q1():
    assert eleve.ques_1 == 6
    
def test_Q2():
    assert eleve.ques_2 == m.factorial(10)
    
def test_Q3():
    print(eleve.ques_3)

def test_Q4_01():
    pt0,pt1 = pts[0], pts[1]
    dist_el = eleve.distance(pt0,pt1)
    dist_ref = ref.distance(pt0,pt1)
    assert True == np.allclose(np.array(dist_el),np.array(dist_ref))

def test_Q4_02():    
    pt0,pt1 = pts[1], pts[2]
    dist_el = eleve.distance(pt0,pt1)
    dist_ref = ref.distance(pt0,pt1)
    assert True == np.allclose(np.array(dist_el),np.array(dist_ref))
    
def test_Q4_03():    
    pt0,pt1 = pts[2], pts[3]
    dist_el = eleve.distance(pt0,pt1)
    dist_ref = ref.distance(pt0,pt1)
    assert True == np.allclose(np.array(dist_el),np.array(dist_ref))
    
def test_Q5():
    tab_eleve = eleve.distances(pts,depart)
    tab_ref = ref.distances(pts,depart)
    return True == np.allclose(np.array(tab_eleve),np.array(tab_ref))

def test_Q6():
    assert eleve.ques_6 == 10*9/2
    
def test_Q7_01():
    tab_eleve = eleve.distances(pts,depart)
    tab_ref = ref.distances(pts,depart)
    chemin = [0,1,2,3,4]    
    l_eleve = eleve.longueur(chemin, tab_eleve)
    l_ref = ref.longueur(chemin, tab_ref)    
    assert True == np.allclose(np.array(l_eleve),np.array(l_ref))

def test_Q7_02():
    tab_eleve = eleve.distances(pts,depart)
    tab_ref = ref.distances(pts,depart)
    chemin = [0,2,4,6,8]    
    l_eleve = eleve.longueur(chemin, tab_eleve)
    l_ref = ref.longueur(chemin, tab_ref)    
    assert True == np.allclose(np.array(l_eleve),np.array(l_ref))
    
    
def test_Q8_01():
    tab_eleve = eleve.distances(pts,depart)
    tab_ref = ref.distances(pts,depart)
    chemin = [0,1,2,3,4]    
    l_eleve = eleve.longueur_rec(chemin, tab_eleve)
    l_ref = ref.longueur(chemin, tab_ref)    
    assert True == np.allclose(np.array(l_eleve),np.array(l_ref))

def test_Q8_02():
    tab_eleve = eleve.distances(pts,depart)
    tab_ref = ref.distances(pts,depart)
    chemin = [0,2,4,6,8]    
    l_eleve = eleve.longueur_rec(chemin, tab_eleve)
    l_ref = ref.longueur(chemin, tab_ref)    
    assert True == np.allclose(np.array(l_eleve),np.array(l_ref))
    

def test_Q9_01():
    assert eleve.ques_9_pts == 5
    
def test_Q9_02():
    assert eleve.ques_9_pts_parc == 3 
    
def test_Q9_03():
    assert eleve.ques_9_pts_parc_liste == "a,p3,p4"
 
def test_Q10():
      print(eleve.ques_10)

def test_Q11_01():
    tab_eleve = eleve.distances(pts,depart)
    tab_ref = ref.distances(pts,depart)
    position, dispo = 19, [True, True, True, False, True, True, True, True, True, True, True, True, True, True, True, True, False, True, True, False]
    ind_el = eleve.indice(position, tab_eleve, dispo)
    ind_ref = eleve.indice(position, tab_ref, dispo)
    assert ind_el == ind_ref

def test_Q11_02():
    tab_eleve = eleve.distances(pts,depart)
    tab_ref = ref.distances(pts,depart)
    position, dispo = 9, [False, True, True, False, True, False, True, False, True, False, True, True, True, True, True, True, False, True, True, False]
    ind_el = eleve.indice(position, tab_eleve, dispo)
    ind_ref = ref.indice(position, tab_ref, dispo)
    assert ind_el == ind_ref
    

def test_Q12():
    tab_eleve = eleve.distances(pts,depart)
    tab_ref = ref.distances(pts,depart)
    ch_eleve = eleve.plus_court(tab_eleve)
    ch_ref = ref.plus_court(tab_ref)
    assert ch_eleve == ch_ref
    
    
    