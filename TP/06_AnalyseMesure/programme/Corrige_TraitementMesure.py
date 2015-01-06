# -*- coding: utf-8 -*-
"""
Created on Tue Jan  6 10:49:24 2015

@author: Xavier
"""
import numpy as np
import matplotlib.pyplot as plt

def lireFichierMesure_01(file):
    """
    Permet de lire un fichier de mesure et de stocker les lignes utiles dans une liste.
    (Pas de suppression des premières lignes)
    Entrées : 
      * file : str, nom du fichier
    Sortie :
      * tab : list, liste des lignes utiles
          (Exemple de ligne utile : '0,009800\t16,152722\t0,426743\n')
    """
    tab=[]
    fid = open(file,'r')
    for ligne in fid:
        tab.append(ligne)
    fid.close()
    return tab

def lireFichierMesure_02(file):
    """
    Permet de lire un fichier de mesure et de stocker les lignes utiles dans une liste.
    (Suppression des 22 premières lignes)
    Entrées : 
      * file : str, nom du fichier
    Sortie :
      * tab : list, liste des lignes utiles
          (Exemple de ligne utile : '0,009800\t16,152722\t0,426743\n')
    """
    tab=[]
    fid = open(file,'r')
    for ligne in fid:
        tab.append(ligne)
    fid.close()
    tab[0:22]=[]
    return tab
    
def lireFichierMesure_03(file):
    """
    Permet de lire un fichier de mesure et de stocker les lignes utiles dans une liste.
    (Découpage des lignes)
    Entrées : 
      * file : str, nom du fichier
    Sortie :
      * res : list, liste des listes d'informations utiles
          (Strucutre de res : [...,[0.009800,16.152722,0.426743],...]
    """
    tab=[]
    fid = open(file,'r')#,newline='\n')
    for ligne in fid:
        tab.append(ligne)
    fid.close()
    tab[0:22]=[]
    tab.pop()
    res=[]
    for i in range(len(tab)):
        ligne=tab[i].replace("\n","").replace(",",".").split("\t")
        ligne = [float(ligne[0]),float(ligne[1]),float(ligne[2])]
        res.append(ligne)
    return res


def lireFichierMesure_04(file):
    """
    Permet de lire un fichier de mesure et de stocker les lignes utiles dans une liste.
    Découpage en colonnes
    Entrée : 
      * file : str, nom du fichier
    Sorties :
      * t : list, première colonne du fichier, temps
      * c2 : list, seconde colonne du fichier
      * c3 : list, troisième colonne du fichier
    """
    tab=[]
    fid = open(file,'r')#,newline='\n')
    for ligne in fid:
        tab.append(ligne)
    fid.close()
    tab[0:22]=[]
    tab.pop()
    res=[]
    t,c2,c3=[],[],[]
    for i in range(len(tab)):
        ligne=tab[i].replace("\n","").replace(",",".").split("\t")
        t.append(float(ligne[0]))
        c2.append(float(ligne[1]))
        c3.append(float(ligne[2]))
    return t,c2,c3

def plotFichier(file):
    t,c1,c2 = lireFichierMesure_04("MesureCapsuleuse.lvm")
    plt.plot(t,c1,label="C1")
    plt.plot(t,c2,label="C2")
    plt.legend(loc='lower center')
    plt.xlabel("Abscisse")
    plt.ylabel("Ordonnée")
    plt.show()

def filtrageMoyenne(fichier,nbEch):
    print("Lecture Fichier")
    t,man,mal = lireFichierMesure_04("MesureCapsuleuse.lvm")
    t2,mal2 = [],[]
    print("Calcul Moyenne")
    for i in range (0,len(t)-nbEch,nbEch):
        t2.append(t[i])
        moy = 0
        for j in range(i,i+nbEch):
            moy = moy + mal[j]
        moy = moy / nbEch
        mal2.append(moy)
    print("Affichage")
    plt.plot(t2,mal2)
    plt.show()
    
def filtrageMoyenneGlissante(fichier,nbEch):
    print("Lecture Fichier")
    t,man,mal = lireFichierMesure_04("MesureCapsuleuse.lvm")
    t2,mal2 = [],[]
    print("Calcul Moyenne")
    for i in range (0,len(t)-nbEch):
        t2.append(t[i])
        moy = 0
        for j in range(i,i+nbEch):
            moy = moy + mal[j]
        moy = moy / nbEch
        mal2.append(moy)
    print("Affichage")
    plt.plot(t2,mal2)
    plt.show()

fichier = "MesureCapsuleuse.lvm"

# plotFichier(fichier)
filtrageMoyenneGlissante(fichier,20)


input("Tapper une touche pour terminer")