# -*- coding: utf-8 -*-
"""
Created on Thu Jul  6 12:47:07 2023

@author: xavier.pessoles2
"""

## Question 1 ##
def compter_lettres_cor(c,mot):
    cpt = 0
    for lettre in mot :
        if lettre == c :
            cpt += 1
    return cpt

def test_q01(foo):
    pts = 0
    total = 0
    
    c,mot = "c","abde"
    total +=1
    try :
        if (compter_lettres_cor(c,mot) ==  foo(c,mot)):
            pts +=1 
    except : 
        pass
    
    c,mot = "c","abccde"
    total +=1
    try :
        if (compter_lettres_cor(c,mot) ==  foo(c,mot)):
            pts +=1 
    except : 
        pass
        
    c,mot = "c","cabccdec"
    total +=1
    try :
        if (compter_lettres_cor(c,mot) ==  foo(c,mot)):
            pts +=1 
    except : 
        pass

    c,mot = "c","cabefgh"
    total +=1
    try :
        if (compter_lettres_cor(c,mot) ==  foo(c,mot)):
            pts +=1 
    except : 
        pass
        
    return pts,total

## Question 2 ##
def enlever_lettre_cor(c,mot):
    mot2 = ''
    for lettre in mot :
        if lettre != c :
            mot2 = mot2 + lettre
    return mot2

def test_q02(foo):
    pts = 0
    total = 0
    
    c,mot = "c","abde"
    total +=1
    try :
        if (enlever_lettre_cor(c,mot) ==  foo(c,mot)):
            pts +=1 
    except : 
        pass
    
    c,mot = "c","abccde"
    total +=1
    try :
        if (enlever_lettre_cor(c,mot) ==  foo(c,mot)):
            pts +=1 
    except : 
        pass
        
    c,mot = "c","cabccdec"
    total +=1
    try :
        if (enlever_lettre_cor(c,mot) ==  foo(c,mot)):
            pts +=1 
    except : 
        pass

    c,mot = "c","cabefgh"
    total +=1
    try :
        if (enlever_lettre_cor(c,mot) ==  foo(c,mot)):
            pts +=1 
    except : 
        pass
        
    return pts,total

## Question 3 ##
def inverser_chaine_cor(mot):
    mot2 = ''
    for lettre in mot :
            mot2 = lettre + mot2
    return mot2

def test_q03(foo):
    pts = 0
    total = 0
    
    c,mot = "c","abde"
    total +=1
    try :
        if (inverser_chaine_cor(mot) ==  foo(mot)):
            pts +=1 
    except : 
        pass
    
    c,mot = "c","abccde"
    total +=1
    try :
        if (inverser_chaine_cor(mot) ==  foo(mot)):
            pts +=1 
    except : 
        pass
        
    c,mot = "c","cabccdec"
    total +=1
    try :
        if (inverser_chaine_cor(mot) ==  foo(mot)):
            pts +=1 
    except : 
        pass

    c,mot = "c","cabefgh"
    total +=1
    try :
        if (inverser_chaine_cor(mot) ==  foo(mot)):
            pts +=1 
    except : 
        pass
        
    return pts,total
  
## Question 6 ##
def affiche_voyelle_last_cor(mot):
    indice = -1
    voyelles = 'aeiouy'
    for i in range(len(mot)) :
        lettre = mot[i]
        if lettre in voyelles :
            indice = i 
    return indice

def test_q06(foo):
    pts = 0
    total = 0
    
    c,mot = "c","abde"
    total +=1
    try :
        if (affiche_voyelle_last_cor(mot) ==  foo(mot)):
            pts +=1 
    except : 
        pass
    
    c,mot = "c","abccde"
    total +=1
    try :
        if (affiche_voyelle_last_cor(mot) ==  foo(mot)):
            pts +=1 
    except : 
        pass
        
    c,mot = "c","cabccdec"
    total +=1
    try :
        if (affiche_voyelle_last_cor(mot) ==  foo(mot)):
            pts +=1 
    except : 
        pass

    c,mot = "c","cabefgh"
    total +=1
    try :
        if (affiche_voyelle_last_cor(mot) ==  foo(mot)):
            pts +=1 
    except : 
        pass
        
    return pts,total

## Question 8 ##
def indice_lettre2_cor(c,mot):
    indice = -1
    for i in range(len(mot)) :
        lettre = mot[i]
        if lettre == c :
            indice = i 
    return indice

def test_q08(foo):
    pts = 0
    total = 0
    
    c,mot = "c","abde"
    total +=1
    try :
        if (indice_lettre2_cor(c,mot) ==  foo(c,mot)):
            pts +=1 
    except : 
        pass
    
    c,mot = "c","abccde"
    total +=1
    try :
        if (indice_lettre2_cor(c,mot) ==  foo(c,mot)):
            pts +=1 
    except : 
        pass
        
    c,mot = "c","cabccdec"
    total +=1
    try :
        if (indice_lettre2_cor(c,mot) ==  foo(c,mot)):
            pts +=1 
    except : 
        pass

    c,mot = "c","cabefgh"
    total +=1
    try :
        if (indice_lettre2_cor(c,mot) ==  foo(c,mot)):
            pts +=1 
    except : 
        pass
        
    return pts,total
    


## Question 9 ##
def is_egal(mot1:str, mot2:str):
    return mot1 == mot2

def test_q09(foo):
    pts = 0
    total = 0
    
    mot1,mot2 = 'mot','mot'
    total +=1
    try :
        if (is_egal(mot1,mot2) ==  foo(c,mot)):
            pts +=1 
    except : 
        pass
    
    mot1,mot2 = 'mot','mot2'
    total +=1
    try :
        if (is_egal(mot1,mot2) ==  foo(c,mot)):
            pts +=1 
    except : 
        pass
        
    mot1,mot2 = 'mot1','mot'
    total +=1
    try :
        if (is_egal(mot1,mot2) ==  foo(c,mot)):
            pts +=1 
    except : 
        pass
        
    mot1,mot2 = 'm','m'
    total +=1
    try :
        if (is_egal(mot1,mot2) ==  foo(c,mot)):
            pts +=1 
    except : 
        pass

    
    return pts,total
    
## Question 10 ##
def indice_diff(mot1:str, mot2:str):
    if mot1 == mot2 :
        return -1
    else :
        for i in range(len(mot1)):
            if mot1[i]!=mot2[i] :
                return i            

def test_q10(foo):
    pts = 0
    total = 0
    
    mot1,mot2 = 'mot','mot'
    total +=1
    try :
        if (is_egal(mot1,mot2) ==  foo(c,mot)):
            pts +=1 
    except : 
        pass
    
    mot1,mot2 = 'mot','mos'
    total +=1
    try :
        if (is_egal(mot1,mot2) ==  foo(c,mot)):
            pts +=1 
    except : 
        pass
        
    mot1,mot2 = 'aot','mot'
    total +=1
    try :
        if (is_egal(mot1,mot2) ==  foo(c,mot)):
            pts +=1 
    except : 
        pass
        
    mot1,mot2 = 'mat','mot'
    total +=1
    try :
        if (is_egal(mot1,mot2) ==  foo(c,mot)):
            pts +=1 
    except : 
        pass

    
    return pts,total
    
    
#1,2,3,6,8,9,10
def go(foo1,foo2,foo3,foo6,foo8,foo9,foo10):
    i = 0
    notes = {}
    tot = 4
    
    pts = 0
    i += 1
    try :
        pts,tot = test_q01(foo1)
    except : 
        pass
    print("Question "+str(i)+" : ",str(pts),"/",str(tot))
    notes[i] = (pts,tot)

    
    pts = 0
    i = 2
    try :
        pts,tot = test_q02(foo2)
    except : 
        pass
    print("Question "+str(i)+" : ",str(pts),"/",str(tot))
    notes[i] = (pts,tot)

    
    pts = 0
    i = 3
    try :
        pts,tot = test_q03(foo3)
    except : 
        pass
    print("Question "+str(i)+" : ",str(pts),"/",str(tot))
    notes[i] = (pts,tot)

    
    pts = 0
    i = 6
    try :
        pts,tot = test_q06(foo6)
    except : 
        pass
    print("Question "+str(i)+" : ",str(pts),"/",str(tot))
    notes[i] = (pts,tot)
    
    pts = 0
    i = 8
    try :
        pts,tot = test_q08(foo8)
    except : 
        pass
    print("Question "+str(i)+" : ",str(pts),"/",str(tot))
    notes[i] = (pts,tot)
    
    pts = 0
    i += 1
    try :
        pts,tot = test_q09(foo9)
    except : 
        pass
    print("Question "+str(i)+" : ",str(pts),"/",str(tot))
    notes[i] = (pts,tot)
    
    pts = 0
    i += 1
    try :
        pts,tot = test_q10(foo10)
    except : 
        pass
    print("Question "+str(i)+" : ",str(pts),"/",str(tot))
    notes[i] = (pts,tot)