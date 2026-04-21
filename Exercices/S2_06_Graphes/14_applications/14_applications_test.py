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

def add_dpt(d:{}, dpt:int, nom:str) -> None :
    d[dpt]=nom

add_dpt(dico_test,23,"Creuse")


aqui_test = {33:[47], 47:[33]}

def add_dpt_d(G:{}, dpt:int, voisins : [int]) -> None :
    # On ajoute les voisins à dpt
    if dpt in G :
        for v in voisins :
            if v not in G[dpt]:
                G[dpt].append(v)
    else :
        G[dpt] = voisins

    # On ajoute les voisons si nécessaires
    for v in voisins :
        if v not in G :
            G[v] = [dpt]
        else :
            print("ici")
            if dpt not in G[v] :
                G[v].append(dpt)


aqui_test = {33:[47], 47:[33]}
add_dpt_d(aqui_test,24,[33,47])

aqui_cor = {33: [47, 24], 47: [33, 24], 24: [33, 47]}

