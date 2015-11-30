import os
os.chdir(r'J:\annee 2015 2016\PT\IPT\03_Tris')

### algorithme de tri

from tris_2 import *
import random as rd
import time
import matplotlib.pyplot as plt
import sys
sys.setrecursionlimit(100000)

### exercice 1 - cout temporel des algorithmes de tris
ti=time.time()
L_insert=[]
L_rapide=[]
L_fusion=[]
L_sort=[]
L=[i for i in range(0,10001,1000)]
# pour des listes allant jusqu'à 1000 éléments mon ordi met 1 minute à faire tous les tris - image illisible
# pour les listes allant jusqu'à 10000 éléments avec des sauts de 500 éléments mon ordi met 1 minute à faire tous les calculs
# pour les listes allant jusqu'à 100000 éléments avec des sauts de 10000 éléments mon ordi met trop de minutes à faire tous les calculs
# pour les listes allant jusqu'à 20000 éléments avec des sauts de 2000 éléments mon ordi met 104 secondes à faire tous les calculs
for i in L:
    L1=[]
    for j in range(i):
        L1.append(rd.randint(0,i))
    L_i=L1[:]
    L_f=L1[:]
    L_q=L1[:]
    td=time.time()
    tri_insertion(L_i) #attention L1 est triée
    tf=time.time()-td
    L_insert.append(tf)
    td=time.time()
    tri_fusion(L_f,0,len(L_f)-1)
    tf=time.time()-td
    L_fusion.append(tf)
    td=time.time()
    quickSort(L_q)
    tf=time.time()-td
    L_rapide.append(tf)
    td=time.time()
    L1.sort()
    tf=time.time()-td
    L_sort.append(tf)
print(time.time()-ti)    
plt.figure()
plt.grid()
plt.xlabel('taille de la liste')
plt.ylabel('temps de tri en seconde')
plt.plot(L,L_insert,label='insertion')
plt.plot(L,L_fusion,label='fusion')
plt.plot(L,L_rapide,label='rapide')
plt.plot(L,L_sort,label='sort')
plt.legend(loc='upper left')
plt.show()



### exercice 2 : le tour de france
### lecture des fichiers
# 'classement_general.txt'
# 'etape_10.txt'
# >>> (executing lines 1 to 86 of "TP_tri.py")
# ['1.', 'GBRFROOME', 'Christopher', '31', 'TEAM', 'SKY', '31h', "34'", "12''"]

def charge_classement(fichier):
    f=open(fichier,'r')
    fichier=f.readlines()
    L=[]
    for ligne in fichier:
        ligne=ligne.split()
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
    f.close()
    return L
        
        
# >>> charge_classement('classement_general.txt')
# [['GBRFROOME', 31, 113652], ['USAVAN', 61, 113664], ['BELVAN', 68, 113679], ['SV
# KSAGAN', 47, 113690], ['ESPCONTADOR', 41, 113715], ['COLURAN', 118, 113730], ['E
# SPVALVERDE', 59, 113762], ['GBRTHOMAS', 39, 113764], ['COLQUINTANA', 51, 113771]
# , ['CZESTYBAR', 116, 113771], ['FRAGALLOPIN', 71, 113773], ['CZEKREUZIGER', 44, 
# 113790], ['ITANIBALI', 1, 113794], ['FRABARGUIL', 82, 113815], ['NEDGESINK', 131
# , 113824], ['NEDMOLLEMA', 141, 113828], ['FRAPÉRAUD', 11, 113862], ['ESPRODRIGUE
# Z', 91, 113884], ['USATALANSKY', 161, 113909], ['SUIFRANK', 181, 113924], ['FRAB
# ARDET', 12, 113930], ['BELBAKELANTS', 13, 113960], ['PORCOSTA', 151, 113972], ['
# DENFUGLSANG', 3, 113974], ['ESPSANCHEZ', 66, 114029], ['GERNERZ', 191, 66700], [
# 'ESPIZAGIRRE', 57, 114052], ['FRAVUILLERMOZ', 19, 114061], ['FRAPINOT', 21, 1141
# 37], ['SLOKOREN', 165, 114167], ['IRLMARTIN', 167, 114213], ['FRACHAVANEL', 183,
#  114213], ['NORBOASSON', 211, 114266], ['ESPLOSADA', 97, 114289], ['COLPANTANO',
#  188, 114332], ['FRAROLLAND', 121, 114355], ['GERVOSS', 199, 66705], ['ARGSEPULV
# EDA', 201, 114397], ['POLKWIATKOWSKI', 111, 114570], ['AUSROGERS', 46, 114609], 
# ['SUIMORABITO', 27, 114636], ['GERGESCHKE', 86, 114659], ['FRAGAUTIER', 123, 114
# 686], ['DENBAK', 72, 114690], ['NEDDE', 84, 114716], ['GBRYATES', 108, 114717], 
# ['UKRGRIVKO', 4, 114721], ['NEDTANKINK', 136, 114735], ['GBRYATES', 109, 114761]
# , ['FRALAPORTE', 173, 114833], ['POLGOLAS', 113, 114875], ['ESPCASTROVIEJO', 53,
#  114885], ['RSAJANSE', 215, 114906], ['FRACHEREL', 14, 114906], ['ITAOSS', 64, 1
# 14911], ['GERGREIPEL', 75, 114964], ['GERDEGENKOLB', 81, 114987], ['FRASOUPE', 1
# 78, 114997], ['NEDVAN', 138, 115032], ['FRALADAGNOUS', 26, 115033], ['GERSIEBERG
# ', 78, 115034], ['BELVANMARCKE', 139, 115038], ['GBRCAVENDISH', 112, 115063], ['
# SUISCHÄR', 67, 115081], ['NEDSINKELDAM', 88, 115104], ['FRASICARD', 127, 115123]
# , ['BELVERMOTE', 119, 115124], ['NEDCURVERS', 83, 115139], ['FRAVAUGRENARD', 29,
#  115142], ['FRASIMON', 177, 115157], ['ESTTAARAMÄE', 8, 115163], ['IRLROCHE', 36
# , 115177], ['RSAJANSE', 214, 115188], ['FRASENECHAL', 176, 115194], ['FRACOQUARD
# ', 122, 115209], ['SUIRAST', 148, 115236], ['AUSDENNIS', 63, 115241], ['SUIWYSS'
# , 69, 115246], ['FRADEMARE', 24, 115263], ['NORKRISTOFF', 96, 115286], ['CZEBART
# A', 192, 66721], ['ESTKANGERT', 6, 115293], ['AUTPREIDLER', 87, 115294], ['PORMA
# CHADO', 98, 115306], ['ESPZUBELDIA', 149, 115331], ['LTUNAVARDAUSKAS', 168, 1153
# 34], ['NEDLEEZER', 134, 115336], ['GERMARTENS', 135, 115351], ['FRAFONSECA', 206
# , 115371], ['AUSDEMPSTER', 195, 66722], ['ITABENNATI', 43, 115392], ['GBRSTANNAR
# D', 38, 115396], ['BELPAUWELS', 218, 115420], ['FRADELAPLACE', 203, 115431], ['F
# RAVACHON', 209, 115453], ['NEDKRUIJSWIJK', 133, 115469], ['ESPIRIZAR', 146, 1154
# 71], ['ITAQUINZIATO', 65, 115486], ['DENANDERSEN', 49, 115514], ['AUSRENSHAW', 1
# 15, 115527], ['ITATRENTIN', 117, 115548], ['SUIHOLLENSTEIN', 187, 115555], ['ITA
# MALORI', 58, 115569], ['SUIWYSS', 189, 115578], ['LUXGASTAUER', 15, 115581], ['N
# EDKELDERMAN', 132, 115606], ['USAFARRAR', 213, 115610], ['ITAPOZZATO', 157, 1156
# 18], ['ERITEKLEHAIMANOT', 219, 115671], ['COLSERPA', 158, 115701], ['FRATULIK', 
# 128, 115702], ['BELWELLENS', 79, 115714], ['FRAFEDRIGO', 204, 115723], ['NEDWEST
# RA', 9, 115739], ['POROLIVEIRA', 155, 115758], ['ESPMATE', 174, 115760], ['POLHU
# ZARSKI', 196, 66729], ['NEDCLEMENT', 184, 115779], ['FRAROY', 28, 115827], ['FRA
# GENE', 124, 115833], ['CRODURASEK', 154, 115838], ['CANHESJEDAL', 164, 115840], 
# ['ITACARUSO', 62, 115840], ['FRAGERARD', 207, 115841], ['ITASCARPONI', 7, 115864
# ], ['ITAGUARNIERI', 93, 115918], ['FRAGAUDIN', 16, 115920], ['AUTBRÄNDLE', 182, 
# 115935], ['ESPNAVARRO', 175, 115989], ['CZEKONIG', 33, 115990], ['FRAQUEMENEUR',
#  126, 116020], ['GBRROWE', 37, 116023], ['COLARREDONDO', 142, 116045], ['FRARIBL
# ON', 17, 116052], ['POLMAJKA', 45, 116113], ['ITACARUSO', 92, 116147], ['LUXJUNG
# ELS', 147, 116168], ['AUSDURBRIDGE', 103, 116206], ['AUSHAAS', 163, 116227], ['F
# RAGENIEZ', 25, 116251], ['FRACOPPEL', 185, 116255], ['SUIELMIGER', 186, 116261],
#  ['FRAFEILLU', 205, 116261], ['AUSPORTE', 35, 116296], ['FRAPERICHON', 208, 1163
# 53], ['ESPHERRADA', 56, 116361], ['ESPERVITI', 55, 116411], ['FRACHAVANEL', 23, 
# 116455], ['NEDPOELS', 34, 116462], ['NEDTIMMER', 89, 116524], ['COLANACONA', 52,
#  116571], ['BELVANBILSEN', 179, 116571], ['ESPVALLS', 159, 116580], ['NEDLANGEVE
# LD', 166, 116609], ['ESPPLAZA', 156, 116615], ['BELDEBUSSCHERE', 74, 116667], ['
# ITACIMOLAI', 153, 116726], ['ITABASSO', 42, 116735], ['NEDBOOM', 2, 116736], ['N
# EDVAN', 169, 116753], ['GBRCUMMINGS', 212, 116763], ['KAZGRUZDEV', 5, 116772], [
# 'GBRKENNAUGH', 32, 116779], ['ITATOSATTO', 48, 116782], ['ERIKUDUS', 216, 116795
# ], ['LUXDIDIER', 145, 116809], ['FRANAULLEAU', 125, 116826], ['PORPIMANTA', 197,
#  66747], ['AUTHALLER', 94, 116848], ['BELDEVOLDER', 144, 116850], ['FRAVOECKLER'
# , 129, 116862], ['ITABONO', 152, 116916], ['RSAMEINTJES', 217, 116919], ['GERBUC
# HMANN', 194, 66749], ['NEDWEENING', 107, 117081], ['BELDE', 73, 117209], ['IRLBE
# NNETT', 193, 66754], ['NEDTEN', 137, 117298], ['BELVAN', 18, 117363], ['CANTUFT'
# , 106, 117509], ['FRABRUN', 202, 117612], ['AUSHANSEN', 76, 117624], ['FRAEDET',
#  172, 117846], ['GBRDOWSETT', 54, 118033], ['AUSMATTHEWS', 105, 118222]]


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
# [['GBRFROOME', 31, 129379], ['AUSPORTE', 35, 132082], ['COLQUINTANA', 51, 129562
# ], ['NEDGESINK', 131, 129644], ['ESPVALVERDE', 59, 129610], ['GBRTHOMAS', 39, 12
# 9612], ['GBRYATES', 108, 130568], ['FRAROLLAND', 121, 130206], ['FRAGALLOPIN', 7
# 1, 129642], ['USAVAN', 61, 129541], ['ESPCONTADOR', 41, 129613], ['ESPVALLS', 15
# 9, 132496], ['DENFUGLSANG', 3, 129890], ['BELPAUWELS', 218, 131346], ['FRABARGUI
# L', 82, 129741], ['ESPSANCHEZ', 66, 129996], ['NEDMOLLEMA', 141, 129804], ['RSAJ
# ANSE', 214, 131164], ['ARGSEPULVEDA', 201, 130380], ['ESTKANGERT', 6, 131285], [
# 'ITANIBALI', 1, 129786], ['NEDTEN', 137, 133290], ['SUIFRANK', 181, 129935], ['R
# SAMEINTJES', 217, 132984], ['FRAPÉRAUD', 11, 129927], ['FRAVOECKLER', 129, 13292
# 7], ['FRACOPPEL', 185, 132328], ['COLURAN', 118, 129811], ['AUSROGERS', 46, 1306
# 93], ['ESPIZAGIRRE', 57, 130136], ['FRAVUILLERMOZ', 19, 130152], ['NEDKRUIJSWIJK
# ', 133, 131560], ['NEDPOELS', 34, 132553], ['ESPRODRIGUEZ', 91, 129978], ['ESPZU
# BELDIA', 149, 131433], ['GERBUCHMANN', 194, 131817], ['GERNERZ', 191, 131768], [
# 'POLHUZARSKI', 196, 131797], ['FRAFEILLU', 205, 132468], ['COLPANTANO', 188, 130
# 539], ['FRAGAUTIER', 123, 130904], ['FRASOUPE', 178, 131224], ['BELBAKELANTS', 1
# 3, 130217], ['FRABARDET', 12, 130187], ['CANHESJEDAL', 164, 132097], ['ITACARUSO
# ', 92, 132404], ['FRACHEREL', 14, 131188], ['POLMAJKA', 45, 132432], ['FRAPINOT'
# , 21, 130467], ['SUIMORABITO', 27, 130966], ['CZEKREUZIGER', 44, 130120], ['ITAC
# ARUSO', 62, 132170], ['SUIWYSS', 189, 131908], ['DENBAK', 72, 131020], ['NEDWEST
# RA', 9, 132128], ['ESPHERRADA', 56, 132781], ['IRLMARTIN', 167, 130634], ['USATA
# LANSKY', 161, 130330], ['FRAFEDRIGO', 204, 132159], ['FRASICARD', 127, 131582], 
# ['ERIKUDUS', 216, 133254], ['FRADELAPLACE', 203, 131915], ['LUXJUNGELS', 147, 13
# 2668], ['ESPLOSADA', 97, 130789], ['ESPCASTROVIEJO', 53, 131433], ['FRAGENIEZ', 
# 25, 132799], ['FRAQUEMENEUR', 126, 132568], ['ESPIRIZAR', 146, 132019], ['COLANA
# CONA', 52, 133119], ['AUTPREIDLER', 87, 131842], ['NEDKELDERMAN', 132, 132154], 
# ['FRAPERICHON', 208, 132901], ['UKRGRIVKO', 4, 131269], ['BELDE', 73, 133757], [
# 'IRLROCHE', 36, 131735], ['FRAEDET', 172, 134422], ['GERGESCHKE', 86, 131254], [
# 'PORMACHADO', 98, 131920], ['FRAROY', 28, 132488], ['GERVOSS', 199, 131782], ['C
# ZEKONIG', 33, 132662], ['ITASCARPONI', 7, 132560], ['ESPNAVARRO', 175, 132716], 
# ['ESPMATE', 174, 132487], ['BELDEVOLDER', 144, 133577], ['ESPPLAZA', 156, 133342
# ], ['CRODURASEK', 154, 132565], ['POROLIVEIRA', 155, 132485], ['GBRKENNAUGH', 32
# , 133506], ['PORPIMANTA', 197, 131825], ['SUISCHÄR', 67, 131808], ['FRAFONSECA',
#  206, 132098], ['NEDTANKINK', 136, 131462], ['RSAJANSE', 215, 131633], ['SLOKORE
# N', 165, 130894], ['NEDCURVERS', 83, 131866], ['FRACHAVANEL', 183, 130940], ['CZ
# EBARTA', 192, 131799], ['GBRCUMMINGS', 212, 133490], ['PORCOSTA', 151, 130699], 
# ['NEDDE', 84, 131443], ['SUIRAST', 148, 131963], ['FRABRUN', 202, 134339], ['KAZ
# GRUZDEV', 5, 133499], ['NORBOASSON', 211, 130993], ['BELVANMARCKE', 139, 131855]
# , ['GERMARTENS', 135, 132168], ['DENANDERSEN', 49, 132331], ['SUIWYSS', 69, 1320
# 63], ['FRAVACHON', 209, 132270], ['NEDTIMMER', 89, 133341], ['ITATOSATTO', 48, 1
# 33599], ['ITABENNATI', 43, 132209], ['COLARREDONDO', 142, 132965], ['FRATULIK', 
# 128, 132672], ['FRAGENE', 124, 132803], ['BELVAN', 68, 130649], ['BELDEBUSSCHERE
# ', 74, 133637], ['GBRYATES', 109, 131757], ['NEDCLEMENT', 184, 132800], ['AUTBRÄ
# NDLE', 182, 132956], ['AUSHAAS', 163, 133248], ['ESPERVITI', 55, 133432], ['USAF
# ARRAR', 213, 132631], ['SUIELMIGER', 186, 133282], ['ITAMALORI', 58, 132590], ['
# NEDSINKELDAM', 88, 132125], ['SUIHOLLENSTEIN', 187, 132576], ['FRASENECHAL', 176
# , 132215], ['NEDWEENING', 107, 134102], ['BELVERMOTE', 119, 132145], ['ERITEKLEH
# AIMANOT', 219, 132692], ['POLGOLAS', 113, 131896], ['GBRDOWSETT', 54, 135054], [
# 'NEDVAN', 138, 132053], ['AUSDURBRIDGE', 103, 133227], ['FRARIBLON', 17, 133073]
# , ['FRAGERARD', 207, 132862], ['AUSDENNIS', 63, 132285], ['GERDEGENKOLB', 81, 13
# 2053], ['ITAQUINZIATO', 65, 132555], ['ITAPOZZATO', 157, 132687], ['FRALADAGNOUS
# ', 26, 132102], ['GERSIEBERG', 78, 132103], ['GERGREIPEL', 75, 132033], ['ITABON
# O', 152, 133985], ['COLSERPA', 158, 132770], ['FRANAULLEAU', 125, 133895], ['ITA
# OSS', 64, 131980], ['ESTTAARAMÄE', 8, 132232], ['BELWELLENS', 79, 132783], ['FRA
# VAUGRENARD', 29, 132211], ['FRASIMON', 177, 132226], ['AUSHANSEN', 76, 134693], 
# ['ITAGUARNIERI', 93, 132994], ['FRAGAUDIN', 16, 132996], ['NORKRISTOFF', 96, 132
# 364], ['SVKSAGAN', 47, 130776], ['POLKWIATKOWSKI', 111, 131698], ['CZESTYBAR', 1
# 16, 130899], ['NEDVAN', 169, 133881], ['NEDLANGEVELD', 166, 133737], ['LUXDIDIER
# ', 145, 133937], ['LUXGASTAUER', 15, 132709], ['IRLBENNETT', 193, 131839], ['AUT
# HALLER', 94, 133976], ['FRALAPORTE', 173, 131961], ['BELVANBILSEN', 179, 133699]
# , ['GBRROWE', 37, 133151], ['FRACOQUARD', 122, 132337], ['GBRCAVENDISH', 112, 13
# 2191], ['ITATRENTIN', 117, 132676], ['GBRSTANNARD', 38, 132524], ['AUSRENSHAW', 
# 115, 132655], ['AUSDEMPSTER', 195, 131807], ['LTUNAVARDAUSKAS', 168, 132462], ['
# CANTUFT', 106, 134637], ['NEDLEEZER', 134, 132464], ['BELVAN', 18, 134491], ['IT
# ACIMOLAI', 153, 133868], ['FRADEMARE', 24, 132577], ['AUSMATTHEWS', 105, 135536]
# , ['FRACHAVANEL', 23, 133937]]    
### tri par insertion

### modifications des algorithmes de tri pour travailler sur la 3eme valeur

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
    






