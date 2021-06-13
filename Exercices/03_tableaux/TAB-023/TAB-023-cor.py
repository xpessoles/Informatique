def nb_sousleau(T):
    """Nombre de positions sous l'eau dans T
    Préconditions : T tableau de nombres"""
    n = len(T)
    max_deb, max_fin = [0]*n, [0]*n
    max_deb[0] = T[0]
    max_fin[-1] = T[-1]
    for i in range(1,n) :
        # Inv : max_deb[:i] contient les max cumulés de T[:i]
        # Inv : max_fin[n-1-i:] contient les max cumulés de T[n-1-i:]
        max_deb[i] = max(max_deb[i-1],T[i])
        max_fin[n-1-i] = max(max_fin[n-i],T[n-1-i])
    nb = 0
    for i in range(1,n-1) :
        if T[i] < max_deb[i-1] and T[i] < max_fin[i+1] :
            nb = nb+1
    return nb

T = [-1,2,1,0,4,3,5,1]
        
