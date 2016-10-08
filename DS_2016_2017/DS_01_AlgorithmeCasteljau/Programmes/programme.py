import numpy as np
import matplotlib.pyplot as plt
import math

global k
def deCasteljau(P, i, j, t):
    """
    Retourne l'abscisse(ou l'ordonnées) d'un point de la courbe de Bézier pour un paramètre donné.
    Entrées : 
     * P (list) : listes des abscisses (ou des ordonnéees) des poles
     * i,j (int) : poles considérés
     * t (float) : paramètre compris entre O et 1
    Sortie : 
     * float : abscisse ou ordonnée d'un point de la courbe 
    """

    if j == 0:
        return P[i]
    else : 
        return deCasteljau(P,i,j-1,t)*(1-t)+deCasteljau(P,i+1,j-1,t)*t

"""
resx = []
resy = []
n=15
x = [i for i in range(n)]
for i in range (n):
    k=0
    deCasteljau(x,0,i,0.5)
    print(i,k)
    resx.append(i)
    resy.append(k)
xx = [i for i in range(n)]
yy = [2*pow(2,i) for i in range(n)]
plt.plot(resx,resy)
plt.plot(xx,yy,"*")

plt.show()
"""

def fact(n):
    """
    Calcul de n! = 1 x 2 x ... x (n-1) x n
    Par convention, 0! = 1
    n doit être un int
    """
    if n==0 :
        return 1
    else : 
        return n*fact(n-1)

def coef_binom(i,n):
    """
    Retourne le coefficient binomial : 
    C_n^i = n! / (i! (n-i)!)
    """
    res = fact(n)/(fact(i)*fact(n-i))
    return res

def calculPointCourbe(poles,u):
    """ 
    Retourne le point de la courbe de Bézier pour un paramètre donné.
    Entrées :
        * poles (list): liste des coordonnées des poles [[x1,y1],[x2,y2],...]
        * u (float) : paramètre appartenant à [0,1]
    Sortie :
        * pointM (list): point appartenant à la courbe de Bézier au paramètre u
    """
    px,py = [],[]
    for i in range(len(poles)):
        px.append(poles[i][0])
        py.append(poles[i][1])
    
    pointM = [fonctionBernstein(px,u),fonctionBernstein(py,u)]
    return pointM
    
def fonctionBernstein(p,u):
    """
    Calcul d'une des coordonnées d'un point appartenant à une courbe de Bézier.
        Entrées :
            * p (list): tableau contenant l'abscisse des poles
            * u (float): paramètre
        Sortie :
            * x (float) : une des coordonnées (suivant x ou y) d'un point de la courbe
    """
    n = len(p)
    x=0
    for i in range(n):
        x=x+coef_binom(i,n-1)*pow(u,i)*pow((1-u),n-i-1)*p[i]
    return x

poles = [[0,0],[0,20],[40,20],[40,0]]
les_u = np.linspace(0,1,100)

les_x_bern = []
les_y_bern = []
for t in les_u:
    pt = calculPointCourbe(poles,t)
    les_x_bern.append(pt[0])
    les_y_bern.append(pt[1])

les_u = np.linspace(0,1,11)
les_x_cast = []
les_y_cast = []

poles_x = [e[0] for e in poles]
poles_y = [e[1] for e in poles]
for t in les_u:
    les_x_cast.append(deCasteljau(poles_x,0,3,t))
    les_y_cast.append(deCasteljau(poles_y,0,3,t))


#plt.plot(les_x_bern,les_y_bern,"b.")
#plt.plot(les_x_cast,les_y_cast,"r*")
#plt.axis('equal')
#plt.show()



#print(deCasteljau(poles_x,0,2,0.5))

def horner(L,t):
    if(len(L))==0:
        return 0
    else : 
        return horner(L[0:len(L)-1],t)*t+L[len(L)-1]
        
print(horner([3,2,1],0.5))
print(deCasteljau([0,0,40,40],0,3,0.5))