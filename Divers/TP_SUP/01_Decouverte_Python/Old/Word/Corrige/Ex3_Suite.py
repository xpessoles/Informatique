#! /usr/bin/env python
# -*- coding: utf-8 -*-



n = int(input("Saisir un nombre entier positif : "))

somme = 0
#Calcul des termes d'une suite
for i in range(0,n+1):
    somme=somme+i

# Sans boucle
somme2 = n*(n+1)/2

print(somme)
print(somme2)
