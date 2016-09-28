import numpy as np
import matplotlib.pyplot as plt

def triangle(A,B,C):
    """
    Entrées :
     * A,B,C : couples de coordonnées des points A B et C
    Sortie : 
     * Rien (plot) 
    """
    X,Y = [],[]
    X.append(A[0])
    X.append(B[0])
    X.append(C[0])
    Y.append(A[1])
    Y.append(B[1])
    Y.append(C[1])
    plt.fill(X,Y,'b')

#triangle((0,0),(1,0),(.5,np.sqrt(3)/2))

def trace(n,A,B,C):
    if n==1:
        triangle(A,B,C)
    else :
        a = (.5*(B[0]+C[0]),.5*(B[1]+C[1]))
        b = (.5*(C[0]+A[0]),.5*(C[1]+A[1]))
        c = (.5*(A[0]+B[0]),.5*(A[1]+B[1]))
        trace(n-1,A,c,b)
        trace(n-1,c,B,a)
        trace(n-1,b,a,C)
        
trace(4,(0,0),(1,0),(.5,np.sqrt(3)/2))
        