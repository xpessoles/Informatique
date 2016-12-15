### equation du plan Approché d'un nuage de points mesurés avec pour equation ax+by+cz+d=0
### a partir du calcul de la normale et d'un point du plan
import numpy as np


# *****************
# ** Question 1 **
# *****************
### Création de la liste des coordonnées des points palpés - vous nommerez cette liste "pointMesure"








# *****************
# ** Question 2 ** ANALYSE DU PROGRAMME
# *****************

# *****************
# ** Question 3 ** MODIFICATION DE LA FONCTION planApproche
# *****************
### fonction planApproche d'argument la liste des points mesurés qui renvoie les 3 points du plan et la normale au plan
def planApproche(pointMesure):
    """planApproche est l'equation du plan passant par 3 points mesurés non alignés. Ces points sont pris à l'index 0, l'index n/3 et l'index 2n/3"""
    n=len(pointMesure)
    a=pointMesure[0]
    b=pointMesure[int(n/3)]
    c=pointMesure[int(2*n/3)]
    ax,ay,az=a[0],a[1],a[2]
    bx,by,bz=b[0],b[1],b[2]
    cx,cy,cz=c[0],c[1],c[2]
    norme=np.sqrt(((ay-cy)*(bz-cz)-(az-cz)*(by-cy))**2+((az-cz)*(bx-cx)-(ax-cx)*(bz-cz))**2+((ax-cx)*(by-cy)-(ay-cy)*(bx-cx))**2)
    normale=[((ay-cy)*(bz-cz)-(az-cz)*(by-cy))/norme,((az-cz)*(bx-cx)-(ax-cx)*(bz-cz))/norme,((ax-cx)*(by-cy)-(ay-cy)*(bx-cx))/norme]
    return (a,b,c,normale)
### équation du plan approché de la forme AM(scalaire)n=0 : nx*(x-ax)+ny*(y-ay)+nz*(z-az)=0

# *****************************************
# ** PROGRAMME DE CHANGEMENT DE REPERE   **
# *****************************************
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


# *****************
# ** Question 4 ** CALCUL DES MATRICES UTILES
# *****************

# *****************
# ** Question 5 ** CREATION DE LA MATRICE M
# *****************
### fonction matriceM







# *****************
# ** Question 6 ** CREATION DU VECTEUR V
# *****************
### fonction vecteurV






# *****************
# ** Question 7 ** RESOLUTION DU CALCUL MATRICIEL POUR DETERMINER LE VECTEUR P
# *****************
### fonction vecteurP




# *****************
# ** Question 8 ** DETERMINATION DU DEFAUT DE PLANEITE
# *****************
### fonction defautPlaneite






# *****************
# **  affichage  ** AFFICHER LE RESULTAT DU DEFAUT DE PLANEITE
# *****************

