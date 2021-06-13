def add_creuse (M,N) :
    """M+N, représentation creuse"""
    S=[]
    lM = len(M)
    lN = len(N)
    n = 0
    m = 0
    while n < lN :
        # invariant : S contient tous les termes de M+N de coordonnées
        # inférieures (ordre lexicographique) à celles du dernier
        # élément de N[:n]
        # variant : lN-n
        pN = N[n][:2]
        while m < lM and M[m][:2] < pN :
        # invariant : S contient tous les termes de M+N de coordonnées
        # strictement inférieures à celles de N[n] et N[m]
        # variants : lM-m et pN-M[m][:2]
            S.append(M[m])
            m += 1
        pM = M[m][:2]
        # S contient tous les éléments de M+N de positions
        # strictement inférieures à pN, on rajoute maintenant
        # celui de position pN

        if pM == pN :
            S.append(pM+(M[m][2] + N[n][2],))
            m += 1
            n += 1
        else :
            S.append(N[n])
            n += 1
            
    S += M[m:] # on rajoute les éléments de M qui restent
    return S
