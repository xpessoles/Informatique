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
#savsql = u"Aeroport_sav.db3"

cnx = sqlite3.connect(basesql)
curseur = cnx.cursor()



def Q7():
    # Nombre d'aeroports
    requete = "SELECT * FROM airports WHERE type='seaplane_base'"
    curseur.execute(requete)

    type_air=[]
    n=0
    for cur in curseur:
        print(cur)
        n+=1
        if n>3:
            break

def Q8():
    requete = "SELECT * FROM airports"
    curseur.execute(requete)
    res = []
    for cur in curseur:
        res.append(cur)
    print(len(res))

def Q9_1():
    requete = "SELECT * FROM airports WHERE type='seaplane_base'"
    curseur.execute(requete)
    res=[]
    for cur in curseur:
        res.append(cur)
    print(len(res))

def Q9_2():
    requete = "SELECT COUNT(*) FROM airports WHERE type='seaplane_base'"
    curseur.execute(requete)
    print(curseur.fetchall())



def Q10():
    requete = "SELECT municipality FROM airports WHERE type='seaplane_base' AND iso_country='FR'"
    curseur.execute(requete)
    res=[]
    for cur in curseur:
        res.append(cur)
        print(cur)

def Q11():
    requete = "SELECT name,municipality FROM airports WHERE type='seaplane_base' AND continent='EU'"
    curseur.execute(requete)
    res=[]
    for cur in curseur:
        res.append(cur)
        print(cur)

def Q12():
    requete = "SELECT name FROM (SELECT name,iso_country FROM airports WHERE type='seaplane_base') as aeroports JOIN (SELECT Countries.code FROM Countries WHERE name='United States') as pays ON pays.code = aeroports.iso_country" 
    curseur.execute(requete)
    res=[]
    for cur in curseur:
        res.append(cur)
        print(cur)

def Q13():
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
    generateKML.GenFileKML(fichier,'testXP2')
    
    
Q13()
    

"""    



"""