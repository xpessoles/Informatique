import random as rd
import numpy as np
import math as m

import sys
import inspect
import copy


fid = open('pg13951.txt', mode='r', encoding='utf-8-sig')
livre_cor = fid.readlines()
fid.close()

def cor_creer_dico(ligne:str) -> {str:int} :
    dico = {}
    for lettre in ligne : 
        if lettre in dico : 
            dico[lettre] += 1
        else :
            dico[lettre] = 1
    return dico

def cor_fusion_dico(d1,d2) -> {str:int} :
    dico = {}
    # On ajoute d1 dans dico :
    for c,v in d1.items():
        dico[c]=v
    # On ajoute d2 dans dico :
    for c,v in d2.items():
        if c in dico : 
            dico[c] += v
        else :
            dico[c]=v
    return dico     

def cor_creer_dico_livre(livre: [str]) -> {str:int} :
    dico =  {}
    for ligne in livre : 
        d1 = cor_creer_dico(ligne)
        dico = cor_fusion_dico(dico,d1)
    return dico

def cor_copie_dico(d:{}) -> {} :
    dcop = {}
    for cle,valeur in d.items() :
        dcop[cle]=valeur
    return dcop

def cor_max_dico(d: {str:int},n) -> [[str,int]] :
    res = []
    dcop = cor_copie_dico(d)
    while len(res)<n :
        # on cherche la clef avec la plus grande valeurs
        cmaxi = ""
        vmaxi = float('-inf')
        for cle,valeur in dcop.items() :
            if valeur > vmaxi : 
                vmaxi = valeur
                cmaxi = cle
        # On supprime la cle maxi
        del(dcop[cmaxi])
        res.append((cmaxi,vmaxi))
    return res

from collections import deque

def cor_verif(livre:[str],po:str,pf:str) -> bool :
    pile = deque()
    for ligne in livre : 
        for c in ligne : 
            if c == po : 
                pile.append(c)
            elif c == pf :
                if len(pile) > 0 :
                    pile.pop()
                else :
                    return False
    return len(pile) == 0

def cor_stack(livre:[str],po:str,pf:str) -> bool :
    pile = deque()
    for i in range(len(livre)) : 
        for c in livre[i] : 
            if c == po : 
                pile.append((c,i))
            elif c == pf :
                if len(pile) > 0 :
                    pile.pop()
                else :
                    return pile
    return pile
    

def test_q01(foo,verbose):
    pts = 0
    total = 0
    # Copie du livre
    lcor = copy.deepcopy(livre_cor)
    lel = copy.deepcopy(livre_cor)
    
    for ligne in lcor :

        total +=1
        try :
            
            d_cor = cor_creer_dico(ligne)
            d_eleve = foo(ligne)
            
            if d_cor == d_eleve:
                pts +=1 
            else : 
                if verbose :
                    print('n :',n)
                    print('Corrigé :',d_cor)
                    print('Votre fonction :',d_eleve)
                    print()
        except : 
            pass

    return pts,total


def test_q02(foo,verbose):
    pts = 0
    total = 0
    
    # Copie du livre
    lcor = copy.deepcopy(livre_cor)
    lel = copy.deepcopy(livre_cor)
    
    for i in range(len(lcor)-1) :
        total +=1

        try :
            d1 = cor_creer_dico(lel[i])
            d2 = cor_creer_dico(lel[i+1])
            
            d_cor = cor_fusion_dico(d1,d2)
            d_el = foo(d1,d2)
            
            
            if d_cor == d_el :
                pts +=1 
            else : 
                if verbose :
                    print('n :',n)
                    print('Corrigé :',d_cor)
                    print('Votre fonction :',d_el)
                    print()
        except : 
            pass

    return pts,total
    
    
def test_q03(foo,verbose):
    pts = 0
    total = 0
    lcor = copy.deepcopy(livre_cor)
    lel = copy.deepcopy(livre_cor)
    
    
    for i in range(1) :
        total +=1

        try :
            d_cor = cor_creer_dico_livre(lcor)
            d_el = cor_creer_dico_livre(lel)

            
            if d_cor == d_el :
                pts +=1 
            else : 
                if verbose :
                    print('n :',n)
                    print('Corrigé :',d_cor)
                    print('Votre fonction :',d_el)
                    print()
        except : 
            pass

    return pts,total  
    


def test_q04(foo,verbose):
    pts = 0
    total = 0
    
    # Copie du livre
    lcor = copy.deepcopy(livre_cor)
    lel = copy.deepcopy(livre_cor)
    
    for i in range(len(lcor)-1) :
        total +=1

        try :
            d1 = cor_creer_dico(lel[i])
            
            d_cor = cor_copie_dico(d1)
            d_el = foo(d1)
            
            
            if d_cor == d_el:
                pts +=1 
            else : 
                if verbose :
                    print('n :',n)
                    print('Corrigé :',d_cor)
                    print('Votre fonction :',d_el)
                    print()
        except : 
            pass

    return pts,total

def test_q05(foo,verbose):
    pts = 0
    total = 0
    
    # Copie du livre
    lcor = copy.deepcopy(livre_cor)
    lel = copy.deepcopy(livre_cor)
    
    for i in range(len(lcor)-1) :
        total +=1

        try :
            d1 = cor_creer_dico(lel[i])
            
            d_cor = cor_max_dico(d1,min([len(d1),3]))
            d_el = foo(d1,min([len(d1),3]))
            
            
            if d_cor == d_el:
                pts +=1 
            else : 
                if verbose :
                    print('n :',n)
                    print('Corrigé :',d_cor)
                    print('Votre fonction :',d_el)
                    print()
        except : 
            pass

    return pts,total
    

def test_q06(foo,verbose):
    pts = 0
    total = 0
    
    po,pf = "(",")"
    # Copie du livre
    lcor = copy.deepcopy(livre_cor)
    lel = copy.deepcopy(livre_cor)

    total = 1
    try :
        res_cor = cor_verif(lcor,po,pf)
        res_el = foo(lel,po,pf)
        
        if res_cor == res_el :
            pts +=1 
        else : 
            if verbose :
                print('n :',n)
                print('Corrigé :',res_cor)
                print('Votre fonction :',res_el)
                print()
    except : 
        pass

    return pts,total
    
def test_q07(foo,verbose):
    pts = 0
    total = 0
    
    po,pf = "(",")"
    # Copie du livre
    lcor = copy.deepcopy(livre_cor)
    lel = copy.deepcopy(livre_cor)

    total = 1
    try :
        res_cor = cor_stack(lcor,po,pf)
        res_el = foo(lel,po,pf)
        
        if res_cor == res_el :
            pts +=1 
        else : 
            if verbose :
                print('n :',n)
                print('Corrigé :',res_cor)
                print('Votre fonction :',res_el)
                print()
    except : 
        pass

    return pts,total

    

def go(foo1,foo2,foo3,foo4,foo5,foo6,foo7,verbose = False):
    i = 0
    notes = {}
    tot = 2
    
    tests = [[test_q01,foo1],[test_q02,foo2],[test_q03,foo3],[test_q04,foo4],[test_q05,foo5],[test_q06,foo6],[test_q07,foo7]]
    
    for t in tests : 
        tq,f = t
        pts = 0
        i +=1
        try :
            pts,tot = tq(f,verbose)
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
    print(points*20/total,20)


        
#go(fact,cor_f,cor_longueur,cor_est_triee,True)