### equation du plan au mieux d'un nuage de points mesurés avec pour equation Ax+By+z+D=0
### a partir du calcul des moindres carres
import numpy as np



import os
os.chdir(r'K:\annee 2015 2016\PT\IPT\Exercices_SII\programmes\04_planeite')#avec r devant le path appelé raw string


# Ouvrir le fichier en mode lecture
fichier = open("plan.csv", "r")

# Lire la première ligne : nom des variables
variable = fichier.readline().rstrip('\n\r').split(";")

pointMesure=[]
# lire les lignes une à une
for ligne in fichier:
    # Mettre le bon séparateur décimal (remplace les virgules par des points)
    ligne = ligne.replace(',','.') # Précaution
    # Enlever le retour chariot en fin de ligne
    # Séparer des données repéré par un point virgule    
    donnees = ligne.rstrip('\n\r').split(";")
    # Créer de la liste des points    
    pointMesure.append([float(donnees[0]),float(donnees[1]),float(donnees[2])])
    
fichier.close()

def vecteurP(pointMesure):
### création de 3 listes des x, y et z
    X,Y,Z=[],[],[]
    for point in pointMesure:
        X.append(point[0])
        Y.append(point[1])
        Z.append(point[2])
        
### plan des moindres carres # ei=zi-z=zi+Axi+Byi+D
    Sziyi,Syi,Syi2,Sxiyi,Sxizi,Sxi,Sxi2,Szi=0,0,0,0,0,0,0,0
    for i in range(len(X)):
        Sziyi=Sziyi+Z[i]*Y[i]
        Syi=Syi+Y[i]
        Syi2=Syi2+Y[i]**2
        Sxiyi=Sxiyi+X[i]*Y[i]
        Sxizi=Sxizi+X[i]*Z[i]
        Sxi=Sxi+X[i]
        Sxi2=Sxi2+X[i]**2
        Szi=Szi+Z[i]
    
    matriceMoindreCarre=np.array([(Sxi2,Sxiyi,Sxi),(Sxiyi,Syi2,Syi),(Sxi,Syi,len(X))])
    vecteurMoindreCarre=np.array([(-Sxizi),(-Sziyi),(-Szi)])
    
### inverser la matriceMoindreCarre et faire le produit avec vecteurMoindreCarre ATTENTION certaines matrices sont non inversibles det(matrice)=0...
    if np.linalg.det(matriceMoindreCarre)!=0:
        matriceInversee=np.linalg.inv(matriceMoindreCarre)
        vecteur_plan=np.dot(matriceInversee,vecteurMoindreCarre)
    else:
        print ('la matrice des moindres carrés n\'est pas inversible')
    return vecteur_plan,vecteurMoindreCarre,matriceMoindreCarre

vecteur=vecteurP(pointMesure)[0]
print ('les paramètres du plan des moindres carrés sont A='+str(vecteur[0])+' B='+str(vecteur[1])+' D='+str(vecteur[2]))

### calcul des ecarts A FAIRE





