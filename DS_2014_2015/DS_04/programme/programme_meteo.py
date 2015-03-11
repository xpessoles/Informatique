def mini(t):
    """Calcule le minimum d'un tableau d'entiers ou de flottants."""
    if len(t) == 0:
        return None
    p = t[0]
    for i in range(len(t)):
        if t[i] <= p:
            p = t[i]
    return p

def maxi(t):
    """Calcule le minimum d'un tableau d'entiers ou de flottants."""
    if len(t) == 0:
        return None
    p = t[0]
    for i in range(len(t)):
        if t[i] >= p:
            p = t[i]
    return p


def position_mini(t):
    """Calcule l'indice du minimum d'un tableau d'entiers ou de flottants."""
    if len(t) == 0:
        return None
    p = 0
    for i in range(len(t)):
        if t[i] <= t[p]:
            p = i
    return p

def mini2D(t):
    if len(t)==0:
        return t
    p = t[0][0]
    for i in range(len(t)):
        m = mini(t[i])
        if m<p:
            p=m
    return p
    
def chaine_mini(t):
    if len(t)==0:
        return None
    p = 0
    for i in range(len(t)):
        if t[i][1]<t[p][1]:
            p=i
    return t[p][0]

def majores_par(t,nb):
    cpt = 0
    for i in range(len(t)):
        if t[i]>nb:
            cpt = cpt+1
    return cpt

print(majores_par([12,-5,10,9],10))

print(chaine_mini([['Tokyo',7000],['Paris',6000],['Londres',8000]]))
    
    
print(mini2D([[10,3,15],[5,13,10]]))

#mm = position_mini([6,2,15,2,15])
#print(mm)