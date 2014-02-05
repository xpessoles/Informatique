from math import sin
from math import pi
from math import sqrt
from math import fabs
from math import radians

# Paramètres physiques du problème

L = 1                                   # Longueur de la tige
g = 9.81                              # Accélération de la pesanteur
To = 2 * pi * sqrt (L / g)    # Période propre du pendule

# Fonction mathématique à intégrer

f = lambda ThetaZero, Phi :To * ((2 / pi)  / sqrt (1 - pow ((sin (ThetaZero / 2) * sin (Phi)), 2)))

# Création de la fonction "Periode"

def Periode (PeriodePropre, ThetaZero, Methode) :
    a = 0                         # Borne inférieure de l'intégrale
    b = pi / 2                  # Borne supérieure de l'intégrale
    N = 1000                  # Nombre de rectangles ou de trapèzes
    h = (b - a) / N          # Largeur d'un rectangle ou d'un trapèze

    if Methode == "Rectangle à gauche" :
        Integrale = 0
        for i in range (1, N + 1, 1) :
            xi = a + (i - 1) * h
            Integrale = Integrale + f (ThetaZero, xi) * h
        return Integrale

    if Methode == "Rectangle à droite" :
        Integrale = 0
        for i in range (1, N + 1, 1) :
            xi = a + i * h
            Integrale = Integrale + f (ThetaZero, xi) * h
        return Integrale

    if Methode == "Trapèze" :
        Integrale = 0
        for i in range (1, N + 1, 1) :
            xi = a + i * h
            xi1 = a + (i + 1) * h
            Integrale = Integrale + ((f (ThetaZero, xi) + f (ThetaZero, xi1)) * h) /2
        return Integrale

    if Methode == "Simpson" :
        Integrale = 0
        for i in range (1, N + 1, 1) :
            xi = a + i * h
            xi1 = a + (i + 1) * h            
            Integrale = Integrale + (1 / 6) * (xi1 - xi) * (f (ThetaZero, xi) + 4 * f (ThetaZero, (xi + xi1) / 2) + f (ThetaZero, xi1))
        return Integrale

# Création de la fonction "EcartRelatif"

def EcartRelatif (T, To) :
    Epsilon = 100 * fabs ((T - To) / To)
    return Epsilon

# Création des listes de résultats

ListeAngle = list ()
ListePeriode = list ()
ListeEcartRelatif = list ()

for i in range (1, 91, 1) :
    ListeAngle.append (i)
    T = round (Periode (To, radians (i), "Simpson"), 5)
    ListePeriode.append (T)
    ListeEcartRelatif.append (round (EcartRelatif (T, To), 2))

# Recherche d'un angle

def EcartRelatifMax (x) :
    AngleCherche = 0
    for i in range (0, 90, 1) :
        if ListeEcartRelatif [i] > x :
            break
    return ListeAngle [i - 1]

x = 1
print ("L'écart relatif entre la période propre et la période est inférieur à", x, "%", "tant que l'angle theta zero reste inférieur à", EcartRelatifMax (x), "°")

# Création et écriture dans le fichier

import os
os.chdir ("C:\Informatique")
mon_fichier = open ("Fichier_Source.txt", "w")
for i in range (0, 90, 1) :
    mon_fichier.write (str (ListeAngle [i]))
    mon_fichier.write ("    ")
    mon_fichier.write (str (ListePeriode [i]))
    mon_fichier.write ("    ")
    mon_fichier.write (str (ListeEcartRelatif [i]))
    mon_fichier.write ("\n")
mon_fichier.close ()

   
