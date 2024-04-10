from capytale.autoeval import ValidateVariables,ValidateFunction,ValidateFunctionPretty,Validate
import random as r

go = Validate()
# Test sur une variable
test_q1 = ValidateVariables({"Q1":(4,6)})


## Q2 : init
def _init(C: int, N: int)-> [(int, int)]:
    return [(c, 1) for c in range(C) for _ in range(N)]

valeurs_q2 = [(x,y) for x in range(4) for y in range(4)]

test_q2 = ValidateFunctionPretty(
    "init",
    valeurs_q2,
    valid_function = _init,
    check_signature = True)

## Q3 : compatibles
def _compatibles(coli: (int, int), colj: (int, int))-> bool:
    return coli[0] == colj[0] or coli[1] == colj[1]

valeurs_q3 = []
for x in range(3) :
    for y in range(3) :
        for z in range(3) :
            for zz in range(3) :
                valeurs_q3.append(((x,y),(z,zz)))

test_q3 = ValidateFunctionPretty(
    "compatibles",
    valeurs_q3,
    valid_function = _compatibles,
    check_signature = True)

## Q4 : jouer coup
def _jouerCoup(config: [(int, int)], i:int, j: int)-> [(int, int)]:
    prochConfig =config.copy() # copie de la configuration actuelle
    col_i = prochConfig.pop(i) # retirer la colonne indexée i
    col_j = prochConfig.pop(j if j <i else j- 1) # retirer la colonne indexée j (en prenant en compte ledécalage d’index si i< j)
    nouvCol =(col_j[0], col_i[1] + col_j[1]) # calculer la nouvelle colonne résultante (j sur i)
    prochConfig.append(nouvCol) # ajouter la nouvelle colonne à prochConfig
    return sorted(prochConfig) # trier et renvoyer
valeurs_q4 = [
    ([(0,1), (1, 2), (2, 1), (2, 2)], 0,2 ),
    ([(0,1), (1, 2), (2, 1), (2, 2)], 2,0)]
test_q4 = ValidateFunctionPretty(
    "jouerCoup",
    valeurs_q4,
    valid_function = _jouerCoup,
    check_signature = True)

## Question 6
def _insertion(L, elt):
    i = len(L)- 1
    L.append(elt)
    while i >= 0 and L[i] > elt:
        L[i + 1] = L[i]
        i-= 1
    L[i + 1] = elt

valeurs_q6 = []

test_q6 = ValidateFunctionPretty(
    "insertion",
    valeurs_q6,
    valid_function = _insertion,
    check_signature = False)

## Question 8
def _configSuivantes(config: [(int, int)])-> [[(int, int)]]:
    FutureConfigs = []
    nCol = len(config)
    for i in range(nCol):
        for j in range(nCol):
            if i != j and _compatibles(config[i], config[j]):
                prochConfig = _jouerCoup(config, i, j)
                if prochConfig not in FutureConfigs:
                    FutureConfigs.append(prochConfig)
    return FutureConfigs

# Liste de configurations initiales
v_q8 = [(x,y) for x in range(5) for y in range(5)]
valeurs_q8 = []
for t in v_q8 :
    x = _init(t[0],t[1])
    if x != []:
        valeurs_q8.append(x)


test_q8 = ValidateFunctionPretty(
    "configSuivantes",
    valeurs_q8,
    valid_function = _configSuivantes,
    check_signature = False)

## Question 10
def _tour(config: [(int, int)], C: int, N: int)-> int:
    nbColonnesInit = C * N
    nbColonnesActu = len(config)
    nbCoupsJoues = nbColonnesInit- nbColonnesActu
    return nbCoupsJoues % 2

v_q10 = [(x,y) for x in range(2,5) for y in range(2,5)]
valeurs_q10 = []
for t in v_q10 :
    x = _init(t[0],t[1])
    if x != []:
        valeurs_q10.append((x,t[0],t[1]))
        c = _configSuivantes(x)
        if c != []:
            valeurs_q10.append((c,t[0],t[1]))

test_q10 = ValidateFunctionPretty(
    "tour",
    valeurs_q10,
    valid_function = _tour,
    check_signature = False)

## Question 11
def _partieAleatoire(C: int, N: int)-> int:
    config = _init(C, N)
    while True:
        next_configs = _configSuivantes(config)
        if not next_configs:
            return (_tour(config, C, N) + 1) % 2
        config = r.choice(next_configs)


valeurs_q11 = [(x,y) for x in range(5) for y in range(5)]


test_q11 = ValidateFunctionPretty(
    "partieAleatoire",
    valeurs_q11,
    valid_function = _partieAleatoire,
    check_signature = False)