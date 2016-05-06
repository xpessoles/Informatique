#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = "Xavier PESSOLES"


# EXERCICE 13
# Question 1 
# ==========

import numpy as np

def fibo(n):
    M = np.array([[1,1],[1,0]])
    X0 = np.array([1,1])
    M = np.linalg.matrix_power(M,n-1)
    X = np.dot(M,X0)
    return X[1]

for i in range(20):
    print(i,fibo(i))    