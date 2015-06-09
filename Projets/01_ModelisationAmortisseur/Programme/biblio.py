#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__      = "Xavier Pessoles"
__email__ = "xpessoles.ptsi@free.fr"



def solve_eq(m,k,c,x0,v0,h,T):
    """
    Résolution de l'équation différentielle du second ordre pour un système
    masse amortisseur.
    Entrées : 
     * m,flt : masse en kg
     * k,flt : raideur du ressort en N/m
     * c,flt : coefficient d'amortissement en N.s/m
     * x0,flt : position initiale en m
     * v0,flt : vitesse initiale en m/s
     * h,flt : pas de temps de calcul
     * T,flt ; temps de simulation
    Sortie : 
     * 
    
    """
    res=[x0,v0]
    t=h
    temps = [0,t]
    while t<T:
        t=t+h
        res.append((1/(m+k*h*h+c*h))*(h*h*f(t)+res[-1]*(2*m+c*h)-m*res[-2]))
        temps.append(t)
        
    return temps,res