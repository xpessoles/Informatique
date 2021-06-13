## Intersection de deux ensembles de points
## Sujet X-ENS Informatique B 2017

# Définition de quelques constantes et listes de tests
n = 5 # donc entiers de 0 à 31
E1 = [[1, 2], [4, 5], [4, 8]]

E2 = [[1, 4], [4, 6], [4, 8], [5, 12]]

E3 = [[4, 8], [5, 12], [0, 1], [24, 12]]

# Importation de modules
import numpy as np


## Partie I Solution naïve en Python
def membre(p, Q):
    '''version puriste'''
    i, cont = 0, False
    n = len(Q)
    while i < n and not cont :
        if p[0] == Q[i][0]:
            if p[1] == Q[i][1]:
                cont = True
        i += 1
    return(cont)

def membre_bis(p, Q):
    '''version pythonesque'''
    for point in Q:
        if point == p:
            return(True)
        return(False)

def intersection(P, Q):
    LI = []
    p, q = len(P), len(Q)
    if p <= q:
        for i in range(p):
            if membre(P[i], Q):
                LI.append(P[i])
    else :
        for j in range(q):
            if membre(Q[j], P):
                LI.append(Q[j])
    return(LI)

def intersection_bis(P, Q):
    res = []
    for point in P:
        if membre_bis(point, Q):
            res.append(point)
    return(res)

## Partie II Voir fichier bdd avec Sqliteman

## Partie III Codage de Lebesgue

def conv_entier_binaire_rec(n):
    if n == 1:
        return(1)
    else:
        return(str(conv_entier_binaire_rec(n // 2)) + str(n % 2))

def bits_naif(x, k):
    if k > np.log2(x):
        return(0)
    else:
        return(int(conv_entier_binaire_rec(x)[-1 - k]))

def bits(x, k):
    return ((x // pow(2, k)) % 2)

def code(n, p):
    res = []
    for i in range(n - 1, -1, -1):
        res.append(2 * bits(p[0], i) + bits(p[1], i))
    return(res)

## Partie IV Représentation d'un ensemble de points
        
c1, c2, c3, c4, c5 = [3, 1, 1], [0, 0, 0], [0, 1, 2], [1, 0, 1], [2, 3, 3]

def compare_pcodes(n, c1, c2):
    i = 0
    while i < n - 1 and c1[i] == c2[i]:
        i += 1
    if c1[i] < c2[i]:
        res = 1
    elif c1[i] > c2[i]:
        res = -1
    else:
        res = 0
    return(res)
    
S0 = [[0, 0], [0, 1], [0, 2], [0, 3], [2, 2], [3, 0]]

## Partie V Calcul efficace de l'intersection d'ensembles de points

S1 = [[0, 0], [0, 3], [1, 2], [3, 0], [3, 1], [3, 2], [3, 3]]

S2 = [[0, 0, 0], [0, 0, 3], [0, 3, 0], [0, 3, 3], \
[1, 1, 0], [1, 1, 1], [1, 1, 2], [1, 1, 3], \
[1, 2, 0], [1, 2, 1], [1, 2, 2], [1, 2, 3], \
[2, 0, 0], [2, 0, 1], [2, 0, 2], [2, 0, 3], \
[2, 1, 0], [2, 1, 1], [2, 1, 2], [2, 1, 3], \
[2, 2, 0], [2, 2, 1], [2, 2, 2], [2, 2, 3], \
[2, 3, 0], [2, 3, 1], [2, 3, 2], [2, 3, 3], \
[3, 3, 0], [3, 3, 1], [3, 3, 2], [3, 3, 3]]

def ksuffixe(n, k, Q):
    test = True
    for i in range(n - 1, n - 1 - k, -1):
        if Q[i] != 4:
            test = False
    if test :
        return(Q[: n - 1 - k] + [4] * (k + 1))
    else:
        return(Q)

def compare(n, i0, rep, L):
    '''Compare rep éléments consécutifs de L à partir du rang i0.
    L est une liste de codes de Lebesgue en base 4 de Dn x Dn.
    Renvoie True s'ils sont tous égaux, False sinon.'''
    indice, compt = i0, 2
    taille = len(L)
    test = compare_pcodes(n, L[indice], L[indice + 1]) == 0
    while compt < rep and test and indice < taille - 2:
        indice += 1
        compt += 1
        test = compare_pcodes(n, L[indice], L[indice + 1]) == 0
    return(test)
    
def compacte_bloc(n, k, S):
    '''S est une liste de codages Lebesgue triée 
    pour l'ordre lexicographique, et sans répétition.
    k est le rang à tester pour compacter les codages, donc de 1 à n.
    Renvoie la liste de codages compactés au rang k'''
    taille = len(S)
    res = []
    iS = 0    # iS parcourt S
    
    # On applique ksuffixe() à tous les éléments de S au rang précédent
    Smod = [ksuffixe(n, k - 1, si) for si in S]
    # Alors si un bloc de 4 éléments de rang k - 1 existe dans S
    # ils auront le même suffixe
    
    while iS < taille :   # Parcourt de tout S
        if iS < taille - 3 and compare(n, iS, 4, Smod):
            # si il reste plus de 4 éléments dans S
            # et si les 4 éléments suivants forme un même bloc
            res.append(Smod[iS])
            iS += 4
        else:
            res.append(S[iS])
            iS += 1
    return(res)

def compacte(n, S):
    for k in range(n):
        S = compacte_bloc(n, k + 1, S)
        # S en argument ne sera pas modifié car le S de la boucle for
        # est une variable locale de la fonction compacte()
    return(S)

def compare_ccodes(n, P, Q):
    np, nq = len(P), len(Q)
    k, res= 0, 0
    while k < n and P[k] == Q[k] and P[k] != 4:
        # Parcourt des deux codes
        k += 1
    if P[k] < Q[k]:
        if Q[k] == 4:
            # P inclus dans Q
            res = 2
        else:
            # P inférieur à Q
            res = 1
    elif P[k] > Q[k]:
        if P[k] == 4:
            # Q inclus dans P
            res = -2
        else:
            # Q inférieur à P
            res = -1
    else:
        # dernier cas si P et Q ont même préfixe
        res = 0
    return(res)

def intersection2(n, P, Q):
    np, nq = len(P), len(Q)
    LI = [] # initialisation de la liste intersection
    kp, kq = 0, 0   # indices d'exploration des listes P et Q
    
    while kp < np and kq < nq:
        # variant : (np - kp) + (nq - kq)
        test = compare_ccodes(n, P[kp], Q[kq])
        if test == 0:       # P[kp] et Q[kq] égaux
            LI.append(P[kp])    # P[kp]=Q[kq] est dans l'intersection
            kp += 1             # Passage à P[kp + 1]
            kq += 1             # Passage à Q[kq + 1]
        elif test == 1:     # P[kp] < Q[kq]
            kp += 1             # Passage à P[kp + 1]
        elif test == -1:    # Q[kq] < P[kp]
            kq += 1             # Passage à Q[kq + 1]
        elif test == 2:     # P[kp] inclus dans Q[kq]
            LI.append(P[kp])    # P[kp] est dans l'intersection
            kp += 1             # Passage à P[kp + 1]
        elif test == -2:    # Q[kq] inclus dans P[kp]
            LI.append(Q[kq])    # Q[kq] est dans l'intersection
            kq += 1         # Passage à Q[kq + 1]
    return(LI)
                
# Pour test

S3 = [[0, 0, 4], [1, 1, 2], [1, 3, 4], [2, 1, 4], [3, 1, 0], [3, 3, 2]]