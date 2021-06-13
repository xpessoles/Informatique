from numpy import array, zeros

def coeff_prod(V,L,C,X,i) : 
    """ieme coefficient de AX
    V,L,C : représentation CSR de A"""
    S = 0
    for j in range(L[i],L[i+1]):
        S = S + X[C[j]] * V[j]
    return S

def prod(V,L,C,X) : 
    n = len(L)-1
    Y = zeros(n,1)
    for i in range(n) : 
        Y[i] = coeff_prod(V,L,C,X,i)
    return Y

def prod_naif(A,X) : 
    n,p = A.shape
    Y = zeros(n,1)
    for i in range(n) : 
        S = 0
        for j in range(p) : 
            S = S + A[i,j] * X[j]
    return Y

def V_A(n) :
    """Vecteur V de la représentation CSR de A"""
    V = zeros(2*n)
    V[0], V[1], V[2*n-2], V[2*n-1] = -1,1,-1,1
    for i in range(1,n-1):
        V[2*i], V[2*i+1] = -.5,.5
    return V

def L_A(n) :
    """Vecteur L de la représentation CSR de A"""
    L = zeros(n+1)
    for i in range(1,n+1) :
        L[i] = 2*i
    return L

def C_A(n) :
    """Vecteur C de la représentation CSR de A"""
    C = zeros(2*n)
    C[0], C[1], C[2*n-2], C[2*n-1] = 0,1,n-2,n-1
    for i in range(1,n-1):
        C[2*i], C[2*i+1] = i-1,i+1
    return C

def CSR_A(n) :
    """Représentation CSR de A"""
    return V_A(n), L_A(n), C_A(n)
