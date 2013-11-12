#!/usr/bin/env python
# -*- coding: utf-8 -*-


def triInsertion(tab):
    for i in range(1,len(tab)):
        a=tab[i] # i vaut 2 a : tab[2]
        j=i-1    # j vaut 1
        while j>=0 and tab[j]>a:
            tab[j+1]=tab[j]
            j=j-1
        tab[j+1]=a
    return tab


tab = [17, 38, 10, 25, 72, 4, 98, 32,11]
print(tab)

print(triInsertion(tab))
