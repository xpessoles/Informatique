def mystere(n,p):
    """Précondition : n,p entiers"""
    if p < 0 or p > n : 
        return 0
    else : 
        f = 1
        for i in range(p) : 
            f = f * (n + 1 - p + i) // (i + 1)
        return f
