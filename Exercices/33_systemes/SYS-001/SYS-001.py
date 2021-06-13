from numpy import zeros, array

def produit(P,Q,n):
    """Produit PQ tronqué à l'ordre n"""
    L = [0.]*(n+1)
    for k in range(n+1):
        for i in range(k+1):
            if k-len(Q) < i < len(P) :
                L[k] = L[k] + P[i]*Q[k-i]
    return L

def matrice(P):
    """Matrice du systeme donnant les coefficients du DL de la réciproque de f
       P : coefficients du DL de f"""
    n = len(P)-1
    B = zeros((n,n))
    Q = P.copy()
    for j in range(n):
        for i in range(j,n):
            B[i,j] = Q[i+1]
        Q = produit(P,Q,n)
    return B

def resoutTI(T,Y):
    """Donne X solution de TX = Y, avec T triangulaire inférieure"""
    n,_ = T.shape
    X = zeros((n,1))
    for i in range(n):
        X[i,0] = Y[i,0]
        for j in range(i):
            X[i,0] = X[i,0] - T[i,j]*X[j,0]
        X[i,0] = X[i,0] / T[i,i]
    return X

def DLreciproque(P):
    """Donne le DL de la reciproque de f(x)+o(x n)
       Précondition : f(0)=0"""
    T = matrice(P)
    n = len(P)-1
    Y =zeros((n,1))
    Y[0,0] = 1.
    X = resoutTI(T,Y)
    Q = [0.]*(n+1)
    for i in range(1,n+1):
        Q[i] = X[i-1,0]
    return Q

def DLtan(n):
    """Donne la partie principale du DL de la tangente à l'ordre n"""
    atan = [0.]*(n+1)
    i = -1
    s = -1
    while i+2 <= n :
        i = i+2
        s = -s
        atan[i] = s / i
    return DLreciproque(atan)
