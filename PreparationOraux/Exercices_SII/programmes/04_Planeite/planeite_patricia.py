### equation du plan APproché d'un nuage de points mesurés avec pour equation ax+by+cz+d=0
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

### constantes du plan des moindres carrés vecteurP d'argument la liste des points mesurés qui renvoie le vecteurP, le vecteurV et la matriceM




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
        alpha=np.dot(matriceInversee,vecteurMoindreCarre)
    else:
        print ('la matrice des moindres carrés n\'est pas inversible')
    return alpha,vecteurMoindreCarre,matriceMoindreCarre

vecteur=vecteurP(pointMesure)[0]

### calcul des ecarts
def defautPlaneite(vecteur,pointMesure):
    """vecteur est le vecteur A,B,D des moindres carrés. pointMesure est la liste des points dont les coordonnées sont définies dans le repère du plan approché"""
    ecart=[]
    for point in pointMesure:
        ecart.append((vecteur[0]*point[0]+vecteur[1]*point[1]+point[2]+vecteur[2])/np.sqrt(vecteur[0]**2+vecteur[1]**2+1))
    defaut=max(ecart)-min(ecart)
    return defaut
    
print('le défaut de planéité par la méthode des moindres carrés est de ',defautPlaneite(vecteur,pointMesure),' mm')



# >>> (executing lines 1 to 77 of "planeite.py")
# le défaut de planéité par la méthode des moindres carrés est de  0.188383051255  mm




