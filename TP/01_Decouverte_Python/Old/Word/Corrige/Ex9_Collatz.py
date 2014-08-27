#! /usr/bin/env python
# -*- coding: utf-8 -*-


#Suite de Collatz

u0 = 8
u=u0
for i in range (0,10):
    if u%2==0:
        u=u/2
    else :
        u=3*u+1
    print(u)
print()

u=u0
i=0
while u!=4:
    if u%2==0:
        u=u/2
    else :
        u=3*u+1
    i=i+1
    print(u)

print(i)
