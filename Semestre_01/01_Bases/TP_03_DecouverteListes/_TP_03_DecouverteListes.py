# -*- coding: utf-8 -*-


## Listes d'entiers de [O à n[
def generer_liste_entiers_01_corrige(n: int) -> list :
    res = []
    for i in range(n):
        res.append(i)
    return res

def generer_liste_entiers_01_test(foo,n):
    if foo(n) == generer_liste_entiers_01_corrige(n):
        print(f"Test generer_liste_entiers_01({n}) : réussi")
    else :
        print(f"Test generer_liste_entiers_01({n}) : échoué")


def generer_liste_entiers_02_corrige(n: int) -> list :
    res = []
    i = 0
    while i<n :
        res.append(i)
        i = i+1
    return res

def generer_liste_entiers_02_test(foo,n):
    if foo(n) == generer_liste_entiers_02_corrige(n):
        print(f"Test generer_liste_entiers_02({n}) : réussi")
    else :
        print(f"Test generer_liste_entiers_02({n}) : échoué")


def generer_liste_entiers_03_corrige(n: int) -> list :
    return[ i for i in range(n)]

def generer_liste_entiers_03_test(foo,n):
    if foo(n) == generer_liste_entiers_03_corrige(n):
        print(f"Test generer_liste_entiers_03({n}) : réussi")
    else :
        print(f"Test generer_liste_entiers_03({n}) : échoué")



## Listes d'entiers de [a à b]
def generer_liste_entiers_04_corrige(deb: int, fin: int) -> list :
    res = []
    for i in range(deb,fin+1):
        res.append(i)
    return res   
    
def generer_liste_entiers_04_test(foo,a,b):
    if foo(a,b) == generer_liste_entiers_04_corrige(a,b):
        print(f"Test generer_liste_entiers_04({a,b}) : réussi")
    else :
        print(f"Test generer_liste_entiers_04({a,b}) : échoué")



def generer_liste_entiers_05_corrige(deb: int, fin: int) -> list :
    res = []
    i = deb
    while i <=fin :
        res.append(i)
        i = i +1
    return res   
    
def generer_liste_entiers_05_test(foo,a,b):
    if foo(a,b) == generer_liste_entiers_05_corrige(a,b):
        print(f"Test generer_liste_entiers_05({a,b}) : réussi")
    else :
        print(f"Test generer_liste_entiers_05({a,b}) : échoué")



def generer_liste_entiers_06_corrige(deb: int, fin: int) -> list :
     return [i for i in range(deb,fin+1)]
    
def generer_liste_entiers_06_test(foo,a,b):
    if foo(a,b) == generer_liste_entiers_06_corrige(a,b):
        print(f"Test generer_liste_entiers_06({a,b}) : réussi")
    else :
        print(f"Test generer_liste_entiers_06({a,b}) : échoué")



## Liste d'entiers
def generer_liste_pairs_corrige(nb:int):
    res=[]
    for i in range(nb//2):
        res.append(2*i)
    return(res)

def generer_liste_pairs_test(foo,n):
    if foo(n) == generer_liste_pairs_corrige(n):
        print(f"Test generer_liste_pairs({n}) : réussi")
    else :
        print(f"Test generer_liste_pairs({n}) : échoué")
        
def generer_liste_impairs_corrige(nb:int):
    res=[]
    for i in range(nb//2):
        res.append(2*i+1)
    return(res)

def generer_liste_impairs_test(foo,n):
    if foo(n) == generer_liste_impairs_corrige(n):
        print(f"Test generer_liste_impairs({n}) : réussi")
    else :
        print(f"Test generer_liste_impairs({n}) : échoué")


## Existence d'une valeur dans une liste
def recherche_nb_01_corrige(nb:int,L:list):
    test=False
    for x in L:
        if nb==x:
            test=True
    return(test)

def recherche_nb_test(foo):
    L = [0,1,2,3,4,3]
    nb = 0
    if foo(nb,L) == recherche_nb_01_corrige(nb,L):
        print(f"Test recherche_nb({nb,L}) : réussi")
    else :
        print(f"Test recherche_nb({nb,L}) : échoué")
    nb = 3
    if foo(nb,L) == recherche_nb_01_corrige(nb,L):
        print(f"Test recherche_nb({nb,L}) : réussi")
    else :
        print(f"Test recherche_nb({nb,L}) : échoué")
    nb = 4
    if foo(nb,L) == recherche_nb_01_corrige(nb,L):
        print(f"Test recherche_nb({nb,L}) : réussi")
    else :
        print(f"Test recherche_nb({nb,L}) : échoué")
    nb = 5
    if foo(nb,L) == recherche_nb_01_corrige(nb,L):
        print(f"Test recherche_nb({nb,L}) : réussi")
    else :
        print(f"Test recherche_nb({nb,L}) : échoué")

def recherche_nb_02_corrige(nb:int,L:list):
    n=len(L)
    i=0
    while i<=n-1 and nb!=L[i]:
        i=i+1
    return(i<n)

def recherche_nb_03_corrige(nb:int, L:list):
    return(nb in L)


## Q6 à Q10
def recherche_first_index_nb_01_corrige(nb:int, L:list):
    n=len(L)
    index=-1
    for i in range(n):
        if nb==L[i] and index==-1:
            index=i
    return(index)

def recherche_first_index_nb_test(foo):
    L = [0,1,2,3,4,3]
    nb = 0
    if foo(nb,L) == recherche_first_index_nb_01_corrige(nb,L):
        print(f"Test recherche_first_index_nb({nb,L}) : réussi")
    else :
        print(f"Test recherche_first_index_nb({nb,L}) : échoué")
    nb = 3
    if foo(nb,L) == recherche_first_index_nb_01_corrige(nb,L):
        print(f"Test recherche_first_index_nb({nb,L}) : réussi")
    else :
        print(f"Test recherche_first_index_nb({nb,L}) : échoué")
    nb = 4
    if foo(nb,L) == recherche_first_index_nb_01_corrige(nb,L):
        print(f"Test recherche_first_index_nb({nb,L}) : réussi")
    else :
        print(f"Test recherche_first_index_nb_01({nb,L}) : échoué")
    nb = 5
    if foo(nb,L) == recherche_first_index_nb_01_corrige(nb,L):
        print(f"Test recherche_first_index_nb({nb,L}) : réussi")
    else :
        print(f"Test recherche_first_index_nb({nb,L}) : échoué")


def recherche_first_index_nb_02(nb:int, L:list):
    n=len(L)
    i=0
    while i<=n-1 and nb!=L[i]:
        i=i+1
    if i<n:
        index=i
    else:
        index=-1
    return(index)



def recherche_last_index_nb_01_corrige(nb:int, L:list):
    n=len(L)
    index=-1
    for i in range(n):
        if nb==L[i]:
            index=i
    return(index)

def recherche_last_index_nb_02_corrige(nb:int, L:list):
    n=len(L)
    i=n-1   # On part de la fin de la liste
    while i>=0 and nb!=L[i]:
        i=i-1
    if i>0:
        index=i
    else:
        index=-1
    return(index)



def recherche_last_index_nb_test(foo):
    L = [0,1,2,3,4,3]
    nb = 0
    if foo(nb,L) == recherche_last_index_nb_01_corrige(nb,L):
        print(f"Test recherche_last_index_nb({nb,L}) : réussi")
    else :
        print(f"Test recherche_last_index_nb({nb,L}) : échoué")
    nb = 3
    if foo(nb,L) == recherche_last_index_nb_01_corrige(nb,L):
        print(f"Test recherche_last_index_nb({nb,L}) : réussi")
    else :
        print(f"Test recherche_last_index_nb({nb,L}) : échoué")
    nb = 4
    if foo(nb,L) == recherche_last_index_nb_01_corrige(nb,L):
        print(f"Test recherche_last_index_nb({nb,L}) : réussi")
    else :
        print(f"Test recherche_last_index_nb({nb,L}) : échoué")
    nb = 5
    if foo(nb,L) == recherche_last_index_nb_01_corrige(nb,L):
        print(f"Test recherche_last_index_nb({nb,L}) : réussi")
    else :
        print(f"Test recherche_last_index_nb({nb,L}) : échoué")



def recherche_index_nb_01_corrige(nb:int, L:list):
    res=[]
    n=len(L)
    for i in range(n):
        if L[i]==nb:
            res.append(i)
    return(res)


def recherche_index_nb_test(foo):
    L = [0,1,2,3,4,3]
    nb = 0
    if foo(nb,L) == recherche_index_nb_01_corrige(nb,L):
        print(f"Test recherche_index_nb({nb,L}) : réussi")
    else :
        print(f"Test recherche_index_nb({nb,L}) : échoué")
    nb = 3
    if foo(nb,L) == recherche_index_nb_01_corrige(nb,L):
        print(f"Test recherche_index_nb({nb,L}) : réussi")
    else :
        print(f"Test recherche_index_nb({nb,L}) : échoué")
    nb = 4
    if foo(nb,L) == recherche_index_nb_01_corrige(nb,L):
        print(f"Test recherche_index_nb({nb,L}) : réussi")
    else :
        print(f"Test recherche_index_nb({nb,L}) : échoué")
    nb = 5
    if foo(nb,L) == recherche_index_nb_01_corrige(nb,L):
        print(f"Test recherche_index_nb({nb,L}) : réussi")
    else :
        print(f"Test recherche_index_nb({nb,L}) : échoué")


## Q11 et Q12

def is_char_in_str_01_corrige(lettre:str,mot:str):
    n=len(mot)
    i=0
    while i<=n-1 and lettre!=mot[i]:
        i=i+1
    return(i<n)

def is_char_in_str_test(foo,lettre,mot):
    if foo(lettre,mot) == is_char_in_str_01_corrige(lettre,mot):
        print(f"Test is_char_in_str({lettre,mot}) : réussi")
    else :
        print(f"Test is_char_in_str({lettre,mot}) : échoué")
        

def is_char_in_str_02(lettre:str,mot:str):
    return(lettre in mot)

## Q13

def compte_lettre_01_corrige(lettre:str, mot:str):
    nb=0
    for x in mot:
        if x==lettre:
            nb=nb+1
    return(nb)

def compte_lettre_test(foo,lettre,mot):
    if foo(lettre,mot) == compte_lettre_01_corrige(lettre,mot):
        print(f"Test compte_lettre({lettre,mot}) : réussi")
    else :
        print(f"Test compte_lettre({lettre,mot}) : échoué")

#######

alphabet='abcdefghijklmnopqrstuvwxyz'
def load_fichier(file):
    f=open(file,'r')
    mots=f.readlines()
    f.close()
    dico=[]
    for mot in mots:
        dico.append(mot.strip())
    return dico

dictionnaire=load_fichier('liste_francais.txt')

## Q14

def compte_lettre_02_corrige(lettre:str, mots:list):
    nb=0
    for mot in mots:
        if lettre in mot:
            nb=nb+1
    return(nb)


def compte_lettre_02_test(foo,lettre,l_mots):
    if foo(lettre,l_mots) == compte_lettre_02_corrige(lettre,l_mots):
        print(f"Test compte_lettre_02({lettre},l_mots) : réussi")
    else :
        print(f"Test compte_lettre_02({lettre},l_mots) : échoué")


## Q15

def nb_consonnes(mots):
    consonnes='bcdfghjklmnpqrstvwxz'
    L=[compte_lettre_02_corrige(lettre,mots) for lettre in consonnes]
    m,M=L[0],L[0]   # Min et Max des occurrences
    lettre_min=consonnes[0]
    lettre_max=consonnes[0]
    n=len(L)
    for i in range(n):
        if L[i]<m:
            lettre_min=consonnes[i]
            m=L[i]
        if L[i]>M:
            lettre_max=consonnes[i]
            M=L[i]
    occ_consonnes_min=[compte_lettre_02_corrige(lettre_min,mot) for mot in mots]
    occ_consonnes_max=[compte_lettre_02_corrige(lettre_max,mot) for mot in mots]
    return('consonne_max: '+ lettre_max +' '+ str(M)+ ' fois; '+ 'consonne_min: '+ lettre_min+' '+ str(m)+ ' fois.')

## Q 16

def mots_plus_long_corrige(mots:list):
    M=0
    for mot in mots:
        if len(mot)>M:
            max=mot
            M=len(mot)
    return(max)

def mots_plus_long_test(foo,l_mots):
    if foo(l_mots) == mots_plus_long_corrige(l_mots):
        print(f"Test mots_plus_long(l_mots) : réussi")
    else :
        print(f"Test mots_plus_long(l_mots) : échoué")

## Q17

def cherche_mot_in_chaine_01(mot:str,chaine=str):
    p,n=len(mot), len(chaine)
    j=0
    test=False
    while j<=n-p and test==False:
        i=0
        while i<=p-1 and mot[i]==chaine[i+j]:
            i=i+1
        test=(i==p)
        j=j+1
    return(test)

## Q18

def cherche_mot_in_chaine_02(mot:str,chaine=str):
    return(mot in chaine)

## Q19

def cherche_mot_in_dico(nb:int,dico:list):
    # on isole les mots de nb lettres dans liste
    liste=[]
    for mot in dico:
        if len(mot)==nb:
            liste.append(mot)
    M=0
    mot_nb=liste[0]
    for l in liste:   # On compte les occurrences et on prend le max
        n=0
        for mot in dico:
            if cherche_mot_in_chaine_01(l,mot):
                n=n+1
        if n>M:
            M=n
            mot_nb=l
    return(mot_nb)


