# Écrire un programme Python permettant à l’utilisateur de saisir deux entiers n et m tels que n < m
# et de rechercher parmi tous les entiers contenus dans l'intervalle [m, n] ceux qui :
# 1) sont impairs
# 2) sont des multiples de 5
# 3) contiennent le chiffre 2

# Contrainte (pour plus tard) : les nombres impairs devront être écrits sur une même ligne et séparés par un espace

# -*-coding:Latin-1 -*

import os

Borne_Inf = input ("Entrez la borne inférieure : ")
Borne_Inf = int (Borne_Inf)
Borne_Sup = input ("Entrez la borne supérieure : ")
Borne_Sup = int (Borne_Sup)

# Ceux qui sont impairs

print ("\nVoilà la liste des nombres impairs\n")

for entier in range (Borne_Inf, Borne_Sup + 1, 1) :
    if entier % 2 != 0 :
        print (entier)

# Ceux qui sont des multiples de 5

print ("\nVoilà la liste des multiples de 5\n")

for entier in range (Borne_Inf, Borne_Sup + 1, 1) :
    if entier % 5 == 0 :
        print (entier)

# Ceux qui contiennent le chiffre 2

print ("\nVoilà la liste des nombres qui contiennent le chiffre 2\n")

for entier in range (Borne_Inf, Borne_Sup + 1, 1) :
    chaine = str (entier)
    for lettre in chaine :
        if lettre == "2" :
            print (entier)

os.system ("pause")

