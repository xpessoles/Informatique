# ### si les élèves travaillent sous pyzo il faut définir le chemin d'acces aux différents fichiers
import os
os.chdir(r'I:\PT-PTstar 2015-2016\Informatique\P_05_AlgorithmiqueProgrammation\03_Tris\TD_02_TourDeFrance\programmes')






















# ### algorithme de tri
# 
# from tris import *
# import random as rd
# import time
# import matplotlib.pyplot as plt
# import sys
# sys.setrecursionlimit(1000000) # cette ligne permet de modifier le nombre de boucles récursives autorisées (normalement de 1000)
# 
# ### exercice 1 - cout temporel des algorithmes de tris : Question 1
# L_insert=[]
# L_rapide=[]
# L_fusion=[]
# L_sort=[]
# L=[i for i in range(0,10001,1000)] # dépend de la vitesse de calcul de l'ordinateur de l'élève
# # pour des listes allant jusqu'à 1000 éléments mon ordi met 1 minute à faire tous les tris - image illisible
# # pour les listes allant jusqu'à 10000 éléments avec des sauts de 500 éléments mon ordi met 1 minute à faire tous les calculs
# # pour les listes allant jusqu'à 100000 éléments avec des sauts de 10000 éléments mon ordi met trop de minutes à faire tous les calculs
# # pour les listes allant jusqu'à 20000 éléments avec des sauts de 2000 éléments mon ordi met 104 secondes à faire tous les calculs
# for i in L:
#     L1=[]
#     for j in range(i):
#         L1.append(rd.randint(0,i))
#     L_i=L1[:] # bien copier les listes autrement à la seconde fonction on trie une liste triée (voir algorithmes dans le fichier tris.py qui ne renvoient rien, la liste est modifiée sur place
#     L_f=L1[:]
#     L_q=L1[:]
#     td=time.time()
#     tri_insertion(L_i)
#     tf=time.time()-td
#     L_insert.append(tf)
#     td=time.time()
#     tri_fusion(L_f,0,len(L_f)-1)
#     tf=time.time()-td
#     L_fusion.append(tf)
#     td=time.time()
#     tri_quicksort(L_q,0,len(L_f)-1)
#     tf=time.time()-td
#     L_rapide.append(tf)
#     td=time.time()
#     L1.sort()
#     tf=time.time()-td
#     L_sort.append(tf)
# 
# plt.figure()
# plt.grid()
# plt.xlabel('taille de la liste')
# plt.ylabel('temps de tri en seconde')
# plt.plot(L,L_insert,label='insertion')
# plt.plot(L,L_fusion,label='fusion')
# plt.plot(L,L_rapide,label='rapide')
# plt.plot(L,L_sort,label='sort')
# plt.legend(loc='upper left') # place la légende à haut à gauche si pas cette ligne la légende ne s'affiche pas
# plt.show()
# 
# 
# ### exercice 1 - cout temporel des algorithmes de tris les plus rapide : Question 2
# # le tri insertion est supprimé du test
# 
# 
# L_rapide2=[]
# L_fusion2=[]
# L_sort2=[]
# L=[i for i in range(0,20000,500)] # bien garder des sauts autrement trop long
# 
# for i in L:
#     L1=[]
#     for j in range(i):
#         L1.append(rd.randint(0,i)) #certains ont creer une fonction pour générer (ou engendrer) la liste aléatoire
#     # bien copier les listes autrement à la seconde fonction on trie une liste triée (voir algorithmes dans le fichier tris.py qui ne renvoient rien, la liste est modifiée sur place
#     L_f=L1[:]
#     L_q=L1[:]
#     td=time.time()
#     tri_fusion(L_f,0,len(L_f)-1)
#     tf=time.time()-td
#     L_fusion2.append(tf)
#     td=time.time()
#     tri_quicksort(L_q,0,len(L_f)-1)
#     tf=time.time()-td
#     L_rapide2.append(tf)
#     td=time.time()
#     L1.sort()
#     tf=time.time()-td
#     L_sort2.append(tf)
# 
# plt.figure()
# plt.grid()
# plt.xlabel('taille de la liste')
# plt.ylabel('temps de tri en seconde')
# plt.plot(L,L_fusion2,label='fusion')
# plt.plot(L,L_rapide2,label='rapide')
# plt.plot(L,L_sort2,label='sort')
# plt.legend(loc='upper left') # place la légende à haut à gauche si pas cette ligne la légende ne s'affiche pas
# plt.show()
# 
# ### exercice 1 - Question 3 : la complexite
# # en n², nlog(n) faire les calculs
# 
# 
# ### exercice 1 - Question 4 : une liste déjà triée essai sur tous les algorithmes
# liste_triee=[i for i in range(1000000)]
# tinit=time.time()
# tri_insertion(liste_triee)
# print ('temps de tri d\'une liste triée',time.time()-tinit)
# tinit=time.time()
# liste_triee.sort()
# print ('temps de tri d\'une liste triée par sort',time.time()-tinit)
# 
# # ça bloque pour tri_quicksort et tri fusion, il faudra alors interrompre le processus pour les élèves, sur pyzo c'est l'icône 'eclair', sous linux : ouvrir un terminal, ecrire xkill à l'invite et avec précaution cliquer sur la fenetre de l'IDLE
# 
# ### je me suis arretee ici avec les PT





### exercice 2 : le tour de france
### lecture des fichiers
# 'classement_general.txt'
# 'etape_10.txt'
# >>> (executing lines 1 to 86 of "TP_tri.py")
# ['1.', 'GBRFROOME', 'Christopher', '31', 'TEAM', 'SKY', '31h', "34'", "12''"]

### exercice 2 : question 1

def charge_classement1(fichier): #un peu lourd car le split n'est pas complet
    f=open(fichier,'r')
    fichier=f.readlines()
    f.close() #ne pas oublier de fermer le fichier...
    L=[]
    for ligne in fichier:
        ligne=ligne.split() # ligne=ligne.split('\t') pour avoir les noms et prenom ensemble
        L1=[]
        L1.append(ligne[1])
        i=1
        while ligne[i][0] not in '0123456789':
            i=i+1
        L1.append(int(ligne[i]))
        i=i+1
        while ligne[i][0] not in '0123456789':
            i=i+1
        temps=int(ligne[i+2][0:2])+60*int(ligne[i+1][0:2])+3600*int(ligne[i][0:2])
        L1.append(temps)
        L.append(L1)
    
    return L
    
def charge_classement(fichier):
    f=open(fichier,'r',encoding="utf-8")
    fichier=f.readlines()
    f.close() #ne pas oublier de fermer le fichier...
    L=[]
    for ligne in fichier:
        ligne=ligne.split('\t') # coupe aux tabulations
        L1=[]
        L1.append(ligne[1])
        L1.append(ligne[2])
        t_course=ligne[4].split()
        
        temps=int(t_course[2][0:2])+60*int(t_course[1][0:2])+3600*int(t_course[0][0:2])
        
        L1.append(temps)
        L.append(L1)
    return L
        
        
# >>> charge_classement('classement_general.txt')
# [['GBRFROOME Christopher', '31', 113652], ['USAVAN GARDEREN Tejay', '61', 113664
# ], ['BELVAN AVERMAET Greg', '68', 113679], ['SVKSAGAN Peter', '47', 113690], ['E
# SPCONTADOR Alberto', '41', 113715], ['COLURAN URAN Rigoberto', '118', 113730], [
# 'ESPVALVERDE BELMONTE Alejandro', '59', 113762], ['GBRTHOMAS Geraint', '39', 113
# 764], ['COLQUINTANA ROJAS Nairo Alexander', '51', 113771], ['CZESTYBAR Zdenek', 
# '116', 113771], ['FRAGALLOPIN Tony', '71', 113773], ['CZEKREUZIGER Roman', '44',
#  113790], ['ITANIBALI Vincenzo', '1', 113794], ['FRABARGUIL WARREN', '82', 11381






### question 2 : ajouter les temps de l'étape 10
LG=charge_classement('classement_general.txt')
L10=charge_classement('etape_10.txt')
# >>> len(LG)
# 185
# >>> len(L10)
# 183
# attention, les deux listes n'ont pas même longueur

def ajout_temps(L1,L2):
    '''L1 est la classement de l'étape et L2 le classement général certains ont été disqualifiés ou ont abandonné'''
    L=[]
    for dossard in L1:
        L.append(dossard)
        d=dossard[1]
        i=0
        while d!=L2[i][1]: #attention certains n'ont pas fait l'étape complètement et sont disqualifiés
            i=i+1
        L[-1][-1]=L[-1][-1]+L2[i][-1]
    return L
    
# >>> len(ajout_temps(L10,LG))
# 183
# >>> ajout_temps(L10,LG)
# [['GBRFROOME Christopher', '31', 129379], ['AUSPORTE Richie', '35', 132082], ['C
# OLQUINTANA ROJAS Nairo Alexander', '51', 129562], ['NEDGESINK Robert', '131', 12
# 9644], ['ESPVALVERDE BELMONTE Alejandro', '59', 129610], ['GBRTHOMAS Geraint', '
# 39', 129612], ['GBRYATES Adam', '108', 130568], ['FRAROLLAND Pierre', '121', 130
# 206], ['FRAGALLOPIN Tony', '71', 129642], ['USAVAN GARDEREN Tejay', '61', 129541
# ], ['ESPCONTADOR Alberto', '41', 129613], ['ESPVALLS FERRI Rafael', '159', 13249
# 6], ['DENFUGLSANG Jakob', '3', 129890], ['BELPAUWELS Serge', '218', 131346], ['F
# RABARGUIL WARREN', '82', 129741], ['ESPSANCHEZ Samuel', '66', 129996], ['NEDMOLL
# EMA Bauke', '141', 129804], ['RSAJANSE VAN RENSBURG Jacques', '214', 131164], ['



### exercice 2 : question 3 : tri par insertion



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
tri_insertion_modifie(ajout_temps(L10,LG))
print('tri insertion des coureurs prend ',time.time()-td,'s')
    
# >>> tri_insertion_modifie( [['GBRFROOME', 31, 129379], ['AUSPORTE', 35, 132082], ['COLQUINTANA', 51, 129562], ['NEDGESIN', 131, 129644], ['ESPVALVERDE', 59, 129610], ['GBRTHOMAS', 39, 129612], ['GBRYATES', 108, 130568], ['FRAROLLAND', 121, 130206], ['FRAGALLOPIN', 71, 129642], ['USAVAN', 61, 129541], ['ESPCONTADOR', 41, 129613], ['ESPVALLS', 159, 132496], ['DENFUGLSANG', 3, 129890], ['BELPAUWELS', 218, 131346], ['FRABARGUIL', 82, 129741], ['ESPSANCHEZ', 66, 129996], ['NEDMOLLEMA', 141, 129804], ['RSAJANSE', 214, 131164], ['ARGSEPULVEDA', 201, 130380], ['ESTKANGERT', 6, 131285], ['ITANIBALI', 1, 129786], ['NEDTEN', 137, 133290]])
# [['GBRFROOME', 31, 129379], ['USAVAN', 61, 129541], ['COLQUINTANA', 51, 129562], ['ESPVALVERDE', 59, 129610], ['GBRTHOMAS', 39, 129612], ['ESPCONTADOR', 41, 129613], ['FRAGALLOPIN', 71, 129642], ['NEDGESIN', 131, 129644], ['FRABARGUIL', 82, 129741], ['ITANIBALI', 1, 129786], ['NEDMOLLEMA', 141, 129804], ['DENFUGLSANG', 3, 129890], ['ESPSANCHEZ', 66, 129996], ['FRAROLLAND', 121, 130206], ['ARGSEPULVEDA', 201, 130380], ['GBRYATES', 108, 130568], ['RSAJANSE', 214, 131164], ['ESTKANGERT', 6, 131285], ['BELPAUWELS', 218, 131346], ['AUSPORTE', 35, 132082], ['ESPVALLS', 159, 132496], ['NEDTEN', 137, 133290]]

liste_non_triee=[['GBRFROOME', 31, 129379], ['AUSPORTE', 35, 132082], ['COLQUINTANA', 51, 129562], ['NEDGESIN', 131, 129644], ['ESPVALVERDE', 59, 129610], ['GBRTHOMAS', 39, 129612], ['GBRYATES', 108, 130568], ['FRAROLLAND', 121, 130206], ['FRAGALLOPIN', 71, 129642], ['USAVAN', 61, 129541], ['ESPCONTADOR', 41, 129613], ['ESPVALLS', 159, 132496], ['DENFUGLSANG', 3, 129890], ['BELPAUWELS', 218, 131346], ['FRABARGUIL', 82, 129741], ['ESPSANCHEZ', 66, 129996], ['NEDMOLLEMA', 141, 129804], ['RSAJANSE', 214, 131164], ['ARGSEPULVEDA', 201, 130380], ['ESTKANGERT', 6, 131285], ['ITANIBALI', 1, 129786], ['NEDTEN', 137, 133290]]

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
tri_quicksort_modifie(ajout_temps(L10,LG),0,len(L10)-1)
print('tri rapide des coureurs prend ',time.time()-td,'s')
        
# >>> tri_quicksort_modifie(liste_non_triee,0,len(liste_non_triee)-1)
# >>> liste_non_triee qui est triée par quicksort
# [['GBRFROOME', 31, 129379], ['USAVAN', 61, 129541], ['COLQUINTANA', 51, 129562], ['ESPVALVERDE', 59, 129610], ['GBRTHOMAS', 39, 129612], ['ESPCONTADOR', 41, 129613], ['FRAGALLOPIN', 71, 129642], ['NEDGESIN', 131, 129644], ['FRABARGUIL', 82, 129741], ['ITANIBALI', 1, 129786], ['NEDMOLLEMA', 141, 129804], ['DENFUGLSANG', 3, 129890], ['ESPSANCHEZ', 66, 129996], ['FRAROLLAND', 121, 130206], ['ARGSEPULVEDA', 201, 130380], ['GBRYATES', 108, 130568], ['RSAJANSE', 214, 131164], ['ESTKANGERT', 6, 131285], ['BELPAUWELS', 218, 131346], ['AUSPORTE', 35, 132082], ['ESPVALLS', 159, 132496], ['NEDTEN', 137, 133290]]




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
tri_fusion_modifie(ajout_temps(L10,LG),0,len(L10)-1)
print('tri fusion des coureurs prend ',time.time()-td,'s')
        
        
# >>> tri_fusion_modifie(liste_non_triee,0,len(liste_non_triee)-1)
# >>> liste_non_triee maintenant triée
# [['GBRFROOME', 31, 129379], ['USAVAN', 61, 129541], ['COLQUINTANA', 51, 129562], ['ESPVALVERDE', 59, 129610], ['GBRTHOMAS', 39, 129612], ['ESPCONTADOR', 41, 129613], ['FRAGALLOPIN', 71, 129642], ['NEDGESIN', 131, 129644], ['FRABARGUIL', 82, 129741], ['ITANIBALI', 1, 129786], ['NEDMOLLEMA', 141, 129804], ['DENFUGLSANG', 3, 129890], ['ESPSANCHEZ', 66, 129996], ['FRAROLLAND', 121, 130206], ['ARGSEPULVEDA', 201, 130380], ['GBRYATES', 108, 130568], ['RSAJANSE', 214, 131164], ['ESTKANGERT', 6, 131285], ['BELPAUWELS', 218, 131346], ['AUSPORTE', 35, 132082], ['ESPVALLS', 159, 132496], ['NEDTEN', 137, 133290]]



### avec la fonction prédéfinie dans python 'sorted' il faut créer une fonction lambda pour travailler sur le 3e élément de chaque élément de la liste
lambda colonnes: colonnes[2]
sorted(ajout_temps(L10,LG), key=lambda colonnes: colonnes[2])

# [['GBRFROOME', 31, 129379], ['USAVAN', 61, 129541], ['COLQUINTANA', 51, 129562], ['ESPVALVERDE', 59, 129610], ['GBRTHOMAS', 39, 129612], ['ESPCONTADOR', 41, 129613], ['FRAGALLOPIN', 71, 129642], ['NEDGESIN', 131, 129644], ['FRABARGUIL', 82, 129741], ['ITANIBALI', 1, 129786], ['NEDMOLLEMA', 141, 129804], ['DENFUGLSANG', 3, 129890], ['ESPSANCHEZ', 66, 129996], ['FRAROLLAND', 121, 130206], ['ARGSEPULVEDA', 201, 130380], ['GBRYATES', 108, 130568], ['RSAJANSE', 214, 131164], ['ESTKANGERT', 6, 131285], ['BELPAUWELS', 218, 131346], ['AUSPORTE', 35, 132082], ['ESPVALLS', 159, 132496], ['NEDTEN', 137, 133290]]

td=time.time()
sorted(ajout_temps(L10,LG), key=lambda colonnes: colonnes[2])
print('tri sort python des coureurs prend ',time.time()-td,'s')


# tri insertion des coureurs prend  0.007005929946899414 s
# tri rapide des coureurs prend  0.004002094268798828 s
# tri fusion des coureurs prend  0.004002809524536133 s
# tri sort python des coureurs prend  0.0030019283294677734 s



### Classement en cours d'étape - implémentation d'une file
### question 5 : L10 est déjà créée et est considérée comme une file qd elle est triée
L10_triee=sorted(charge_classement('etape_10.txt'), key=lambda colonnes: colonnes[2])

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
    
# >>> ajout(sorted(charge_classement('etape_10.txt'), key=lambda colonnes: colonnes[2]),LG)
# [['GBRFROOME', 31, 129379], ['USAVAN', 61, 129541], ['COLQUINTANA', 51, 129562],
#  ['ESPVALVERDE', 59, 129610], ['GBRTHOMAS', 39, 129612], ['ESPCONTADOR', 41, 129
# 613], ['FRAGALLOPIN', 71, 129642], ['NEDGESINK', 131, 129644], ['FRABARGUIL', 82
# , 129741], ['ITANIBALI', 1, 129786], ['NEDMOLLEMA', 141, 129804], ['COLURAN', 11
# 8, 129811], ['DENFUGLSANG', 3, 129890], ['FRAPÉRAUD', 11, 129927], ['SUIFRANK', 
# 181, 129935], ['ESPRODRIGUEZ', 91, 129978], ['ESPSANCHEZ', 66, 129996], ['CZEKRE
# UZIGER', 44, 130120], ['ESPIZAGIRRE', 57, 130136], ['FRAVUILLERMOZ', 19, 130152]

### question 7  : enfiler serait utiliser si le classement se faisait en temps réel
    






