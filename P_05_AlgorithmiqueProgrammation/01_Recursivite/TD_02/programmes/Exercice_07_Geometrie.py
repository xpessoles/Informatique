#!/usr/bin/env python
# -*- coding: utf-8 -*-
# D'après ressources de Jean-Pierre Becirspahic   \\ \indent \url{http://info-llg.fr/

import matplotlib.pyplot as plt
import numpy as np

def cercle(coord, r):
    x,y=[],[]
    for t in range (101):
        x.append(coord[0]+r*np.cos(t*np.pi/50))
        y.append(coord[1]+r*np.sin(t*np.pi/50))
    plt.plot(x,y)
    
    
def bulle1(n,x=0,y=0,r=8):
    cercle([x,y],r)
    if n>1 :
        bulle1(n-1,x+3*r/2,y,r/2)
        bulle1(n-1,x,y-3*r/2,r/2)

bulle1(6)
plt.axis('equal')
plt.show()