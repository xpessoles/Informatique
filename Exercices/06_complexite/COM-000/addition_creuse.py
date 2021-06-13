def add(M,N):
    """M+N, représentation classique"""
    n = len(M)
    S = [[0]*n for i in range(n)] # M+N
    for i in range(n):
        # Invariant : S[:i] = (M+N)[:i]
        for j in range(n):
            # Invariant : S[:i+1][:j] = (M+N)[:i+1][:j]
            S[i][j] = M[i][j] + N[i][j]
            # Invariant : S[:i+1][:j+1] = (M+N)[:i+1][:j+1]
        # Invariant : S[:i+1] = (M+N)[:i+1]
    return S

def lexico(X,Y):
    """(a,b) < (c,d) pour l'ordre lexicographique
        avec X = (a,b,x), Y = (a,b,y)"""
    a,b,_ = X
    c,d,_ = Y
    return (a < c) or (a==c and b < d) 

def add_creuse(M,N):
    """M+N, représentation creuse"""
    m,n = len(M), len(N)
    iM, iN = 0,0 # Indices des prochains éléments de M, N à ajouter
    S = [] # M+N
    while (iM < m) or (iN < n):
        # Invariant : M[:iM] et N[:iN] ont été additionnés
        # Variant : m+n-iM-iN
        if (iM == m) or (iN < n and lexico(N[iN],M[iM])):
            S.append(N[iN])
            iN += 1
        elif (iN == n) or lexico(M[iM],N[iN]):
            S.append(M[iM])
            iM += 1
        else:
            if M[iM][2]+N[iN][2] != 0:
                S.append((M[iM][0],M[iM][1],M[iM][2]+N[iN][2]))
            iM +=1
            iN +=1
    return S

M = [(0,0,1),(0,2,2),(1,1,3)]
N = [(0,0,2),(0,2,-2),(1,0,1),(2,2,-1)]
