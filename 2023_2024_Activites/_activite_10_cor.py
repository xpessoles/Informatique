import random as rd
import numpy as np
import math as m

import sys
import inspect

        

def cor_fact(n) : 
    if n == 0 :
        return 1
    else : 
        return n*cor_fact(n-1)


def cor_f(n:int) -> int : 
    if n<2 :
        return 1
    else : 
        return 3*cor_f(n-1)+cor_f(n-2)

def cor_longueur(chaine:str) -> int :
    if len(chaine) == 0 :
        return 0
    else : 
        return 1 + cor_longueur(chaine[1:])
        
def cor_est_triee(L) :
    if len(L) <= 1 :
        return True
    if L[0] <= L[1] :
        return cor_est_triee(L[1:])
    else :
        return False
                
    
def test_q01(foo,verbose):
    pts = 0
    total = 0
    
    liste_n = [rd.randrange(1,100) for i in range(10)]
    
    
    ## Test sur la valeur renvoyée par la fonction
    for n in liste_n :
        total +=1

        try :
            n_cor = cor_fact(n)
            n_eleve = foo(n)
            if n_cor == n_eleve:
                pts +=1 
            else : 
                if verbose :
                    print('n :',n)
                    print('Corrigé :',n_cor)
                    print('Votre fonction :',n_eleve)
                    print()
        except : 
            pass
    
    ## Test sur la vérif d'une fonction récursive
    # code = inspect.getsource(foo)
    # if ("while" in code) or ("for" in code) :
    #     print("Fonction possiblement non récursive")
    #     rec  = False
    # else : 
    #     rec = True
    # if not rec :
    #     pts = 0
    # 
    
    # 
    # rec = False
    # with recursion_depth(30):
    #     try : 
    #         fact(40)
    #         
    #     except RecursionError :
    #         rec = True
    #         print('Fonction récursive')
            
    
       
    
    return pts,total
    
def test_q02(foo,verbose):
    pts = 0
    total = 0
    
    liste_n = [rd.randrange(1,20) for i in range(10)]
    
    
    ## Test sur la valeur renvoyée par la fonction
    for n in liste_n :
        total +=1
        try :
            n_cor = cor_f(n)
            n_eleve = foo(n)
            if n_cor == n_eleve:
                pts +=1 
            else : 
                if verbose :
                    print('n :',n)
                    print('Corrigé :',n_cor)
                    print('Votre fonction :',n_eleve)
                    print()
        except : 
            pass
    
    ## Test sur la vérif d'une fonction récursive
    # code = inspect.getsource(foo)
    # if ("while" in code) or ("for" in code) :
    #     print("Fonction possiblement non récursive")
    #     rec  = False
    # else : 
    #     rec = True
    # if not rec :
    #     pts = 0
        
    
    return pts,total


def test_q03(foo,verbose):
    pts = 0
    total = 0
    
    ## Génération de mots aléatoires
    liste_mot =[]
    for i in range(10) :
        mot = "".join([chr(rd.randrange(33,125)) for i in range(rd.randrange(100))])
        liste_mot.append(mot)
    
    
    for mot in liste_mot :
        total +=1

        try :
            n_cor = cor_longueur(mot)
            n_eleve = foo(mot)
            if n_cor == n_eleve:
                pts +=1
            else : 
                if verbose :
                    print('mot :',mot)
                    print('Corrigé :',n_cor)
                    print('Votre fonction :',n_eleve)
                    print()
        except : 
            pass
    ## Test sur la vérif d'une fonction récursive
    # code = inspect.getsource(foo)
    # if ("while" in code) or ("for" in code) :
    #     print("Fonction possiblement non récursive")
    #     rec  = False
    # else : 
    #     rec = True
    # if not rec :
    #     pts = 0
    #     

    return pts,total

def test_q04(foo,verbose):

    pts = 0
    total = 0
    
    ## Génération de listes aléatoires
    liste =[]

    for i in range(2) :
        l = [rd.randint(0,20) for i in range(rd.randint(0,20))]
        l.sort()
        liste.append(l)
    for i in range(2) :
        l = [rd.randint(0,20) for i in range(rd.randint(0,20))]
        l.sort()
        l.reverse()
        liste.append(l)
    
    for i in range(6) :
        l = [rd.randint(0,20) for i in range(rd.randint(0,20))]
        liste.append(l)

    for l in liste :
        total +=1
        try :
           
            n_cor = cor_est_triee(l)
            n_eleve = foo(l)
            if n_cor == n_eleve:
                pts +=1
            else : 
                if verbose :
                    print('Liste :',l)
                    print('Corrigé :',n_cor)
                    print('Votre fonction :',n_eleve)
                    print()
        except : 
            pass
    ## Test sur la vérif d'une fonction récursive
    # code = inspect.getsource(foo)
    # if ("while" in code) or ("for" in code) :
    #     print("Fonction possiblement non récursive")
    #     rec  = False
    # else : 
    #     rec = True
    # if not rec :
    #     pts = 0
    # 

    return pts,total
    

def go(foo1,foo2,foo3,foo4,verbose = False):
    i = 0
    notes = {}
    tot = 2
    
    tests = [[test_q01,foo1],[test_q02,foo2],[test_q03,foo3],[test_q04,foo4]]
    
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



class recursion_depth:
    def __init__(self, limit):
        self.limit = limit
        self.default_limit = sys.getrecursionlimit()
    def __enter__(self):
        sys.setrecursionlimit(self.limit)
    def __exit__(self, type, value, traceback):
        sys.setrecursionlimit(self.default_limit)
 

        
#go(fact,cor_f,cor_longueur,cor_est_triee,True)