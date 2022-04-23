# -*- coding: utf-8 -*-

# ==== NE PAS MODIFIER =====
import numpy as np
dim = 100
n=10
# ==== FIN A NE PAS MODIFIER =====

# Question 1
# ############
ques_1 = 3*2   # Modifier le 0 par votre réponse
# 
# # Question 2
# ############
ques_2 = 10*9*8  # Modifier le 0 par votre réponse
# 
# # Question 3
# ############
ques_3 = "" # Donner votre réponse entre les guillemets  (en fonction de n)


# Question 4
############
def distance(p1:list, p2:list) -> float:
    d=((p2[0]-p1[0])**2+(p2[1]-p1[1])**2)**(1/2)  
    return d

def Q4_test():
    """ Fonction de test pour la question 4."""
    A, p1, p2 = [0,0], [2,4], [6,5]
    return (distance(A,p1) > 4.472135) and (distance(p1,p2) < 4.472136)
 
    
# Question 5
############
def distances(pts:list,a:list) -> list:
    """Fonction qui donne le tableau des distances demandé par le DM"""
    tab=[]
    pts.append(a) #plus pratique : mettons le point A à la suite dans la liste des n points
    for i in range(len(pts)): #boucle sur tous les points dans la liste
        d_inter=[] #initialisation d'une liste intermédiaire pour mettre la ligne 1 du tablea demandé
        for j in range(len(pts)): #Re boucle sur tous les points de la liste
            d=distance(pts[i],pts[j])
            d_inter.append(d)
        tab.append(d_inter)
    return tab

def Q5_test():
    """ Fonction de test pour la question 5."""
    A, p1, p2, p3 = [0,0], [2,4], [6,5], [5,1]
    pts = [p1,p2,p3]
    dist = distances(pts, A)
    tab_dist = [[0, 4.123105625617661, 4.242640687119285, 4.47213595499958], [4.123105625617661, 0, 4.123105625617661, 7.810249675906654], [4.242640687119285, 4.123105625617661, 0, 5.0990195135927845], [4.47213595499958, 7.810249675906654, 5.0990195135927845, 0]]
    return np.allclose(np.array(tab_dist),np.array(dist))

# Question 6
############
ques_6 = n*n#= n^2  # c'est un tableau de n par n donc n*n calculs à faire

# Question 7
############
def longueur(chemin:list, tab:list) -> float:
    """Renvoie la longueur du chemin parcouru"""
    l=0 #initialisation de la longueur du chemin
    for i in range(len(chemin)-1):#boucle pour le nombre de distance à calculer (le nombre de points moins 1)
        l=l+tab[chemin[i]][chemin[i+1]]
    return l

def Q7_test():
    """ Fonction de test pour la question 7."""
    chemin = [3,2,1,0]
    tab_dist = [[0, 4.123105625617661, 4.242640687119285, 4.47213595499958], [4.123105625617661, 0, 4.123105625617661, 7.810249675906654], [4.242640687119285, 4.123105625617661, 0, 5.0990195135927845], [4.47213595499958, 7.810249675906654, 5.0990195135927845, 0]]
    d = longueur(chemin, tab_dist)
    return (d > 13.34523076) and (d < 13.34523077)
    

# Question 8
############
def longueur_rec(chemin, tab):
    """Fonction de test pour la question 7."""
    if len(chemin)==1: #Cas de base, s'il ne reste qu'un point dans chemin, pas de distance à calculer
        return 0
    else :
        d=tab[chemin[0]][chemin[1]] #Calcul de la distance entre le premier et le second point de chemin
        chemin.pop(0) #supression du premier élement de chemin
        return d + longueur_rec(chemin,tab)


# Question 9
############
ques_9_pts  = 6 # A compléter
ques_9_pts_parc  = 3 # A compléter
ques_9_pts_parc_liste = "p1,p2,p5" # Chaine de caractères sous la forme "a,p1,p2,p3"


# Question 10
#############
ques_10  = "car c'est le point lui-même'" # A compléter


# Question 11
#############
def indice(i:int, tab:list, dispo:list) -> int:
    """Determine l'index du point le plus proche du point d'index i parmi les points dispo"""
    min=10000000000 #initialisation de min à un valeur très élevée
    ind=0
    for j in range(len(dispo)): #boucle sur j pour tous les i possibles
        if dispo[j]==True and j!=i: #on compare avec une case j seulement si j est différent de i et si la case j est dispo
            d=tab[i][j] #calcul de la distance entre i et j
            if d<min: #test pour savoir si ce chemin est plus court que le précédent plus court
                min=d
                ind=j #pour obtenir l'indice minimal
    return ind

def Q11_test():
    """ Fonction de test pour la question 11."""
    dispo = [False, True, True, False]
    tab_dist = [[0, 4.123105625617661, 4.242640687119285, 4.47213595499958], [4.123105625617661, 0, 4.123105625617661, 7.810249675906654], [4.242640687119285, 4.123105625617661, 0, 5.0990195135927845], [4.47213595499958, 7.810249675906654, 5.0990195135927845, 0]]
    return 1 == indice(0, tab_dist, dispo)
    
# Question 12
#############
def plus_court(tab:list) -> list:
    """renvoie le chemin le plus court à partir du point a"""
    chemin=[len(tab)-1] #pour commencer on met le point A au début de chemin pour commencer la recherche du chemin
    dispo=[]
    
    for i in range(len(tab)-1): #Création de la liste dispo avec que des True
        dispo.append(True)
    dispo.append(False) #Sauf pour la dernier élement qui est le point A donc False
    
    for i in range(len(tab)-1):
        
        meilleur=indice(chemin[-1],tab,dispo) #Recherche du meilleur point à partir du dernier point de chemin
        chemin.append(meilleur) #ajout à chemin de ce point
        dispo[meilleur]=False #Actualisation de la liste dispo : False à ce point
    chemin.pop(0) #on enlève le premier élement de chemin qui permettait de débuter la recherche du chemin qui est le point A
    
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
        liste = [] #initialisation liste des points
        while len(liste) < n: #boucle qui tourne tant qu'il n'y a pas n points dans la liste
            x = randint(-c, c) #abcisse du point prise aléatoirement entre -c et c
            y = randint(-c, c) #ordonnée du point """"
            if [x, y] not in liste: #Ajout du point créé à la liste seulement si il n'y est pas déjà
                liste.append([x, y])
        return liste
    
    depart = (randint(-dim, dim), randint(-dim, dim)) #Création du point A nommé départ
    import matplotlib.pyplot as plt
    pts = points(nbpoints, dim) #Utilisation de la fonction points pour obtenir une liste des points voulues
    x = [u[0] for u in pts] #Création liste comportant les abcisses de chaque point
    y = [u[1] for u in pts] #Création liste comportant les ordonnées de chaque point
    plt.plot(x, y, "x") #affichage des points
    plt.plot(depart[0], depart[1], "+") #Affichage du point de départ
    plt.show()
    
    tableau = distances(pts, depart) #avec la fonction distances, création du tableau
    ch = plus_court(tableau) #Avec la fonction plus_court, obtention du plus court chemin
    
    xliste = [depart[0]] + [pts[k][0] for k in ch] #Création de la liste des abcisses des points par lesquels passe le meilleur chemin
    yliste = [depart[1]] + [pts[k][1] for k in ch] #Création de la liste des ordonnées des points par lesquels passe le meilleur chemin
    plt.plot(x, y, "bo") # affichage des points
    plt.plot(depart[0], depart[1], "rs")
    plt.plot(xliste, yliste,'b') # affichage du chemin
    plt.grid()
    plt.xlim(-dim,dim)
    plt.ylim(-dim,dim)
    plt.axis("equal")
    plt.show()
