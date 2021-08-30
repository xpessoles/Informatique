### test lecture
def chargeClassement(fichier):
    f=open(fichier,'r')
    les_lignes=f.readlines()
    f.close()
    liste_classement=[]
    for ligne in les_lignes:
        ligne=ligne.split('\t')
        L=[]
        L.append(ligne[1])
        L.append(ligne[2])
        L.append(ligne[4])
        liste_classement.append(L)
    return liste_classement