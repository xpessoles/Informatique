#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__      = "Xavier Pessoles"
__email__ = "xpessoles.ptsi@free.fr"


from math import sin,pi

def solve_eq(m,k,c,x0,v0,h,temps,f):
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
     * temps,flt : liste des instants de temps
     * f,lst : liste de valeurs prise par la fonction sollicitant.
    Sortie : 
     * 
    
    """
    res=[x0,v0]
    for i in range(2,len(temps)):
        res.append((1/(m+k*h*h+c*h))*(h*h*f[i]+res[i-1]*(2*m+c*h)-m*res[i-2]))
        
    return res

def f_sin(A,f,t):
    """
    Fonction retournant la valeur de a*sin(omega*t).
    Entrées :
     * A,flt : Amplitude du sinus
     * f,flt : fréquence du sinus
    Sortie :
     res,flt : résultat
    """
    omega = 2*pi*f
    return A*sin(omega*t)

def echelon(A):
    return A

def syst_diff_echelon(syst,t):
    """
    Définition du système d'équation différentielle pour Scipy
    """
    x = syst[0]
    v = syst[1]
    dxdt = v
    dvdt = (1/m)*echelon(10)-(c/m)*v-(k/m)*x
    return[dxdt,dvdt]

def syst_diff_sinus(syst,t):
    """
    Définition du système d'équation différentielle pour Scipy
    """
    x = syst[0]
    v = syst[1]
    dxdt = v
    dvdt = (1/m)*f_sin(1,1,t)-(c/m)*v-(k/m)*x
    return[dxdt,dvdt]