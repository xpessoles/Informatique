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
    
def filtrageKalman(fichier) :
    # Kalman filter example demo in Python

    # A Python implementation of the example given in pages 11-15 of "An
    # Introduction to the Kalman Filter" by Greg Welch and Gary Bishop,
    # University of North Carolina at Chapel Hill, Department of Computer
    # Science, TR 95-041,
    # http://www.cs.unc.edu/~welch/kalman/kalmanIntro.html

    # by Andrew D. Straw
    import numpy
    import pylab
    t,man,mal = lireFichierMesure_04("MesureCapsuleuse.lvm")
    z=mal
    # intial parameters
    n_iter = len(z)
    sz = (n_iter,) # size of array
    x = -0.37727 # truth value (typo in example at top of p. 13 calls this z)
    #z = numpy.random.normal(x,0.1,size=sz) # observations (normal about x, sigma=0.1)
    
    Q = 1e-5 # process variance
    
    # allocate space for arrays
    xhat=numpy.zeros(sz)      # a posteri estimate of x
    P=numpy.zeros(sz)         # a posteri error estimate
    xhatminus=numpy.zeros(sz) # a priori estimate of x
    Pminus=numpy.zeros(sz)    # a priori error estimate
    K=numpy.zeros(sz)         # gain or blending factor
    
    R = 0.1**2 # estimate of measurement variance, change to see effect intial guesses
    xhat[0] = 0.0
     
    P[0] = 1.0
    for k in range(1,n_iter):
        # time update
        xhatminus[k] = xhat[k-1]
        Pminus[k] = P[k-1]+Q
        
        # measurement update
        K[k] = Pminus[k]/( Pminus[k]+R )
        xhat[k] = xhatminus[k]+K[k]*(z[k]-xhatminus[k])
        P[k] = (1-K[k])*Pminus[k]

    pylab.figure()
    pylab.plot(xhat,'b-',label='a posteri estimate')
    pylab.legend()
    pylab.xlabel('Iteration')
    pylab.ylabel('Voltage')
    
    pylab.show()
    

fichier = "MesureCapsuleuse.lvm"

# plotFichier(fichier)
filtrageMoyenneGlissante(fichier,1000)
#plotFichier(fichier)


input("Tapper une touche pour terminer")