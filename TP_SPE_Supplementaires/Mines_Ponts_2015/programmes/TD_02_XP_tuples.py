#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Exercice 1 : Construction d'une pile de longueur finie
# ======================================================
def creer_pile(n):
    assert n>=2
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
    return (not None in pile) 

def depiler(pile):
    # On recherche l'indice du premier élément None de la pile
    if est_pleine(pile):
        i = len(pile)
    else :
        i=0
        while pile[i] != None:
            i=i+1
    el = pile[i-1]
    pile2 = creer_pile(len(pile))
    for j in range(i-1):
        pile2 = empiler(pile2,pile[j])
    pile = creer_pile(len(pile))
    for i in range(len(pile)):
        pile = empiler(pile,pile2[i])
    return pile,el

def empiler(pile,el):
    n=len(pile)
    taille = len(pile)
    if est_pleine(pile):
        # Si la pile est pleine on ne fait rien
        return pile
    else :
        if est_vide(pile):
            pile = (el,None)+creer_pile(n-2)
        elif pile[1] == None :
            pile = (pile[0],el)+creer_pile(n-2)
        else :
            #On recherche l'indice du premier élément None de la pile
            i=0
            while pile[i] != None:
                i=i+1
            if i == n:
                print(pile)
                return pile
            pile=pile[0:i]+(el,)
            if n-i == 2:
                pile = pile+(None,)
            elif n-i>1:
                pile=pile+creer_pile(n-i)
    return pile    
    
n=4
pile = creer_pile(n)
pile = empiler(pile,1)
pile = empiler(pile,2)
pile = empiler(pile,3)
pile = empiler(pile,4)
pile = empiler(pile,5)
pile = empiler(pile,6)
pile = empiler(pile,7)
pile,el=depiler(pile)
#print(pile)
