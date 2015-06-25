#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__      = "Xavier Pessoles"
__email__ = "xpessoles.ptsi@free.fr"


import math
from random import randint

def generate_profil(f0,a0,df0,f1,a1,f2,a2,f3,a3,b,L,nb):
    """
    Génération d'un profil de rugosité
    Entrée :
     * f0,flt : 
     * f1,flt : fréquence du profil d'ordre 1 (défaut de forme)
     * f2,flt : fréquence du profil d'ordre 2 (défaut d'ondulation)
     * f3,flt : fréquence du profil d'ordre 3 (défaut de rugosité)
     * L,flt : longueur du profil
     * b, flt : amplitude du bruit
     * nb,int : nombre points
    """
    
    # Génération du profil d'ordre 1
    i=0
    x=[]
    profil=[]
    while i<=nb:
        t = i*L/nb
        bruit = b*randint(-100,100)/1000
        profil.append(a0*math.sin(2*math.pi*f0*t+df0)+a1*math.sin(2*math.pi*f1*t)+a2*math.sin(2*math.pi*f2*t)+.04*math.sin(2*math.pi*f3*t)+bruit)
        x.append(t)
        i=i+1
    
    return x,profil
    