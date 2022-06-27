# -*- coding: utf-8 -*-
"""
Created on Mon Jun 27 21:04:00 2022

@author: xpess
"""

def somme_corrige(L:list)-> float :
    """
    Parameters
    ----------
    L : list
        DESCRIPTION.

    Returns
    -------
    float ou int
        somme des éléments de la liste.

    """
    return sum(L)

def somme_test(foo,L):
    # Test sur L
    if foo(L) == somme_corrige(L):
        print(f"Test somme({L}) : réussi")
    else :
        print(f"Test somme({L}) : échoué")
    
    
  