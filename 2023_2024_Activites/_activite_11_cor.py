import random as rd
import numpy as np
import math as m

import sys
import inspect

def test_q01(foo,verbose):
    pts = 0
    total = 0
    
    liste_L = [[rd.randrange(1,100) for i in range(10)] for j in range(10)]
    liste_k = [rd.randrange(1,10) for i in range(10)]
    
    for i in range(len(liste_L)) :
        total +=1
        try :
            L = liste_L[i]
            k = liste_k[i]
            i_cor = cor_recherche_minimum(L,k)
            i_eleve = foo(L,k)
            
            if i_cor == i_eleve:
                pts +=1 
            else : 
                if verbose :
                    print('n :',n)
                    print('Corrigé :',i_cor)
                    print('Votre fonction :',i_eleve)
                    print()
        except : 
            pass

    return pts,total


def test_q02(foo,verbose):
    pts = 0
    total = 0
    
    liste_L = [[rd.randrange(1,100) for i in range(10)] for j in range(10)]
    liste_i = [rd.randrange(1,10) for i in range(10)]
    liste_j = [rd.randrange(1,10) for i in range(10)]
    
    for i in range(len(liste_L)) :
        total +=1

        try :
            L_eleve = liste_L[i][:]
            L_cor = liste_L[i][:]
            ii = liste_i[i]
            jj = liste_j[i]
            
            cor_inversion(L_cor,ii,jj)
            foo(L_eleve,ii,jj)
            
            
            if L_eleve == L_cor :
                pts +=1 
            else : 
                if verbose :
                    print('n :',n)
                    print('Corrigé :',L_cor)
                    print('Votre fonction :',L_eleve)
                    print()
        except : 
            pass

    return pts,total
    
    
def test_q03(foo,verbose):
    pts = 0
    total = 0
    
    liste_L = [[rd.randrange(1,100) for i in range(10)] for j in range(10)]
    
    for i in range(len(liste_L)) :
        total +=1

        try :
            L_eleve = liste_L[i][:]
            L_cor = liste_L[i][:]
        
            cor_tri_selection(L_cor)
            foo(L_eleve)
            
            if L_eleve == L_cor :
                pts +=1 
            else : 
                if verbose :
                    print('n :',n)
                    print('Corrigé :',L_cor)
                    print('Votre fonction :',L_eleve)
                    print()
        except : 
            pass

    return pts,total  
    


def test_q04(foo,verbose):
    pts = 0
    total = 0
    
    liste_L = [[rd.randrange(1,100) for i in range(10)] for j in range(10)]
    liste_k = [rd.randrange(1,100) for i in range(10)]
    
    for i in range(len(liste_L)) :
        total +=1

        try :
            L = liste_L[i]
            k = liste_k[i]
            L_cor = cor_elts_inf(L,k)
            L_eleve = foo(L,k)
            if L_cor == L_eleve:
                pts +=1 
            else : 
                if verbose :
                    print('n :',n)
                    print('Corrigé :',L_cor)
                    print('Votre fonction :',L_eleve)
                    print()
        except : 
            pass

    return pts,total

def test_q05(foo,verbose):
    pts = 0
    total = 0
    
    liste_L = [[rd.randrange(1,100) for i in range(10)] for j in range(10)]
    liste_k = [rd.randrange(1,100) for i in range(10)]
    
    for i in range(len(liste_L)) :
        total +=1

        try :
            L = liste_L[i]
            k = liste_k[i]
            L_cor = cor_elts_sup(L,k)
            L_eleve = foo(L,k)
            if L_cor == L_eleve:
                pts +=1 
            else : 
                if verbose :
                    print('n :',n)
                    print('Corrigé :',L_cor)
                    print('Votre fonction :',L_eleve)
                    print()
        except : 
            pass

    return pts,total
    

def test_q06(foo,verbose):
    pts = 0
    total = 0
    
    liste_L = [[rd.randrange(1,50) for i in range(50)] for j in range(10)]
    
    for i in range(len(liste_L)) :
        total +=1

        try :
            L_eleve = liste_L[i][:]
            L_cor = liste_L[i][:]
        
            cor_tri_rapide(L_cor)
            foo(L_eleve)
            
            if L_eleve == L_cor :
                pts +=1 
            else : 
                if verbose :
                    print('n :',n)
                    print('Corrigé :',L_cor)
                    print('Votre fonction :',L_eleve)
                    print()
        except : 
            pass

    return pts,total

    

def go(foo1,foo2,foo3,foo4,foo5,foo6,verbose = False):
    i = 0
    notes = {}
    tot = 2
    
    tests = [[test_q01,foo1],[test_q02,foo2],[test_q03,foo3],[test_q04,foo4],[test_q05,foo5],[test_q06,foo6]]
    
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