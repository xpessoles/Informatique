# -*- coding: utf-8 -*-
"""
Created on Mon Jun 27 21:04:00 2022

@author: xpess
"""

## Somme
def somme_corrige(a:int,b:int)-> int :
    return a+b
    

def somme_test(foo,a,b):
    if foo(a,b) == somme_corrige(a,b):
        print(f"Test somme({a,b}) : réussi")
    else :
        print(f"Test somme({a,b}) : échoué")

## Racine
def racine_corrige(a:float)->float:
    return a**(.5)

def racine_test(foo,a:float):
    if foo(a) == racine_corrige(a) :
        print(f"Test racine({a}) : réussi")
    else :
        print(f"Test racine({a}) : échoué")
        
## Inverse racine
def inv_racine_corrige(a:float) :
    if a<0 :
        return None
    else : 
        return a**(-.5)
    
def inv_racine_test(foo,a:float):
    if foo(a) == inv_racine_corrige(a) :
        print(f"Test inv_racine({a}) : réussi")
    else :
        print(f"Test inv_racine({a}) : échoué")
    

## Est pair
def est_pair_corrige(a:int) -> bool : 
    return a%2 == True

def est_pair_test(foo,a):
    if foo(a) == est_pair_corrige(a) :
        print(f"Test est_pair({a}) : réussi")
    else :
        print(f"Test est_pair({a}) : échoué")

## Puissance de 2 for
def puissance_2_for_corrige(n:int)->int :
    res = 1
    for i in range(n):
        res = res*2
    return res

def puissance_2_for_test(foo,n):
    if foo(n) == 2**n :
        print(f"Test puissance_2_for({n}) : réussi")
    else :
        print(f"Test puissance_2_for({n}) : échoué")

## Puissance de 2 while
def puissance_2_while_corrige(n:int)->int :
    res = 1
    while n>0:
        res = res*2
        n = n-1
    return res

def puissance_2_while_test(foo,n):
    if foo(n) == 2**n :
        print(f"Test puissance_2_while({n}) : réussi")
    else :
        print(f"Test puissance_2_while({n}) : échoué")

## Puissance de a for
def puissance_for_corrige(a:float,n:int)->int :
    res = 1
    for i in range(n):
        res = res*a
    return res

def puissance_for_test(foo,a,n):
    if foo(a,n) == a**n :
        print(f"Test puissance_for({a,n}) : réussi")
    else :
        print(f"Test puissance_for({a,n} : échoué") 


## Puissance de a while
def puissance_while_corrige(a:float,n:int)->int :
    res = 1
    while n>0:
        res = res*a
        n = n-1
    return res


def puissance_while_test(foo,a,n):
    if foo(a,n) == a**n :
        print(f"Test puissance_while({a,n}) : réussi")
    else :
        print(f"Test puissance_while({a,n}) : échoué")

## Puissance de a 
def puissance_corrige(a,n):
    return a**n

def puissance_test(foo,a,n):
    if foo(a,n) == a**n :
        print(f"Test puissance_while({a,n}) : réussi")
    else :
        print(f"Test puissance_while({a,n}) : échoué")