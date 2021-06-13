#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = "Xavier PESSOLES"

# Import des bibliothèques
import matplotlib.pyplot as plt

# Question 1
# ==========
# Le répertoire courant est Exercice_02.
# Le sous-répertoire data contient le fichier ex_01.txt.

# On ouvre le fichier en lecture
fid = open("C:\Enseignement\GitHub\Informatique\PreparationOraux\Exercices_Maths\programmes\Exercice_02\data\ex_01.txt")
#fid = open("data\ex_01.txt")

# On charge le fichier dans une liste.
# Chaque élément de la liste correspond à chaque ligne sous forme de chaîne de caractère.
file = fid.readlines()
# On ferme le fichier
fid.close()

LX=[]
LY=[]
for ligne in file :
    ligne = ligne.split(';')
    LX.append(float(ligne[0]))
    LY.append(float(ligne[1]))

# Question 2
# ==========
# Ne pas oublier de charger préalablement import matplotlib.pyplot as plt

plt.plot(LX,LY)
plt.show()

# Question 3
# ==========
def trapeze(x,y):
    res = 0 
    for i in range(1,len(LX)):
        res = res + (LX[i]-LX[i-1])*0.5*(LY[i]+LY[i-1])
    return res
print(trapeze(LX,LY))

# Question 4
# ==========
from scipy.integrate import trapz
# Attention à l'ordre des arguments. 
# Après l'import, help(trapz) permet d'avoir de l'aide sur la fonction.
print(trapz(LY,LX))
