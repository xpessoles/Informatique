# -*- coding: utf-8 -*-
"""
Created on Mon Dec 27 21:45:47 2021

@author: xpess
"""


def sac_a_dos(L:list, capacite:int) :
    sac = 0
    liste_fruits= []
    i=0
    while sac <= capacite and i<len(L): 
        delta = capacite - sac
        if L[i][2] < delta :
            sac = sac+L[i][2]
            liste_fruits.append(L[i])
            delta = capacite - sac
        i=i+1
        
    s = sum([f[2] for f in liste_fruits])
    return liste_fruits,s


def sac_a_dos_v2(L:list, capacite:int) :
    sac = 0
    liste_fruits= []
    i=0
    while sac <= capacite and i<len(L): 
        delta = capacite - sac
        if L[i][2] < delta :
            sac = sac+L[i][2]
            liste_fruits.append(L[i])
            delta = capacite - sac
        i=i+1
        
    s = sum([f[2] for f in liste_fruits])
    return liste_fruits,s


cueillette = [[24,"framboises",1], [16,"myrtilles",3],[6,"fraises",5], [3,"mures",2]]
l,s = sac_a_dos(cueillette,5)
print(l)
print(s)
fruitsDisponibles = [[3,"melon de cavaillon",1,1], [2.5,"melon jaune",2,1, 2,"pastèque",3,1]]