### equation du plan APproché d'un nuage de points mesurés avec pour equation ax+by+cz+d=0
### a partir du calcul de la normale et d'un point du plan
import numpy as np

### liste des points de mesure
# pointMesure=[[109.0, 33.0, 0.025], [138.0, 45.0, 0.03], [133.0, 68.0, 0.025], [117.0, 111.0, -0.02], [93.0, 124.0, -0.03], [80.0, 16.6, -0.04], [114.0, 187.0, -0.04], [145.0, 158.0, -0.02], [140.0, 122.0, -0.01], [162.0, 140.0, -0.01], [146.0, 193.0, -0.04], [110.0, 207.0, -0.05], [77.0, 201.0, 0.04], [64.0, 190.0, 0.01], [55.0, 172.0, -0.02], [53.0, 133.0, -0.02], [65.0, 106.0, -0.01], [82.0, 70.0, -0.02]]


### listes de 3 points dans des plans parallèles aux plans du repère machine : le défaut de planéité est bien de 0 mais attention aux matrices de det=0
#pointMesure=[[3,0,2],[3,10,0],[3,0,10]] #plan parallèle au plan (y,z)
#pointMesure=[[3,0,0],[3,10,0],[3,0,10]] #plan parallèle au plan (y,z) dont le det(matriceMoindreCarre)=0
#pointMesure=[[1,10,0],[10,10,0],[0,10,10]] #plan parallèle au plan (x,z)
#pointMesure=[[20,10,5],[0,10,5],[1,-10,5]] #plan parallèle au plan (x,y)
#pointMesure=[[0,0,4],[0,-12,0],[-6,0,0]] #plan 2x+y-3z+12=0

import os
os.chdir(r'F:\annee 2014 2015\PT\python pt\TD5 planeite')#avec r devant le path appelé raw string


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

### fonction planApproche d'argument la liste des points mesurés qui renvoie les 3 points du plan et la normale au plan 
def planApproche(pointMesure):
    """planApproche est l'equation du plan passant par 3 points mesurés non alignés. Ces points sont pris à l'index 0, l'index n/3 et l'index 2n/3"""
    n=len(pointMesure)
    i=0
    norme=0
    while norme==0:
        a=pointMesure[i] #on prend 3 points au hasard dans la liste de points mesures
        b=pointMesure[int(n/3)]
        c=pointMesure[int(2*n/3)]
        ax,ay,az=a[0],a[1],a[2]
        bx,by,bz=b[0],b[1],b[2]
        cx,cy,cz=c[0],c[1],c[2]
        norme=np.sqrt(((ay-cy)*(bz-cz)-(az-cz)*(by-cy))**2+((az-cz)*(bx-cx)-(ax-cx)*(bz-cz))**2+((ax-cx)*(by-cy)-(ay-cy)*(bx-cx))**2)
        i=i+1
    normale=[((ay-cy)*(bz-cz)-(az-cz)*(by-cy))/norme,((az-cz)*(bx-cx)-(ax-cx)*(bz-cz))/norme,((ax-cx)*(by-cy)-(ay-cy)*(bx-cx))/norme]
### équation du plan approché de la forme AM(scalaire)n=0 : nx*(x-ax)+ny*(y-ay)+nz*(z-az)=0
    return (a,b,c,normale)
    
### repère associé au plan approché
ax,ay,az=planApproche(pointMesure)[0][0],planApproche(pointMesure)[0][1],planApproche(pointMesure)[0][2]
bx,by,bz=planApproche(pointMesure)[1][0],planApproche(pointMesure)[1][1],planApproche(pointMesure)[1][2]
cx,cy,cz=planApproche(pointMesure)[2][0],planApproche(pointMesure)[2][1],planApproche(pointMesure)[2][2]
axeXx=(bx-ax)/np.sqrt((bx-ax)**2+(by-ay)**2+(bz-az)**2)
axeXy=(by-ay)/np.sqrt((bx-ax)**2+(by-ay)**2+(bz-az)**2)
axeXz=(bz-az)/np.sqrt((bx-ax)**2+(by-ay)**2+(bz-az)**2)
axeX=[axeXx,axeXy,axeXz]
axeYx=axeXz*planApproche(pointMesure)[3][1]-axeXy*planApproche(pointMesure)[3][2]
axeYy=axeXx*planApproche(pointMesure)[3][2]-axeXz*planApproche(pointMesure)[3][0]
axeYz=axeXy*planApproche(pointMesure)[3][0]-axeXx*planApproche(pointMesure)[3][1]
axeY=[axeYx,axeYy,axeYz]
### Ce repère est constitué du premier point appelé a centre du repère et des 3 axes X, Y et la normale qui est Z
repere=[planApproche(pointMesure)[0],axeX,axeY,planApproche(pointMesure)[3]]

### matrice de passage
matr=np.array([(axeXx,axeYx,planApproche(pointMesure)[3][0]),(axeXy,axeYy,planApproche(pointMesure)[3][1]),(axeXz,axeYz,planApproche(pointMesure)[3][2])])
translation=planApproche(pointMesure)[0]


### mettre les points mesurés dans la nouvelle base. Multiplier deux matrices avec dot(A,B)
nouveauPoint=[]
for point in pointMesure:
    nouveauPoint.append(np.dot(matr,np.array([(point[0]-planApproche(pointMesure)[0][0]),(point[1]-planApproche(pointMesure)[0][1]),(point[2]-planApproche(pointMesure)[0][2])])))

def alpha(nouveauPoint):
### création de 3 listes des x, y et z
    X,Y,Z=[],[],[]
    for point in nouveauPoint:
        X.append(point[0])
        Y.append(point[1])
        Z.append(point[2])
        
### plan des moindres carres
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
    
    matriceMoindreCarre=np.array([(Syi,Syi2,-Sxiyi),(Sxi,Sxiyi,-Sxi2),(len(X),Syi,-Sxi)])
    vecteurMoindreCarre=np.array([(Sziyi),(Sxizi),(Szi)])
    
### inverser la matriceMoindreCarre et faire le produit avec vecteurMoindreCarre ATTENTION certaines matrices sont non inversibles det(matrice)=0...
    if np.linalg.det(matriceMoindreCarre)!=0:
        matriceInversee=np.linalg.inv(matriceMoindreCarre)
        alpha=np.dot(matriceInversee,vecteurMoindreCarre)
    else:
        print ('la matrice des moindres carrés n\'est pas inversible')
    return alpha

alpha=alpha(nouveauPoint)

### calcul des ecarts
def defautPlaneite(alpha,nouveauPoint):
    """alpha est le vecteur alpha,beta,w des petits déplacements. nouveauPoint est la liste des points dont les coordonnées sont définies dans le repère du plan approché"""
    ecart=[]
    for point in nouveauPoint:
        ecart.append(point[2]-(alpha[0]+alpha[1]*point[1]-alpha[2]*point[0]))
    defaut=max(ecart)-min(ecart)
    return defaut
    
print('le défaut de planéité par la méthode des moindres carrés est de ',defautPlaneite(alpha,nouveauPoint),' mm')



# pointMesure=[[109.0, 33.0, 0.025], [138.0, 45.0, 0.03], [133.0, 68.0, 0.025], [117.0, 111.0, -0.02], [93.0, 124.0, -0.03], [80.0, 16.6, -0.04], [114.0, 187.0, -0.04], [145.0, 158.0, -0.02], [140.0, 122.0, -0.01], [162.0, 140.0, -0.01], [146.0, 193.0, -0.04], [110.0, 207.0, -0.05], [77.0, 201.0, 0.04], [64.0, 190.0, 0.01], [55.0, 172.0, -0.02], [53.0, 133.0, -0.02], [65.0, 106.0, -0.01], [82.0, 70.0, -0.02]]
# >>> (executing lines 1 to 95 of "defautPlaneiteVersionTD.py")
# le défaut de planéité par la méthode des moindres carrés est de  0.101888178224  mm

# pointMesure=[[1,0,0],[1,10,0],[4,0,10]]
# >>> (executing lines 1 to 94 of "defautPlaneiteVersionTD.py")
# le défaut de planéité par la méthode des moindres carrés est de  7.9936057773e-15  mm

# pointMesure=[[0,0,4],[0,-12,0],[-6,0,0]] #plan 2x+y-3z+12=0
# >>> (executing lines 1 to 103 of "defautPlaneiteVersionTD.py")
# le défaut de planéité par la méthode des moindres carrés est de  1.42108547152e-14  mm

# plan4
# >>> (executing lines 1 to 125 of "defautPlaneiteVersionTD.py")
# le défaut de planéité par la méthode des moindres carrés est de  0.194332063848  mm

# plan5bis
# >>> (executing lines 1 to 125 of "defautPlaneiteVersionTD.py")
# le défaut de planéité par la méthode des moindres carrés est de  0.269772785128  mm




