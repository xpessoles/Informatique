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
        
def compter_rebours_for_corrige(n:int)->None:
    for i in range(n,-1,-1):
        print(i)

def compter_rebours_while_corrige(n:int)->None:
    while n>=0:
        print(n)
        n=n-1


def epeler_corrige_01(mot:str) -> None :
    for lettre in mot: 
        print(lettre)
    

        