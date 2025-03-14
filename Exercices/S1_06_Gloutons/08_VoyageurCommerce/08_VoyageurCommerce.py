

dist = [[0 	, 64 , 106, 165, 138, 102],
    [64	, 0  , 155, 146, 186, 121],
    [106, 155, 0  , 270, 105, 94],
    [165, 146, 270, 0  , 300, 263],
    [138, 186, 105, 300, 0  , 208],
    [102, 121, 94 , 263, 208, 0]]


def enleve(L, e) :
    # renvoie une liste correspondant à L sans l'élément e
    L_modif = []
    for elt in L :
        if elt != e :
            L_modif.append(elt)
    return L_modif

def enleve_02(L, e) :
    # renvoie une liste correspondant à L sans l'élément e
    i = L.index (e)
    return L[0: i] + L [i+1:]



def enleve_rec(L, e):
    if len(L) == 0 :  # Si la liste est vide
        return []
    elif L[0] == e:  # Si le premier élément est égal à e
        return enleve_rec(L[1:], e)
    else:  # Sinon, conservez le premier élément
        return [L[0]] + enleve_rec(L[1:], e)


def proche (v_actuelle, v_non_visit) :
    """ renvoie la ville la plus proche de la ville actuelle selon les distance dist et la liste des villes non encore visitées """
    n = len(v_non_visit)        # nombre de villes à visiter
    v_proche = v_non_visit[0]  # premi ère ville à visitée
    d_min = dist [v_actuelle][v_proche] # intialisation de la distance minimale
    for j in range (1, n) :     # pour toutes les autres villes
        d = dist [v_actuelle][v_non_visit[j]] # récupération de la distance
        if d < d_min :          # si on trouve une ville plus proche
            v_proche = v_non_visit[j] # mise à jour de la ville la plus proche
            d_min = d           # mise à jour de la distance minimale.
    return v_proche


def glouton(depart) :
    itineraire = [depart] # initialisation à la ville de départ
    # ville actuelle, initialisation à la ville de départ
    v_actuelle = depart
    villes = [i for i in range(len(dist))]
    v_non_visit = enleve(villes,depart) # on enlève la ville actuelle des villes à visiter
    # Tant qu'il y a des villes à visiter
    while len( v_non_visit ) != 0:
        # recherche de la ville la plus proche des villes à visiter
        v_proche = proche(v_actuelle, v_non_visit)
        # ajout dans l'itinéraire
        itineraire.append (v_proche)

        # on enlève la ville la plus proche des villes à visiter
        v_non_visit = enleve(v_non_visit, v_proche)

        # mise à jour de la ville actuelle par la ville la plus proche
        v_actuelle = v_proche
    # fin de l'itinéraire avec retour à la ville de départ
    itineraire.append(depart)
    return itineraire