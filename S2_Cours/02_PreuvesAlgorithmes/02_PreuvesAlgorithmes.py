# -*- coding: utf-8 -*-



def foo(v:int) -> int:
    res = 0
    n = 0
    while res < v : 
        n = n+1
        res = res+n
    return n

# foo(10) renvoie 4
res = 1+2+3+4