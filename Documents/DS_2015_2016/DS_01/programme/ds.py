#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np
from math import sqrt
liste_pt=[[1,2,3],[4,5,6],[7,8,9]]
liste_pt=[[1,1,3],[2,0,3],[0,3,3]]
liste_pt=[[1,1,3],[2,0,3],[0,3,3],[1,1,0],[2,0,0],[0,3,0]]

liste_pt=[[-101.8834062002202400,-155.2156845890713700,-50.3043440673320960],[-99.2104062002202340,-145.5476845890713700,-50.3048440673320980],[-82.4309062002202500,-129.6931845890713600,-50.2928440673320980],[-59.7254062002202420,-134.1281845890713700,-50.3018440673320980],[-36.9524062002202460,-145.8071845890713700,-50.3048440673320980],[-26.2619062002202450,-166.4666845890713800,-50.3413440673321020],[-26.2879062002202420,-184.7511845890713600,-50.3763440673320990],[-46.6174062002202520,-197.5426845890713700,-50.3843440673320940],[-71.3029062002202350,-199.9581845890713800,-50.3503440673321020],[-103.3069062002202300,-189.1391845890713600,-50.3128440673320940]]


Sxx = sum([pt[0]**2 for pt in liste_pt]) 
Syy = sum([pt[1]**2 for pt in liste_pt]) 
Szz = sum([pt[2]**2 for pt in liste_pt]) 
Sxy = sum([pt[0]*pt[1] for pt in liste_pt]) 
Sxz = sum([pt[0]*pt[2] for pt in liste_pt]) 
Syz = sum([pt[1]*pt[2] for pt in liste_pt]) 
Sx = sum([pt[0] for pt in liste_pt]) 
Sy = sum([pt[1] for pt in liste_pt]) 
Sz = sum([pt[2] for pt in liste_pt]) 


def mystere(pl,liste_pt):
    ind=0
    d=dist_pt_plan(pl,liste_pt[ind])
    for i in range(1,len(liste_pt)):
        temp=dist_pt_plan(liste_pt[i],pl)
        print(temp)
        if temp>d :
            ind=i
            d=dist_pt_plan(liste_pt[ind],pl)
    return ind
    
def dist_pt_plan(pt,pl):
    return (pt[2]-pl[0]*pt[0]-pl[1]*pt[1]-pl[2])/(sqrt(pl[0]**2+pl[1]**2+1))
    

def balancage(pl, pt):
    npt=25			#nombre de points pour faire varier a et b (50*50 itérations au total)
    pas=0.000003
    dist=100000
    pl2=[None,None,None]
    for k in range(-npt,npt):		#Boucle pour faire varier a
        pl2[0]=pl[0]+k*pas
        for j in range(-npt,npt):	#Boucle pour faire varier b
            pl2[1]=pl[1]+j*pas
            pl2[2]=pt[2]-pl2[0]*pt[0]-pl2[1]*pt[1]	#on modifie c
            temp=defaut_planeite(pl2,liste_pt)	#on détermine le défaut de planéité
            if temp<dist : #on ne retient la configuration (a,b,c) qui si elle minimise le défaut
                dist=temp
                f=pl2[0]
                g=pl2[1]
                h=pl2[2]

    pl2=[f,g,h]    
    return [pl2,dist]		#on retourne la meilleur configuration ainsi que le défaut


def defaut_planeite(pl,liste_pt):
    dist_p=0
    dist_n=0
    for i in range(len(liste_pt)):
        dist=dist_pt_plan(liste_pt[i],pl)
        if dist_p<dist and dist>0 :
            dist_p=dist
        elif dist_n>dist and dist<0 :
            dist_n=dist
    return dist_p-dist_n

def read_file(file):
    fid = open(file,'r')
    pts=[]
    for ligne in fid:
        ligne = ligne.split(",")
        print(ligne)
        pts.append([float(ligne[0]),float(ligne[1]),float(ligne[2])])
    return pts
        
    
A = np.array([[Sxx,Sxy,Sx],[Sxy,Syy,Sy],[Sx,Sy,len(liste_pt)]])
B = np.array([[Sxz],[Syz],[Sz]])
X = np.linalg.solve(A,B)

for i in range(len(liste_pt)):
    print(dist_pt_plan(liste_pt[i],X))
print()

# Recherche du plan passant par le point le plus éloigné du plan :
ind = mystere(X,liste_pt)
print(ind)
# Plan des moindres carrés ext matière : seul c change : 
X[2]=liste_pt[ind][2]-X[0]*liste_pt[ind][0]-X[1]*liste_pt[ind][1]

#Distance point - droite ... et défaut de planéité
print(dist_pt_plan(liste_pt[ind],X))
print(defaut_planeite(X,liste_pt))

#Balancage par rapport au point 10

res = balancage(X,liste_pt[-1])

import os
os.chdir("E:\Github\Informatique\DS_2015_2016\DS_01\programme")

print(read_file("mesures.txt"))