# -*- coding: utf-8 -*-
"""
Created on Mon Jul 19 22:02:19 2021

@author: JPB
"""

import matplotlib.pyplot as plt
import numpy as np
def circle(coords:list, r:float) -> None :
    X, Y = [], []
    for t in range(101):
        X.append(coords[0]+r*np.cos(t*np.pi/50))
        Y.append(coords[1]+r*np.sin(t*np.pi/50))
    plt.axis("equal")
    plt.plot(X, Y, 'b')

def bubble1(n, x=0, y=0, r=8):
    circle([x, y], r)
    if n > 1:
        bubble1(n-1,x+3*r/2,y,r/2)
        bubble1(n-1,x, y-3*r/2,r/2)



        
def bubble2(n, x=0, y=0, r=8, d=''):
    circle([x, y], r)
    if n > 1:
        if d != 's':
            bubble2(n-1,x,y+3*r/2,r/2,"n")
        if d != 'w':
            bubble2(n-1,x+3*r/2,y,r/2,"e")
        if d != 'n':
            bubble2(n-1,x,y-3*r/2,r/2,"s")
        if d != 'e':
            bubble2(n-1,x-3*r/2,y,r/2,"w")

bubble1(4,0,0,8)
bubble2(4,0,0,8)

        