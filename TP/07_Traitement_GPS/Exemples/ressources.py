#! /usr/bin/env python
# -*- coding: utf-8 -*-


# === Changement de répertoire ===
from os import chdir
chdir("C:\\Users\\Xavier Pessoles\\Documents\\Informatique")
# ================================


# ======== Telechargement ========
from urllib.request import urlretrieve
urlretrieve("http://perso.crans.org/~pessoles/OuCest.kml","OuCest.kml")
# ================================


# === Découpage heure-min-sec ====
def heure(ligne):
   if "when" in ligne :
      heure = ligne[ligne.find("T")+1:ligne.find("Z")]
      h = heure.split(":")
      return [float(h[0]),float(h[1]),float(h[2])]
   else :
      return None
# ================================


# === Calcul de l'orthodromie ====
from math import sin,sqrt,cos,asin,pi
def orthodromie(loA,laA,loB,laB):
   """ loA,laA,loB,laB reorésentent les longitudes et
       latitudes de points exprimés en degrés"""
   R = 6371 # Rayon de la terre en km
   # Conversions en radians
   loA = loA*pi/180 
   loB = loB*pi/180
   laA = laA*pi/180
   laB = laB*pi/180   
   d=2*R*asin(sqrt(
      (sin((laB-laA)/2))**2 +
              cos(laA)*cos(laB)*(sin((loB-loA)/2))**2))
   return d
# ================================


# === Affichage de la courbe  ====
import matplotlib.pyplot as plt
import numpy as np

p1=plt.plot(distance_cumulee,altitude,linewidth=3)
plt.grid(True, which="both", linestyle="dotted")
plt.show()
# ================================

