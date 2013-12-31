#! /usr/bin/env python
# -*- coding: utf-8 -*-

fichier = "Rhune.kml"

   

def Affiche_GPS_n(fichier,n):
   # Ouverture du fichier
   fid=open(fichier,'r')
   i=0
   for ligne in fid.readlines() :
      if "when" in ligne and i<n:
         print(ligne)
      if "gx:coord" in ligne and i<n:
         print(ligne)
         i=i+1
      elif i>=n:
         break
   fid.close()

def coord(ligne):
    if "gx:coord" in ligne :
        lat = ligne[ligne.find(">")+1:ligne.find(" ")]
        ligne = ligne[ligne.find(" ")+1:]
        lon = ligne[:ligne.find(" ")]
        ligne = ligne[ligne.find(" ")+1:]
        alt=ligne[:ligne.find("<")]
        return [float(lat),float(lon),float(alt)]
    else:
        return []

def heure(ligne):
   if "when" in ligne :
      heure = ligne[ligne.find("T")+1:ligne.find("Z")]
      h = heure.split(":")
      return [float(h[0]),float(h[1]),float(h[2])]
   else :
      return[]

def parse_kml(fichier):
   fid=open(fichier,'r')
   kml = []
   for ligne in fid.readlines() :
      if "when" in ligne:
         h = heure(ligne)
      if "gx:coord" in ligne:
         c = coord(ligne)
         kml.append([h[0],h[1],h[2],c[0],c[1],c[2]])
         
   fid.close()
   return kml

k=parse_kml(fichier)
   
