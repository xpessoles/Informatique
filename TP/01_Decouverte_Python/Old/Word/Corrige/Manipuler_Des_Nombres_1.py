# Écrire un programme Python permettant de :

# Question 1 : calculer puis afficher la somme des entiers de 1 à n (inclus) où n > 1 est un entier saisi au clavier par l’utilisateur ;
# Question 2 : calculer n ! où n >= 0 est un entier saisi au clavier par l’utilisateur ;
# Question 3 : calculer et afficher le produit des nombres paires compris entre 1 et n (inclus) où n > 1 est un entier saisi au clavier par l’utilisateur.

# -*-coding:Latin-1 -*

import os

# Réponse 1

n = input ("Entrez la valeur de n : ")
n = int (n)
somme = 0
i = 1
while i <= n :
    somme = somme + i
    i += 1
print ("La somme des entiers compris entre 1 et", n, "(inclus) vaut :", somme)

# Réponse 2 (sans utiliser la fonction factorielle de Python)

n = input ("Entrez la valeur de n : ")
n = int (n)
factoriel = 1
i = 1
while i <= n :
    factoriel = factoriel * i
    i += 1
print (n, "! =", factoriel)

# Réponse 2 (en utilisant la fonction factorielle de Python)

from math import factorial as fact        # On importe la fonction factorial (fonction factoriel)
                                                                # contenue dans le module math et on la renomme fact
print (n, "! =", fact (n))

# Réponse 3

n = input ("Entrez la valeur de n : ")
n = int (n)
produit = 1
i = 2
while i <= n :
    produit = produit * i
    i += 2
print ("Le produit des nombres paires compris entre 1 et", n, "(inclus) vaut :", produit)

os.system ("pause")
