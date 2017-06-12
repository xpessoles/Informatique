import numpy as np
import matplotlib.pyplot as plt
import math

import random as rd

n = 10
temps = [10*rd.randint(0,n) + rd.randint(0,9) for t in range(n)]
a = [rd.randint(0,n//2) for i in range (n)]
temps.sort()
print(temps)
print(a)

def compte (x,a):
    cpt = 0
    for e in a :
        if e == x : 
            cpt=cpt+1
    return cpt
    

def occurences(a):
    r=[]
    for aa in a :
        r.append(compte(aa,a))
    return r

def maxconstant(a,t):
    T=0
    i=0
    deb,fin=0,0
    while i < len(a)-1:
        if a[i]==a[i+1]:
            deb = i
            while i<len(a)-1 and a[i]==a[i+1]:
                i=i+1
            fin = i
            if t[fin]-t[deb]>T:
                T = t[fin]-t[deb]
        else :
            i=i+1
    return T

def maxoccurences(a,occ):
    r = occurences(a)
print(maxconstant(a,temps))
            

r = occurences(a)
print(r)
