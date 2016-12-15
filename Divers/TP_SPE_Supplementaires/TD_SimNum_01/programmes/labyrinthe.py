from numpy.random import randint
import matplotlib.pyplot as plt

def create_labyrinthe(p, q):
    laby = [[[None,False] for j in range(q)] for i in range(p)]
    pile = []
    i, j = randint(p), randint(q)
    pile.append((i, j))
    tab[i][j][1] = True
    while len(pile)!=0:
        i, j = pile.pop()
        v = []
        if j < q-1 and tab[i][j+1][1] == False:
            v.append('N')
        if i > 0 and tab[i-1][j] == False:
            v.append('O')
        if j > 0 and tab[i][j-1] == False:
            v.append('S')
        if i < p-1 and tab[i+1][j] == False:
            v.append('E')
        if len(v) > 1:
            pile.append((i, j))
        if len(v) > 0:
            c = v[randint(len(v))]
            if c == 'N':
                tab[i][j][0] = "N"
                tab[i][j+1][0] = "S"
                tab[i][j+1][1] = True
                pile.append((i, j+1))
            elif c == 'O':
                tab[i][j][0] = "O"
                tab[i-1][j][0] = "E" 
                tab[i-1][j][1] = True
                pile.append((i-1, j))
            elif c == 'S':
                tab[i][j][0] = "S"
                tab[i][j-1][0] = "N"
                tab[i][j-1][1] = True
                pile.append((i, j-1))
            else:
                tab[i][j][0] = "E"
                tab[i+1][j][0] = "O"
                tab[i+1][j][1] = True
                pile.append((i+1, j))
    return laby
    


def show_laby(laby):
    nb_c = len(laby)
    nb_l = len(laby[0])
    plt.plot([0, 0, nb_c, nb_c, 0], [0, nb_l, nb_l, 0, 0], linewidth=2)
    for i in range(nb_c-1):
        for j in range(nb_l):
            if laby[i][j][0]!="E":
                plt.plot([i+1, i+1], [j, j+1], 'b')
    for j in range(nb_l-1):
        for i in range(nb_c):
            if laby[i][j][0]!="N":
                plt.plot([i, i+1], [j+1, j+1], 'b')
    plt.axis([-1, nb_c+1, -1, nb_c+1])
    plt.show()

#labyr=create_labyrinthe(3,1)
labyr = [[['N', True], ['N', True], ['S', True]],
 [['O', True], ['N', True], ['O', True]],
 [['N', True], ['O', True], ['O', True]]]
plt.axis("equal")
show_laby(labyr)
