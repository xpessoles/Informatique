# -*- coding: utf-8 -*-
"""
Created on Mon May 16 14:18:12 2022


@author: Jean-Pierre Becirspahic
@author: xavier.pessoles2
"""

from collections import deque

from math import sqrt, exp, log
op_uni = {'sqrt': sqrt, 'exp': exp, 'ln':log}
def add(x, y):
    return x + y
def sous(x, y):
    return x - y
def mult(x, y):
    return x * y
def div(x, y):
    return x / y
op_bin = {'+': add, '-': sous, '*': mult, '/': div}


def evalue(lst):
    p = deque()
    for t in lst:
        if t in op_bin:
            y = p.pop()
            x = p.pop()
            p.append(op_bin[t](x, y))
        elif t in op_uni:
            x = p.pop()
            p.append(op_uni[t](x))
        else:
            p.append(t)
    return p.pop()


def evalue2(lst):
    p = deque()
    for t in lst:
        if t in op_bin:
            if len(p)==0:
                raise ValueError("expression incorrecte")
            y = p.pop()
            if len(p)==0:
                raise ValueError("expression incorrecte")
            x = p.pop()
            p.append(op_bin[t](x, y))
        elif t in op_uni:
            if len(p)==0:
                raise ValueError("expression incorrecte")
            x = p.pop()
            p.append(op_uni[t](x))
        else:
            p.append(t)
    s = p.pop()
    if not len(p)==0:
        raise ValueError("expression incorrecte")
    return s