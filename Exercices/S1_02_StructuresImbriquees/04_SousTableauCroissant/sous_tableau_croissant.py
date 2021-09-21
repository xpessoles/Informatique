def est_croissant(t):
    """Renvoie un booléen indiquant si t est croissant"""
    for i in range(len(t)-1):
        if t[i] > t[i+1]:
            return False
    return True

def plus_un(e):
    """Si e représente p en binaire, le modifie afin que e représente p+1"""
    i = 1
    while i <= len(e) and e[-i] == 1:
        e[-i] = 0
        i = i+1
    if i <= len(e):
        e[-i] = 1
    return None

def longueur(e):
    """Renvoie le nombre de 1 dans e, contenant des 0 et des 1"""
    return sum(e)

def extrait(t,e):
    """Renvoie le sous-tableau de t indiqué par e"""
    n = len(t)
    assert len(e) == n
    v = []
    for i in range(n):
        if e[i]==1:
            v.append(t[i])
            # On extrait le sous-tableau
    return v

def stc_exhaustif(t):
    """Donne la longueur du plus grand sous-tableau croissant de t"""
    if t == []:
        return 0
    n = len(t)
    e = [0]*n
    maxi = 0
    for i in range(2**n):
        plus_un(e)
        v = extrait(t,e)
        if est_croissant(v):
            maxi = max([maxi,longueur(e)])
    return maxi

def stc_dynamique(t):
    """Donne la longueur du plus grand sous-tableau croissant de t"""
    if t == []:
        return 0
    n = len(t)
    m = [1]
    for i in range(n-1):
        # m a été construit jusqu'à l'indice i
        maxi = 1
        for j in range(i+1):
            if t[i+1] >= t[j]:
                maxi = max([maxi,m[j]+1])
        m.append(maxi)
    return max(m)

# Tests
from random import randrange
t = [randrange(100) for i in range(10)]
print(t)
print(stc_exhaustif(t))
print(stc_dynamique(t))
t2 = [randrange(100) for i in range(100)]
print(t2)
print(stc_dynamique(t2))
t3 = [i for i in range(10)]
print(t3)
print(stc_exhaustif(t3))
print(stc_dynamique(t3))
t4 = [10-i for i in range(10)]
print(t4)
print(stc_exhaustif(t4))
print(stc_dynamique(t4))
