def int2list(n):
    """Donne la liste des chiffres de n en base 10"""
    x = n
    L = []
    while x >=10:
        L.append(x%10)
        x = x//10
    L.append(x)
    L.reverse()
    return L

def list2int(L):
    """Donne l'entier décrit en base 10 par la liste de chiffres L"""
    n = 0
    for c in L:
        n = c + 10*n
    return n

def K(n):
    """Kaprekar de n"""
    c = int2list(n)
    d = int2list(n)
    c.sort()
    d.sort(reverse = True)
    return list2int(d)-list2int(c)

def Kaprekar(n):
    x = n
    L = []
    while not (x in L):
        L.append(x)
        x = K(x)
    return L
