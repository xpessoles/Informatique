def generer_liste_pairs_corrige(nb:int):
    res=[]
    for i in range(nb//2+1):
        res.append(2*i)
    return(res)

def generer_liste_impairs_corrige(nb:int):
    res=[]
    for i in range(nb//2):
        res.append(2*i+1)
    return(res)