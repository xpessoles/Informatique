from capytale.autoeval import ValidateVariables,ValidateFunction,ValidateFunctionPretty,Validate
import random as r

## Question 1 ##
def _creer_graphe(p:int, n:int) -> dict:
    # n : lignes
    # p : colonnes
    G = {}
    sommets = []
    for i in range(n):
        for j in range(p):
            sommets.append((j,i))

    for sommet in sommets :
        (i,j) = sommet
        voisins = [(i+1,j),(i,j+1),(i-1,j),(i,j-1)]
        # On vérifie que les voisins sont dans les sommets
        vv = []
        for v in voisins :
            if v in sommets :
                vv.append(v)
        G[sommet]=vv
    return G

valeurs_q1 = [(x,y) for x in range(4) for y in range(4)]

test_q1 = ValidateFunctionPretty(
    "creer_graphe",
    valeurs_q1,
    valid_function = _creer_graphe)


## Question 2 ##
def _get_sommets(G:{}) -> ([],[]):
    les_x,les_y = [],[]
    for sommet in G.keys() :
        les_x.append(sommet[0])
        les_y.append(sommet[1])
    return les_x,les_y

valeurs_q2 = [_creer_graphe(x,y) for x in range(4) for y in range(4)]

test_q2 = ValidateFunctionPretty(
    "get_sommets",
    valeurs_q2,
    valid_function = _get_sommets)


def _trace_sommets(G:{}) :
    # On trace les sommets
    les_x,les_y = [],[]
    for sommet in G.keys() :
        les_x.append(sommet[0])
        les_y.append(sommet[1])
    plt.plot(les_x,les_y,".",color="royalblue")

    plt.grid()
    plt.axis("equal")
    plt.show()

## QUESTION 4 ##
def _get_aretes(G):
    edges = []
    for sommet,voisins in G.items():
        for v in voisins :
            edge = (sommet,v)
            if (sommet,v) not in edges :
                if (v,sommet) not in edges :
                    edges.append(edge)
    return edges


valeurs_q4 = [_creer_graphe(x,y) for x in range(4) for y in range(4)]

test_q4 = ValidateFunctionPretty(
    "get_aretes",
    valeurs_q4,
    valid_function = _get_aretes)


def _tracer_graphe(G) :
    # On trace les arrêtes
    edges = _get_aretes(G)
    for edge in edges :
        x = [edge[0][0],edge[1][0]]
        y = [edge[0][1],edge[1][1]]
        plt.plot(x,y,'lightcoral')

    # On trace les sommets
    les_x,les_y = [],[]
    for sommet in G.keys() :
        les_x.append(sommet[0])
        les_y.append(sommet[1])
    plt.plot(les_x,les_y,".",color="royalblue")

    plt.grid()
    plt.axis("equal")
    plt.show()