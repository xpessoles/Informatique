fichier='premier_ordre.csv'
f=open(fichier)
texte=f.readlines()
temps=[]
V=[]
for k in range(len(texte)):
    ligne=texte[k].split(";")
    temps.append(float(ligne[0]))
    V.append(float(ligne[1]))