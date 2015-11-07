#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Exercice 1 : Construction d'une pile
# =====================================

def creer_pile(n):
    assert n>2
    pile = (None,None)
    for i in range(2,n):
        pile=pile+(None,)
    return pile
    
def est_vide(pile):
    for el in pile :
        if el != None :
            return False
    return True

def est_pleine(pile):
    return not None in pile 

def depiler(pile,n):
    i=n
    while pile[i]!=None:
        i=i-1


def empiler(pile,el,n):
    if est_pleine(pile):
        # Si la pile est pleine on en fait rien
        return None
    else :
        
        return pile+(el,)

n=4
pile = creer_pile(n)
print(pile)
print(est_pleine(pile))
empiler(pile,1,n)
print(pile)
empiler(pile,2,n)
print(pile)
empiler(pile,3,n)
print(pile)
empiler(pile,4,n)
print(pile)
empiler(pile,5,n)
print(pile)
empiler(pile,6,n)