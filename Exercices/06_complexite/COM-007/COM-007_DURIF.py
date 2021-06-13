import numpy as np

A=np.array([[1,0,3],[0,0,0],[0,-2,0],[0,0,0]])
V=np.array([1,3,-2])
L=np.array([0,2,2,3,0])
C=np.array([0,2,1])

X=np.array([[1],[2],[3]])

Y1=np.dot(A,X)

i=2
Y=[]
for i in range(len(A)):
    Yi=V[L[i]:L[i+1]].dot(X[C[L[i]:L[i+1]]])
    Y.append(Yi)
#Q4    
def coeff_prod(V,L,C,X,i):
    return V[L[i]:L[i+1]].dot(X[C[L[i]:L[i+1]]])[0]
#Complexité en o(li) avec li le nombre d'éléments non nuls sur la ie ligne de A
    
#Q5
def prod(V,L,C,X):
    n=len(L)-1
    Y=n*[0]
    for i in range(n):
        Y[i]=[coeff_prod(V,L,C,X,i)]
    return np.array(Y)
    
#Complexité en o(s) avec s le nombre d'éléments non nuls de la matrice A

Y2=prod(V,L,C,X)

#Q6
def prod_naif(A,X):
    n,p=np.shape(A)
    Y=[]
    for i in range(n):
        S=0
        for j in range(p):
            S+=A[i,j]*X[j]
        Y.append(S)
    return np.array(Y)
        
Y3=prod_naif(A,X)

#Complexité en o(nxp)
    