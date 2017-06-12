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

basesql = u"A REMPPLIR" # Champ à remplir
cnx = sqlite3.connect(basesql) 
curseur = cnx.cursor()

# Nombre d'aeroports
requete = "SELECT * FROM airports WHERE type='seaplane_base'"
curseur.execute(requete)


#Exemple pour afficher 3 éléments de la requête
n=0
for cur in curseur:
    n+=1
    print(cur)
    if n>3:
        break
    
    
"""
import generateKML

requete = "SELECT name,longitude_deg,latitude_deg,type FROM airports WHERE type='seaplane_base'" #AND continent='EU'"
curseur.execute(requete)
res=[]
fichier=[]
for cur in curseur:
    res.append(cur)
    if # A completer, GESTION du &
        
    else :
        ligne = # A completer : Constitution d'une ligne
                # A completer : ajout de la ligne au fichier
generateKML.GenFileKML(fichier,'Nom_fichier')
"""