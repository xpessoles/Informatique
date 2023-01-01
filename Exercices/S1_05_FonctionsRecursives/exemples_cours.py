


def un_rec (n : int) -> float :
    print('Je rentre dans la fonction au rang '+str(n))
    if n == 1 :
        return 1
    else :
        return (un_rec(n-1)+6)/(un_rec(n-1)+2)


def un_rec_v2 (n : int) -> float :
    print('Je rentre dans la fonction au rang '+str(n))
    if n == 1 :
        return 1
    else :
        v = un_rec_v2(n-1)
        return (v+6)/(v+2)


def somme(L:list) -> float :
    print(L)
    if len(L)==1 :
        return L[0]
    else :
        return L[0]+somme(L[1:])

def appartient_dicho_rec(e : int , t : list) -> bool:
    print(t)
    """Renvoie un booléen indiquant si e est dans t. Préconditions : t est un tableau de ↙
    nombres trié par ordre croissant e est un nombre"""
    # Limite gauche de la tranche où l'on recherche e
    g = 0
    # Limite droite de la tranche où l'on recherche e
    d = len(t)-1
    # La tranche où l'on cherche e n'est pas vide
    if len(t)==0:
        return False
    elif len(t)==1 and e!=t[0]:
        return False
    else:
        m = (g+d)//2
        pivot = t[m]
        if e == pivot: # On a trouvé e
            return True
        elif e < pivot:
        # On recherche e dans la partie gauche de la tranche
            d = m-1
            appartient_dicho_rec(e,t[g:d])
        else :
            # On recherche e dans la partie droite de la tranche
            g = m+1
            appartient_dicho_rec(e,t[g:d])

















