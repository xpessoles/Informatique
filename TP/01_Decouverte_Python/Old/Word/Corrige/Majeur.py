# Écrire un programme Python permettant de déterminer si un
# utilisateur dont l’âge est saisi au clavier est ou non majeur.

# Intérêt de l'exercice

# 1) Utilisation de la fonction input.
# 2) La variable saisie est interprétée comme une chaîne de caractères ;
#     nécessité de la convertir en entier en utilisant le mot-clé int.
# 3) Attirer l’attention sur les problèmes rencontrés si la valeur saisie ne peut pas être convertie 
#     en entier (utilisation des mots-clés try et except et création d'une boucle while)
# 4) Utilisation d’une forme conditionnelle avec if et else.
# 5) Utilisation de la fonction print.

# -*-coding:Latin-1 -*

import os

age_est_un_entier = False

while age_est_un_entier == False :
    age = input ("Quel est votre âge ? ")
    try :
        age = int (age)
    except :
        print ("")
        print ("La valeur entrée est incompatible avec le type de donnée attendue (un nombre entier positif) ; veuillez entrer une nouvelle valeur svp !")
        print ("")
    else :
        age_est_un_entier = True

if age >= 18 :
    print ("Vous êtes majeur(e)")
else :
    print ("Vous êtes mineur(e)")

os.system ("pause")
