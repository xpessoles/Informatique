import matplotlib.pyplot as plt
import random as rd
import numpy as np
import math as m

def cor_rendu_monnaie(achat:float,somme:float):
    listRendu=[] # on pourrait initialiser la liste avec des 0 et une longueur identique à celle de S
    y=(somme-achat)
    S = [20, 10, 5, 2, 1, 0.5, 0.2, 0.1, 0.05, 0.02, 0.01]
    n=len(S)
    for i in range(0,n):
        x=S[i]
        if (y-x)>=0:
            c=y//x
            listRendu.append(c)
            y=y%x
        else:
            listRendu.append(0)
    return listRendu


def cor_rendu_monnaie_2(achat:float,somme:float)->list :
    listRendu=[]
    a=int(somme*100)
    b=int(round(achat*100))
    y=a-b
    S = [20, 10, 5, 2, 1, 0.5, 0.2, 0.1, 0.05, 0.02, 0.01]
    n=len(S)
    for i in range(n):
        x=int(S[i]*100)
        if y>=0:
            c=y//x
            listRendu.append(c)
            y=y%x
        else:
            listRendu.append(0)
    return (listRendu)

    
def test_q01(foo,verbose):
    pts = 0
    total = 0
    
    liste_achat = [rd.randrange(1,1000)/100 for i in range(10)]
    liste_somme = [rd.randrange(1001,2000)/100 for i in range(10)]
    
    for achat in liste_achat :
        for somme in liste_somme :
            total +=1

            try :
                L_cor = cor_rendu_monnaie(achat,somme)
                L_eleve = foo(achat,somme)
                if (np.allclose(L_cor,L_eleve)):
                    pts +=1 
                else : 
                    if verbose :
                        print('Achat :',achat)
                        print('Somme :',somme)
                        print('Corrigé :',L_cor)
                        print('Votre fonction :',L_eleve)
                        print()
            except : 
                pass
    
    return pts,total


def test_q02(foo,verbose):
    pts = 0
    total = 0
    
    #liste_achat = [i/100 for i in range(1000)]
    #liste_somme = [i/100 for i in range(1001,2001)]
    liste_achat = [rd.randrange(1,1000)/100 for i in range(10)]
    liste_somme = [rd.randrange(1001,2000)/100 for i in range(10)]
    
    for achat in liste_achat :
        for somme in liste_somme :
            total +=1

            try :
                L_cor = cor_rendu_monnaie_2(achat,somme)
                L_eleve = foo(achat,somme)
                if (np.allclose(L_cor,L_eleve)):
                    pts +=1
                else : 
                    if verbose :
                        print('Achat :',achat)
                        print('Somme :',somme)
                        print('Corrigé :',L_cor)
                        print('Votre fonction :',L_eleve)
                        print()
            except : 
                pass
    
    return pts,total



def go(foo1,foo2):
    verbose = False
    i = 0
    notes = {}
    tot = 2
    
    tests = [[test_q01,foo1],[test_q02,foo2]]
    
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

def gov(foo1,foo2):
    verbose = True
    i = 0
    notes = {}
    tot = 2
    
    tests = [[test_q01,foo1],[test_q02,foo2]]
    
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
    