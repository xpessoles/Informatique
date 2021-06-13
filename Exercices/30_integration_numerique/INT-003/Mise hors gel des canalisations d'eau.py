from math import exp
from math import pi
from math import sqrt

# Paramètres physiques du problème

D = 2.8E-7         # Diffusivité thermique du sol terrestre
To = 278           # Température de la surface du sol terrestre pour t < 0
T1 = 258           # Température de la surface du sol terrestre pour t >= 0
Tf = 273.15      # Température de fusion de l'eau sous la pression de 1,013 bar

# Fonction mathématique à intégrer

f = lambda u : (2 / sqrt (pi)) * exp (- u * u)

# Création de la fonction d'erreur "erf"

def erf (x) :
    a = 0                       # Borne inférieure de l'intégrale
    b = x                       # Borne supérieure de l'intégrale
    N = 500                  # Nombre de trapèzes
    h = (b - a) / N         # Largeur d'un trapèze

    Integrale = 0
    for i in range (1, N + 1, 1) :
        xi = a + i * h
        xi1 = a + (i + 1) * h
        Integrale = Integrale + ((f (xi) + f (xi1)) * h) /2
    return Integrale

# Création de la liste "ListeErreur"

ListeErreur = list ()

for i in range (0, 41, 1) :
    x = 0 + i * 0.05
    ListeErreur.append (erf (x))
    # print (round (x, 2), "    ", round (ListeErreur [i], 4))

# Création de la fonction "Temperature"

def Temperature (z, t) :
    u = z / (2 * sqrt (D * t))
    T = T1 + (To - T1) * erf (u)
    return T

# Recherche de la profondeur à laquelle la canalisation doit être enterrée

z = 0
t = 864000         # 864 000 = 10 * 24 * 3600 secondes = 10 jours
T = Temperature (z, t)
while T < Tf :
    z = z + 0.01     # 0.01 m = 1 cm : précision de la recherche
    T = Temperature (z, t)

print ("La canalisation doit être enterrée à une profondeur minimale de", int (z * 100), "cm")
