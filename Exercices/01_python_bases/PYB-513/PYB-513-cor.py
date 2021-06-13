def somme_chiffres1(n):
    """Somme des chiffres de n, écrit en base 10
    Précondition : n entier naturel"""
    s = str(int(n)) # Pour le cas où n est de type float
    somme = 0
    for c in s :
        # somme contient la somme des chiffres de s jusqu'à c, exclu
        somme = somme + int(c)
        # somme contient la somme des chiffres de s jusqu'à c, inclu
    return somme

def somme_chiffres2(n):
    """Somme des chiffres de n, écrit en base 10
    Précondition : n entier naturel"""
    p = n
    somme = 0 
    while p != 0 : 
        # On commence par le dernier chiffre de n
        # p : nombre obtenu en conservant les chiffres non sommés
        somme = somme + p%10
        # p % 10 est le dernier chiffre de p
        # p // 10 est le nombre obtenu en enlevant le dernier chiffre de p
        p = p // 10
    return somme
