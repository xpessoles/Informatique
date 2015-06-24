# -*- coding: utf-8 -*-
"""
Created on Tue Nov 25 08:54:37 2014

@author: Xavier
"""

def percolateUp (tas) :
    index = len(tas)-1
    val = tas[index]
    while index>0 :
        index_pere = int((index-1)/2)
        pere = tas[index_pere]
        if pere > val :
            break
        else :
            tas[index]= pere
            tas[index_pere]= val
            index = index_pere
        print(tas)



def percolateDown(tas) :
    taille = len(tas)
    indi = 0
    maxi = 0
    while 1 :
        print(tas)
        indi = maxi
        gauche = 2 * indi
        droit = (2*indi)+1
        if ((gauche <= taille-1) and (tas[gauche]>tas[indi])) :
            maxi = gauche
        else :
            maxi = indi
        if ((droit<=taille-1) and (tas[droit]>tas[maxi])) :
            maxi = droit
        if (maxi != indi) :
            tmp = tas[maxi]
            tas[maxi] = tas[indi]
            tas[indi] = tmp
        if (((gauche>(taille - 1)) and (droit > (taille-1))) or (maxi==indi)):
            break       

