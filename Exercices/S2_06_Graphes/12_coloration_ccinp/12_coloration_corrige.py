import random as rd

Gex = {"A":["B","D","F"], "B":["A","C","E"],
        "C":["B","D"], "D":["A","C"],
        "E":["B","F"], "F":["A","E"]}


def voisins(G:{}, s1:str, s2:str) -> bool:
    return s1 in G[s2]

def is_graphe_oriente_01(G:{}) -> bool :
    for s in G :
        for v in G[s] :
            if s not in G[v] :
                print(s,v)
                return False
    return True

def is_graphe_oriente_02(G:{}) -> bool :
    for s in G :
        for v in G[s] :
            if not(voisins(G,s,v)) or not(voisins(G,v,s)):
                return False
    return True


def liste_aretes(G:{}) -> [()] :
    L = []
    for s in G :
        for v in G[s] :
            if ((v,s) not in L) and ((s,v) not in L) :
                L.append((s,v))
    return L

def coloration_valide(G:{}, C:{}) -> bool :
    L = liste_aretes(G)
    for a in L :
        s1,s2 = a
        if C[s1] == C[s2] :
            return False
    return True

C = {'A':0, 'B':1, 'C':0, 'D':1, 'E':0, 'F':1}
C2 = {'A':0, 'B':1, 'C':1, 'D':1, 'E':0, 'F':1}

def init_c(G:{}) -> {} :
    C = {}
    for k in G :
        C[k] = -1
    return C

def colore_sommet(G:{}, C:{}, s:str) -> None :
    voisins = G[s]
    coul = []
    for v in voisins :
        coul.append(C[v])
    # On fait la liste des couleurs absentes
    c_abs = []
    for i in range(0,max(coul)+1) :
        if i not in coul :
            c_abs.append(i)
    #print(c_abs,min(c_abs),s)
    if len(c_abs) == 0 :
        C[s] = max(coul)+1
    else :
        C[s] = min(c_abs)

def colorer1(G):
    C = init_c(G)
    for s in G :
        colore_sommet(G,C,s)
    return C

def colorer2(G,ordre):
    C = init_c(G)
    for s in ordre :
        colore_sommet(G,C,s)
    return C


C3 = {'A':0, 'B':0, 'C':-1, 'D':-1, 'E':-1, 'F':-1}

rd.shuffle(ordre)
ordre = list(Gex.keys())
#colore_sommet(Gex,C3,"C")

cc  = colorer2(Gex,ordre)
