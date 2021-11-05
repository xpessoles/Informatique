# -*- coding: utf-8 -*-

def foo(v:int) -> int:
    res = 0
    n = 0
    while res < v : 
        n = n+1
        res = res+n
    return n

def foo2(v:int) -> int:
    r = 1
    n = 1
    while r < v : 
        r = r+n
        n = n+1
        
    return n,sum([i for i in range(n+1)])

# foo(10) renvoie 4
res = 1+2+3+4