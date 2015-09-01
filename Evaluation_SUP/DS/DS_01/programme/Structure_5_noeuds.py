# -*- coding: utf-8 -*-
"""
Created on Tue Jul 30 16:52:20 2013

@author: Damien
"""
import pylab as plt
import numpy as np
import time
debut = time.time()
#On construit d'abord la liste contenant la position (dans un plan) des pivots. 
#On peut choisir (par exemple) d'utiliser une liste de tuples :
    
pivots = [(0, 0), (3, 3), (6, 0), (9, 3), (12, 0)]
N_piv = len(pivots)
print('treillis à {} pivots (dont 2 pivots de fixation)'.format(N_piv))

# Conversion en tablea NumPy pour bénéficier des facilités du slicing
pivots_arr = np.array(pivots)

# Tracés en boucle:
for piv in pivots:
    plt.plot(piv[0], piv[1], 'o')
    
# Ajustements des limites :
plt.axis('equal')
plt.xlim(-2., 14)

#plt.show()

#Choix des points d'accroche du treillis :
    
# indice des points d'accroche:
iP_A = 0 # 1er point du treillis
iP_B = 1 # 2ème point

P_A = pivots[iP_A]
P_B = pivots[iP_B]

#On crée ensuite la liste des barres. Ici on choisit une liste de paires contenant les points. 

barres = [
 (pivots[0], pivots[1]), 
 (pivots[0], pivots[2]),
 (pivots[1], pivots[2]),
 (pivots[1], pivots[3]),
 (pivots[2], pivots[3]),
 (pivots[2], pivots[4]),
 (pivots[3], pivots[4])]
 
#Représentation graphique :
   
color=(0.6, 0.6, 0.8)

# Tracé des barres, en boucle :
for j, bj in enumerate(barres):
    # Coordonnées des 2 pivots d'accroche:
    (x1,y1), (x2, y2) = bj
    color = (.5, .5, .8)
    plt.plot((x1, x2), (y1, y2), '-', color = color, lw=4, zorder=1)

# Tracés des pivots :
for piv in pivots:
    plt.plot(piv[0], piv[1], 'ro')

# Ajustements des limites :
plt.axis('equal')
plt.xlim(-2., 14)



plt.savefig('output1.jpg')
#plt.show()

#Description du chargement des pivots
#Pour décrire une force extérieure (2 composantes) s'appliquant au niveau de chaque liaison, on utilise un tableau NumPy de taille (Npiv,2).
#Créer F_ext, un tableau de zéros de dimension N_piv * 2

F_ext = np.zeros((2,len(pivots)))
F_ext.T # .T signifie "transposée". (Utilisé ici pour l'esthétique)

#Soit une charge de 1,5 tonne au centre du pont (15KN sur y)
F_ext[1,2]=-15
#En isolant l'ensemble
F_ext[1,0]=7.5
F_ext[1,4]=7.5


#Représenter les forces exterieurs avec des flèches 
#------------------------------------------------------------------------------
color=(0.6, 0.6, 0.8)
# Échelle pour le tracé des forces
F_scale = F_ext.max()*0.5
# Couleur des efforts:
F_color = (1., 0, 0) # rouge
dx, dy  = 1,2

# Tracé des barres 
for j, bj in enumerate(barres):
    # Coordonnées des 2 pivots d'accroche:
    (x1,y1), (x2, y2) = bj
    plt.plot((x1, x2), (y1, y2), '-', color = color, lw=4, zorder=1)
    
# Tracés des pivots et des efforts extérieurs
for j,piv in enumerate(pivots):
    plt.plot(piv[0], piv[1], 'ro', zorder=3)
    print j
    # Tracé des efforts
    plt.arrow(piv[0], piv[1], F_ext[0,j]/F_scale, F_ext[1,j]/F_scale,
              zorder=2, head_width=0.2*dx, lw=0, width=0.06*dx, color=F_color)
   
# Ajustements des limites :
plt.axis('equal')
plt.xlim(-2., 14)

#plt.title(u'Actions mécaniques extérieures')
plt.savefig('output2.jpg')
#plt.show()

#Vecteur directeur des barres

# Conversion des barres en trableau NumPy
barres_arr = np.array(barres)
print(barres_arr.shape) # On obtient un tableau 3D
print('Matrice barres_arr:')
print(barres_arr)

#Pour calculer le vecteur directeur, on calcule d'abord P1P2=OP2−OP1. Il faut donc d'abord récupérer OP1 et OP2 pour chaque barre.
#On procède de manière vectorielle :  
barres_OP1 = barres_arr[:,0,:]
barres_OP2 = barres_arr[:,1,:]
barres_P1P2 = barres_OP2 - barres_OP1
print('Matrice barres_P1P2:')
print(barres_P1P2)

#Il faut à présent normaliser les vecteurs P1P2 pour obtenir les vecteurs directeurs u
barre_l = np.sqrt(barres_P1P2[:,0]**2+barres_P1P2[:,1]**2)
barre_l=barre_l.reshape(len(barre_l),1)
print('barre_l:')
print(barre_l)

barre_dir = barres_P1P2 / barre_l

print('Matrice barre_dir:')
print(barre_dir)

#Matrice d'incidence : construction
Inc_mat = np.zeros((N_piv, len(barres)), dtype=int)

for j, bar_j in enumerate(barres):
    P1, P2 = bar_j
    # Remarquons la convention de signe:
    i1=pivots.index((P1))
    Inc_mat[i1,j] = -1 # la barre j "quitte" P1
    i2=pivots.index((P2))
    Inc_mat[i2,j] = +1 # la barre j "arrive à" P2

print('Matrice d\'incidence:')
print(str(Inc_mat).replace('0','.')) # Méthode d'affichage cosmétique

#Construction des matrices A et b
# 1) Matrice A
Ax = Inc_mat*barre_dir[:,0]
Ay = Inc_mat*barre_dir[:,1]

#La superposition (concaténation) des blocs se fait avec np.vstack (il existe np.hstack et np.concatenate)
A = np.vstack((Ax, Ay))
# Image de la matrice:
# plt.imshow(A, interpolation='nearest')
print('Matrice A:')
print(A)
print(A.round(2))

print(F_ext)
b= np.concatenate((F_ext[0,:], 
                        F_ext[1,:]))

print(b)

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
print('A et b')
print(A)  
print(b)       
print(np.round(A,2),np.round(b))

#remontée
for k in range(N-1,0,-1):   #-1 pour pas negatif
        for i in range(k):
            b[i] -= b[k]*A[i,k]/A[k,k]        
            A[i,:] -= A[k,:]*A[i,k]/A[k,k]


print(np.round(A,2),np.round(b))

#fin de la resolution
solution= np.zeros((1,2*len(pivots)))
print solution
for k in range(N):
    solution[0,k]=b[k]/A[k,k]
print('solution')
print(solution)

#affichage du résultat
#-------------------------------------------------------
#Représentation des efforts
color=(0.8, 0.8, 0.8)
# Échelle pour le tracé des forces
F_scale = 0.3*barre_l.mean()/solution.max()
# Couleur des efforts:
F_color = (0., 0, 1) # bleu
dx, dy  = 1,2

# Tracé des barres et des efforts
for j, bj in enumerate(barres):
    # Coordonnées des 2 pivots d'accroche:
    (x1,y1), (x2, y2) = bj
    # direction :
    uj = barre_dir[j]
    trac = solution[0,j]
    
    plt.plot((x1, x2), (y1, y2), '-', color = color, lw=4, zorder=1)
    
    # Tracé des efforts barre -> pivot1 et pivot 2
    plt.arrow(x1, y1, +trac*uj[0]*F_scale, +trac*uj[1]*F_scale,
              zorder=2, head_width=0.08*dx, lw=0, width=0.02*dx, color=F_color)
    plt.arrow(x2, y2, -trac*uj[0]*F_scale, -trac*uj[1]*F_scale,
              zorder=2, head_width=0.08*dx, lw=0, width=0.02*dx, color=F_color)

# Tracés des pivots :
for piv in pivots:
    plt.plot(piv[0], piv[1], 'wo', zorder=3)

# Ajustements des limites :
plt.axis('equal')
plt.xlim(-2., 14)

#plt.title(u'Forces exercées par les barres sur les liasons')
plt.savefig('output3.jpg')
#plt.show()
fin = time.time()

print 'temps',fin-debut