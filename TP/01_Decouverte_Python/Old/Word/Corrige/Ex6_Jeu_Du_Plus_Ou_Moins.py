# Écrire un programme Python permettant à l’utilisateur de trouver un nombre
# choisi au hasard par le programme en ayant comme unique indication « le
# nombre cherché est plus grand » ou « le nombre cherché est plus petit ».
# L’intervalle dans lequel se trouve le nombre cherché est précisé à l’utilisateur
# (entre 1 et 100 par exemple).

# -*-coding:Latin-1 -*

import os
from random import randrange

Valeur_Min = 1
Valeur_Max = 100

Nombre_Propose = 0
Nombre_Mystere = randrange (Valeur_Min, Valeur_Max)

print ("JEU DU PLUS OU MOINS\nLe nombre cherché est compris entre", Valeur_Min, "et", Valeur_Max, "\n")

# print (Nombre_Mystere)

while Nombre_Propose != Nombre_Mystere :

    Nombre_Propose = input ("Proposez un nombre : ")
    Nombre_Propose = int (Nombre_Propose)

    if Nombre_Propose < Nombre_Mystere :

        print ("C'est plus")

    elif Nombre_Propose > Nombre_Mystere :

        print ("C'est moins")

    else :

        print ("Féliciations, vous avez trouvé le nombre mystère !")

os.system ("pause")
