#! /usr/bin/python
# -*- coding: utf-8 -*-
"""
Created on Mon May 26 09:13:41 2014

@author: Xavier
"""


import sqlite3
import matplotlib.pyplot as plt
import numpy as np

basesql = u"Aeroports.db3"
savsql = u"Aeroport_sav.db3"

cnx = sqlite3.connect(basesql)
curseur = cnx.cursor()

# Nombre d'aeroports
requete = "SELECT * FROM airports WHERE type='seaplane_base'"
curseur.execute(requete)

type_air=[]
n=0
for cur in curseur:
    #print(cur)
    n+=1
    if n>3:
        break
    
requete = "SELECT * FROM airports WHERE type='seaplane_base'"
curseur.execute(requete)
res=[]
for cur in curseur:
    res.append(cur)
#print(len(res))
    

requete = "SELECT name,municipality FROM airports WHERE type='seaplane_base' AND iso_country='FR'"
curseur.execute(requete)
res=[]
for cur in curseur:
    res.append(cur)
    #print(cur)
    
        

requete = "SELECT name,municipality FROM airports WHERE type='seaplane_base' AND continent='EU'"
curseur.execute(requete)
res=[]
for cur in curseur:
    res.append(cur)
    #print(cur)


requete = "SELECT name,longitude_deg,latitude_deg FROM airports WHERE type='seaplane_base' AND continent='EU'"
curseur.execute(requete)
res=[]
for cur in curseur:
    res.append(cur)
    print(cur)
    