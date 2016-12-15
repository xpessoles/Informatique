### TD01 le tri
### algorithme de tri

from tris_PT import *
import random as rd
import time #time.perf_counter
import matplotlib.pyplot as plt

import sys
sys.setrecursionlimit(1000000)

### exercice 1 - cout temporel des algorithmes de tris
L_insert=[]
L_rapide=[]
L_fusion=[]
L_sort=[]
# 
# # pour des listes allant jusqu'à 1000 éléments mon ordi met 1 minute à faire tous les tris - image illisible
# # pour les listes allant jusqu'à 10000 éléments avec des sauts de 500 éléments mon ordi met 1 minute à faire tous les calculs
# 
# # de 0 à 20000 sauf pour le tri insertion
# 
# 
# # on ne voit rien sur les courbes pour les petites tailles de liste
L=[i for i in range(0,20001,2000)]
for i in L:
    L1=[]#création de la liste de n éléments au hasard
    for j in range(i):
        L1.append(rd.randint(0,i))
    L_i=L1[:]
    L_f=L1[:]
    L_q=L1[:]
#     td=time.perf_counter()
#     tri_insertion(L_i) #attention L1 est triée
#     tf=time.perf_counter()-td
#     L_insert.append(tf)
    td=time.perf_counter()
    tri_fus(L_f)
    tf=time.perf_counter()-td
    L_fusion.append(tf)
    td=time.perf_counter()
    tri_rap(L_q)
    tf=time.perf_counter()-td
    L_rapide.append(tf)
    td=time.perf_counter()
    L1.sort()
    tf=time.perf_counter()-td
    L_sort.append(tf)
#     
#     
plt.figure()
plt.grid()
plt.xlabel('taille de la liste')
plt.ylabel('temps de tri en seconde')
# plt.plot(L,L_insert,label='insertion')
plt.plot(L,L_fusion,label='fusion')
plt.plot(L,L_rapide,label='rapide')
plt.plot(L,L_sort,label='sort')
plt.legend(loc='upper left')
plt.show()


### test sur tri_quicksort pour des listes triées dans le pire des cas
# L_rapide=[i for i in range(0,4001,400)]
# temps=[]
# for j in L_rapide:
#     liste_triee2=[i for i in range(j)]
#     td=time.perf_counter()
#     tri_rap(liste_triee2)
#     tf=time.perf_counter()-td
#     temps.append(tf)
# plt.figure(3)
# plt.grid()
# plt.xlabel('taille de la liste')
# plt.ylabel('temps de tri en seconde')
# plt.title('tri rapide dans le cas d\'une liste triée')
# plt.plot(L_rapide,temps,label='tri_rapide')
# plt.legend(loc='upper left')
# plt.show()

### une liste déjà triée
# liste_triee=[i for i in range(1000000)]
# tinit=time.time()
# tri_insertion(liste_triee) #la version PT est trop complexe en temps
# print ('temps de tri d\'une liste triée par tri_insertion',time.time()-tinit)
# tinit=time.time()
# tri_fus(liste_triee)
# print ('temps de tri d\'une liste triée par tri_fusion',time.time()-tinit)
# tinit=time.time()
# liste_triee.sort()
# print ('temps de tri d\'une liste triée par sort',time.time()-tinit)

# temps de tri d'une liste triée par tri_insertion 0.3382248878479004
# temps de tri d'une liste triée par tri_fusion 16.4103901386261
# temps de tri d'une liste triée par sort 0.025000810623168945

# remarque : le tri rapide fait planter mon programme...



### tri

import time as t
f=open('films_martiniere.csv','r')
ligne1=f.readline()
fichier=f.readlines()
f.close()

# titre, année, réalisateur, box-office
# '"CONTAGION";"2011";"STEVEN SODERBERGH";"1193697"\n'


L=[]
for ligne in fichier:
    ligne=ligne.replace('"','')#enlever les guillemets
    ligne=ligne.split(';')#création d'une liste en coupant au niveau des ;
    ligne[-1]=ligne[-1].rstrip('\n')
    ligne[-1]=int(ligne[-1])#remplacer la chaine de caractères par un entier
    ligne[1]=int(ligne[1])#remplacer la chaine de caractères par un entier
    L.append(ligne)
    
# [['CONTAGION', '2011', 'STEVEN SODERBERGH', '1193697'], ['PIEGEE', '2012', 'STEVEN SODERBERGH', '282322'], ['MAGIC MIKE', '2012', 'STEVEN SODERBERGH', '569230'], ['EFFETS SECONDAIRES', '2013', 'STEVEN SODERBERGH', '991128'], ['MA VIE AVEC LIBERACE', '2013', 'STEVEN SODERBERGH', '496591']]
    
# In [3]: len(L)
# Out[3]: 2024

### tri sens inverse 
def tri_insertion_modifie(tab):
    """ 
    Trie une liste de nombre en utilisant la méthode du tri par insertion.
    En Python, le passage se faisant par référence, il n'est pas indispensable
    de retourner le tableau.
    Keyword arguments:
    Entrées :
        tab -- liste de nombres
    """
    for i in range (1,len(tab)):
        x=tab[i][-1]
        j=i
        while j>0 and tab[j-1][-1]<x:
            tab[j],tab[j-1]=tab[j-1],tab[j]
            j = j-1
        
    return (tab)

# td=t.perf_counter()
# L1=tri_insertion_modifie(L[:])
# t=t.perf_counter()-td

# 0.5764270816090051
# ['INTOUCHABLES', 2011, 'OLIVIER NAKACHE', 35648468],
#  ['INTOUCHABLES', 2011, 'ERIC TOLEDANO', 35648468],
#  ["QU'EST-CE QU'ON A FAIT AU BON DIEU ?",2014,'PHILIPPE DE CHAUVERON',26908059],
#  ['STAR WARS : EPISODE 7, LE REVEIL DE LA FORCE',2015,'JEFFREY ABRAMS',22157106],
#  ['LA FAMILLE BELIER', 2014, 'ERIC LARTIGAU', 16485214],
#  ['LES MINIONS', 2015, 'PIERRE COFFIN', 14288287],

### quicksort modifie inverse
def segmente_modifie(tab,i,j):
    """
    Segmentation d'un tableau par rapport à un pivot.
    Keyword arguments: 
    Entrées :
        tab (list) -- liste de nombres
        i,j (int) -- indices de fin et de début de la segmentation
    Sorties :    
        tab (list) -- liste de nombres avec le pivot à sa place définitive
        k (int) -- indice de la place du pivot
    """
    g =i+1
    d=j
    p=tab[i][-1]
    while g<=d :
        while d>=0 and tab[d][-1]>p:
            d=d-1
        while g<=j and tab[g][-1]<=p:
            g=g+1
        if g<d :
            tab[g],tab[d]=tab[d],tab[g]
            d=d-1
            g=g+1
    k=d
    tab[i],tab[d]=tab[d],tab[i]
    return k
    
def tri_quicksort_modifie(tab,i,j):
    """
    Tri d'une liste par l'utilisation du tri rapide (Quick sort).
    Keyword arguments:
    Entrées :
        tab (list) -- liste de nombres
        i,j (int) -- indices de fin et de début de la zone de tri
    Sorties :    
        tab (list) -- liste de nombres avec le pivot à sa place définitive
    """
    if i<j :
        k = segmente_modifie(tab,i,j)
        tri_quicksort_modifie(tab,i,k-1)
        tri_quicksort_modifie(tab,k+1,j)
        
        
#
