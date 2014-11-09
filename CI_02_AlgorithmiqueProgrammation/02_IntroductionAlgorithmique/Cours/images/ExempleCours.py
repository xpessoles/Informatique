# Courbe de de Bézier d'ordre 2 - Définition de la fonction
def f(u,x0,x1,x2):
    """ Calcule l'abscisse d'un point d'une courbe de Bézier d'ordre 2
    * Entrées :
      - u (float) : paramètre compris entre 0 et 1
      - x0, x1, x2 (float): abscisses des poles
    * Sorties : 
      - val (float) : abscisse du point appartenant à la courbe
    """
    val = (1-u)**2*x0 + 2*u*(1-u)*x1 + u**2*x2
    return val


#f(1,0,1,2)
#a=f(1,0,1,2)
#print(a)


#print(f(1,0,1,2))


#def factorielle(n):
#    if n==0:
#        return 1
#    else :
#        res = 1
#        if n==1:
#            return res
#        else :
#            res=res*(n)
#            n=n-1
#            return factorielle(n)


# Calcul de factorielle en récursif :
def factorielle_rec(n):
    if n==0:
        return 1
    else :
        res=n*factorielle(n-1)
        return res

    
def factorielle(n):
    if n==0:
        return 1
    else :
        i=1
        res=1
        while i<=n:
            res=res*i
            i+=1
        return res
    


    
def calc_factorielle(n):
    if (type(n)==int) & (n>=0):
        return(factorielle(n))
    else :
        print("Oooops... il faut saisir un nombre entier POSITIF ou nul")


def calc_factorielle2(n):
    try:
        if (type(n)==int) & (n>=0):
            return(factorielle(n))
        else :
            print("Oooops... il faut saisir un nombre entier POSITIF ou nul")
    except TypeError:
        print("Oooops... le type de la variable n'est pas le bon")

    

class MonException(Exception):
    def __init__(self,raison):
        self.raison = raison
     
    def __str__(self):
        return self.raison
 
def calc_factorielle3(n):
    if (type(n)!=int):
        raise MonException("La variable n'est pas un integer.")
    if (type(n)==int) & (n<0):
        raise MonException("La variable est négative!")
    else:
        return factorielle(n)
    
    

def fx(u):
    val = (1-u)**2*x_0 + 2*u*(1-u)*x_1 + u**2*x_2
    return val
    
global x_0,x_1,x_2
x_0,x_1,x_2=0,1,2

#print(calc_factorielle3(3))
#print(calc_factorielle3(-1))
#print(calc_factorielle3("a"))

"""
import numpy as np
import pylab as pl

x0=0;y0=0
x1=10;y1=10
x2=20;y2=0
n=50
x,y=[],[]
for i in range(0,n):
    u=i/(n-1)
    x.append(f(u,x0,x1,x2))
    y.append(f(u,y0,y1,y2))
    
pl.plot(x,y)
pl.axis('equal')
pl.show()
"""

"""
for i in range(0,10,2):
    print(i)
"""

def f(u,x0,x1,x2):
    """
    Retourne la coordonnee d'un point pour une courbe de Bezier d'ordre 2
    """
    val = (1-u)**2*x0 + 2*u*(1-u)*x1 + u**2*x2
    return val

def f(u,x0,x1,x2):
    """
    Retourne la coordonnee d'un point pour une courbe de Bezier d'ordre 2
    Keyword arguments:
    u -- parametre de la courbe parametree (doit etre compris entre 0 et 1)
    x0 -- coordonnee du pole 0 (sur x, y ou z)
    x1 -- coordonnee du pole 1 (sur x, y ou z)
    x2 -- coordonnee du pole 2 (sur x, y ou z)
    """
    val = (1-u)**2*x0 + 2*u*(1-u)*x1 + u**2*x2
    return val
