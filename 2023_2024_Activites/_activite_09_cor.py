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

    
def test_q01(foo):
    pts = 0
    total = 0
    
    liste_achat = [i/100 for i in range(1000)]
    liste_somme = [i/100 for i in range(1001,2001)]
    
    for achat in liste_achat :
        for somme in liste_somme :
            total +=1

            try :
                L_cor = cor_rendu_monnaie(achat,somme)
                L_eleve = foo(achat,somme)
                if (np.allclose(L_cor,L_eleve)):
                    pts +=1 
            except : 
                pass
    
    return pts,total


def test_q02(foo):
    pts = 0
    total = 0
    
    liste_achat = [i/100 for i in range(1000)]
    liste_somme = [i/100 for i in range(1001,2001)]
    
    for achat in liste_achat :
        for somme in liste_somme :
            total +=1

            try :
                L_cor = cor_rendu_monnaie_2(achat,somme)
                L_eleve = foo(achat,somme)
                if (np.allclose(L_cor,L_eleve)):
                    pts +=1 
            except : 
                pass
    
    return pts,total



def go(foo1,foo2):
    i = 0
    notes = {}
    tot = 2
    
    tests = [[test_q01,foo1],[test_q02,foo2],[test_q03,foo3],[test_q04,foo4],[test_q05,foo5],[test_q06,foo6],[test_q07,foo7],[test_q08,foo8]]
    
    for t in tests : 
        tq,f = t
        pts = 0
        i +=1
        try :
            pts,tot = tq(f)
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