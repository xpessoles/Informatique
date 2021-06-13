def pascal(n):
    """Calcule la n-ième ligne du triangle de Pascal"""
    t = [1]
    for m in range(n):
        # Invariant : t = pascal(m)
        nouv = [1]*(m+2)
        for i in range(1,m+1):
            # Invariant : nouv[:i] = pascal(m+1)[:i]
            nouv[i] = t[i-1]+t[i]
        t = nouv.copy()
    return t

def pascal_rapide(n):
    t = [1]*(n+1)
    for m in range(n):
        t[1:m+1] = [t[i-1]+t[i] for i in range(1,m+1)]
    return t
