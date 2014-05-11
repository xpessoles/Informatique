# -*- coding: utf-8 -*-
"""
Created on Fri May  9 21:16:30 2014

@author: Xavier
"""
import numpy

def recherche_pivot(A,i):
    n = len(A) # le nombre de lignes
    j = i # la ligne du maximum provisoire
    for k in range(i+1, n):
        if abs(A[k][i]) > abs(A[j][i]):
            j = k # un nouveau maximum provisoire
    return j
    
def echange_lignes(A,i,j):
    # Li <-->Lj
    A[i][:],A[j][:]=A[j][:],A[i][:]


def transvection_ligne(A, i, j, mu):
    # L_i <- L_i + mu.L_j """
    nc = len(A[0]) # le nombre de colonnes
    for k in range(nc):
        A[i][k] = A[i][k] + mu * A[j][k]

def resolution(AA, BB):
    """Résolution de AA.X=BB; AA doit etre inversible"""
    A, B = AA.copy(), BB.copy()
    n = len(A)
    assert len(A[0]) == n
    # Mise sous forme triangulaire
    for i in range(n):
        print(id(A))
        print(id(AA))
        j = recherche_pivot(A, i)
        if j > i:
            echange_lignes(A, i, j)
            echange_lignes(B, i, j)
        for k in range(i+1, n):
            x = A[k][i] / float(A[i][i])
            transvection_ligne(A, k, i, -x)
            transvection_ligne(B, k, i, -x)
    # Phase de remontée
    X = [0.] * n
    for i in range(n-1, -1, -1):
        X[i] = (B[i][0]-sum(A[i][j]*X[j] for j in range(i+1,n))) / A[i][i]
    return X

#AA = [[1,1,-2,4],[2,2,-3,1],[3,3,-4,-2],[1,2,3,3]]
#BB = [[5],[3],[1],[-1]]

AA = [[-1,-2,-3],[0,-1,-4],[-3,-4,-1]]
BB = [[1],[1],[1]]

def afficheMat(A):
    for i in range(len(A)):
        print(A[i][:])
    print()
        
res1 = resolution(AA,BB)
res2 = numpy.linalg.solve(AA,BB)
print(res1)
print(res2)