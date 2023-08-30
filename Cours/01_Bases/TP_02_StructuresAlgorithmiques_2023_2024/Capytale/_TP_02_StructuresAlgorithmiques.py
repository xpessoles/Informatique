# -*- coding: utf-8 -*-
"""
@author: xpess
"""

## Valeur absolue - Question 1
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


## Coût voyage - Question 2
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



## Q3 
def is_exists_corrige(a:int, b:int, c:int) -> bool :
    # Pour vérifier l'existence du triangle on utilise l'inégalité triangulaire : 
    if (a <= b+c) and (b <= a+c) and (c <= b+a) :
        return True
    return False

def is_exists_test(foo,a,b,c):
    assert a > 0     
    assert b > 0
    assert c > 0
    if foo(a,b,c) == is_exists_corrige(a,b,c):
        print(f"Test is_exists({a,b,c}) : réussi")
    else :
        print(f"Test is_exists({a,b,c}) : échoué")

## Q4
def is_equilateral_corrige(a:int, b:int, c:int) -> bool :
    if a == b and a == c :
        return True
    return False
    
    # Plus simplement, on pourraut écrire 
    # return (a==b) and (a==c)

def is_equilateral_test(foo,a,b,c):
    assert a > 0     
    assert b > 0
    assert c > 0
    if foo(a,b,c) == is_equilateral_corrige(a,b,c):
        print(f"Test réussi")
    else :
        print(f"Test échoué")


## Q5
def is_isocele_corrige(a:int, b:int, c:int) -> bool :
    if a == b or a == c or b == c:
        return True
    return False
    
def is_isocele_test(foo,a,b,c):
    assert a > 0     
    assert b > 0
    assert c > 0
    if foo(a,b,c) == is_isocele_corrige(a,b,c):
        print(f"Test réussi")
    else :
        print(f"Test échoué")

## Q6
def is_rectangle_corrige(a:int, b:int, c:int) -> bool :
    if a*a == (b**b + c**c) :
        return True
    if b*b == (a**a + c**c) :
        return True
    if c*c == (b**b + a**a) :
        return True
    
    return False
    
def is_rectangle_test(foo,a,b,c):
    assert a > 0     
    assert b > 0
    assert c > 0
    if foo(a,b,c) == is_rectangle_corrige(a,b,c):
        print(f"Test réussi")
    else :
        print(f"Test échoué")

