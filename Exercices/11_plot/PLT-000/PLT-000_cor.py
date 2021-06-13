from random import randrange
import matplotlib.pyplot as plt

def R():
    """Réalisation d'une v.a. de Rademacher"""
    return 2*randrange(2)-1

def marche(n):
    """Une réalisation de [S_0,...,S_n]"""
    S = 0
    les_S = [S]
    for i in range(n):
        S = S + R()
        les_S.append(S)
    return les_S

def excursions(m):
    """Liste des excursions hors de 0 de la marche m"""
    les_e = []
    e = [0]
    for i in range(1,len(m)):
        S = m[i]
        e.append(S)
        if S == 0:
            les_e.append(e)
            e = [0]
    return les_e

def trace_marche(m,nom_de_fichier):
    """Trace la marche m = [S_0,...,S_n] dans nom_de_fichier"""
    plt.clf()
    n = len(m)
    plt.plot(list(range(n)),m,label='$S_n$')
    plt.xlabel('$n$')
    plt.title("Tracé de l'évolution de la marche $S$")
    plt.legend(loc=0)
    plt.savefig(nom_de_fichier)

def trace_excursions(les_e,nom_de_fichier):
    """Trace les excursions écrites dans les_e dans nom_de_fichier"""
    plt.clf()
    i = 0
    for e in les_e:
        i = i+1
        n = len(e)
        plt.plot(list(range(n)),e,label="Excursion no$"+str(i)+"$")
    plt.title("Tracé des excursions hors de zéro de la marche $S$")
    plt.legend(loc=0)
    plt.savefig(nom_de_fichier)    

