from random import randrange

def liste_triee(n):
    """Renvoie une liste d'éléments de range(100), de longueur n,
       triée par ordre croissant """
    L = []
    for i in range(n):
        L.append(randrange(100))
    for i in range(1,n):
        # Inv : L[:i] est triée par ordre croissant
        # Idée : on fait redescendre L[i] pour l'insérer au bon endroit
        j = i
        while j >= 1 and L[j] < L[j-1]:
            # On échange L[j-1] et L[j]
            L[j], L[j-1] = L[j-1], L[j]
            j = j-1
    return L
