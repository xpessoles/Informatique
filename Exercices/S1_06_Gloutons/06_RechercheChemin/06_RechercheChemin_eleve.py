# -*- coding: utf-8 -*-

# ==== NE PAS MODIFIER =====
import numpy as np
n=10
A = [0,0]
p1 = [2,4]
p2 = [6,5]
p3 = [5,1]
pts = [p1,p2,p3]
chemin = [3,2,1,0]
tab_dist = [[0, 4.123105625617661, 4.242640687119285, 4.47213595499958], [4.123105625617661, 0, 4.123105625617661, 7.810249675906654], [4.242640687119285, 4.123105625617661, 0, 5.0990195135927845], [4.47213595499958, 7.810249675906654, 5.0990195135927845, 0]]
# ==== FIN A NE PAS MODIFIER =====

# Question 1
ques_1 = 0  # Modifier le 0 par votre réponse

# Question 2
ques_2 = 0  # Modifier le 0 par votre réponse (en fonction de n)

# Question 3
ques_3 = "" # Donner votre réponse entre les guillemets


# Question 4
def distance(p1:list, p2:list) -> float:
    # A compléter    
    return 0.

def test_Q4():
    """ Fonction de tester la question 4."""
    return (distance(A,p1) > 4.472135) and (distance(p1,p2) < 4.472136)
 
    
# Question 5
def distances(pts, dep):
    # A compléter    
    return []

def test_Q5():
    """ Fonction de tester la question 5."""
    dist = distances(pts, A)
    return np.allclose(np.array(tab_dist),np.array(dist))


# Question 6
ques_2 = 0  # Modifier le 0 par votre réponse (en fonction de n)


# Question 7
def longueur(chemin, dist):
    # A compléter    
    return 0.

def test_Q7():
    """ Fonction de tester la question 7."""
    d = longueur(chemin, tab_dist)
    return (d > 13.34523076) and (d < 13.34523077)
    



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

"""
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
"""
