# -*- coding: utf-8 -*-
"""
@auteur: David Fournier
"""

import matplotlib.pyplot as plt

def quadrillage(largeur, hauteur):
    for j in range(hauteur+1):
        plt.plot([0,largeur],[j,j],color='k')
    for i in range(largeur+1):
        plt.plot([i,i],[0,hauteur],color='k')
    axes = plt.gca()
    axes.set_xlim(-1,largeur+1)
    axes.set_ylim(-1,hauteur+1)
#    axes.set_xticklabels([])
#    axes.set_yticklabels([])

largeur, hauteur = 6, 4

def listeParticules(grille):
    particules = []
    largeur, hauteur = len(grille), len(grille[0])
    for i in range(largeur):
        for j in range(hauteur):
            if grille[i][j] != None:
                particules.append(grille[i][j])
    return particules

def illustration(particules, largeur, hauteur, couleur):
    for particule in particules:
        x, y, vx, vy = particule
        plt.plot(x,y,'o',color=couleur)
        plt.plot([x,x+vx],[y,y+vy],'-',color=couleur)
        plt.quiver(x,y,vx,vy,angles='xy',scale_units='xy',scale=1,color=couleur)



particules = [(2.2, 1.6, 0.1, 0.6), (3.25, 2.45, -0.45, 0.05), (0.2, 2.7, -0.5, -0.3), (5.7, 3.7, 0.5, 0.6)]
quadrillage(largeur, hauteur)
illustration(particules, largeur, hauteur, 'r')

def deplacerParticule(particule, largeur, hauteur):
    x, y, vx, vy = particule
    if x+vx<=0 or x+vx>=largeur: vx *= -1
    if y+vy<=0 or y+vy>=hauteur: vy *= -1
    return (x+vx, y+vy, vx, vy)

nParticules = []
for particule in particules:
    nParticules.append(deplacerParticule(particule, largeur, hauteur))
illustration(nParticules, largeur, hauteur, 'g')
plt.show()

def nouvelleGrille(largeur, hauteur):
    return [[None for j in range(hauteur)] for i in range(largeur)]

grille = nouvelleGrille(largeur, hauteur)
for particule in particules:
    x, y, vx, vy = particule
    grille[int(x)][int(y)] = particule
print(grille)

def majGrilleOuCollision(grille):
    largeur, hauteur = len(grille), len(grille[0])
    nGrille = nouvelleGrille(largeur, hauteur)    
    collision = False
    for i in range(largeur):
        for j in range(hauteur):
            if grille[i][j] != None:
                particule = grille[i][j]
                x, y, xv, vy = deplacerParticule(particule, largeur, hauteur)
                if nGrille[int(x)][int(y)] == None:
                    nGrille[int(x)][int(y)] = (x, y, xv, vy)
                else:
                    collision = True
    if collision:
        return None
    else:
        return nGrille
    
print(majGrilleOuCollision(grille))

def attendreCollisionGrille(grille, tMax):
#    O(tMax * largeur * hauteur)
    t = 0 
    while t < tMax and grille != None:
        t += 1
        grille = majGrilleOuCollision(grille)
    if t == tMax:
        return None
    else:
        return t

print(attendreCollisionGrille(grille, 10))






