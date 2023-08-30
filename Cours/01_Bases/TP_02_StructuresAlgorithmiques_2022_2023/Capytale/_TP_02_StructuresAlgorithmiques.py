# -*- coding: utf-8 -*-
"""
@author: xpess
"""

## Valeur absolue
def val_absolue_corrige(x:float)-> float:
    if x>=0 : 
        return x
    else :
        return -x
        
def val_absolue_test(foo,x):
    if foo(x) == val_absolue_corrige(x):
        print(f"Test val_absolue({x}) : réussi")
    else :
        print(f"Test val_absolue({x}) : échoué")


## Coût voyage
def cout_voyage_corrige(n):
    if n<=2 :
        prix = 80
    elif n<=5 :
        prix = 70
    elif n<=9 : 
        prix = 60
    else : 
        prix = 50
    return n*prix

def cout_voyage_test(foo,x):
    assert x>0
    assert type(x)==type(0)
    if foo(x) == cout_voyage_corrige(x):
        print(f"Test cout_voyage({x}) : réussi")
    else :
        print(f"Test cout_voyage({x}) : échoué")


## Compter
def compter_for_corrige(n:int)->None:
    for i in range(n):
        print(i)

def compter_while_corrige(n:int)->None:
    i = 0
    while i<n :
        print(i)
        i=i+1

## Compter à rebours
def compter_rebours_for_corrige(n:int)->None:
    for i in range(n,-1,-1):
        print(i)

def compter_rebours_while_corrige(n:int)->None:
    while n>=0:
        print(n)
        n=n-1

## Epeler
def epeler_corrige_01(mot:str) -> None :
    for lettre in mot: 
        print(lettre)

def epeler_corrige_02(mot:str) -> None :
    for i in range(len(mot) ):
        print(mot[i])
    
# Factorielle
def factorielle_corrige(n:int)->int : 
    if n==0 : 
        return 1
    else : 
        res = 1
        for i in range(1,n+1):
            res = res*i
        return res
    
def factorielle_test(foo,n):
    if foo(n) == factorielle_corrige(n):
        print(f"Test factorielle({n}) : réussi")
    else :
        print(f"Test factorielle({n}) : échoué")       

## Plus petit entier
def plus_petit_entier_corrige(N):
    i = 0
    res = 0
    while res <N : 
        res = res+i
        i = i+1
    return i

def plus_petit_entier_test(foo,x):
    if foo(x) == plus_petit_entier_corrige(x):
        print(f"Test plus_petit_entier({x}) : réussi")
    else :
        print(f"Test plus_petit_entier({x}) : échoué")

### Syracuse
## Q1
def tempsdevol_corrige(c:int):
    u=c
    n=0
    while u!=1:
        if u%2==0:
            u=u//2
        else:
            u=3*u+1
        n=n+1
    return(n)


def tempsdevol_test(foo,n):
    if foo(n) == tempsdevol_corrige(n):
        print(f"Test tempsdevol({n}) : réussi")
    else :
        print(f"Test tempsdevol({n}) : échoué")
        
## Q2
def altitude_corrige(c:int):
    u=c
    M=c
    n=0
    while u!=1:
        if u%2==0:
            u=u//2
        else:
            u=3*u+1
        n=n+1
        if u>M:
            M=u
    return(M)

def altitude_test(foo,n):
    if foo(n) == altitude_corrige(n):
        print(f"Test altitude({n}) : réussi")
    else :
        print(f"Test altitude({n}) : échoué")
        
## Q3
def tempsdarret_corrige(c:int):
    if c==1:
        n=0
    else:
        u=c
        n=0
        while u>=c:
            if u%2==0:
                u=u//2
            else:
                u=3*u+1
            n=n+1
    return(n)

def tempsdarret_test(foo,n):
    if foo(n) == tempsdarret_corrige(n):
        print(f"Test tempsdarret({n}) : réussi")
    else :
        print(f"Test tempsdarret({n}) : échoué")

## Q4
import time as t

def verification_corrige(m:int):
    tps=t.time()
    for c in range(2,m+1):
        tempsdarret_corrige(c)
    return(t.time()-tps)
    

## Q5

# Si c est pair, le temps d'arrêt vaut 1
# Si c=4n+1, u1=12n+4, u2=6n+2, u3=3n+1: le temps d'arret est donc 3
# Il ne reste que les nombres impairs congrus à 3 modulo 4 ie de la forme 3n+4



def verification2_corrige(m:int):
    tps=t.time()
    k=0
    while 4*k+3<=m:
        tempsdarret_corrige(4*k+3)
        k=k+1
    return(t.time()-tps)

## Q6
def max_altitude_corrige(a,b):
    #a,b = 1,1000001
    M=0
    for c in range(a,b):
        alt=altitude_corrige(c)
        if alt>M:
            M=alt
            cmin=c
    return(M,cmin)

def max_altitude_test(foo,a,b):
    if foo(a,b) == max_altitude_corrige(a,b):
        print(f"Test max_altitude({a,b}) : réussi")
    else :
        print(f"Test max_altitude({a,b}) : échoué")

## Q7
def max_tempsdarret_corrige():   # On se limite à c=4n+3
    M=0
    n=0
    while 4*n+3<=1000000:
        t=tempsdarret_corrige(4*n+3)
        if t>M:
            M=t
            cmin=4*n+3
        n=n+1
    return(M,cmin)

def max_tempsdarret_test(foo,a,b):
    if foo(a,b) == max_tempsdarret_corrige(a,b):
        print(f"Test max_tempsdarret({a,b}) : réussi")
    else :
        print(f"Test max_tempsdarret({a,b}) : échoué")
## Q8
def record_corrige(a,b):
    liste=[]
    for c in range(a,b):
        t=tempsdarret_corrige(c)
        i=1
        while i<=c-1 and tempsdarret_corrige(i)<=t:
            i=i+1
        if i==c:
            liste.append(c)
    return(liste)

def record_test(foo,a,b):
    if foo(a,b) == record_corrige(a,b):
        print(f"Test record({a,b}) : réussi")
    else :
        print(f"Test record({a,b}) : échoué")
        
## Q9 Affichage de vol
import matplotlib.pyplot as plt

def graphique(c:int):
    t=tempsdarret_corrige(c)
    les_x=[i for i in range(t)]
    les_y=[c]
    u=c
    for i in range(1,t):
        if u%2==0:
            u=u//2
        else:
            u=3*u+1
            
        les_y.append(u)
    plt.plot(les_x,les_y)
    plt.xlabel("n")
    plt.ylabel("u(n)")
    plt.show()
    