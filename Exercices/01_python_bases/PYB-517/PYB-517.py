def mystere(a,b) :
    """Précondition : a,b sont des entiers naturels"""
    k,p = 0,1
    while a % p == 0 :
        k = k+1
        p = p*b
    return k-1
