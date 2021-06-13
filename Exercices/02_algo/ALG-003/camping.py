# camping

from numpy import array
def camping (t) :
    n = len(t) # nombre de lignes de t
    p = len(t[0]) # nombre de colonnes de t
    # nous allons construire un tableau Tl tel que Tl[i,j]=k, où
    # k est le nombre de zéros consécutifs du tableau t, à partir de t[i,j]
    # et sur la même ligne (si Tl[i,j]=0, c'est que t[i,j]=1, si Tl[i,j]=3,
    # c'est que t[i,j]=t[i,j+1]=t[i,j+2]=0 et t[i,j+3]=1 ou on est
    # en bout de ligne
    # pour cela on parcourt chaque ligne de la droite vers la gauche,
    # et à chaque coeff, on fait 1 + le coeff suivant
    Tl = []
    for i in range(n) :
        Tl.append([0]*p)
    for i in range(n) :
        for j in range(p) :
            if t[i][p-1-j] == 1 :
                Tl[i][p-1-j] = 0
            else :
                if j == 0 : # on est en bout de ligne
                    Tl[i][p-1-j] = 1
                else :
                    Tl[i][p-1-j] = Tl[i][p-j] + 1
    # on fait pareil en colonne
    Tc = []
    for i in range(n) :
        Tc.append([0]*p)
    for j in range(p) :
        for i in range(n) :
            if t[n-1-i][j] == 1 :
                Tc[n-1-i][j] = 0
            else :
                if i == 0 : # on est en bout de colonne
                    Tc[n-1-i][j] = 1
                else :
                    Tc[n-1-i][j] = Tc[n-i][j] + 1

    # et maintenant on compte en diagonale, de bas en haut et de
    # droite à gauche
    Td = []
    for i in range(n) :
        Td.append([0]*p)
    for i in range(n) :
        for j in range(p) :
            if t[n-1-i][p-1-j] == 1 : # pas de zéro dans cette case
                Td[i][j] = 0
            elif i == 0 or j ==0 : # on est en bout de ligne ou de colonne
                Td[n-1-i][p-1-j] = 1
            else : # on rajoute la taille du carré en bas à droite, limité
                # par le nombre de zéros vers la droite et vers le bas
                Td[n-1-i][p-1-j] = min(Tl[n-1-i][p-1-j],Tc[n-1-i][p-1-j],\
                                       1+Td[n-i][p-j])
    # on renvoie le max de Td
    c = Td[0][0]
    for i in range(n) :
        for j in range(p) :
            if Td[i][j] > c :
                c = Td[i][j]
    return c
    
"""
t = array([[0,0,0],[0,0,0],[0,0,1]])

t1 = array([[1,0,0,1,0,0,1],[0,0,0,0,0,0,0],[1,0,0,0,0,0,0],[0,0,0,0,0,0,0],\
      [0,1,0,0,0,0,1],[1,0,0,0,1,0,1]])

t2 = array([[0,0,0,1,1,1,1],[0,0,0,1,1,1,1],[0,0,0,1,1,1,1],[1,1,1,1,1,0,0],\
      [1,1,1,1,1,0,0]])

t3 = array([[1,0,0,1,0,0],[0,0,0,0,0,0],[1,0,0,0,0,0],[0,0,0,0,0,0],\
      [0,1,0,0,0,0],[1,0,0,0,1,0]])
"""
