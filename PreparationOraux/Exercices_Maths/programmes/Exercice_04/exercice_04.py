#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = "Xavier PESSOLES"


# Question 1 
# ==========
def nombreZeros(t,i):
    if t[i]==1:
        return 0
    else : 
        res = 1
        j=i+1
        while j<len(t) and t[j]==0:
            res = res+1
            j=j+1
    return res
# t1=[0,1,1,1,0,0,0,1,0,1,1,0,0,0,0]
# print(nombreZeros(t1,4))
# print(nombreZeros(t1,1))
# print(nombreZeros(t1,8))

# Question 2
# ==========
def nombreZerosMax(t):
    max=nombreZeros(t,0)
    for i in range(1,len(t)):
        tmp = nombreZeros(t,i)
        if tmp>max:
            max = tmp
    return max
print(nombreZerosMax(t1))


# Question 3 et 4
# ================
