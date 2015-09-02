# Écrire un programme Python permettant de calculer le temps écoulé entre deux horaires
# saisis au clavier par l'utilisateur ; les horaires seront saisis au format (heures, minutes, secondes)
# et le résultat sera affiché en secondes et au format (heures, minutes, secondes).

# -*-coding:Latin-1 -*

import os

# Premier horaire

print ("PREMIER HORAIRE")
h = input ("Entrez le nombre d'heures : ")
h = int (h)
m = input ("Entrez le nombre de minutes : ")
m = int (m)
s = input ("Entrez le nombre de secondes : ")
s = int (s)

Nb_Secondes_1 = h * 3600 + m * 60 + s

# Second horaire

print ("\nSECOND HORAIRE")
h = input ("Entrez le nombre d'heures : ")
h = int (h)
m = input ("Entrez le nombre de minutes : ")
m = int (m)
s = input ("Entrez le nombre de secondes : ")
s = int (s)

Nb_Secondes_2 = h * 3600 + m * 60 + s

# Temps écoulé au format secondes

if Nb_Secondes_2 - Nb_Secondes_1 > 0 :
    s = Nb_Secondes_2 - Nb_Secondes_1
else :
    s = Nb_Secondes_1 - Nb_Secondes_2

Nb_Secondes = s

# Conversion du temps écoulé au format (heures, minutes, secondes)

if s // 3600 == 0 :
    h = 0
else :
    h = s // 3600

s = s - h * 3600

if s // 60 == 0 :
    m = 0
else :
    m = s // 60

s = s - m *60

print ("\nL'écart entre les deux horaires est de", Nb_Secondes, "s ou encore de", h, "h", m, "min", s, "s")

os.system ("pause")

