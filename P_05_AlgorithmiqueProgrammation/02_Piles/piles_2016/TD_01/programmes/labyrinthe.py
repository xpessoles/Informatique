from numpy.random import randint
import matplotlib.pyplot as plt

def create_labyrinthe(nb_c,nb_l):
    laby=[[[None,False] for j in range(nb_l)] for i in range(nb_c)]
    pile = []
    i, j = randint(nb_c), randint(nb_l)
    pile.append((i,j))
    laby[i][j][1] = True
    while len(pile)!=0:
        i,j=pile.pop()
        v=[]
        if j<nb_l-1 and laby[i][j+1][1]==False:
            v.append("N")
        if i>0 and laby[i-1][j][1]==False:
            v.append("O")
        if j>0 and laby[i][j-1][1]==False:
            v.append("S")
        if i<nb_c-1 and laby[i+1][j][1]==False:
            v.append("E")
        if len(v)>1:
            pile.append((i,j))
        if len(v)>0:
            c=v[randint(len(v))]
            if c == "N":
                laby[i][j][0] = "N"
                laby[i][j+1][0] = "S"
                laby[i][j+1][1] = True
                pile.append((i,j+1))
            elif c == "O":
                laby[i][j][0] = "O"
                laby[i-1][j][0] = "E"
                laby[i-1][j][1] = True
                pile.append((i-1, j))
            elif c == "S":
                laby[i][j][0] = "S"
                laby[i][j-1][0] = "N"
                laby[i][j-1][1] = True
                pile.append((i, j-1))
            else:
                laby[i][j][0] = "E"
                laby[i+1][j][0] = "O"
                laby[i+1][j][1] = True
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
labyr = [[['E', True]], [['O', True]], [['O', True]]]
plt.axis("equal")
show_laby(labyr)
