# Écrire un programme Python permettant de construire le triangle
# de Pascal et de déterminer la plus grande valeur apparaissant dans
# une ligne. Le nombre de lignes sera saisi au clavier par l'utilisateur.

# -*-coding:Latin-1 -*

import os

# On importe la fonction factorial (fonction factorielle)
# contenue dans le module math et on la renomme fact
from math import factorial as fact

# On construit une fonction permettant de calculer les coefficients du binôme de Newton

Coef_Bin = lambda n, p : fact (n) / (fact (n - p) * fact (p))

Nb_Lignes = input ("Entrez le nombre de lignes : ")
Nb_Lignes = int (Nb_Lignes)

# Construction de la n ième ligne

n = 0
while n <= Nb_Lignes :
    print ("\nLes coefficients de la", n + 1, "ème ligne sont :\n")
    p = 0
    while p <= n :
        Cnp = Coef_Bin (n, p)
        print (int (Cnp))           # Pour éviter que Python n'affiche un nombre à virgules
        p += 1
    n += 1
    print ("Valeur maximale : ", Coef_Bin (n-1, int ((n-1)/2)))

os.system ("pause")
