def code(b,k):
    """Code le tableau de bits b avec niveau de redondance k
       Préconditions : b tableau de 0 / 1
                       k entier"""
    n = len(b)
    c = [0] * (n*(2*k+1))
    for i in range(n):
        if b[i] == 1 : 
            for j in range(2*k+1) :
                c[i*(2*k+1)+j] = 1
            # On pouvait aussi écrire : 
            # c[i*(2*k+1):(i+1)*(2*k+1)] = [1]*(2*k+1)
    return c

def decode(c,k):
    """Décode le tableau de bits c avec niveau de redondance k
       Préconditions : c tableau de 0 / 1
                       len(c) multiple de 2k+1
                       k entier"""
    m = len(c)
    n = m // (2*k+1)
    b = [0]*n
    for i in range(n):
        v = 0 
        for j in range(2*k+1):
            v = v + c[i*(2*k+1)+j]
        # v : somme des bits dans le ie bloc de c.
        # v > k ssi il y a une majorité de 1 dans ce bloc.
        if v > k : 
            b[i] = 1
    return b
