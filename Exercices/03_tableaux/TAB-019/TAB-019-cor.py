def plus_haute_ascension(t):
    """Plus haute ascension de t, ou 0 s'il n'y en a pas
    Précondition : t est un tableau de nombres."""
    M = 0
    n = len(t)
    for i in range(n):
        m = 0
        for j in range(i+1,n):
            if t[j] - t[i] > m :
                m = t[j] - t[i]
        if m > M :
            M = m
    return M

def nb_ascensions(t):
    """Nombre d'ascensions du tableau t.
    Préconditions : t est un tableau de nombres."""
    n = len(t)
    nb = 0
    for i in range(n):
        for j in range(i+1,n):
            if t[j] > t[i]:
                nb = nb + 1
    return nb

test = [1,2,1,1,3,1,1,2,3,2,1,0,1,2,1,0,1,2,3,4,3,2,1,0,1]
