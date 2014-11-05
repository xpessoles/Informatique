# -*- coding: utf-8 -*-
"""
Created on Tue Jul 30 16:52:20 2013

@author: Damien
"""
import pylab as plt
import numpy as np
import time
debut = time.time()

import cProfile, pstats, io
pr = cProfile.Profile()
pr.enable()
#On construit d'abord la liste contenant la position (dans un plan) des pivots. 
#On peut choisir (par exemple) d'utiliser une liste de tuples :
pivots = []
neuds=999
for i in range(neuds):    
    if np.mod(i,2)==0: 
        pivots.append((3*i,0))
    else:
        pivots.append((3*i,3))

N_piv = len(pivots)
#print('treillis à {} pivots (dont 2 pivots de fixation)'.format(N_piv))

# Conversion en tableau NumPy pour bénéficier des facilités du slicing
pivots_arr = np.array(pivots)

#Choix des points d'accroche du treillis :
    
# indice des points d'accroche:
iP_A = 0 # 1er point du treillis
iP_B = 1 # 2ème point

P_A = pivots[iP_A]
P_B = pivots[iP_B]

#On crée ensuite la liste des barres. Ici on choisit une liste de paires contenant les points. 
barres = []
for i in range(neuds-2):    
    barres.append((pivots[i], pivots[i+1]))
    barres.append((pivots[i], pivots[i+2]))

barres.append((pivots[neuds-2], pivots[neuds-1]))

print len(barres)
#Description du chargement des pivots
#Pour décrire une force extérieure (2 composantes) s'appliquant au niveau de chaque liaison, on utilise un tableau NumPy de taille (Npiv,2).
#Créer F_ext, un tableau de zéros de dimension N_piv * 2

F_ext = np.zeros((2,len(pivots)))
F_ext.T # .T signifie "transposée". (Utilisé ici pour l'esthétique)

#Soit une charge de 1,5 tonne au centre du pont (15KN sur y)
F_ext[1,neuds/2]=-15
#En isolant l'ensemble
F_ext[1,0]=7.5
F_ext[1,neuds-1]=7.5

#Vecteur directeur des barres

# Conversion des barres en trableau NumPy
barres_arr = np.array(barres)

#Pour calculer le vecteur directeur, on calcule d'abord P1P2=OP2−OP1. Il faut donc d'abord récupérer OP1 et OP2 pour chaque barre.
#On procède de manière vectorielle :  
barres_OP1 = barres_arr[:,0,:]
barres_OP2 = barres_arr[:,1,:]
barres_P1P2 = barres_OP2 - barres_OP1

#Il faut à présent normaliser les vecteurs P1P2 pour obtenir les vecteurs directeurs u
barre_l = np.sqrt(barres_P1P2[:,0]**2+barres_P1P2[:,1]**2)
barre_l=barre_l.reshape(len(barre_l),1)

barre_dir = barres_P1P2 / barre_l



#Matrice d'incidence : construction
Inc_mat = np.zeros((N_piv, len(barres)), dtype=int)



for j, bar_j in enumerate(barres):
    P1, P2 = bar_j
    # Remarquons la convention de signe:
    i1=pivots.index((P1))
    Inc_mat[i1,j] = -1 # la barre j "quitte" P1
    i2=pivots.index((P2))
    Inc_mat[i2,j] = +1 # la barre j "arrive à" P2


#Construction des matrices A et b
# 1) Matrice A
Ax = Inc_mat*barre_dir[:,0]
Ay = Inc_mat*barre_dir[:,1]

#La superposition (concaténation) des blocs se fait avec np.vstack (il existe np.hstack et np.concatenate)
###A = np.vstack((Ax, Ay))
# Image de la matrice:
# plt.imshow(A, interpolation='nearest')

A= np.zeros((2*N_piv, len(barres)), dtype=float)
A[0::2,::1]=Ax[:,:]
A[1::2,::1]=Ay[:,:]


b= np.zeros((2*N_piv), dtype=float)
b[0::2]=F_ext[0,:]
b[1::2]=F_ext[1,:]
###b= np.concatenate((F_ext[0,:],F_ext[1,:]))

t1 = time.time()
#Résolution du problème
N = A.shape[1]
M = A.shape[0]

for k in range(N):
    # Trouver le pivot
    piv_candidats = A[k:,k]
    k_piv = np.argmax(np.abs(piv_candidats)) + k
    piv = A[k_piv,k]
    if piv == 0:
        raise ValueError('Systeme non inversible')
    
    # échange des lignes k et k_piv:
    A[[k,k_piv], :] = A[[k_piv,k], :]
    # On applique les memes opérations sur le second membre
    b[[k,k_piv], :] = b[[k_piv,k], :]

       
    # Mise à zéro 
    for i in range(k+1,M):
        #On modifie le second membre avant de modifier A        
        b[i] -= b[k]*A[i,k]/A[k,k]        
        A[i,:] -= A[k,:]*A[i,k]/A[k,k]
        

          
t3 = time.time()
#remontée
for k in range(N-1,0,-1):   #-1 pour pas negatif
        for i in range(k):
            b[i] -= b[k]*A[i,k]/A[k,k]        
            A[i,:] -= A[k,:]*A[i,k]/A[k,k]
t4 = time.time()


#fin de la resolution
solution= np.zeros((1,N))

for k in range(N):
    solution[0,k]=b[k]/A[k,k]


fin = time.time()


pr.disable()
#pr.create_stats()
#pr.print_stats()

f = open('x.pstats', 'a')
sortby = 'time'
pstats.Stats(pr, stream=f).strip_dirs().sort_stats(sortby).print_stats()
f.close()

print 'total',fin-debut
print 'mise en donne',t1-debut
print 'utilisation du pivot',t3-t1
print 'remontée',t4-t3
print 'fin de la résolution',fin-t4
b=b.reshape(size(b),1)
residu=b-np.dot(A,solution.T)
print 'residu',residu
print 'residu.max()',residu.max()
