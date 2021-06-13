#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = "Xavier PESSOLES"


# Question 1
n = 1234
q = n//10
r =  n%q

# r contient le nombre d'unités de n


# Question 2
s=0
while n!=0:
    q=n//10
    r = n%10
    #print(r)
    s=s+r**3
    n=q

# Question 3
def somcube(n):
    """
    Entrées :
     * n, int : nombre
    Sortie : 
     * s, int : somme des cubes du chiffre n
    """
    s=0
    while n!=0:
        q=n//10
        r = n%10
        s=s+r**3
        n=q
    return s

# Question 4
res = []
for i in range (10001):
    if i == somcube(i):
        res.append(i)
print(res)
        
# Question 5
def somcube2(n):
    """
    Entrées :
     * n, int : nombre
    Sortie : 
     * s, int : somme des cubes du chiffre n
    """
    nombre=str(n)
    s=0
    for chiffre in nombre :
        s = s+int(chiffre)**3
    return s
    
print(somcube2(1234))