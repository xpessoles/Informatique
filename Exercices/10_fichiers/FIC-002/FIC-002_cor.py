import matplotlib.pyplot as plt

def somme():
    """Somme des nombres du fichier"""
    with open('nombres.txt') as f:
        t = f.read()
    L = t.split()
    S = 0
    for x in L : 
        S = S + int(x)
    return S

def moyenne():
    """Moyenne des produits des nombres de chaque ligne"""
    with open('nombres.txt') as f:
        L = f.readlines()
    S = 0
    for li in L : 
        n = 1
        li = li.split()
        for x in li : 
            n = n * int(x)
        S = S + n
    return S / len(L)

def inversion():
    """Nombre d'inversions dans la somme des nombres de chaque ligne"""
    with open('nombres.txt') as f:
        L = f.readlines()
    T = []
    for li in L : 
        # Inv : T contient la somme des lignes de L avant li.
        S = 0
        li = li.split()
        for x in li : 
            # Inv : S contient la somme des éléments de li avant x.
            S = S + int(x)
        # Inv : S contient la somme des éléments de li
        T.append(S)
    # Inv : T contient les sommes des lignes de L. 
    c = 0
    for i in range(len(L)-1):
        # Inv : c = nombre de (k,l) avec k<i et k < l et T[k] > T[l]
        for j in range(i+1,len(L)):
            # Inv : c = nombre de (k,l) avec k<i et k < l et T[k] > T[l]
            #           + nombre de (i,l) avec i<l<j et T[i] > T[l]
            if T[i]>T[j]:
                c = c+1
            # Inv : c = nombre de (k,l) avec k<i et k < l et T[k] > T[l]
            #           + nombre de (i,l) avec i<l<=j et T[i] > T[l]
    # Inv : c = nombre de (k,l) avec k < l et T[k] > T[l]
    return c
