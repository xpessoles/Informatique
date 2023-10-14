# -*- coding: utf-8 -*-
"""
Created on Thu Jul  6 12:47:07 2023

@author: xavier.pessoles2
"""

    
## Question 1 ##
def cor_generer_liste_entiers_01(n):
    L = []
    for i in range(n):
        L.append(i)
    return L

def cor_generer_liste_entiers_02(n):
    L = []
    i = 0
    while i < n:
        L.append(i)
        i = i+1
    return L
    
def cor_generer_liste_entiers_03(n: int) -> list :
    return [i for i in range(n)]
    
def cor_generer_liste_entiers_04(deb,fin):
    L = []
    for i in range(deb,fin+1) : 
        L.append(i)
    return L
    
def cor_generer_liste_entiers_05(deb,fin):
    L = []
    i = deb
    while i <= fin: 
        L.append(i)
        i = i+1
    return L

def cor_generer_liste_entiers_06(deb,fin):
    return [i for i in range(deb,fin+1)]
    
def cor_recherche_nb_01(nb: int, L: list) -> bool:
    for e in L : 
        if e == nb : 
            return True
    return False
    
def cor_recherche_nb_02(nb: int, L: list) -> bool:
    i = 0 
    while i < len(L):
        if L[i] == nb : 
            return True
        i = i+1
    return False
    
def cor_recherche_nb_03(nb,L):
    return nb in L

def cor_recherche_first_index_nb_01(nb: int, L: list)-> int :
    for i in range(len(L)):
        if L[i]==nb :
            return i
    return -1

def cor_recherche_first_index_nb_02(nb: int, L: list)-> int :
    i = 0
    while i < len(L):
        if L[i]==nb :
            return i
        i = i+1
    return -1

def cor_recherche_last_index_nb_01(nb: int, L: list)-> int :
    res = -1
    for i in range(len(L)):
        if L[i]==nb :
            res = i
    return res
    
####

    
def test_q01(foo):
    pts = 0
    total = 0
    
    n = 2
    total +=1
    try :
        if (cor_generer_liste_entiers_01(n) ==  foo(n)):
            pts +=1 
    except : 
        pass
    
    n = 5
    total +=1
    try :
        if (cor_generer_liste_entiers_01(n) ==  foo(n)):
            pts +=1 
    except : 
        pass
        
    return pts,total

def test_q02(foo):
    pts = 0
    total = 0
    
    n = 2
    total +=1
    try :
        if (cor_generer_liste_entiers_02(n) ==  foo(n)):
            pts +=1 
    except : 
        pass
    
    n = 5
    total +=1
    try :
        if (cor_generer_liste_entiers_02(n) ==  foo(n)):
            pts +=1 
    except : 
        pass
        
    return pts,total


def test_q03(foo):
    pts = 0
    total = 0
    
    n = 2
    total +=1
    try :
        if (cor_generer_liste_entiers_03(n) ==  foo(n)):
            pts +=1 
    except : 
        pass
    
    n = 5
    total +=1
    try :
        if (cor_generer_liste_entiers_03(n) ==  foo(n)):
            pts +=1 
    except : 
        pass
        
    return pts,total


def test_q04(foo):
    pts = 0
    total = 0
    
    deb,fin = 0,10
    total +=1
    try :
        if (cor_generer_liste_entiers_04(deb,fin) ==  foo(deb,fin)):
            pts +=1 
    except : 
        pass
    
    deb,fin = -5,5
    total +=1
    try :
        if (cor_generer_liste_entiers_04(deb,fin) ==  foo(deb,fin)):
            pts+=1
    except : 
        pass
        
    return pts,total
    
def test_q05(foo):
    pts = 0
    total = 0
    
    deb,fin = 0,10
    total +=1
    try :
        if (cor_generer_liste_entiers_05(deb,fin) ==  foo(deb,fin)):
            pts +=1 
    except : 
        pass
    
    deb,fin = -5,5
    total +=1
    try :
        if (cor_generer_liste_entiers_05(deb,fin) ==  foo(deb,fin)):
            pts+=1
    except : 
        pass
        
    return pts,total


    
def test_q06(foo):
    pts = 0
    total = 0
    
    deb,fin = 0,10
    total +=1
    try :
        if (cor_generer_liste_entiers_06(deb,fin) ==  foo(deb,fin)):
            pts +=1 
    except : 
        pass
    
    deb,fin = -5,5
    total +=1
    try :
        if (cor_generer_liste_entiers_06(deb,fin) ==  foo(deb,fin)):
            pts+=1
    except : 
        pass
        
    return pts,total
    
    
    
def test_q07(foo):
    pts = 0
    total = 0
    
    nb,L = 0, [1,2,3,4]
    total +=1
    try :
        if (cor_recherche_nb_01(nb,L) ==  foo(nb,L)):
            pts +=1 
    except : 
        pass
    
    
    nb,L = 1, [1,2,3,4]
    total +=1
    try :
        if (cor_recherche_nb_01(nb,L) ==  foo(nb,L)):
            pts +=1 
    except : 
        pass
        
    nb,L = 4, [1,2,3,4]
    total +=1
    try :
        if (cor_recherche_nb_01(nb,L) ==  foo(nb,L)):
            pts +=1 
    except : 
        pass
        
    nb,L = 5, [1,2,3,4]
    total +=1
    try :
        if (cor_recherche_nb_01(nb,L) ==  foo(nb,L)):
            pts +=1 
    except : 
        pass
        
    return pts,total

def test_q08(foo):
    pts = 0
    total = 0
    
    nb,L = 0, [1,2,3,4]
    total +=1
    try :
        if (cor_recherche_nb_02(nb,L) ==  foo(nb,L)):
            pts +=1 
    except : 
        pass
    
    
    nb,L = 1, [1,2,3,4]
    total +=1
    try :
        if (cor_recherche_nb_02(nb,L) ==  foo(nb,L)):
            pts +=1 
    except : 
        pass
        
    nb,L = 4, [1,2,3,4]
    total +=1
    try :
        if (cor_recherche_nb_02(nb,L) ==  foo(nb,L)):
            pts +=1 
    except : 
        pass
        
    nb,L = 5, [1,2,3,4]
    total +=1
    try :
        if (cor_recherche_nb_02(nb,L) ==  foo(nb,L)):
            pts +=1 
    except : 
        pass
        
    return pts,total
    
def test_q09(foo):
    pts = 0
    total = 0
    
    nb,L = 0, [1,2,3,4]
    total +=1
    try :
        if (cor_recherche_nb_03(nb,L) ==  foo(nb,L)):
            pts +=1 
    except : 
        pass
    
    
    nb,L = 1, [1,2,3,4]
    total +=1
    try :
        if (cor_recherche_nb_03(nb,L) ==  foo(nb,L)):
            pts +=1 
    except : 
        pass
        
    nb,L = 4, [1,2,3,4]
    total +=1
    try :
        if (cor_recherche_nb_03(nb,L) ==  foo(nb,L)):
            pts +=1 
    except : 
        pass
        
    nb,L = 5, [1,2,3,4]
    total +=1
    try :
        if (cor_recherche_nb_03(nb,L) ==  foo(nb,L)):
            pts +=1 
    except : 
        pass
        
    return pts,total

def test_q10(foo):
    pts = 0
    total = 0
    
    nb,L = 0, [1,2,3,4]
    total +=1
    try :
        if (cor_recherche_first_index_nb_01(nb,L) ==  foo(nb,L)):
            pts +=1 
    except : 
        pass
    
    
    nb,L = 1, [1,2,3,4]
    total +=1
    try :
        if (cor_recherche_first_index_nb_01(nb,L) ==  foo(nb,L)):
            pts +=1 
    except : 
        pass
        
    nb,L = 1, [1,1,3,4]
    total +=1
    try :
        if (cor_recherche_first_index_nb_01(nb,L) ==  foo(nb,L)):
            pts +=1 
    except : 
        pass
        
    nb,L = 4, [1,2,3,4]
    total +=1
    try :
        if (cor_recherche_first_index_nb_01(nb,L) ==  foo(nb,L)):
            pts +=1 
    except : 
        pass
        
    return pts,total
    

def test_q11(foo):
    pts = 0
    total = 0
    
    nb,L = 0, [1,2,3,4]
    total +=1
    try :
        if (cor_recherche_first_index_nb_02(nb,L) ==  foo(nb,L)):
            pts +=1 
    except : 
        pass
    
    
    nb,L = 1, [1,2,3,4]
    total +=1
    try :
        if (cor_recherche_first_index_nb_02(nb,L) ==  foo(nb,L)):
            pts +=1 
    except : 
        pass
        
    nb,L = 1, [1,1,3,4]
    total +=1
    try :
        if (cor_recherche_first_index_nb_02(nb,L) ==  foo(nb,L)):
            pts +=1 
    except : 
        pass
        
    nb,L = 4, [1,2,3,4]
    total +=1
    try :
        if (cor_recherche_first_index_nb_02(nb,L) ==  foo(nb,L)):
            pts +=1 
    except : 
        pass
        
    return pts,total

def test_q12(foo):
    pts = 0
    total = 0
    
    nb,L = 0, [1,2,3,4]
    total +=1
    try :
        if (cor_recherche_last_index_nb_01(nb,L) ==  foo(nb,L)):
            pts +=1 
    except : 
        pass
    
    
    nb,L = 1, [1,2,3,4]
    total +=1
    try :
        if (cor_recherche_last_index_nb_01(nb,L) ==  foo(nb,L)):
            pts +=1 
    except : 
        pass
        
    nb,L = 1, [1,1,3,4]
    total +=1
    try :
        if (cor_recherche_last_index_nb_01(nb,L) ==  foo(nb,L)):
            pts +=1 
    except : 
        pass
        
    nb,L = 4, [1,2,3,4]
    total +=1
    try :
        if (cor_recherche_last_index_nb_01(nb,L) ==  foo(nb,L)):
            pts +=1 
    except : 
        pass
        
    return pts,total
    
    
def go(foo1,foo2,foo3,foo4,foo5,foo6,foo7,foo8,foo9,foo10,foo11,foo12):
    i = 0
    notes = {}
    tot = 2
    
    pts = 0
    i += 1
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
    
    pts = 0
    i +=1
    try :
        pts,tot = test_q05(foo5)
    except : 
        pass
    print("Question "+str(i)+" : ",str(pts),"/",str(tot))
    notes[i] = (pts,tot)
    
    pts = 0
    i +=1
    try :
        pts,tot = test_q06(foo6)
    except : 
        pass
    print("Question "+str(i)+" : ",str(pts),"/",str(tot))
    notes[i] = (pts,tot)
    
    pts = 0
    i +=1
    try :
        pts,tot = test_q07(foo7)
    except : 
        pass
    print("Question "+str(i)+" : ",str(pts),"/",str(tot))
    notes[i] = (pts,tot)
    
    pts = 0
    i +=1
    try :
        pts,tot = test_q08(foo8)
    except : 
        pass
    print("Question "+str(i)+" : ",str(pts),"/",str(tot))
    notes[i] = (pts,tot)
    
    pts = 0
    i +=1
    try :
        pts,tot = test_q09(foo9)
    except : 
        pass
    print("Question "+str(i)+" : ",str(pts),"/",str(tot))
    notes[i] = (pts,tot)
    
    pts = 0
    i +=1
    try :
        pts,tot = test_q10(foo10)
    except : 
        pass
    print("Question "+str(i)+" : ",str(pts),"/",str(tot))
    notes[i] = (pts,tot)
    
    pts = 0
    i +=1
    try :
        pts,tot = test_q11(foo11)
    except : 
        pass
    print("Question "+str(i)+" : ",str(pts),"/",str(tot))
    notes[i] = (pts,tot)
    
    pts = 0
    i +=1
    try :
        pts,tot = test_q12(foo12)
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