from PLT_000 import *

def ecrit_marche(m,nom_de_fichier):
    """Écrit une réalisation de m = [S0,...,Sn] dans nom_de_fichier"""
    with open(nom_de_fichier,'w') as f:
        for x in m:
            f.write(str(x)+' ')
    return None

def ecrit_excursions(les_e,nom_de_fichier):
    """Écrit les excursions écrites dans les_e dans nom_de_fichier"""
    with open(nom_de_fichier,'w') as f:
        for e in les_e:
            for x in e:
                f.write(str(x)+' ')
            f.write('\n')
    return None

if __name__ == '__main__':
    m = marche(500)
    ecrit_marche(m,'marche.txt')
    les_e = excursions(m)
    ecrit_excursions(les_e,'excursions.txt')
    trace_marche(m,'d02m-nom-marche.png')
    trace_excursions(les_e,'d02m-nom-excursions.png')
