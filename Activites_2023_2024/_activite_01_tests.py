# -*- coding: utf-8 -*-
"""
Created on Thu Jul  6 12:47:07 2023

@author: xavier.pessoles2
"""

## Question 1 ##
def heure_to_sec_cor(h, m, s):
    return h * 3600 + m * 60 + s

def test_q01(foo):
    pts = 0
    
    h,m,s = 1,1,1
    try :
        if (heure_to_sec_cor(h, m, s) ==  foo(h, m, s)):
            pts +=1 
    except : 
        pass
   
    h,m,s = 1,0,1
    try :
        if (heure_to_sec_cor(h, m, s) ==  foo(h, m, s)):
            pts +=1 
    except : 
        pass
    
    h,m,s = 0,1,1
    try :
        if (heure_to_sec_cor(h, m, s) ==  foo(h, m, s)):
            pts +=1 
    except : 
        pass
    
    h,m,s = 12,11,8
    try :
        if (heure_to_sec_cor(h, m, s) ==  foo(h, m, s)):
            pts +=1 
    except : 
        pass
    
    return pts       


## Question 3 ##
def sec_to_heure_cor(s):
    m, s = s // 60, s % 60
    h, m = m // 60, m % 60
    return (str(h)+":"+str(m)+":"+str(s))

## Question 4 ##
def duree_cor(h1, m1, s1, h2, m2, s2):
    s = heure_to_sec_cor(h2, m2, s2) -heure_to_sec_cor(h1, m1, s1)
    return sec_to_heure_cor(s)


## Question 5 ##
def est_bissextile_cor(a:int)-> bool : 
    if a%4 == 0 : 
        if a%100 == 0 :
            if a%400 ==0 :
                return True
            else : 
                return False
        else : 
            return True
    return False


## Question 6 ##
def nb_bissextile_cor(a1:int,a2:int) -> int : 
    nb = 0
    for i in range(a1,a2):
        if est_bissextile_cor(i) : 
            nb = nb +1
    return nb


## Question 7 ##
def nb_annees_cor(a1:int, a2:int) -> int : 
    # On compte le nombre d'années
    nba = a2 - a1
    if nba > 1 : 
        return nba -1
    else : 
        return 0
    
## Question 8 ##
def nb_jours_from_cor(j:int, m:int, a:int) -> int :
    nb_jours = 0
    if m == 12 :
        nb_jours = 31 - j
    elif m == 11 :
        nb_jours = 30 - j + 31
    elif m == 10 :
        nb_jours = 31 - j + 30 + 31
    elif m == 9 :
        nb_jours = 30 - j + 31 + 30 + 31
    elif m == 8 :
        nb_jours = 31 - j + 30 + 31 + 30 + 31
    elif m == 7 :
        nb_jours = 31 - j + 31 + 30 + 31 + 30 + 31
    elif m == 6 :
        nb_jours = 30 - j + 31 + 31 + 30 + 31 + 30 + 31
    elif m == 5 :
        nb_jours = 31 - j + 30 + 31 + 31 + 30 + 31 + 30 + 31
    elif m == 4 :
        nb_jours = 30 - j + 31 + 30 + 31 + 31 + 30 + 31 + 30 + 31
    elif m == 3 :
        nb_jours = 31 - j + 30 + 31 + 30 + 31 + 31 + 30 + 31 + 30 + 31
    elif m == 2 and est_bissextile_cor(a) :
        nb_jours = 29 - j + 31 + 30 + 31 + 30 + 31 + 31 + 30 + 31 + 30 + 31
    elif m == 2 and not (est_bissextile_cor(a)) :
        nb_jours = 28 - j + 31 + 30 + 31 + 30 + 31 + 31 + 30 + 31 + 30 + 31
    elif m == 1 and est_bissextile_cor(a) :
        nb_jours = 31 - j + 29 + 31 + 30 + 31 + 30 + 31 + 31 + 30 + 31 + 30 + 31
    elif m == 1 and not (est_bissextile_cor(a)) :
        nb_jours = 31 - j + 28 + 31 + 30 + 31 + 30 + 31 + 31 + 30 + 31 + 30 + 31
    return nb_jours


## Question 9 ##
def nb_jours_to_cor(j:int, m:int, a:int) -> int :
    if est_bissextile_cor(a):
        return 366 - nb_jours_from_cor(j, m, a)
    else :
        return 365 - nb_jours_from_cor(j, m, a)

## Question 10 ##
def nb_jours_cor(j1:int, m1:int, a1:int, j2:int, m2:int, a2:int) -> int :
    if a1 == a2 :
        return nb_jours_to_cor(j2,m2,a2) - nb_jours_to_cor(j1,m1,a1)
    else : 
        nb = nb_jours_to_cor(j2,m2,a2) + nb_jours_from_cor(j1,m1,a1)
        for i in range (a1+1,a2):
            if est_bissextile_cor(i) :
                nb = nb + 366
            else : 
                nb = nb + 365
        return nb
    

import time
time.time()

## Question 11 ##
def calc_sec_cor(j:int, m:int, a:int, h:int, mi:int, s:int) : 
    return nb_jours_cor(1,1,1970,j,m,a)*24*3600 + heure_to_sec_cor(h,mi,s)






