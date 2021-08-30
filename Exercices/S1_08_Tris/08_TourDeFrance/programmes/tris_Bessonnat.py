### algorithme de tri

# from tris import *
from copy import deepcopy
import random as rd
import time
import numpy as np
# import matplotlib.pyplot as plt
import sys
sys.setrecursionlimit(1000000) # cette ligne permet de modifier le nombre de boucles récursives autorisées (normalement de 1000)

### exercice 1 : le tour de france
### lecture des fichiers
# 'classement_general.txt'
# 'etape_18.txt'






### exercice 2 : question 1

def chargeClassement(fichier):
    f=open(fichier,'r')
    fichier=f.readlines()
    f.close() #ne pas oublier de fermer le fichier...
    L=[]
    for ligne in fichier:
        ligne=ligne.split('\t') # coupe aux tabulations
        L1=[]
        L1.append(ligne[1])
        L1.append(ligne[2])
        L1.append(ligne[4])
        L.append(L1)
    return L


def convertirTemps(temps:str):
    '''temps est un str de la forme "06h 09' 39''" '''
    t_course=temps.split('h') #on peut aussi couper à h
    print (t_course)
    heure=int(t_course[0])
    t_course2=t_course[1].split("'")
    print (t_course2)
    duree=int(t_course2[1])+60*int(t_course2[0])+3600*heure
    return duree
  


def classement(fichier):
    L=chargeClassement(fichier)
    for element in L:
        element[2]=convertirTemps(element[2])
    return L
    
LG=classement('classement_general.txt')
L18=classement('etape_18.txt')    

        
#         
# >>> LG[:20]
# [['JULIAN ALAPHILIPPE ', '21', 250756], ['GERAINT THOMAS ', '1', 250851], ['STEVEN KRUIJSWIJK ', '81', 250863], ['THIBAUT PINOT ', '51', 250866], ['EGAN BERNAL ', '2', 250878], ['EMANUEL BUCHMANN ', '12', 250890], ['MIKEL LANDA MEANA ', '65', 251050], ['ALEJANDRO VALVERDE ', '62', 251056], ['RIGOBERTO URAN ', '91', 251089], ['RICHIE PORTE ', '131', 251146], ['WARREN BARGUIL ', '211', 251198], ['NAIRO QUINTANA ', '61', 251326], ['XANDRO MEURISSE ', '195', 251424], ['DANIEL MARTIN ', '121', 251455], ['ROMAN KREUZIGER ', '206', 251482], ['GUILLAUME MARTIN ', '191', 251578], ['FABIO ARU ', '122', 251611], ['DAVID GAUDU ', '53', 251689], ['BAUKE MOLLEMA ', '136', 251861], ['JESUS HERRADA ', '154', 252385]]

# >>> L18[:20]
# [['NAIRO QUINTANA ', '61', 20055], ['ROMAIN BARDET ', '31', 20150], ['ALEXEY LUTSENKO ', '76', 20203], ['LENNARD KÄMNA ', '145', 20233], ['DAMIANO CARUSO ', '42', 20235], ['TIESJ BENOOT ', '162', 20341], ['MICHAEL WOODS ', '98', 20341], ['EGAN BERNAL ', '2', 20341], ['SERGE PAUWELS ', '115', 20341], ['STEVEN KRUIJSWIJK ', '81', 20373], ['EMANUEL BUCHMANN ', '12', 20373], ['THIBAUT PINOT ', '51', 20373], ['GERAINT THOMAS ', '1', 20373], ['JULIAN ALAPHILIPPE ', '21', 20373], ['RIGOBERTO URAN ', '91', 20373], ['MIKEL LANDA MEANA ', '65', 20373], ['RICHIE PORTE ', '131', 20373], ['WARREN BARGUIL ', '211', 20398], ['ALEJANDRO VALVERDE ', '62', 20431], ['GUILLAUME MARTIN ', '191', 20462]]





### question 2 : ajouter les temps de l'étape 10

# >>> len(LG)
# 158
# >>> len(L18)
# 156
# attention, les deux listes n'ont pas même longueur

def ajout_temps(L1,L2):
    '''L1 est la classement de l'étape et L2 le classement général certains ont été disqualifiés ou ont abandonné'''
    assert len(L1)<=len(L2)
    Lnew=deepcopy(L1)
    n=len(Lnew)
    for i in range(n):
        d=Lnew[i][1]
        j=0
        while d!=L2[j][1]: #attention certains n'ont pas fait l'étape complètement et sont disqualifiés
            j+=1
        Lnew[i][-1]=Lnew[i][-1]+L2[j][-1]
    return Lnew
    
# NewTemps=ajout_temps(LG,L18)
#     assert len(L1)<=len(L2)
# AssertionError
    
# >>> ajout_temps(L18,LG)
# [['NAIRO QUINTANA ', '61', 271381], ['ROMAIN BARDET ', '31', 272559], ['ALEXEY L
# UTSENKO ', '76', 273322], ['LENNARD KÄMNA ', '145', 276161], ['DAMIANO CARUSO ',
#  '42', 277793], ['TIESJ BENOOT ', '162', 276508], ['MICHAEL WOODS ', '98', 27518
# 6], ['EGAN BERNAL ', '2', 271219], ['SERGE PAUWELS ', '115', 278092]]
    
NewTemps=ajout_temps(L18,LG)

### exercice 2 : question 3 : tri par insertion
###Tri par insertion :
def tri_Insertion_v3(t) :
    '''Trie la liste t
    Entrée :
        Une liste
    Sortie :
        La liste est modifiée mais n’est pas renvoyée'''
    for i in range(1,len(t)) :
        element=t[i]
        x=t[i][-1]
        k=0
        while (k<i and x>t[k][-1]) :
            k=k+1
        for j in range(i,k,-1) :
            t[j]=t[j-1]
        t[k]=element


###  exercice 2 : question 4 : modifications des algorithmes de tri pour travailler sur la 3eme valeur

def tri_insertion_modifie(tab):
    """ 
    Trie une liste de nombre en utilisant la méthode du tri par insertion.
    En Python, le passage se faisant par référence, il n'est pas indispensable
    de retourner le tableau.
    Keyword arguments:
    Entrées :
        tab -- liste de nombres
    """
    for i in range (1,len(tab)):
        x=tab[i][-1]
        j=i
        while j>0 and tab[j-1][-1]>x:
            tab[j],tab[j-1]=tab[j-1],tab[j]
            j = j-1
        
    return (tab)
    
td=time.time()
Lins=deepcopy(NewTemps)
tri_insertion_modifie(Lins)
print('tri insertion des coureurs prend ',time.time()-td,'s')


# 
# tri insertion des coureurs prend  0.0029981136322021484 s

# >>> NewTemps[:20]
# [['JULIAN ALAPHILIPPE ', '21', 271129], ['EGAN BERNAL ', '2', 271219], ['GERAINT THOMAS ', '1', 271224], ['STEVEN KRUIJSWIJK ', '81', 271236], ['THIBAUT PINOT ', '51', 271239], ['EMANUEL BUCHMANN ', '12', 271263], ['NAIRO QUINTANA ', '61', 271381], ['MIKEL LANDA MEANA ', '65', 271423], ['RIGOBERTO URAN ', '91', 271462], ['ALEJANDRO VALVERDE ', '62', 271487], ['RICHIE PORTE ', '131', 271519], ['WARREN BARGUIL ', '211', 271596], ['GUILLAUME MARTIN ', '191', 272040], ['FABIO ARU ', '122', 272110], ['ROMAN KREUZIGER ', '206', 272149], ['DAVID GAUDU ', '53', 272246], ['XANDRO MEURISSE ', '195', 272492], ['ROMAIN BARDET ', '31', 272559], ['DANIEL MARTIN ', '121', 273192], ['SÉBASTIEN REICHENBACH ', '57', 273281]]


### quicksort modifie
def segmente_modifie(tab,i,j):
    """
    Segmentation d'un tableau par rapport à un pivot.
    Keyword arguments: 
    Entrées :
        tab (list) -- liste de nombres
        i,j (int) -- indices de fin et de début de la segmentation
    Sorties :    
        tab (list) -- liste de nombres avec le pivot à sa place définitive
        k (int) -- indice de la place du pivot
    """
    g =i+1
    d=j
    p=tab[i][-1]
    while g<=d :
        while d>=0 and tab[d][-1]>p:
            d=d-1
        while g<=j and tab[g][-1]<=p:
            g=g+1
        if g<d :
            tab[g],tab[d]=tab[d],tab[g]
            d=d-1
            g=g+1
    k=d
    tab[i],tab[d]=tab[d],tab[i]
    return k
    
def tri_quicksort_modifie(tab,i,j):
    """
    Tri d'une liste par l'utilisation du tri rapide (Quick sort).
    Keyword arguments:
    Entrées :
        tab (list) -- liste de nombres
        i,j (int) -- indices de fin et de début de la zone de tri
    Sorties :    
        tab (list) -- liste de nombres avec le pivot à sa place définitive
    """
    if i<j :
        k = segmente_modifie(tab,i,j)
        tri_quicksort_modifie(tab,i,k-1)
        tri_quicksort_modifie(tab,k+1,j)
        
td=time.time()
Lquick=deepcopy(NewTemps)
tri_quicksort_modifie(Lquick,0,len(Lquick)-1)
print('tri rapide des coureurs prend ',time.time()-td,'s')

# tri rapide des coureurs prend  0.0019986629486083984 s
        


### tri fusion modifie
def fusion_listes_modifie(tab,g,d,m):
    """
    Fusionne deux listes triées.
    Keyword arguments:
    Entrées :
        tab (list) -- liste : une liste de nombres tab[g:d] avec g indice de la 
            valeur de gauche, d indice de la valeur de droite
        g,d,m (int) -- entiers : indices tels que g<=m<d et tel que les 
            sous-tableaux tab[g:m] et tab[m+1:d] soient ordonnés
    Sorties :
        tab (list) : liste triée entre les indices g et d
    """
    n1 = m-g+1
    n2 = d-m
    G,D = [],[]
    for i in range (n1):
        G.append(tab[g+i])
    for j in range (n2):
        D.append(tab[m+j+1])
    i,j=0,0
    G.append(['','',99999999999])
    D.append(['','',99999999999])
    for k in range (g,d+1):
        if i<=n1 and  G[i][-1]<=D[j][-1]:
            tab[k]=G[i]
            i=i+1
        elif j<=n2 and G[i][-1]>D[j][-1]:
            tab[k]=D[j]
            j=j+1
            
def tri_fusion_modifie(tab,g,d):
    """
    Tri d'une liste par la méthode du tri fusion
    Keyword arguments:
    Entrées : 
        tab (list) -- liste : une liste de nombres non triés tab[g:d]
        g,d (int) -- entiers : indices de début et de fin de liste si on veut trier
                           tout le tableau g=0, d=len(tab)-1
    Sortie :
        tab (list) : liste triée entre les indices g et d
    """
    if g<d:
        m=(g+d)//2
        tri_fusion_modifie(tab,g,m)
        tri_fusion_modifie(tab,m+1,d)
        fusion_listes_modifie(tab,g,d,m)
        
td=time.time()
Lfusion=deepcopy(NewTemps)
tri_fusion_modifie(Lfusion,0,len(Lfusion)-1)
print('tri fusion des coureurs prend ',time.time()-td,'s')
        
        

### avec la fonction prédéfinie dans python 'sorted' il faut créer une fonction lambda pour travailler sur le 3e élément de chaque élément de la liste
lambda colonnes: colonnes[2]
Lsorted=deepcopy(NewTemps)
td=time.time()
sorted(Lsorted, key=lambda colonnes: colonnes[2])
print('tri sort python des coureurs prend ',time.time()-td,'s')

# >>> (executing file "tris_Bessonnat.py")
# tri insertion des coureurs prend  0.002997159957885742 s
# tri rapide des coureurs prend  0.0019989013671875 s
# tri fusion des coureurs prend  0.002999544143676758 s
# tri sort python des coureurs prend  0.001998424530029297 s






### Classement en cours d'étape - implémentation d'une file
### question 5 : L10 est déjà créée et est considérée comme une file qd elle est triée
L18_triee=sorted(classement('etape_18.txt'), key=lambda colonnes: colonnes[2])

# il faut sortir le premier élément de la file

def enfiler(file, element):
    return file.append(element)

file=[2,5,7,8]
    
def defiler(file):
    return file.pop(0)
    
def est_vide(file):
    return len(file)==0
    
### question 6 implémenter la fonction ajout ayant pour but d'ajouter le temps de l'étape et de trier
def ajout(L_etape_triee,LG):
    ''' ajout au classement général le temps de la nouvelle étape et refait le classement'''
    new_classement=[]
    while est_vide(L_etape_triee)==False: #tant que la file n'est pas vide
        cycliste=defiler(L_etape_triee)# on prend le premier élément et on l'enlève
        i=0
        new_classement.append(cycliste)# on place le nouvel arrivant à la queue de la liste triée du classement général
        while cycliste[1]!=LG[i][1]: #je cherche le même dossard de cycliste
            i=i+1
        new_classement[-1][-1]=new_classement[-1][-1]+LG[i][-1] #on additionne les temps du classement général et du classement d'étape
        tri_insertion_modifie(new_classement) #on trie le nouveau classement
    return new_classement
    


### question 7  : enfiler serait utiliser si le classement se faisait en temps réel
    






