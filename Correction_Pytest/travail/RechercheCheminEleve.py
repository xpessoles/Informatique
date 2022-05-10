# -*- coding: utf-8 -*-

# ==== NE PAS MODIFIER =====
import numpy as np
dim = 100
n=10
# ==== FIN A NE PAS MODIFIER =====

# Question 1
############
ques_1 = 6  # Modifier le 0 par votre réponse

# Question 2
############
ques_2 = 3628800  # Modifier le 0 par votre réponse

# Question 3
############
ques_3 = "il y a n! operations, le temps de calcul est donc long vite, càd pour des valers de n petites" # Donner votre réponse entre les guillemets  (en fonction de n)


# Question 4
############
def distance(p1:list, p2:list) -> float:
        
    return # A compléter

def Q4_test():
    """ Fonction de test pour la question 4."""
    A, p1, p2 = [0,0], [2,4], [6,5]
    return (distance(A,p1) > 4.472135) and (distance(p1,p2) < 4.472136)
 
    
# Question 5
############
def distances(pts:list,a:list) -> list:
    dist=[]
    for point in pts:
        dist.append(((point[0]-a[0])**2+(point[1]-a[1])**2)**(1/2))
    return dist

def Q5_test():
    """ Fonction de test pour la question 5."""
    A, p1, p2, p3 = [0,0], [2,4], [6,5], [5,1]
    pts = [p1,p2,p3]
    dist = distances(pts, A)
    tab_dist = [[0, 4.123105625617661, 4.242640687119285, 4.47213595499958], [4.123105625617661, 0, 4.123105625617661, 7.810249675906654], [4.242640687119285, 4.123105625617661, 0, 5.0990195135927845], [4.47213595499958, 7.810249675906654, 5.0990195135927845, 0]]
    return np.allclose(np.array(tab_dist),np.array(dist))

# Question 6
############
ques_6 = (n+1)**2  # Modifier le 0 par votre réponse (en fonction de n)

# Question 7
############
def longueur(chemin:list, tab:list) -> float:
    long=0
    for i in range(len(chemin)-1):
        long+=tab[i][i+1]
    return long

def Q7_test():
    """ Fonction de test pour la question 7."""
    chemin = [3,2,1,0]
    tab_dist = [[0, 4.123105625617661, 4.242640687119285, 4.47213595499958], [4.123105625617661, 0, 4.123105625617661, 7.810249675906654], [4.242640687119285, 4.123105625617661, 0, 5.0990195135927845], [4.47213595499958, 7.810249675906654, 5.0990195135927845, 0]]
    d = longueur(chemin, tab_dist)
    return (d > 13.34523076) and (d < 13.34523077)
    

# Question 8
############
def longueur_rec(chemin, tab):
    
    return 

# Question 9
############
ques_9_pts  = 5
ques_9_pts_parc  = 3
ques_9_pts_parc_liste = "p2,p3,p5" 


# Question 10
#############
ques_10  = "car c'est la case où l'on se trouve, on est en train de la visiter" 


# Question 11
#############
def indice(i:int, tab:list, dispo:list) -> int:
    min=max(tab[i])
    index=0 #change dans tous les cas par l'indice veritable
    for j in range(len(dispo)):
        if j!=i or dispo[j]!=False:
            if tab[i][j]<=min:
                min,index=tab[i][j],j
    dispo[index]=False
    return index

def Q11_test():
    """ Fonction de test pour la question 11."""
    dispo = [False, True, True, False]
    tab_dist = [[0, 4.123105625617661, 4.242640687119285, 4.47213595499958], [4.123105625617661, 0, 4.123105625617661, 7.810249675906654], [4.242640687119285, 4.123105625617661, 0, 5.0990195135927845], [4.47213595499958, 7.810249675906654, 5.0990195135927845, 0]]
    return 1 == indice(0, tab_dist, dispo)
    
# Question 12
#############
def plus_court(tab:list) -> list:
    dispo=[True for i in range(len(tab))]    
    chemin=[len(tab)]
    for i in range(len(tab)-1):
        chemin.append(index(chemin[-1],tab,dispo)
    return chemin

def Q12_test():
    """ Fonction de test pour la question 12."""
    tab_dist = [[0, 4.123105625617661, 4.242640687119285, 4.47213595499958], [4.123105625617661, 0, 4.123105625617661, 7.810249675906654], [4.242640687119285, 4.123105625617661, 0, 5.0990195135927845], [4.47213595499958, 7.810249675906654, 5.0990195135927845, 0]]
    return  plus_court(tab_dist) == [0, 1, 2]



# Question 13
#############

def plot_chemin():
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
    
    xliste = [depart[0]] + [pts[k][0] for k in ch]
    yliste = [depart[1]] + [pts[k][1] for k in ch]
    plt.plot(x, y, "bo") # affichage des points
    plt.plot(depart[0], depart[1], "rs")
    plt.plot(xliste, yliste,'b') # affichage du chemin
    plt.grid()
    plt.xlim(-dim,dim)
    plt.ylim(-dim,dim)
    plt.axis("equal")
    plt.show()
