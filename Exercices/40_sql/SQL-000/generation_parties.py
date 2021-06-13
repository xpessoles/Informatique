from random import shuffle

def gagne(t,j):
    """Teste si le joueur j gagne dans le tableau t"""
    for i in range(3):
        if j == t[1+3*i] == t[2+3*i] == t[3+3*i]:
            # Ligne 1+i
            return True
    for i in range(3):
        if j == t[1+i] == t[4+i] == t[7+i]:
            # Colonne 1+i
            return True
    if j == t[1] == t[5] == t[9]:
        # Diagonale
        return True
    if j == t[3] == t[5] == t[7]:
        # Antidiagonale
        return True
    return False

def genere_partie_rand():
    """Génère une partie aléatoire et indique quel est le gagnant
    0 = match nul"""
    coups = [1,2,3,4,5,6,7,8,9]
    shuffle(coups)
    p = 0
    t = [0]*10
    for i,c in enumerate(coups):
        j = (i%2) + 1 # numéro du joueur
        t[c] = j
        p = 10*p+c
        if gagne(t,j):
            return p,j
    return p,0

def genere_parties(joueur,nb=1000):
    """Génère nb parties différentes gagnées par joueur
    0 = match nul"""
    L = []
    while len(L)<nb:
        p,j = genere_partie_rand()
        if j == joueur and (p not in L):
            L.append(p)
    return L

def ecrit_csv_parties(j,nb=3000):
    """Écrit dans csv nb parties gagnées par j
    0 = match nul"""
    L = genere_parties(j,nb)
    with open("parties"+str(j)+".csv",'w') as f:
        for p in L:
            f.write(str(p)+'\n')
    return None
