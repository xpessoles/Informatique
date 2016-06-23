#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Exercice 1 : Construction d'une pile de longueur finie
# ======================================================
def creer_pile(n):
    return n*[None]
    
def est_vide(pile):
    for el in pile :
        if el != None :
            return False
    return True

def est_pleine(pile):
    return (not None in pile) 

def empiler(pile,el):
    if est_pleine(pile):
        return None
    # On recherche le premier emplacement vide
    i=0
    while pile[i]!= None:
        i=i+1
    pile[i]=el

def depiler(pile):
    if est_vide(pile):
        return None
    # On recherche le premier emplacement vide
    if est_pleine(pile):
        l = len(pile)
        el = pile[l-1]
        pile[l-1]=None
        return el
    i=0
    while pile[i]!= None:
        i=i+1
    el = pile[i-1]
    pile[i-1]=None
    return el    
    
def taille_pile(pile):
    return len(pile)
# Exercice 2 : NPI
# ================
def est_nombre(el):
    return type(el)==float or type(el)==int

def est_operation(el):
    return el in ["+","-","*","/"]
    
def inverse(pile):
    pile2=creer_pile(taille_pile(pile))
    pile3=creer_pile(taille_pile(pile))
    while not (est_vide(pile)):
        empiler(pile2,depiler(pile))
    while not (est_vide(pile2)):
        empiler(pile3,depiler(pile2))
    while not (est_vide(pile3)):
        empiler(pile,depiler(pile3))

def operer(nb1,nb2,op):
    if op == "+":
        return nb1+nb2
    elif op == "*":
        return nb1*nb2
        
def evaluer(pile):
    inverse(pile)
    pile2=creer_pile(taille_pile(pile))
    while not est_vide(pile):
        el = depiler(pile)
        if est_nombre(el):
            empiler(pile2,el)
        elif est_operation(el) :
            empiler(pile2,operer(depiler(pile2),depiler(pile2),el))
    return depiler(pile2)
            
    
    
pile1=[1,2,"+",4,"*",3,"+"]
pile2=[1,2,"+",4,"*",-3,"+",5,"+"]
print(evaluer(pile2))