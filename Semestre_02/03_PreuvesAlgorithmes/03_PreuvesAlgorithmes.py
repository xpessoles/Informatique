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
        n = n+1
        r = r+n
        print(r,n,v)
    return n,sum([i for i in range(n+1)])

def foo3(v:int) -> int:
    r = 0
    n = 0
    while r <= v : 
        n = n+1
        r = r+n
        print(r,n,v)
    return n,sum([i for i in range(n+1)])



