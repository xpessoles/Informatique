#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = "MMe Barré, Lycée LESAGE, Vannes -- Xavier PESSOLES"

# EXERCICE 5

import math
import scipy.misc as scim
# Question 1 
# ==========
def Px_poisson(k, n, p):
    """
    Entrée : 
     * k(int)
     * n(int) : strictement positif
     * p(flt) : réel compris entre ]0, 1[
    X suit une loi de Poisson P(n*p)
    Sortie : 
     * flt : (np)^k exp(-np)/k!
    """
    np = n * p
    return (np)**k * math.exp(- np) / math.factorial(k)

n, p = 30, 0.1
lst_px = [Px_poisson(k, n, p) for k in range(n + 1)]
#print(lst_px)


# Question 2
# ==========
def Py_binomiale(k, n, p):
    """
    Entrée : 
     * k(int)
     * n(int) : strictement positif
     * p(flt) : réel compris entre ]0, 1[
    Y suit une loi binomiale B(n,k)
    Sortie : 
     * int : B(n,k)*p^k *(1-p)^(n-k)
    """
    return scim.comb(n,k)*p**k*(1-p)**(n-k)

n, p = 30, 0.1
lst_py = [Py_binomiale(k, n, p) for k in range(n + 1)]

# Question 3
# ==========
def ecarts(n,p):
	"""
	Entrée :
     * n(int) : strictement positif
     * p(flt) : réel compris entre ]0, 1[
    Sortie : 
     * maxi(flt) écart maxi entre P(Y=k) et P(X=k)
    """
     
	lst_px = [Px_poisson(k, n, p) for k in range(n + 1)]
    lst_py = [Py_binomiale(k, n, p) for k in range(n + 1)]
    maxi = max([abs(lst_py[i]-lst_px[i]) for i in range(len(lst_px))])
    return maxi
    
#print(ecarts(n,p))

# Question 4
# ==========
def E(e,p):
	"""
	Retourne le plus petit entier naturel n tq ecart(n,p)<=e
	Entrée : 
	 * e(flt) : >0
	 * p(flt) : réel compris entre ]0, 1[
    Sortie :
     n(int)
	"""
	n=1
	while (ecarts(n,p))>e :
		n=n+1
	return n

# Question 5
# ==========
print(E(0.008,0.075))
print(E(0.005,0.075))
print(E(0.008,0.1))
#print(E(0.005,0.1))

