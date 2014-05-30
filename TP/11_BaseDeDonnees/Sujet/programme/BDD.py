#! /usr/bin/python
# -*- coding: utf-8 -*-
"""
Created on Mon May 26 09:13:41 2014

@author: Xavier
"""


import sqlite3
import matplotlib.pyplot as plt
import numpy as np
import generateKML

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
    
requete = "SELECT COUNT(*) FROM airports WHERE type='seaplane_base'"
curseur.execute(requete)


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


requete = "SELECT municipality,name,type FROM airports WHERE municipality='Mandalay' ORDER BY municipality"
curseur.execute(requete)
for cur in curseur:
    print(cur)

"""
import generateKML

requete = "SELECT name,longitude_deg,latitude_deg,type FROM airports WHERE type='seaplane_base'" #AND continent='EU'"
curseur.execute(requete)
res=[]
fichier=[]
for cur in curseur:
    res.append(cur)
    if "&" in cur[0]:
        print(cur[0])
    else :
        ligne = cur[0]+','+cur[1]+','+cur[2]+','+cur[3]+'\n' 
        fichier.append(ligne)
generateKML.GenFileKML(fichier,'testXP')
"""