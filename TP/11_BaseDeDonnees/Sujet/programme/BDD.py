#! /usr/bin/python
# -*- coding: utf-8 -*-
"""
Created on Mon May 26 09:13:41 2014

@author: Xavier
"""


import sqlite3
import matplotlib.pyplot as plt
import numpy as np

basesql = u"Aeroport.db3"
savsql = u"Aeroport_sav.db3"

cnx = sqlite3.connect(basesql)
curseur = cnx.cursor()

# Nombre d'aeroports
requete = "SELECT type FROM airports"
curseur.execute(requete)

type_air=[]
print("Boucle")
for cur in curseur:
        type_air.append(l[0])
