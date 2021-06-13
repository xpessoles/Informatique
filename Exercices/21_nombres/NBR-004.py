from math import ceil,sqrt
def somme_div(a):
    """Somme des diviseurs stricts de a"""
    S = 1
    n = ceil(sqrt(a))
    for k in range(2,n+1):
        if a % k == 0 :
            i = a//k
            if k < i : 
                S = S + k + i
            else :
                S = S + k
    return S

def abondance(n):
    return somme_div(n)-n

def nb_deficients(A,B):
    S = 0
    for i in range(A,B):
        if abondance(i) < 0 :
            S = S + 1
    return S

def somme_div_naif(a):
    """Somme des diviseurs stricts de a"""
    S = 1
    for k in range(2,a):
        if a % k == 0 :
            S = S + k
    return S

def abondance_naif(n):
    return somme_div_naif(n)-n

def nb_deficients_naif(A,B):
    S = 0
    for i in range(A,B):
        if abondance_naif(i) < 0 :
            S = S + 1
    return S
