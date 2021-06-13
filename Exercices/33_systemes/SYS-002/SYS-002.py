from numpy import zeros, array

#Q1
def produit(P,Q,n):
    """Produit PQ tronqué à l'ordre n"""
    L = [0.]*(n+1)
    for k in range(n+1):
        for i in range(k+1):
            if k-len(Q) < i < len(P) :
                L[k] = L[k] + P[i]*Q[k-i]
    return L


