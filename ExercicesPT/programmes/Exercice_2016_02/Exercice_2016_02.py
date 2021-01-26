import numpy as np

#Q1

def produit(L,C):
    """ Renvoie le produit de la ligne L par la colonne C """
    l = np.array(L)
    c = np.array(C)

    return(np.dot(L,C))
    
L1 = [[1,-1]]
C1 = [[1],[1]]

#print(produit(L1,C1))
#[[0]]

#Q2

def ligne(M,i) :
    """ Renvoie le vecteur de la ligne i de M,
    M sous la forme d'une liste simple"""
    n = len(M)
    j = int(np.sqrt(n))

    return (M[(i-1)*j : i*j])

M = [1,1,1,1,1,0,1,0,0]
#print(ligne(M,2))
#[1, 1, 0]

#Q3

def colonne(M,j) :
    """ Renvoie le vecteur de la colonne j de M,
    M sous la forme d'une liste simple"""
    n = len(M)
    i = int(np.sqrt(n))

    return([M[(a*i)+(j-1)] for a in range(i)])

#print(colonne(M,3))
#[1, 0, 0]

#Q4

def produit_mat(M,N) :
    """ Effectue le produit matriciel de M par N, deux matrices sous forme de liste """
    P =[]
    n = int(np.sqrt(len(M)))

    for i in range(1,n+1):
        for j in range(1,n+1):
            L = ligne(M,i)
            C = colonne(N,j)
            
            P.append(produit(L,C))
    return(P)

N = [1,0,0,0,1,0,0,0,1]

#print(produit_mat(M,N))
#[1, 1, 1, 1, 1, 0, 1, 0, 0]      
