# -*- coding: utf-8 -*-
"""
Created on Thu Jan 13 10:18:46 2022

@author: xpess
"""

def fonction(x,y = []) :
    if x == [] : 
        return y
    else : 
        z = x.pop(0)
        if z not in y : 
            y.append(z)
        return fonction(x, y)
    

def fonction_02(L):
    LL = []
    for elt in L : 
        if elt not in LL : 
            LL.append(elt)
    return LL

def fonction_03_v1(L):
    n = len(L)
    LL = []
    i = 0
    while i<=n :
        x = L[i]
        j=0
        flag = False
        while j<=n:
            if L[j]==x :
                flag == True
            j=j+1
        if flag == True : 
            LL.append(x)
        i=i+1
    return LL

def fonction_03_v2(L):
    n = len(L)
    LL = []
    i = 0
    while i<n :
        x = L[i]
        j=0
        flag = False
        while j<n:
            print(i,j)
            if L[j]==x :
                flag == True
            j=j+1
        if flag == False : 
            LL.append(x)
        i=i+1
    return LL

test = [1,2,3,1,2,3,4]