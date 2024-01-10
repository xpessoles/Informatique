# -*- coding: utf-8 -*-
"""
Created on Thu Jul  6 12:47:07 2023

@author: xavier.pessoles2
"""

import matplotlib.pyplot as plt
import random as rd
import numpy as np
import math as m

## Question 1
def cor_distance(p1:[int],p2:[int])-> float :
    x1,y1 = p1
    x2,y2 = p2
    dx = x2 - x1
    dy = y2 - y1
    return m.sqrt(dx*dx+dy*dy)

## Question 2
def cor_creer_grille(n:int)-> [[int]] :
    L = []
    for i in range(n+1):
        for j in range(n+1):
            L.append([i,j])
    return L
    
## Question 3
def cor_creer_distances(n:int)-> [[float]] :
    G = cor_creer_grille(n)
    tab_dist = []
    for i in range(len(G)) :
        L = []
        for j in range(len(G)) :
            L.append(cor_distance(G[i],G[j]))
        tab_dist.append(L)
    return tab_dist   
    
## Question 4
def cor_longueur(chemin:[int], tab:[[float]]) -> float :
    l = 0
    for i in range(len(chemin)-1) :
        l = l + tab[i][i+1]
    return l

    
## TESTS ##
def test_q01(foo):
    pts = 0
    total = 0
    
    total +=1
    p1,p2 = [0,0],[1,0]
    try :
        L1 = cor_distance(p1,p2)
        L2 = foo(p1,p2)
        if (np.allclose(L1,L2)):
            pts +=1 
    except : 
        pass
    
    total +=1
    p1,p2 = [0,0],[1,1]
    try :
        L1 = cor_distance(p1,p2)
        L2 = foo(p1,p2)
        if (np.allclose(L1,L2)):
            pts +=1 
    except : 
        pass
    
    total +=1
    p1,p2 = [0,0],[-1,-1]
    try :
        L1 = cor_distance(p1,p2)
        L2 = foo(p1,p2)
        if (np.allclose(L1,L2)):
            pts +=1 
    except : 
        pass
    
    total +=1
    p1,p2 = [2,5],[-3,-5]
    try :
        L1 = cor_distance(p1,p2)
        L2 = foo(p1,p2)
        if (np.allclose(L1,L2)):
            pts +=1 
    except : 
        pass
    return pts,total

def test_q02(foo):
    pts = 0
    total = 0
    
    total +=1
    n = 1
    try :
        L1 = cor_creer_grille(n)
        L2 = foo(n)
        if (np.allclose(L1,L2)):
            pts +=1 
    except : 
        pass
    
    total +=1
    n = 2
    try :
        L1 = cor_creer_grille(n)
        L2 = foo(n)
        if (np.allclose(L1,L2)):
            pts +=1 
    except : 
        pass
    
    total +=1
    n = 4
    try :
        L1 = cor_creer_grille(n)
        L2 = foo(n)
        if (np.allclose(L1,L2)):
            pts +=1 
    except : 
        pass
    
    return pts,total



def test_q03(foo):
    pts = 0
    total = 0
    
    total +=1
    n = 1
    try :
        L1 = cor_creer_distances(n)
        L2 = foo(n)
        if (np.allclose(L1,L2)):
            pts +=1 
    except : 
        pass
    
    total +=1
    n = 2
    try :
        L1 = cor_creer_distances(n)
        L2 = foo(n)
        if (np.allclose(L1,L2)):
            pts +=1 
    except : 
        pass
    
    total +=1
    n = 4
    try :
        L1 = cor_creer_distances(n)
        L2 = foo(n)
        if (np.allclose(L1,L2)):
            pts +=1 
    except : 
        pass
    
    return pts,total
    

def test_q04(foo):
    pts = 0
    total = 0
    
   
    total +=1
    n = 2
    ch = [rd.randrange(0,n) for i in range(5)]
    G = cor_creer_distances(n)
    try :
        L1 = cor_longueur(ch,G)
        L2 = foo(ch,G)
        if (np.allclose(L1,L2)):
            pts +=1 
    except : 
        pass
    
    total +=1
    n = 4
    ch = [rd.randrange(0,n) for i in range(5)]
    G = cor_creer_distances(n)
    try :
        L1 = cor_longueur(ch,G)
        L2 = foo(ch,G)
        if (np.allclose(L1,L2)):
            pts +=1 
    except : 
        pass
    
    return pts,total


    
def go(foo1,foo2,foo3,foo4):
    i = 0
    notes = {}
    tot = 2
    

    pts = 0
    i +=1
    try :
        pts,tot = test_q01(foo1)
    except : 
        pass
    print("Question "+str(i)+" : ",str(pts),"/",str(tot))
    notes[i] = (pts,tot)
    
    pts = 0
    i +=1
    try :
        pts,tot = test_q02(foo2)
    except : 
        pass
    print("Question "+str(i)+" : ",str(pts),"/",str(tot))
    notes[i] = (pts,tot)
    
    pts = 0
    i +=1
    try :
        pts,tot = test_q03(foo3)
    except : 
        pass
    print("Question "+str(i)+" : ",str(pts),"/",str(tot))
    notes[i] = (pts,tot)

    pts = 0
    i +=1
    try :
        pts,tot = test_q04(foo4)
    except : 
        pass
    print("Question "+str(i)+" : ",str(pts),"/",str(tot))
    notes[i] = (pts,tot)



    
    #bilan : 
    points,total = 0,0
    for n in notes.values() :
        points = points + n[0]
        total = total + n[1]
    print(points,total)