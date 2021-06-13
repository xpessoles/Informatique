def nb_pyramides_2(t):
    """Nombre de pyramides de hauteur 2 dans t"""
    nb = 0
    for i in range(len(t)-2):
        if t[i+1]>t[i] and t[i+1]>t[i+2] :
            nb = nb+1
    return nb

def pyramide_a_partir(t,i):
    """Hauteur de la pyramide partant de i"""
    n = len(t)
    m = 1
    # On monte :
    while i+m < n and t[i+m-1] < t[i+m] :
        m = m+1
    d = 1
    # On descend :
    while i+m+d-1 < n and t[i+m+d-2] > t[i+m+d-1]:
        d = d+1
    # Il y a une pyramide de longueur min(m,d) en i
    return min(m,d)

def plus_haute_pyramide(t):
    """Plus haute pyramide présente dans t"""
    n = len(t)
    M = 0
    for i in range(n):
        h = pyramide_a_partir(t,i)
        if h > M :
            M = h
    return M

test = [1,2,1,1,3,1,1,2,3,2,1,0,1,2,1,0,1,2,3,4,3,2,1,0,1]

