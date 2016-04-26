# -*- coding: utf-8 -*-
"""
@author: Xavier PESSOLES
"""
import numpy as np
import matplotlib.pyplot as plt


# Définition des fonctions
# =========================
def lireFichierMesure(file):
    les_temps=[]
    les_vm=[]
    les_vc=[]
    fid = open(file,'r')
    for ligne in fid:
        ligne = ligne.split("\t")
        les_temps.append(float(ligne[0]))
        les_vm.append(float(ligne[1]))
        les_vc.append(float(ligne[2]))
        
    fid.close()
    return les_temps,les_vm,les_vc


def filtrageMoyenne(fichier,nbEch):
    t,man,mal = lireFichierMesure(fichier)
    t2,mal2 = [],[]
    for i in range (0,len(t)-nbEch,nbEch):
        t2.append(t[i])
        moy = 0
        for j in range(i,i+nbEch):
            moy = moy + mal[j]
        moy = moy / nbEch
        mal2.append(moy)
    
    return t2,mal2
    
def filtrageMoyenneGlissante(fichier,nbEch):
    t,man,mal = lireFichierMesure(fichier)
    t2,mal2 = [],[]
    for i in range (0,len(t)-nbEch):
        t2.append(t[i])
        moy = 0
        for j in range(i,i+nbEch):
            moy = moy + mal[j]
        moy = moy / nbEch
        mal2.append(moy)
    return t2,mal2



# Instructions
# ============
import os
os.chdir('F:\\GitHub_Clef\\Informatique\\PreparationOraux\\Exercices_SII\\programmes\\02_FiltrageCapsuleuse')
fichier = "data\mesures.txt"
t1,y1,y2 = lireFichierMesure(fichier)
t2,fy2 = filtrageMoyenne(fichier,5)
t3,ffy2 = filtrageMoyenneGlissante(fichier,5)
plt.plot(t1,y2,label="Sans filtre");
plt.plot(t2,fy2,label="Moyenne");
#plt.plot(t3,ffy2,label="Moyenne glissante");

plt.legend()
plt.show()