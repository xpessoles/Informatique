# -*- coding: utf-8 -*-
"""
@auteur: David Fournier
"""

from math import sqrt

global rayon
rayon = 0.3
global vMax
vMax = sqrt(0.5**2+0.6**2)
distance = 2 * (rayon + vMax)

largeur = 6
hauteur = 4
listeParticules = [(0.2, 2.7, -0.5, -0.3), (2.2, 1.6, 0.1, 0.6), (3.25, 2.45, -0.45, 0.05), (5.7, 3.7, 0.5, 0.6)] # triée par abscisse croissante
particules = (largeur, hauteur, listeParticules)

def deplacerParticule(particule, largeur, hauteur): # rappel de la fonction
    x, y, vx, vy = particule
    if x+vx<=0 or x+vx>=largeur: vx *= -1
    if y+vy<=0 or y+vy>=hauteur: vy *= -1
    return (x+vx, y+vy, vx, vy)

def maj(particules): # rappel de la fonction
    largeur, hauteur, listeParticules = particules
    nListeParticules = []
    for particule in listeParticules:
        nListeParticules.append(deplacerParticule(particule, largeur, hauteur))
    return(largeur, hauteur, nListeParticules)

def detecterCollisionEntreParticules(p1, p2): # rappel de la fonction
    x1, y1, vx1, vy1 = p1
    x2, y2, vx2, vy2 = p2
    return (x2-x1)**2+(y2-y1)**2 <= (2*rayon)**2

def majOuCollisionX(particules):
    nParticules = maj(particules)
    largeur, hauteur, listeParticules = particules
    largeur, hauteur, nlisteParticules = nParticules
    collision = False
    for i in range(len(listeParticules)-1):
        j = i + 1
        while (listeParticules[j][0]-listeParticules[i][0]<=2*(vMax + rayon)) and (j<len(listeParticules)-1) and not collision:  
            if detecterCollisionEntreParticules(nlisteParticules[i], nlisteParticules[j]):
                collision = True
            j += 1
    if collision:
        return None
    else:
        return nParticules 

print(majOuCollisionX(particules))