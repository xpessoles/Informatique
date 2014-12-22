#!/usr/bin/env python
# -*- coding: utf-8 -*-


def is_number_in_list(nb,tab):
    """
	Renvoie True si le nombre nb est dans la liste de nombres tab.
    Renvoie False sinon. 
    
    Keyword arguments:
    nb -- nombre entier
    tab -- liste de nombre entiers
    """
    i=0
    while i<len(tab) and tab[i]!=nb:
        i+=1
    return i<len(tab)
# Exemple :
#nb1,nb2,liste = 4,9,[1,2,3,5,9]
#print(is_number_in_list(nb1,liste))
#print(is_number_in_list(nb2,liste))


def what_is_max(tab):
    """ 
	Renvoie le plus grand nombre d'une liste
    
    Keyword arguments:
    tab -- liste de nombres
    """
    i=1
    maxi=tab[0]
    while i<len(tab):
        if tab[i]>maxi:
            maxi=tab[i]
        i+=1
    return maxi
# Exemple :
#liste = [1,2,3,5,9]
#print(what_is_max(liste))


def what_is_max(tab):
    """ 
    Renvoie le plus grand nombre d'une liste.
    Keyword arguments:
    tab -- liste de nombres
    """
    i=1
    maxi=tab[0]
    while i<len(tab):
        if tab[i]>maxi:
            maxi=tab[i]
        i+=1
    return maxi
# Exemple :
#liste = [1,2,3,5,9,5,3,1,5]
#print(what_is_max(liste))


def is_number_in_list_dicho(nb,tab):
    """ 
    Renvoie l'index si le nombre nb est dans la liste de nombres tab.
    Renvoie None sinon.
    
    Keyword arguments:
    nb -- nombre entier
    tab -- liste de nombres entiers triés
    """
    g, d = 0, len(tab)-1
    while g <= d:
        m = (g + d) // 2
        if tab[m] == nb:
            return m
        if tab[m] < nb:
            g = m+1
        else:
            d = m-1
    return None
# Exemple :
#nb1,nb2,liste = 4,9,[1,2,3,5,9]
#print(is_number_in_list_dicho(nb1,liste))
#print(is_number_in_list_dicho(nb2,liste))



def calcul_moyenne(tab):
    """ 
	Renvoie la moyenne des éléments d'un tableau.
    
	Keyword arguments:
    tab -- liste de nombres entiers
    """
    res = 0
    for i in range(len(tab)):
        res = res+tab[i]
    
    return res/(len(tab))
# Exemple :
#liste = [1,2,3,5,9]
#print(calcul_moyenne(liste))

def calcul_variance(tab):
    """ 
	Calcule la variance des éléments d'un tableau.
    
	Keyword arguments:
    tab -- liste de nombres entiers
    """
    m = calcul_moyenne(tab)
    res = 0
    for i in range(len(tab)):
        res = res+(tab[i]-m)**2
    
    return res/(len(tab))
# Exemple :
#liste = [1,2,3,5,9]
#print(calcul_moyenne(liste))
#print(calcul_variance(liste))


def index_of_word_in_text(mot, texte):
    """ 
	Recherche si le mot est dans le texte.
    Renvoie l'index si le mot est présent, None sinon.
    
    Keyword arguments:
    mot -- mot recherché
    texte -- texte
    """
    for i in range(1 + len(texte) - len(mot)):
        j = 0
        while j < len(mot) and mot[j] == texte[i + j]:
            j += 1
        if j == len(mot):
            return i
    return None

# Exemple
#Texte = "Chuck Norris has a grizzly bear carpet in his room. The bear isn't dead it is just afraid to move."
#Mot = "ove."
#print(index_of_word_in_text(Mot,Texte))

# ====================
# Algorithmes de tris
# ====================

def tri_insertion_01(tab):
    """ 
    Trie une liste de nombre en utilisant la méthode du tri par insertion.
    En Python, le passage se faisant par référence, il n'est pas indispensable
    de retourner le tableau.
    Keyword arguments:
    tab -- liste de nombres
    """
    for i in range (1,len(tab)):
        x=tab[i]
        j=0
        while j<=i-1 and tab[j]<x:
            j = j+1
        for k in range(i-1,j-1,-1):
            tab[k+1]=tab[k]
        tab[j]=x

# Exemple :
#liste = [1,9,7,6,5]
#print(liste)
#tri_insertion_01(liste)
#print(liste)


def tri_insertion_02(tab):
    """ 
    Trie une liste de nombre en utilisant la méthode du tri par insertion.
    En Python, le passage se faisant par référence, il n'est pas indispensable
    de retourner le tableau.
    Keyword arguments:
    tab -- liste de nombres
    """
    for i in range (0,len(tab)):
        x=tab[i]
        j=0
        while j>1 and tab[j-1]>x:
            tab[j]=tab[j-1]
            j = j-1
        tab[j]=x

# Exemple :
liste = [10,9,7,6,5]
print(liste)
tri_insertion_02(liste)
print(liste)
        
def exponentiation_naive(x,n):
    """ 
	Renvoie x**n par la méthode naïve.
    
    Keyword arguments:
    x -- un nombre réel
    n -- un nombre entier
    """
    
    j=n
    res = 1
    while j>=1:
        res = res * x
        j=j-1
    return res

#print(exponentiation_naive(3,2))
#print(exponentiation_naive(3,0))