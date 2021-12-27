# -*- coding: utf-8 -*-
"""
Created on Mon Dec 27 14:34:42 2021

@author: xpess
"""



def rendre_monnaie(caisse:list, cout:float, somme_client:float) -> list :
    """
    Algorithme glouton du rendu de monnaie

    Parameters
    ----------
    caisse : list
        liste de liste contenant les valeurs des billets et leur quantité.
        On utilise une liste (plutôt qu'un dictionnaire) car les valeurs 
        doivent être triées
    cout : float
        coût à payer en euros
    somme_client : float
        somme donnée par le client (en euros)

    Returns
    -------
    list 
        DESCRIPTION.

    """
    rendu = []
    somme = int(100*somme_client)
    cout = int(100*cout)
    delta = somme- cout
    while delta > 0 :
        for valeur in caisse :
            while valeur[0]<=delta :
                delta = delta - valeur[0]
                rendu.append(valeur[0])
    return rendu


def rendre_monnaie_v2(caisse:list, cout:float, somme_client:float) -> list :
    """
    Algorithme glouton du rendu de monnaie avec MAJ de la caisse.
    """
    rendu = []
    somme = int(100*somme_client)
    cout = int(100*cout)
    delta = somme- cout
    while delta > 0 :
        for i in range(len(caisse)):
            while caisse[i][0]<=delta and caisse[i][1]>0:
                delta = delta - caisse[i][0]
                caisse[i][1]=caisse[i][1]-1
                rendu.append(caisse[i][0])
        print(delta)
        if delta>0 :
            return []
    return rendu



caisse = [[2000,5],[1000,5],[500,5],[200,5],[100,5],\
    [50,5],[20,5],[10,5],[5,5],[2,5],[1,5]]

    
cout = 15.99
somme_client = 200
r = rendre_monnaie_v2(caisse, cout, somme_client)
print(r)
print(caisse)

caisse2 = [[5000,10],[2000,10],[1000,10],[800,10],[100,10]]
r = rendre_monnaie_v2(caisse2, 34, 50)
# L'optimal serait de 
