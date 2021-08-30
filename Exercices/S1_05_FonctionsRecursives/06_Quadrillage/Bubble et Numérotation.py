# -*- coding: utf-8 -*-
"""
Created on Tue Aug 17 10:20:13 2021

@author: jphbe
"""

## Q1

import matplotlib.pyplot as plt
import numpy as np
def circle(coords:list, r:float):
    X,Y=[],[]
    for t in range(101):
        X.append(coords[0]+r*np.cos(t*np.pi/50))
        Y.append(coords[1]+r*np.sin(t*np.pi/50))
    plt.plot(X,Y,'b')
    plt.axis('equal')
    
def bubble1(n:int, x:float, y:float, r:float):
    circle([x,y],r)
    if n==0:
        return(None)
    bubble1(n-1,x+3*r/2,y,r/2)
    bubble1(n-1,x,y-3*r/2,r/2)
    
    
# bubble1(3,0,0,6)

 
## Q2

def bubble2(n:int, x:float, y:float, r:float, d:str):  # d=direction 'd','g','h','b'
    circle([x,y],r)
    if n==0:
        return(None)
    if d=='d':
        bubble2(n-1,x+3*r/2,y,r/2,'h')
        bubble2(n-1,x+3*r/2,y,r/2,'d')
        bubble2(n-1,x+3*r/2,y,r/2,'b')
    if d=='g':
        bubble2(n-1,x-3*r/2,y,r/2,'h')
        bubble2(n-1,x-3*r/2,y,r/2,'g')
        bubble2(n-1,x-3*r/2,y,r/2,'b')
    if d=='h':
        bubble2(n-1,x,y+3*r/2,r/2,'h')
        bubble2(n-1,x,y+3*r/2,r/2,'d')
        bubble2(n-1,x,y+3*r/2,r/2,'g')
    if d=='b':
        bubble2(n-1,x,y-3*r/2,r/2,'g')
        bubble2(n-1,x,y-3*r/2,r/2,'d')
        bubble2(n-1,x,y-3*r/2,r/2,'b')
        
bubble2(3,0,0,6,'d')
bubble2(3,0,0,6,'g')
bubble2(3,0,0,6,'h')
bubble2(3,0,0,6,'b')

## Q3

def numerote(x:int, y:int):
    if y==0:
        return(sum(k for k in range(x+1)))
    if y>=1:
        return(1+numerote(x+1,y-1))
    
    
def reciproque(n:int):
    if n==0:
        return([0,0])
    R=reciproque(n-1)
    if R[0]>=1:
        return([R[0]-1,R[1]+1])
    else:
        return([R[1]+1,0])
    
