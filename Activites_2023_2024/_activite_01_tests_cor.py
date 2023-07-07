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
    total = 0
    
    h,m,s = 1,1,1
    total +=1
    try :
        if (heure_to_sec_cor(h, m, s) ==  foo(h, m, s)):
            pts +=1 
    except : 
        pass
   
    h,m,s = 1,0,1
    total +=1
    try :
        if (heure_to_sec_cor(h, m, s) ==  foo(h, m, s)):
            pts +=1 
    except : 
        pass
    
    h,m,s = 0,1,1
    total +=1
    try :
        if (heure_to_sec_cor(h, m, s) ==  foo(h, m, s)):
            pts +=1 
    except : 
        pass
    
    h,m,s = 12,11,8
    total +=1
    try :
        if (heure_to_sec_cor(h, m, s) ==  foo(h, m, s)):
            pts +=1 
    except : 
        pass
    
    return pts,total


## Question 3 ##
def sec_to_heure_cor(s):
    m, s = s // 60, s % 60
    h, m = m // 60, m % 60
    return (h,m,s)

def test_q03(foo):
    pts = 0
    total = 0
    
    s=30
    total +=1
    try :
        if (sec_to_heure_cor(s) ==  foo(s)):
            pts +=1 
    except : 
        pass
        
    s=183
    total +=1
    try :
        if (sec_to_heure_cor(s) ==  foo(s)):
            pts +=1 
    except : 
        pass
        
    s=3683
    total +=1
    try :
        if (sec_to_heure_cor(s) ==  foo(s)):
            pts +=1 
    except : 
        pass
        
    s=8383
    total +=1
    try :
        if (sec_to_heure_cor(s) ==  foo(s)):
            pts +=1 
    except : 
        pass
   
    
    return pts,total


## Question 4 ##
def duree_cor(h1, m1, s1, h2, m2, s2):
    s = heure_to_sec_cor(h2, m2, s2) - heure_to_sec_cor(h1, m1, s1)
    return sec_to_heure_cor(s)

def test_q04(foo):
    pts = 0
    total = 0
    
    h1, m1, s1, h2, m2, s2 = 1,1,1,2,2,2
    total +=1
    try :
        if (duree_cor(h1, m1, s1, h2, m2, s2) ==  foo(h1, m1, s1, h2, m2, s2)):
            pts +=1 
    except : 
        pass
        
    h1, m1, s1, h2, m2, s2 = 10,20,30,40,50,59
    total +=1
    try :
        if (duree_cor(h1, m1, s1, h2, m2, s2) ==  foo(h1, m1, s1, h2, m2, s2)):
            pts +=1 
    except : 
        pass
    
    h1, m1, s1, h2, m2, s2 = 40,50,59,50,59,12
    total +=1
    try :
        if (duree_cor(h1, m1, s1, h2, m2, s2) ==  foo(h1, m1, s1, h2, m2, s2)):
            pts +=1 
    except : 
        pass
    
    h1, m1, s1, h2, m2, s2 = 30,30,39,59,59,59
    total +=1
    try :
        if (duree_cor(h1, m1, s1, h2, m2, s2) ==  foo(h1, m1, s1, h2, m2, s2)):
            pts +=1 
    except : 
        pass
    
    return pts,total
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

def test_q05(foo):
    pts = 0
    total = 0

    total +=1
    a = 1900
    try :
        if (est_bissextile_cor(a) ==  foo(a)):
            pts +=1 
    except : 
        pass
        
    total +=1
    a = 1901
    try :
        if (est_bissextile_cor(a) ==  foo(a)):
            pts +=1 
    except : 
        pass
        
    total +=1
    a = 1902
    try :
        if (est_bissextile_cor(a) ==  foo(a)):
            pts +=1 
    except : 
        pass
        
    total +=1
    a = 1904
    try :
        if (est_bissextile_cor(a) ==  foo(a)):
            pts +=1 
    except : 
        pass
        
    return pts,total



## Question 6 ##
def nb_bissextile_cor(a1:int,a2:int) -> int : 
    nb = 0
    for i in range(a1,a2):
        if est_bissextile_cor(i) : 
            nb = nb +1
    return nb

def test_q06(foo):
    pts = 0
    total = 0
    
    total +=1
    a1,a2 = 1895,1902
    try :
        if (nb_bissextile_cor(a1,a2) ==  foo(a1,a2)):
            pts +=1 
    except : 
        pass
   
    total +=1
    a1,a2 = 1895,1903
    try :
        if (nb_bissextile_cor(a1,a2) ==  foo(a1,a2)):
            pts +=1 
    except : 
        pass
   
    total +=1
    a1,a2 = 1895,1904
    try :
        if (nb_bissextile_cor(a1,a2) ==  foo(a1,a2)):
            pts +=1 
    except : 
        pass
    
    total +=1
    a1,a2 = 1895,1905
    try :
        if (nb_bissextile_cor(a1,a2) ==  foo(a1,a2)):
            pts +=1 
    except : 
        pass
        
    return pts,total


## Question 7 ##
def nb_annees_cor(a1:int, a2:int) -> int : 
    # On compte le nombre d'années
    nba = a2 - a1
    if nba > 1 : 
        return nba -1
    else : 
        return 0

def test_q07(foo):
    pts = 0
    total = 0
    
    total +=1
    a1,a2 = 1895,1902
    try :
        if (nb_annees_cor(a1,a2) ==  foo(a1,a2)):
            pts +=1 
    except : 
        pass

    total +=1
    a1,a2 = 1800,2023
    try :
        if (nb_annees_cor(a1,a2) ==  foo(a1,a2)):
            pts +=1 
    except : 
        pass


    total +=1
    a1,a2 = 2023,2034
    try :
        if (nb_annees_cor(a1,a2) ==  foo(a1,a2)):
            pts +=1 
    except : 
        pass


    total +=1
    a1,a2 = 1234,5678
    try :
        if (nb_annees_cor(a1,a2) ==  foo(a1,a2)):
            pts +=1 
    except : 
        pass
   
    return pts,total
        
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

def test_q08(foo):
    pts = 0
    total = 0
    
    j,m,a = 25,12,2030
    total +=1
    try :
        if (nb_jours_from_cor(j,m,a) ==  foo(j,m,a)):
            pts +=1 
    except : 
        pass
    
    j,m,a = 15,1,2031
    total +=1
    try :
        if (nb_jours_from_cor(j,m,a) ==  foo(j,m,a)):
            pts +=1 
    except : 
        pass
        
    
    j,m,a = 15,2,2000
    total +=1
    try :
        if (nb_jours_from_cor(j,m,a) ==  foo(j,m,a)):
            pts +=1 
    except : 
        pass
        
    
    j,m,a = 15,3,2000
    total +=1
    try :
        if (nb_jours_from_cor(j,m,a) ==  foo(j,m,a)):
            pts +=1 
    except : 
        pass
   
    
    return pts,total

## Question 9 ##
def nb_jours_to_cor(j:int, m:int, a:int) -> int :
    if est_bissextile_cor(a):
        return 366 - nb_jours_from_cor(j, m, a)
    else :
        return 365 - nb_jours_from_cor(j, m, a)

def test_q09(foo):
    pts = 0
    total = 0
    
    j,m,a = 25,12,2030
    total +=1
    try :
        if (nb_jours_to_cor(j,m,a) ==  foo(j,m,a)):
            pts +=1 
    except : 
        pass
    
    j,m,a = 15,1,2031
    total +=1
    try :
        if (nb_jours_to_cor(j,m,a) ==  foo(j,m,a)):
            pts +=1 
    except : 
        pass
        
    
    j,m,a = 15,2,2000
    total +=1
    try :
        if (nb_jours_to_cor(j,m,a) ==  foo(j,m,a)):
            pts +=1 
    except : 
        pass
        
    
    j,m,a = 15,3,2000
    total +=1
    try :
        if (nb_jours_to_cor(j,m,a) ==  foo(j,m,a)):
            pts +=1 
    except : 
        pass
   
    return pts,total
    
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

def test_q10(foo):
    pts = 0
    total = 0
    
    j1, m1, a1, j2, m2, a2 = 1,1,2001,10,1,2001
    total +=1
    try :
        if (nb_jours_cor(j1, m1, a1, j2, m2, a2) ==  foo(j1, m1, a1, j2, m2, a2)):
            pts +=1 
    except : 
        pass
   
    j1, m1, a1, j2, m2, a2 = 1,1,1999,10,1,2001
    total +=1
    try :
        if (nb_jours_cor(j1, m1, a1, j2, m2, a2) ==  foo(j1, m1, a1, j2, m2, a2)):
            pts +=1 
    except : 
        pass
   
    j1, m1, a1, j2, m2, a2 = 1,1,2001,10,1,2003
    total +=1
    try :
        if (nb_jours_cor(j1, m1, a1, j2, m2, a2) ==  foo(j1, m1, a1, j2, m2, a2)):
            pts +=1 
    except : 
        pass
   
    j1, m1, a1, j2, m2, a2 = 1,1,1800,10,1,2200
    total +=1
    try :
        if (nb_jours_cor(j1, m1, a1, j2, m2, a2) ==  foo(j1, m1, a1, j2, m2, a2)):
            pts +=1 
    except : 
        pass
   
    
    return pts,total
    

import time
time.time()

## Question 11 ##
def calc_sec_cor(j:int, m:int, a:int, h:int, mi:int, s:int) : 
    return nb_jours_cor(1,1,1970,j,m,a)*24*3600 + heure_to_sec_cor(h,mi,s)

def test_q11(foo):
    pts = 0
    total = 0
    
    j1, m1, a1, j2, m2, a2 = 1,1,2001,10,1,2001
    total +=1
    try :
        if (calc_sec_cor(j1, m1, a1, j2, m2, a2) ==  foo(j1, m1, a1, j2, m2, a2)):
            pts +=1 
    except : 
        pass
   
    j1, m1, a1, j2, m2, a2 = 1,1,1999,10,1,2001
    total +=1
    try :
        if (calc_sec_cor(j1, m1, a1, j2, m2, a2) ==  foo(j1, m1, a1, j2, m2, a2)):
            pts +=1 
    except : 
        pass
   
    j1, m1, a1, j2, m2, a2 = 1,1,2001,10,1,2003
    total +=1
    try :
        if (calc_sec_cor(j1, m1, a1, j2, m2, a2) ==  foo(j1, m1, a1, j2, m2, a2)):
            pts +=1 
    except : 
        pass
   
    j1, m1, a1, j2, m2, a2 = 1,1,1800,10,1,2200
    total +=1
    try :
        if (calc_sec_cor(j1, m1, a1, j2, m2, a2) ==  foo(j1, m1, a1, j2, m2, a2)):
            pts +=1 
    except : 
        pass
   
    
    return pts,total



def go(foo1,foo3,foo4,foo5,foo6,foo7,foo8,foo9,foo10,foo11):
    i = 0
    notes = {}
    tot = 4
    
    pts = 0
    i += 1
    try :
        pts,tot = test_q01(foo1)
    except : 
        pass
    print("Question "+str(i)+" : ",str(pts),"/",str(tot))
    notes[i] = (pts,tot)

    
    pts = 0
    i = 3
    try :
        pts,tot = test_q03(foo3)
    except : 
        pass
    print("Question "+str(i)+" : ",str(pts),"/",str(tot))
    notes[i] = (pts,tot)

    
    pts = 0
    i += 1
    try :
        pts,tot = test_q04(foo4)
    except : 
        pass
    print("Question "+str(i)+" : ",str(pts),"/",str(tot))
    notes[i] = (pts,tot)

    
    pts = 0
    i += 1
    try :
        pts,tot = test_q05(foo5)
    except : 
        pass
    print("Question "+str(i)+" : ",str(pts),"/",str(tot))
    notes[i] = (pts,tot)
    
    pts = 0
    i += 1
    try :
        pts,tot = test_q06(foo6)
    except : 
        pass
    print("Question "+str(i)+" : ",str(pts),"/",str(tot))
    notes[i] = (pts,tot)
    
    pts = 0
    i += 1
    try :
        pts,tot = test_q07(foo7)
    except : 
        pass
    print("Question "+str(i)+" : ",str(pts),"/",str(tot))
    notes[i] = (pts,tot)
    
    pts = 0
    i += 1
    try :
        pts,tot = test_q08(foo8)
    except : 
        pass
    print("Question "+str(i)+" : ",str(pts),"/",str(tot))
    notes[i] = (pts,tot)
    
    pts = 0
    i += 1
    try :
        pts,tot = test_q09(foo9)
    except : 
        pass
    print("Question "+str(i)+" : ",str(pts),"/",str(tot))
    notes[i] = (pts,tot)
    
    pts = 0
    i += 1
    try :
        pts,tot = test_q10(foo10)
    except : 
        pass
    print("Question "+str(i)+" : ",str(pts),"/",str(tot))
    notes[i] = (pts,tot)
    
    
    pts = 0
    i += 1
    try :
        pts,tot = test_q11(foo11)
    except : 
        pass
    print("Question "+str(i)+" : ",str(pts),"/",str(tot))
    notes[i] = (pts,tot)  



