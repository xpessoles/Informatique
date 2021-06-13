def comb(n,p):
    """Calcule 'p parmi n'"""
    # On note (n | p) : 'p parmi n'
    q = min(p,n-p) # (n | p) == (n | q)
    c = 1 # c == (n-q | 0)
    for k in range(q):
        # Inv : c == (n-q+k | k)
        c = ((n-q+k+1) * c) // (k+1)
        # Inv : c == (n-q+k+1 | k+1)
    # Au dernier tour de boucle, k = q-1, donc c == (n || q)
    return c
