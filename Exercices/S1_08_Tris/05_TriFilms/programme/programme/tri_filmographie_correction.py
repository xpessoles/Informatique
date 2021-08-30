### TD01 le tri
### algorithme de tri

from tris import *
import random as rd
import time
import numpy as np
import matplotlib.pyplot as plt
import sys
sys.setrecursionlimit(1000000)

### exercice 1 - cout temporel des algorithmes de tris
# hasardListe
def hasardListe(n):
    L1=[]#création de la liste de n éléments au hasard
    for j in range(n):
        L1.append(rd.randint(0,n))
    return L1
    

ti=time.perf_counter()
L_insert=[]
L_rapide=[]
L_fusion=[]
L_sort=[]
L=[i for i in range(0,1001,20)]
# pour des listes allant jusqu'à 1000 éléments mon ordi met 1 minute à faire tous les tris - image illisible
# pour les listes allant jusqu'à 10000 éléments avec des sauts de 500 éléments mon ordi met 1 minute à faire tous les calculs

# de 0 à 20000 sauf pour le tri insertion


# on ne voit rien sur les courbes pour les petites tailles de liste
n=1001
def comparaison_liste_hasard(n):
    L=[i for i in range(0,n,50)]
    L_insert=[]
    L_rapide=[]
    L_fusion=[]
    L_sort=[]
    for i in L:
        L1=hasardListe(i)
        L_i=L1[:]
        L_f=L1[:]
        L_q=L1[:]
        td=time.perf_counter()
        tri_Insertion(L_i) #attention L1 est triée
        tf=time.perf_counter()-td
        L_insert.append(tf)
        td=time.perf_counter()
        tri_fusion(L_f)
        tf=time.perf_counter()-td
        L_fusion.append(tf)
        td=time.perf_counter()
        tri_quicksort(L_q,0,len(L_q)-1)
        tf=time.perf_counter()-td
        L_rapide.append(tf)
        td=time.perf_counter()
        L1.sort()
        tf=time.perf_counter()-td
        L_sort.append(tf)
    plt.figure()
    plt.grid()
    plt.xlabel('taille de la liste')
    plt.ylabel('temps de tri en seconde')
    plt.plot(L,L_insert,'bo',label='insertion')
    plt.plot(L,L_fusion,'b+',label='fusion')
    plt.plot(L,L_rapide,'b*',label='rapide')
    plt.plot(L,L_sort,label='sort')
    plt.legend(loc='upper left')
    plt.show()
    
# comparaison_liste_hasard(1000)

### test sur tri_quicksort pour des listes triées dans le pire des cas
def comparaison_liste_triee(n=3001):
    L_rapide=[i for i in range(0,n,300)]
    temps=[]
    temps_2=[]
    for j in L_rapide:
        liste_triee2=[i for i in range(j)]
        td=time.perf_counter()
        tri_rapide(liste_triee2)
        tf=time.perf_counter()-td
        temps.append(tf)
        td=time.perf_counter()
        tri_quicksort(liste_triee2,0,len(liste_triee2)-1)
        tf=time.perf_counter()-td
        temps_2.append(tf)
    plt.figure(3)
    plt.grid()
    plt.xlabel('taille de la liste')
    plt.ylabel('temps de tri en seconde')
    plt.title('tri rapide dans le cas d\'une liste triée')
    plt.plot(L_rapide,temps,label='tri_rapide')
    plt.plot(L_rapide,temps_2,label='tri_quicksort')
    plt.legend(loc='upper left')
    plt.show()

### comparaison de tri_rapide avec liste triée et non triée
# tailles=np.arange(0,800,40)
# les_triee=[]
# les_non_triee=[]
# for i in tailles:
#     L=[j for j in range(i)]
#     t1=time.perf_counter()
#     L=tri_rapide(L)
#     t2=time.perf_counter()
#     les_triee.append(t2-t1)
#     L1=hasardListe(i)
#     t1=time.perf_counter()
#     L=tri_rapide(L1)
#     t2=time.perf_counter()
#     les_non_triee.append(t2-t1)
# plt.figure(4)
# plt.grid()
# plt.title('tri rapide')
# plt.plot(tailles,les_triee,label='listes triées')
# plt.plot(tailles,les_non_triee,label='listes non triées')
# plt.legend(loc='upper left')
# plt.show()



### une liste déjà triée
liste_triee=[i for i in range(100000)]
# tinit=time.perf_counter()
# tri_Insertion(liste_triee)
# print ('temps de tri d\'une liste triée par tri_insertion',time.perf_counter()-tinit)
tinit=time.perf_counter()
tri_fusion(liste_triee)
print ('temps de tri d\'une liste triée par tri_fusion',time.perf_counter()-tinit)
# tinit=time.perf_counter()
# tri_quicksort(liste_triee,0,len(liste_triee)-1)
# print ('temps de tri d\'une liste triée par tri_quicksort',time.perf_counter()-tinit)
tinit=time.perf_counter()
liste_triee.sort()
print ('temps de tri d\'une liste triée par sort',time.perf_counter()-tinit)

# pour 10000 éléments
# temps de tri d'une liste triée par tri_insertion 3.8509149223894283
# temps de tri d'une liste triée par tri_fusion 0.047487974890565
# temps de tri d'une liste triée par sort 0.00010635396950675613
# 
# # remarque : le tri rapide fait planter mon programme...


### tri

# import time as t
# f=open('films_martiniere_2018.csv','r')
# ligne1=f.readline()
# fichier=f.readlines()
# f.close()
# 
# # titre, année, réalisateur, box-office
# # '"CONTAGION";"2011";"STEVEN SODERBERGH";"1193697"\n'
# 
# 
# L=[]
# for ligne in fichier:
#     ligne=ligne.replace('"','')#enlever les guillemets
#     ligne=ligne.split(';')#création d'une liste en coupant au niveau des ;
#     ligne[-1]=ligne[-1].rstrip('\n')
#     ligne[-1]=int(ligne[-1])#remplacer la chaine de caractères par un entier
#     ligne[1]=int(ligne[1])#remplacer la chaine de caractères par un entier
#     L.append(ligne)
# print (L[:3])
#     
# # [['CONTAGION', '2011', 'STEVEN SODERBERGH', '1193697'], ['PIEGEE', '2012', 'STEVEN SODERBERGH', '282322'], ['MAGIC MIKE', '2012', 'STEVEN SODERBERGH', '569230'], ['EFFETS SECONDAIRES', '2013', 'STEVEN SODERBERGH', '991128'], ['MA VIE AVEC LIBERACE', '2013', 'STEVEN SODERBERGH', '496591']]
# [['127 HEURES', 2011, 'DANNY BOYLE', 609908], ['17 FILLES', 2011, 'DELPHINE COULIN', 139790], ['17 FILLES', 2011, 'MURIEL COULIN', 139790]]
#     
# # In [3]: len(L)
# # Out[3]: 2024
# 
# ### tri sens inverse 
# def tri_insertion_modifie(tab):
#     """ 
#     Trie une liste de nombre en utilisant la méthode du tri par insertion.
#     En Python, le passage se faisant par référence, il n'est pas indispensable
#     de retourner le tableau.
#     Keyword arguments:
#     Entrées :
#         tab -- liste de nombres
#     """
#     for i in range (1,len(tab)):
#         x=tab[i][-1]
#         j=i
#         while j>0 and tab[j-1][-1]<x:
#             tab[j],tab[j-1]=tab[j-1],tab[j]
#             j = j-1
#         
#     return (tab)
# 
# td=t.perf_counter()
# L1=tri_insertion_modifie(L[:])
# t=t.perf_counter()-td
# print (t)
# # 0.5764270816090051
# # ['INTOUCHABLES', 2011, 'OLIVIER NAKACHE', 35648468],
# #  ['INTOUCHABLES', 2011, 'ERIC TOLEDANO', 35648468],
# #  ["QU'EST-CE QU'ON A FAIT AU BON DIEU ?",2014,'PHILIPPE DE CHAUVERON',26908059],
# #  ['STAR WARS : EPISODE 7, LE REVEIL DE LA FORCE',2015,'JEFFREY ABRAMS',22157106],
# #  ['LA FAMILLE BELIER', 2014, 'ERIC LARTIGAU', 16485214],
# #  ['LES MINIONS', 2015, 'PIERRE COFFIN', 14288287],
# 
# ### quicksort modifie inverse
# def segmente_modifie(tab,i,j):
#     """
#     Segmentation d'un tableau par rapport à un pivot.
#     Keyword arguments: 
#     Entrées :
#         tab (list) -- liste de nombres
#         i,j (int) -- indices de fin et de début de la segmentation
#     Sorties :    
#         tab (list) -- liste de nombres avec le pivot à sa place définitive
#         k (int) -- indice de la place du pivot
#     """
#     g =i+1
#     d=j
#     p=tab[i][-1]
#     while g<=d :
#         while d>=0 and tab[d][-1]>p:
#             d=d-1
#         while g<=j and tab[g][-1]<=p:
#             g=g+1
#         if g<d :
#             tab[g],tab[d]=tab[d],tab[g]
#             d=d-1
#             g=g+1
#     k=d
#     tab[i],tab[d]=tab[d],tab[i]
#     return k
#     
# def tri_quicksort_modifie(tab,i,j):
#     """
#     Tri d'une liste par l'utilisation du tri rapide (Quick sort).
#     Keyword arguments:
#     Entrées :
#         tab (list) -- liste de nombres
#         i,j (int) -- indices de fin et de début de la zone de tri
#     Sorties :    
#         tab (list) -- liste de nombres avec le pivot à sa place définitive
#     """
#     if i<j :
#         k = segmente_modifie(tab,i,j)
#         tri_quicksort_modifie(tab,i,k-1)
#         tri_quicksort_modifie(tab,k+1,j)
#         
        
#
