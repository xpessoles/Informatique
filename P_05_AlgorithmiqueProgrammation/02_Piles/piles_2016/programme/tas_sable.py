#!/usr/bin/env python
# -*- coding: utf-8 -*-
import time
from random import randint

def creer_pile():
    return []
    
def empiler2(pile):
    pile.append(el)

def empiler(pile):
    pile.append("*")
    
def depiler(pile):
    return pile.pop()

def est_vide(pile):
    return len(pile)==0
    
def taille(pile):
    i=0
    pile_tmp=creer_pile()
    while not est_vide(pile):
        i=i+1
        empiler(pile_tmp)
        depiler(pile)
    while not est_vide(pile_tmp):
        depiler(pile_tmp)
        empiler(pile)
    return i

def creer_tas(n):
    tas = []
    for i in range(n):
        tas.append(creer_pile())
    return tas

def empiler_grain(tas,n):
    empiler(tas[n])
 
def sommet_tas(tas):
    hauteur_tas = 0
    for pile in tas:
        if taille(pile)>hauteur_tas:
            hauteur_tas = taille(pile)
    return hauteur_tas

def affichage_tas(tas,hauteur_tas):
    #hauteur_tas = 0
    #for pile in tas:
    #    if taille(pile)>hauteur_tas:
    #        hauteur_tas = taille(pile)

    for i in range(hauteur_tas,0,-1):
        ch=""
        for pile in tas :
            if taille(pile)>=i:
                ch = ch +"*"
            else :
                ch=ch + "_"
        print(ch)

def sablier(tas):
    indice_m = taille_tas//2
    empiler_grain(tas,indice_m)
    hauteur_tas = sommet_tas(tas)

    
    if (taille(tas[indice_m-1])==hauteur_tas-2 and taille(tas[indice_m+1])==hauteur_tas-2):
        sens = randint(0,1)
    elif (taille(tas[indice_m-1])==hauteur_tas-2 and taille(tas[indice_m+1])==hauteur_tas-1):
        sens = 0
    else :
        sens = 1
    
    chute(tas,indice_m,sens)
        
    
    
def chute(tas,indice,sens):
    """
    Gestion d'une chute de grain de sable.
    Entrées : 
     * tas(liste de piles) : tas de sable
     * indice(int) : pile à laquelle on a déposé le dernier grain de sable
     * sens(int) : 0 chute à gauche, 1 chute à droite
    Sortie : 
     * le tas est modifié mais n'est pas retourné.
    """
    if sens == 0 :
        if (taille(tas[indice])>taille(tas[indice-1])+1 and taille(tas[indice])>1 and indice >0):
            depiler(tas[indice])
            empiler(tas[indice-1])
            chute(tas,indice-1,sens)
        else :
            return None
    if sens == 1 :
        if (indice==len(tas)-1):
            return None
        elif (taille(tas[indice])>taille(tas[indice+1])+1 and taille(tas[indice])>1):
            depiler(tas[indice])
            empiler(tas[indice+1])
            chute(tas,indice+1,sens)
        else :
            return None
    return None
    
    
nb_grains = 9
taille_tas = 7
tas = creer_tas(taille_tas)
for i in range(nb_grains):
    #print("Chute "+str(i+1))
    sablier(tas)
    #print(tas)
    affichage_tas(tas,4)
    time.sleep(0.5)
