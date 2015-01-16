# -*- coding: utf-8 -*-
"""
Created on Mon Jan 12 21:08:25 2015

@author: Xavier
"""
import math

def is_number_in_area(tab,ii,jj,nb):
    """
    Recherche si le le nombre nb que l'on souhaite mettre à la case i,j est 
    présent dans la zone
    Entrées : 
     * tab, list : grille de sudoku
     * ii, int : indice de la ligne
     * jj, int : indice de la colonne
     * nb, int : nombre à tester
    Sortie : 
     * bool : True si le nombre est dans la zone, False sinon
    """
    # Taille de la zone
    taille = int(math.sqrt(len(tab)))
    # Délimitation de la zone
    i_mini=(ii//taille)
    j_mini=(jj//taille)
    
    for i in range(i_mini,i_mini+taille):
        for j in range(j_mini,j_mini+taille):
            if tab[i][j]==nb:
                return True
    return False
     
def is_number_in_column(tab,jj,nb):
    """
    Recherche si le le nombre nb est présent dans une colonne
    Entrées : 
     * tab, list : grille de sudoku
     * jj, int : indice de la colonne
     * nb, int : nombre à tester
    Sortie : 
     * bool : True si le nombre est dans la colonne, False sinon
    """
    for i in range(len(tab)):
        if tab[i][jj] == nb:
            return True
    return False

def is_number_in_raw(tab,ii,nb):
    """
    Recherche si le le nombre nb est présent dans une ligne
    Entrées : 
     * tab, list : grille de sudoku
     * ii, int : indice de la ligne
     * nb, int : nombre à tester
    Sortie : 
     * bool : True si le nombre est dans la ligne, False sinon
    """
    for j in range(len(tab)):
        if tab[ii][j] == nb:
            return True
    return False
    

def check_number(tab,i,j,nb):
    res1 = is_number_in_area(tab,i,j,nb)
    res2 = is_number_in_column(tab,j,nb)
    res3 = is_number_in_raw(tab,i,nb)
    if res1 or res2 or res3 :
        return True
    return False
    
def solve_grille(grille):
    i,j=0,0
    while i <len(grille):
        print("Ligne "+str(i))
        while j<len(grille):
            input(" ")
            print("Colonne "+str(j))
            if grille[i][j]==0:
                nb=grille[i][j]+1
                if check_number(grille,i,j,nb) == False :
                    # Le nombre n'est ni dans la colonne ni dans la case
                    grille[i][j]=nb
                    if j == len(grille)-1:
                        # Derniere ligne, on passe en haut de la colonne suivante
                        j = 0
                        i = i+1
                    else :
                        j = j+1
                elif j>0:
                    # On remonte d'un cran
                    j=j-1
                else :
                    # On retourne à la fin de la colonne suivante
                    i = i-1
                    j = len(grille)-1
            else:
                if j == len(grille)-1:
                    j=0
                    i = i+1
                else : 
                    j = j+1
    return grille


grille = [
[0,0,3,6,9,0,0,4,0],
[0,7,5,0,0,0,0,0,0],
[9,0,0,0,1,5,0,3,6],
[5,3,2,7,0,0,1,0,4],
[0,0,0,0,0,0,0,0,0],
[7,0,8,0,0,1,2,9,5],
[3,8,0,1,4,0,0,0,7],
[0,0,0,0,0,0,9,2,0],
[0,5,0,0,6,3,4,0,0]]

gr = solve_grille(grille)
print(gr)