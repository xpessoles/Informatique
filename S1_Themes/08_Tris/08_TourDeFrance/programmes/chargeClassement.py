def chargeClassement(fichier):
    f=open(fichier,'r')
    fichier=f.readlines()
    f.close() #ne pas oublier de fermer le fichier...
    L=[]
    for ligne in fichier:
        ligne=ligne.split('\t') # coupe aux tabulations
        L1=[]
        L1.append(ligne[1])
        L1.append(ligne[2])
        L1.append(ligne[4])
        L.append(L1)
    return L