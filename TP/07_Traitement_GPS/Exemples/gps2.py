#! /usr/bin/env python
# -*- coding: utf-8 -*-
fid=open('OuCest.kml','r')

def is_word_in_string(mot,chaine):
    for i in range(1+len(chaine)-len(mot)):
        j=0
        while j<len(m) and m[j]==t[i+j]:
            j=j+1
        if j==len(m):
            return True
    return False
    
 
def chercher(l,c):
    tab=fid.readlines()
    line= tab[l]
    if str(c) in line:
        return True
    else:
        return False
        
