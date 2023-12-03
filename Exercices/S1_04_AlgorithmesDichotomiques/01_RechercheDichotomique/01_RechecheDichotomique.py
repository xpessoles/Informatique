def recherche_dichotomie(L:list, x0:int)-> bool:
    n = len(L)
    g = 0 # c'est l'indice de gauche
    d = n - 1 # c'est l'indice de droite
    rep = False
    while g <= d and rep == False :
        # si x0 est dans L alors L[g] <= x0 <= L[d]     {invariant}
        m = (g+d) // 2
        if x0 == L[m]:
            rep = True
        elif x0 < L[m]:
            d= m - 1
        else:
            g = m + 1
            # si x0 est dans L alors L[g] <= x0 <= L[d]     {invariant}
    return(rep)

def zero_dichotomie(f:callable, a:float, b:float, epsilon:float):
    g = a # c'est un flottant
    d = b # c'est un flottant
    while d-g > 2*epsilon :
        m = (g + d) / 2
        if f(g)*f(m) <= 0:
            d = m
        else:
            g = m
    return ((g + d)/2)


def f(x):
    return x*x-2
print(recherche_dichotomie(L,-4))
print(recherche_dichotomie(L,1))
print(recherche_dichotomie(L,5))


print(recherche_dichotomie(L,-3))
print(recherche_dichotomie(L,0))
print(recherche_dichotomie(L,4))