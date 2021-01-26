#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = "Xavier PESSOLES"

import math as m
# EXERCICE 2016 01

def suite (n,nb):
    i=1
    res=nb
    while n > 0:
        res = (res+module(res))/2
       # print(i,res)
        n=n-1
        i+=1
    return res


def module(nb):
    return(m.sqrt(nb.real**2+nb.imag**2))

def suite2(nb):
    i=1
    res=nb
    while abs(res.imag)>0.01:
        res = (res+module(res))/2
        i=i+1
    return i

print(suite(12,1+10j))
print(suite2(1+10j))
