import matplotlib.pyplot as plt
import random as rd

def plot_chemin(chemin:[[int]]) -> None :
    les_x = [c[0] for c in chemin]
    les_y = [c[1] for c in chemin]

    plt.axis('equal')
    plt.plot(les_x,les_y,'-r')		# À utiliser où on veut dans le fichier
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

# def rot(p:[int], q:[int], a:int) -> [int]:
#     dx = q[0]-p[0]
#     dy = q[1]-p[1]
#     if a == 0 :
#         return [p[0]-dx,p[1]-dy]
#     elif a == 1 :
#         return [p[0]+dy,p[1]+dx]
#     else :
#         return [p[0]-dy,p[1]-dx]

def rot(p,q,a):
    x,y = p
    u,v = q
    assert(a in [0,1,2])
    if a==0:
        return [2*x-u,2*y-v]
    elif a==1:
        return [x+y-v,y+u-x]
    else:
        return [x+v-y,y+x-u]
#
# def rotation_chemin(chemin,i_piv,a):
#     new_chemin = chemin[:i_piv]
#     p = chemin[i_piv]
#     for i in range(i_piv+1,len(chemin)):
#         new_chemin.append(rot(p,chemin[i],a))
#     return new_chemin

def rotation(chemin,i_piv,a):
    chemin_piv=[]
    for i in range(i_piv+1):
        chemin_piv.append(chemin[i])
    p=chemin[i_piv]
    for i in range(i_piv+1,len(chemin)):
        chemin_piv.append(rot(p,chemin[i],a))
    return chemin_piv

#
# def chemin_genere_pivot(n,n_rot):
#     chemin = [[i,0] for i in range(n)]
#
#     for i in range(n_rot):
#         print(i)
#         ae = False
#         while not ae :
#             c = chemin.copy()
#             ipiv = rd.randrange(1,n-1)
#             a = rd.randrange(0,3)
#             print(ipiv)
#             c = rotation_chemin(c,ipiv,a)
#             ae = est_CAE(c)
#         chemin = c
#     return c

def genere_chemin_pivot(n,n_rot):
    chemin = [[i,0] for i in range(n+1)] # intialisation donnée dans l'énoncé
    for i in range(n_rot):
        bloque = True
        while bloque: # tant que l'on génère un chemin qui bloque
            i_piv = rd.randrange(1,n)
            a = rd.randrange(0,3)
            chemin_piv = rotation(chemin,i_piv,a) # nouveau chemin potentiel
            if est_CAE(chemin_piv): # le nouveau chemin est un CAE
                chemin = chemin_piv # mise à jour du chemin
                bloque = False # on sort de la boucle while
    return chemin

c = genere_chemin_pivot(300,2000)
plot_chemin(c)