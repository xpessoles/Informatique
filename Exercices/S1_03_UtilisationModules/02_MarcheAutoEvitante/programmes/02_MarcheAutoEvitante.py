import matplotlib.pyplot as plt
import random as rd

def plot_chemin(chemin:[[int]]) -> None :
    les_x = [c[0] for c in chemin]
    les_y = [c[1] for c in chemin]

    plt.axis('equal')
    plt.plot(les_x,les_y,'-or')		# À utiliser où on veut dans le fichier
    plt.grid()
    plt.show()

def positions_voisines(p:[int]) -> [[int,int]] :
    x,y = p
    return [[x,y+1],[x+1,y],[x,y-1],[x-1,y]]

def positions_possibles(p:[int], atteints:[[int]]) -> [[int]] :
    voisins = positions_voisines(p)
    possibles = []
    for v in voisins :
        if v not in atteints :
            possibles.append(v)
    return possibles

def genere_chemin_naif(n:int) -> [[int]] :
    chemin = [[0,0]]
    p = [0,0]
    for i in range(n-1):
        pos = positions_possibles(p,chemin)
        if len(pos) == 0 :
            return [[]]
        else :
            p = rd.choice(pos)
            chemin.append(p)

    return chemin

def plot_proba():
    les_l = []
    les_p = []

    for i in range(351):
        print(i)
        les_l.append(i)
        cpt = 0
        for j in range(1000):
            ch = genere_chemin_naif(i)
            if ch == [[]] :
                cpt = cpt+1
        les_p.append(cpt/1000)

    plt.plot(les_l,les_p)
    plt.grid()
    plt.xlabel('Longueur du chemin')
    plt.ylabel("Probabilité d'échec")
    plt.show()


def est_CAE(chemin:[[int]]) -> bool :
    ch = sorted(chemin)
    for i in range(1,len(ch)) :
        if ch[i] == ch[i-1] :
            return False
    return True

def rot(p:[int], q:[int], a:int) -> [int]:
    dx = q[0]-p[0]
    dy = q[1]-p[1]
    if a == 0 :
        return [p[0]-dx,p[1]-dy]
    elif a == 1 :
        return [p[0]+dy,p[1]+dx]
    else :
        return [p[0]-dy,p[1]-dx]