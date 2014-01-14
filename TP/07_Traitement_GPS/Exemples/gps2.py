#! /usr/bin/env python
# -*- coding: utf-8 -*-
fid=open('OuCest.kml','r')

            
def chercher(l,c):
    tab=fid.readlines()
    line= tab[l]
    if str(c) in line:
        return True
    else:
        return False
        