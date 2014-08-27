#! /usr/bin/env python
# -*- coding: utf-8 -*-

# L'année est-elle bissextile ?

annee= 2000

if annee%100==annee%400==0:
        print("L'année est bissextile")
elif annee%100!=annee%4==0:
    print("L'année est bissextile")

else :
        print("L'année n'est pas bissextile")
