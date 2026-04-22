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
