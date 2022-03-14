# -*- coding: utf-8 -*-
"""
Created on Thu Jan  6 15:55:01 2022

@author: xpess
@author Serge Bays https://mathematice.fr/fichier.php?menu=pcsi&adr=pcsi_tp06a.pdf&vid=6

"""

from math import sqrt

def distance(p1, p2):
    x1, y1 = p1
    x2, y2 = p2
    return sqrt((x1 - x2)**2 + (y1 - y2)**2)

def distances(pts, dep):
    n = len(pts)
    tab = [(n+1)*[0] for i in range(n+1)]
    for i in range(n):
        for j in range(i):
            tab[i][j] = distance(pts[i], pts[j])
            tab[j][i] = tab[i][j]
        tab[n][i] = distance(dep, pts[i])
        tab[i][n] = tab[n][i]
    return tab

def longueur(chemin, dist):
    d = 0
    id_pt = len(dist) - 1
    for point in chemin:
        d = d + dist[id_pt][point]
        id_pt = point
    return d

def indice(position, dist, dispo):
    n = len(dist) - 1
    global dim
    mini = 3 * dim # supérieur à la diagonale du carré
    for i in range(n):
        if dispo[i]:
            d = dist[position][i]
            if d < mini:
                mini = d
                ind = i
    return ind

def plus_court(dist):
    n = len(dist) - 1
    chemin = []
    dispo = n * [True]
    position = n
    while len(chemin) < n:
        position = indice(position, dist, dispo)
        chemin.append(position)
        dispo[position] = False
    return chemin


from random import randint
nbpoints, dim = 20, 20
def points(n, c):
    liste = []
    while len(liste) < n:
        x = randint(-c, c)
        y = randint(-c, c)
        if [x, y] not in liste:
            liste.append([x, y])
    return liste

depart = (randint(-dim, dim), randint(-dim, dim))
import matplotlib.pyplot as plt
pts = points(nbpoints, dim)
x = [u[0] for u in pts]
y = [u[1] for u in pts]
plt.plot(x, y, "x")
plt.plot(depart[0], depart[1], "+")
plt.show()

tableau = distances(pts, depart)
ch = plus_court(tableau)
print(longueur(ch, tableau))
xliste = [depart[0]] + [pts[k][0] for k in ch]
yliste = [depart[1]] + [pts[k][1] for k in ch]
plt.plot(x, y, "bo") # affichage des points
plt.plot(depart[0], depart[1], "rs")
plt.plot(xliste, yliste,"b") # affichage du chemin
plt.grid()
plt.xlim(-dim,dim)
plt.ylim(-dim,dim)
plt.axis("equal")
plt.show()

