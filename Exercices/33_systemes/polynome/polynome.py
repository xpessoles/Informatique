from numpy import array,zeros
import numpy as np
import pdb
import matplotlib.pyplot as plt

def cherche_pivot(A, j):
    """Cherche et renvoie un i tel que abs(A[i,j]) est maximal, avec i<=j"""
    n = len(A)
    best = j
    for i in range(j+1, n):
        # Inv : pour tout k <= i, abs(A[best,j]) >= abs(A[k,j])
        if abs(A[i,j]) > abs(A[best,j]):
            best = i
    return best

def echange_lignes(A, i, j):
    """Échange les lignes i et j de la matrice A"""
    A[i,:],A[j,:] = A[j,:].copy(), A[i,:].copy()
    return None

def descente(A,b):
    """Phase de descente de la méthode du pivot pour résoudre Ax = b.
    Préconditions : A et b sont de type array,
    A est inversible,
    b a même nombre de lignes que A.
    Attention: cette fonction modifie A et b."""
    n = len(A)
    for j in range(n-1):
        ip = cherche_pivot(A, j)
        # on met en place la ligne du pivot :
        echange_lignes(A, j, ip)
        echange_lignes(b, j, ip)
        p = A[j, j] # le pivot
        for i in range(j+1, n):
            alpha = - A[i,j] / p # Coefficient multiplicateur
            b[i,:] = b[i,:] + alpha * b[j,:]
            A[i,:] = A[i,:] + alpha * A[j,:]
    return None

def remontee(U,B):
    """Résout le système UX = b.
    Préconditions: U triangulaire supérieure
    b a autant de lignes que U."""
    n, m = B.shape
    X = zeros((n, m))
    for k in range(n):
        i = n-1-k
        # Invariant X[i+1:] est correct
        s = U[i, i+1:].dot(X[i+1:])
        X[i] = (B[i] - s) / U[i, i]
    return X

def resout(A,b):
    """Applique la méthode du pivot pour résoudre Ax = b.
    Renvoie la solution x trouvée.
    Préconditions : A et b sont de type array,
    A est inversible,
    b a même nombre de lignes que A."""
    n = len(A)
    # On copie A et b
    A_, b_ = A.copy(), b.copy()
    descente(A_,b_)
    return remontee(A_,b_)


A=array([[(-1.)**2,-1.,1.],[1.**2,1.,1.],[2.**2,2.,1.]])
b=array([[9.],[3.],[3.]])

X=resout(A,b)

def f(x):
    return X[0]*x**2+X[1]*x+X[2]

vx=np.linspace(-3,3,101)
plt.plot([-1,1,2],[9,3,3],'b*')
plt.plot(vx,f(vx),'r-',label='$y=a\cdot x^2+b\cdot x+c$')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.savefig('polynome.png')




