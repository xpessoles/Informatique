

# ================================
# EXERCICE 1
# ================================

from random import randint
from time import clock


# Création du tableau de nombres aléatoires
tab=[]
nn = 100
for i in range(0,10*nn):
    tab.append(randint(0,nn))
# Méthode un peu plus élégante
tab2 = [randint(0,100*nn) for x in range (100*nn*2)]

    
def moyenne(tab):
    """
    Calcul de la moyenne des valeurs d'un tableau
    """
    somme=0
    for nb in tab:
        somme+=nb
    moyenne=somme/len(tab)
    return moyenne

def variance(tab):
    """
    Calcul de la variance
    """
    moy=moyenne(tab)
    # variance au carré
    variance=0
    for nb in tab:
        variance=variance+(moy-nb)**2
    # Variance
    variance = variance/len(tab)
    return variance

# Vérifications avec Numpy
from numpy import var,average
print("Moyenne calculée : "+str(moyenne(tab))+ "\t Moyenne numpy : "+ str(average(tab)))
print("Variance calculée : "+str(variance(tab))+ "\t Variance numpy : "+ str(var(tab)))

# Temps d'exécution
t0=clock()
moyenne(tab2)
t_moy_prog = clock()-t0

t0=clock()
average(tab)
t_moy_py = clock()-t0

t0=clock()
variance(tab2)
t_var_prog = clock()-t0

t0=clock()
var(tab)
t_var_py = clock()-t0

print("Moyenne : Tps Prog "+str(t_moy_prog)+ "\t Tps py : "+ str(t_moy_py))
print("Variance : Tps Prog "+str(t_var_prog)+ "\t Tps py : "+ str(t_var_py))


# Chercher si un nombre est dans un tableau
nombre_aleat = randint(0,nn)
i=0
while (tab[i]!=nombre_aleat) & (i<=len(tab)):
    i+=1

if(tab[i]==nombre_aleat):
    print(str(nombre_aleat)+" est dans le tableau à la place "+str(i))
else:
    print(str(nombre_aleat)+" n'est pas dans le tableau")

tab.sort()


       
    




"""
##  Lire Un fichier ...
def lire_fichier(fichier):
    fid=open(fichier, "r")
    tab=[]
    for ligne in fid:
        tab.append(fid.readline().rstrip('\n\r'))

    fid.close()
    return tab

tab=lire_fichier("liste_francais.txt")

maxi = 0
for i in range(0,len(tab)):
    if len(tab[i])>maxi:
        maxi=len(tab[i])
print(maxi)
"""

        
    
