## Question 1
# Corrigé Q1
def add_dpt(d:{}, dpt:int, nom:str) -> None :
    d[dpt]=nom

# Test Q1
def test_q1 () :
    if dico_test == dico_dpt :
        print("Ok pour la Q1")
    else :
        print("Q1 à revoir")

dico_test = {
    19 : "Corrèze",
    64 : "Pyrénées-Atlantiques",
    40 : "Landes",
    33 : "Gironde",
    47 : "Lot-et-Garonne",
    16 : "Charente",
    17 : "Charente-Maritime",
    24 : "Dordogne",
    79 : "Deux-Sèvres",
    86 : "Vienne",
    87 : "Haute-Vienne",
    }
dico_dpt = {
    64 : "Pyrénées-Atlantiques",
    40 : "Landes",
    33 : "Gironde",
    47 : "Lot-et-Garonne",
    16 : "Charente",
    17 : "Charente-Maritime",
    24 : "Dordogne",
    79 : "Deux-Sèvres",
    86 : "Vienne",
    87 : "Haute-Vienne",
    19 : "Corrèze",
    23 : "Creuse"
    }

add_dpt(dico_test,23,"Creuse")
test_q1()
# Fin test Q1


## Question 2
aqui_test = {33:[47], 47:[33]}

## Question 3
def existe_d(G:{}, dpt:int) -> bool :
    return dpt in G

print("Q3 :", existe_d(aqui_test,33))
print("Q3 :", existe_d(aqui_test,64))

## Question 4
def ajoute_dpt_d(G:{}, dpt:int) -> None :
    if not existe_d(G,dpt):
        G[dpt] = []

ajoute_dpt_d(aqui_test,64)
ajoute_dpt_d(aqui_test,40)
print("Q4 :",aqui_test)


## Question 5
def sont_voisins_d(G:{}, dpt1:int, dpt2:int) -> bool :
    assert existe_d(G,dpt1)
    assert existe_d(G,dpt2)
    if dpt1 in G[dpt2] and dpt2 in G[dpt1] :
        return True
    return False

print("Q5 :",sont_voisins_d(aqui_test,33,47))
print("Q5 :",sont_voisins_d(aqui_test,33,64))


## Question 6
def ajoute_une_frontiere_d(G:{}, s1: int, s2: int
) -> None :
    assert not sont_voisins_d(G,s1,s2)
    G[s1].append(s2)
    G[s2].append(s1)

ajoute_une_frontiere_d(aqui_test,64,40)
print("Q6 :",aqui_test)


## Question 7
def ajoute_dpt_voisins_d(G:{}, dpt:int, voisins : [int]) -> None :
    ajoute_dpt_d(G,dpt)
    for v in voisins :
        ajoute_dpt_d(G,v)
        ajoute_une_frontiere_d(G,dpt,v)


ajoute_dpt_voisins_d(aqui_test,24,[16,17,33,47,19,87])
print("Q7 :",aqui_test)


## Question 8
def voisins_d(G:{}, dpt:int) -> [int] :
    assert dpt in G
    return G[dpt]

## Question 9
def suppr_dpt_d(G:{}, dpt:int) -> None :
    G.pop(dpt)
    for k in G :
        voisins = G[k]
        if dpt in voisins :
            voisins.remove(dpt)

suppr_dpt_d(aqui_test,24)
print("Q9 :",aqui_test)

## Question 10
def frontieres_d(G:{}) -> [()] :
    f = []
    for s1 in G :
        voisins = G[s1]
        for s2 in voisins :
            if (s1,s2) not in f and (s2,s1) not in f :
                f.append((s1,s2))
    return f

f = frontieres_d(aqui_test)
print("Q10 :", f)


## Question 11
def degre_d(G:{}, dpt:int) -> int :
    return len(G[dpt])

## Question 12
def degre_max_d(G:{}) -> [int] :
    maxi = -1
    for k in G :
        if len(G[k]) > maxi :
            maxi = len(G[k])
    l = []
    for k in G :
        if len(G[k]) == maxi :
            l.append(k)
    return l

## Question 13
def degre_max_dpt_d(G:{}, d:{}) -> [str] :
    l = degre_max_d(G)
    return [d[i] for i in l]

print(degre_max_dpt_d(aqui_test,dico_dpt))
# #
# # def _add_dpt_d(G:{}, dpt:int, voisins : [int]) -> None :
# #     # On ajoute les voisins à dpt
# #     if dpt in G :
# #         for v in voisins :
# #             if v not in G[dpt]:
# #                 G[dpt].append(v)
# #     else :
# #         G[dpt] = voisins
# #
# #     # On ajoute les voisons si nécessaires
# #     for v in voisins :
# #         if v not in G :
# #             G[v] = [dpt]
# #         else :
# #             print("ici")
# #             if dpt not in G[v] :
# #                 G[v].append(dpt)
# #
# #
# # # aqui_test = {33:[47], 47:[33]}
# # # add_dpt_d(aqui_test,24,[33,47])
# # #
# # # aqui_cor = {33: [47, 24], 47: [33, 24], 24: [33, 47]}
# #
