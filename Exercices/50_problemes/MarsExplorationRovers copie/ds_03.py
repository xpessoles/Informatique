# -*- coding: utf-8 -*-
"""
Created on Thu Nov 10 11:22:26 2022

@author: xavier.pessoles2
"""
import random
import math
def generer_PI(n,cmax):
    L = []
    for i in range(n):
        x = random.randrange(0,cmax+1)
        y = random.randrange(0,cmax+1)
        pt = [x,y]
        L.append(pt)
    return L

def generer_PI_dis(n,cmax):
    L = []
    i = 0
    while i < n :
        x = random.randrange(0,cmax+1)
        y = random.randrange(0,cmax+1)
        pt = [x,y]
        if pt not in L : 
            L.append(pt)
            i=i+1
    return L     

def distance(p1,p2):
    x1,y1 = p1       
    x2,y2 = p2
    return(math.sqrt((x2-x1)**2+(y2-y1)**2))

def calculer_distances(PI):
    L = []
    for i in range(len(PI)):
        l = [0 for j in range(len(PI))]
        L.append(l)
    pr = (0,0) #position_robot()
    for i in range(len(PI)):
        for j in range(i):
            L[i][j]=distance(pr,PI[i][j])
            L[i][j]=L[j][i]    
    return L