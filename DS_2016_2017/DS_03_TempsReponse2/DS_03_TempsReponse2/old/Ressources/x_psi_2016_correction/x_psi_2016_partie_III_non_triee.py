# -*- coding: utf-8 -*-
"""
@auteur: David Fournier
"""

largeur = 6
hauteur = 4
listeParticules = [(2.2, 1.6, 0.1, 0.6), (3.25, 2.45, -0.45, 0.05), (0.2, 2.7, -0.5, -0.3), (5.7, 3.7, 0.5, 0.6)]
particules = (largeur, hauteur, listeParticules)
global rayon
rayon = 0.3


def detecterCollisionEntreParticules(p1, p2):
    x1, y1, vx1, vy1 = p1
    x2, y2, vx2, vy2 = p2
    return (x2-x1)**2+(y2-y1)**2 <= (2*rayon)**2

print(detecterCollisionEntreParticules(listeParticules[0], listeParticules[1]))

def deplacerParticule(particule, largeur, hauteur): # rappel de la fonction
    x, y, vx, vy = particule
    if x+vx<=0 or x+vx>=largeur: vx *= -1
    if y+vy<=0 or y+vy>=hauteur: vy *= -1
    return (x+vx, y+vy, vx, vy)

def maj(particules):
    largeur, hauteur, listeParticules = particules
    nListeParticules = []
    for particule in listeParticules:
        nListeParticules.append(deplacerParticule(particule, largeur, hauteur))
    return(largeur, hauteur, nListeParticules)

print(maj(particules))

def majOuCollision(particules):
    nParticules = maj(particules)
    largeur, hauteur, listeParticules = nParticules
    collision = False    
    for i in range(len(listeParticules)-1):
        for j in range(i+1, len(listeParticules)):
            if detecterCollisionEntreParticules(listeParticules[i], listeParticules[j]):
                collision = True
    if collision:
        return None
    else:
        return nParticules 

print(majOuCollision(particules))

def attendreCollision(particules, tMax):
    # O(n * n * tMax)
    t = 0
    while t < tMax and particules != None:
        t += 1
        particules = majOuCollision(particules)
    if t == tMax:
        return None
    else:
        return t

print(attendreCollision(particules, 10))


