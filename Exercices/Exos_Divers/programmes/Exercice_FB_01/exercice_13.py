#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = "Xavier PESSOLES"

# EXERCICE 13

P = [0,1,2,3,4,5]

# Question 1 
# ==========
def affiche_poly(P):
    """
    Affiche un polynôme sous la forme a0*X^0+a1*X^1+a2*X^2+...
    Entrée : 
     * P(lst) : liste des coefficients du polynome [a0,a1,...,an]
    Sortie : 
     * Rien. Affichage
    """
    ch=""
    for i in range(len(P)):
        signe="+"
        if P[i]<0 :
            signe="-"
        
        ch=ch+signe+str(abs(P[i]))+"*X^"+str(i)
    print(ch)
    
#affiche_poly(P)

# Question 2
# ==========
def degre_poly(P):
    """
    Calcule le degré d'un polynôme.
    On se base uniquement sur la taille de la liste à cause de la comparaison à zero
    Entrée : 
     * P(lst) : liste des coefficients du polynome [a0,a1,...,an]
    Sortie : 
     * deg(int) : degé du polynôme
    """
    return len(P)-1

#print(degre_poly(P))

# Question 3
# ==========
def add_poly(P1,P2):
    """
    Calcule la somme de deux polynômes.
    Attention à bien faire une copie...
    Entrée : 
     * P1, P2(lst) : liste des coefficients du polynome [a0,a1,...,an]
    Sortie : 
     * P(lst) : liste des coefficients du polynome [a0+b0,a1+b1,...,an+bn]
    """
    # On cherche le polynôme le plus grand
    if degre_poly(P1)>=degre_poly(P2):
        P=P1.copy()
        for i in range(len(P2)):
            P[i]=P[i]+P2[i]
    else :
        P=P2.copy()
        for i in range(len(P1)):
            P[i]=P[i]+P1[i]
    return P

P1 = [0,1,2,3,4,5]
P2 = [-1,-1,-1,-1]
#affiche_poly(add_poly(P1,P2))
#affiche_poly(add_poly(P2,P1))
    
def mul_poly(P1,P2):
    """
    Calcule la multiplication de deux polynômes.
    Entrée : 
     * P1, P2(lst) : liste des coefficients du polynome [a0,a1,...,an]
    Sortie : 
     * P(lst) : produits des polynomes
    """
    P=[0]*(degre_poly(P1)+degre_poly(P2)+1)
    for i in range(len(P1)):
        for j in range(len(P2)):
           P[i+j] = P[i+j]+ P1[i]*P2[j]
    return P

P1 = [1,1,1]
P2 = [2,2]
#affiche_poly(P1)
#affiche_poly(P2)
#affiche_poly(mul_poly(P1,P2))

def mul_poly(P1,P2):
    """
    Calcule la multiplication de deux polynômes.
    Entrée : 
     * P1, P2(lst) : liste des coefficients du polynome [a0,a1,...,an]
    Sortie : 
     * P(lst) : produits des polynomes
    """
    P=[0]*(degre_poly(P1)+degre_poly(P2)+1)
    for i in range(len(P1)):
        for j in range(len(P2)):
           P[i+j] = P[i+j]+ P1[i]*P2[j]
    return P
   
#affiche_poly(mul_sca_poly(3,P))

    

# Question 4
# ==========
def prsc_poly(P1,P2):
    """
    Calcule le produit scalaire de deux polynômes.
    Attention à bien faire une copie...
    Entrée : 
     * P1, P2(lst) : liste des coefficients du polynome [a0,a1,...,an]
    Sortie : 
     * P(flt) :produit des coefficients des polynomes a0*b0+a1*b1+...
    """
     # On cherche le polynôme le plus grand
    if degre_poly(P1)>=degre_poly(P2):
        P=P1.copy()
        for i in range(len(P2)):
            P[i]=P[i]*P2[i]
    else :
        P=P2.copy()
        for i in range(len(P1)):
            P[i]=P[i]*P1[i]
    return sum(P)


P1 = [1,1,1]
P2 = [2,2]
#print(prsc_poly(P1,P2))
#print(prsc_poly(P2,P1))

# Question 5
# ==========
def deriv_poly(P):
    """
    Calcule la dérivée d'un polynôme.
    Entrée : 
     * P(lst) : liste des coefficients du polynome [a0,a1,...,an]
    Sortie : 
     * coefficients du polynôme dérivé
    """
    return [P[i]*i for i in range(1,len(P))]

P = [0,1,2,3,4,5]
affiche_poly(P)
affiche_poly(deriv_poly(P))
    