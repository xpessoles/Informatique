# -*- coding: utf-8 -*-
"""
Created on Thu Oct  2 07:39:24 2014

@author: emiliendurif2
"""


def matches(joueurs): 
    """ Fonction recursive qui renvoie une liste de matches
    a partir d'une liste de joueurs """ 
    #s'il n'y a qu'un seul joueur, on n'organise aucun match
    if len(joueurs)==1: 
        return [] 
    #on enleve le dernier joueur de la liste, et on demande les matchs sans lui
    else:
        dernier_joueur = joueurs.pop()
        vs=matches(joueurs) 
        print vs
    #on rajoute un match entre lui et tous les autres joueurs 
        for j in joueurs:
            vs.append([j,dernier_joueur]) 
    #on le remet dans la liste des joueurs, et on renvoie 
    #la liste des matchs 
        joueurs.append(dernier_joueur) 
        return vs
    
joueurs=range(1,5)
print matches(joueurs)