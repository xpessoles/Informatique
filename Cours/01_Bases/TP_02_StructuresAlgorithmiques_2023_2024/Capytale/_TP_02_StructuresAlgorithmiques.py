# -*- coding: utf-8 -*-
"""
@author: xpess
"""

## Valeur absolue - Question 1
def val_absolue_corrige(x:float)-> float:
    if x>=0 : 
        return x
    else :
        return -x
        
def test_q01(foo) :
    pts,total = 0,0
    
    total +=1
    x = 0
    try :
        if (val_absolue_corrige(x) ==  foo(x)):
            pts +=1 
    except : 
        pass
    
    total +=1
    x = 2
    try :
        if (val_absolue_corrige(x) ==  foo(x)):
            pts +=1 
    except : 
        pass
    
    total +=1
    x = -2
    try :
        if (val_absolue_corrige(x) ==  foo(x)):
            pts +=1 
    except : 
        pass
    
    total +=1
    x = -3.5
    try :
        if (val_absolue_corrige(x) ==  foo(x)):
            pts +=1 
    except : 
        pass
        
    return pts,total
    
    
def val_absolue_test(foo,x):
    if foo(x) == val_absolue_corrige(x):
        print(f"Test val_absolue({x}) : réussi")
    else :
        print(f"Test val_absolue({x}) : échoué")


## Coût voyage - Question 2
def cout_voyage_corrige(n):
    if n<=2 :
        prix = 80
    elif n<=5 :
        prix = 70
    elif n<=9 : 
        prix = 60
    else : 
        prix = 50
    return n*prix

def cout_voyage_test(foo,x):
    assert x>0
    assert type(x)==type(0)
    if foo(x) == cout_voyage_corrige(x):
        print(f"Test cout_voyage({x}) : réussi")
    else :
        print(f"Test cout_voyage({x}) : échoué")

def test_q02(foo) :
    pts,total = 0,0
    
    total +=1
    x = 1
    try :
        if (cout_voyage_corrige(x) ==  foo(x)):
            pts +=1 
    except : 
        pass
    
    total +=1
    x = 2
    try :
        if (cout_voyage_corrige(x) ==  foo(x)):
            pts +=1 
    except : 
        pass
        
    total +=1
    x = 3
    try :
        if (cout_voyage_corrige(x) ==  foo(x)):
            pts +=1 
    except : 
        pass
        
    total +=1
    x = 12
    try :
        if (cout_voyage_corrige(x) ==  foo(x)):
            pts +=1 
    except : 
        pass

    return pts,total

## Q3 
def is_exists_corrige(a:int, b:int, c:int) -> bool :
    # Pour vérifier l'existence du triangle on utilise l'inégalité triangulaire : 
    if (a <= b+c) and (b <= a+c) and (c <= b+a) :
        return True
    return False


def is_exists_test(foo,a,b,c):
    assert a > 0     
    assert b > 0
    assert c > 0
    if foo(a,b,c) == is_exists_corrige(a,b,c):
        print(f"Test is_exists({a,b,c}) : réussi")
    else :
        print(f"Test is_exists({a,b,c}) : échoué")
        
def test_q03(foo) :
    pts,total = 0,0
    
    total +=1
    a,b,c = 10,1,1
    try :
        if (is_exists_corrige(a,b,c) ==  foo(a,b,c)):
            pts +=1 
    except : 
        pass

    total +=1
    a,b,c = 10,9,8
    try :
        if (is_exists_corrige(a,b,c) ==  foo(a,b,c)):
            pts +=1 
    except : 
        pass
        
    total +=1
    a,b,c = 10,10,9
    try :
        if (is_exists_corrige(a,b,c) ==  foo(a,b,c)):
            pts +=1 
    except : 
        pass
        
    total +=1
    a,b,c = 10,10,10
    try :
        if (is_exists_corrige(a,b,c) ==  foo(a,b,c)):
            pts +=1 
    except : 
        pass
    
    return pts,total
    

## Q4
def is_equilateral_corrige(a:int, b:int, c:int) -> bool :
    if a == b and a == c :
        return True
    return False
    
    # Plus simplement, on pourraut écrire 
    # return (a==b) and (a==c)

def is_equilateral_test(foo,a,b,c):
    assert a > 0     
    assert b > 0
    assert c > 0
    if foo(a,b,c) == is_equilateral_corrige(a,b,c):
        print(f"Test réussi")
    else :
        print(f"Test échoué")

def test_q04(foo) :
    pts,total = 0,0
    
    foo_corrige = is_equilateral_corrige
    total +=1
    a,b,c = 10,1,1
    try :
        if (foo_corrige(a,b,c) ==  foo(a,b,c)):
            pts +=1 
    except : 
        pass

    total +=1
    a,b,c = 10,9,8
    try :
        if (foo_corrige(a,b,c) ==  foo(a,b,c)):
            pts +=1 
    except : 
        pass
        
    total +=1
    a,b,c = 10,10,9
    try :
        if (foo_corrige(a,b,c) ==  foo(a,b,c)):
            pts +=1 
    except : 
        pass
        
    total +=1
    a,b,c = 10,10,10
    try :
        if (foo_corrige(a,b,c) ==  foo(a,b,c)):
            pts +=1 
    except : 
        pass
    
    return pts,total

## Q5
def is_isocele_corrige(a:int, b:int, c:int) -> bool :
    if not(is_exists_corrige(a,b,c)):
        return False
    if a == b or a == c or b == c:
        return True
    return False
    
def is_isocele_test(foo,a,b,c):
    assert a > 0     
    assert b > 0
    assert c > 0
    if foo(a,b,c) == is_isocele_corrige(a,b,c):
        print(f"Test réussi")
    else :
        print(f"Test échoué")

def test_q05(foo) :
    pts,total = 0,0
    
    foo_corrige = is_isocele_corrige
    total +=1
    a,b,c = 10,1,1
    try :
        if (foo_corrige(a,b,c) ==  foo(a,b,c)):
            pts +=1 
    except : 
        pass

    total +=1
    a,b,c = 10,9,8
    try :
        if (foo_corrige(a,b,c) ==  foo(a,b,c)):
            pts +=1 
    except : 
        pass
        
    total +=1
    a,b,c = 10,10,9
    try :
        if (foo_corrige(a,b,c) ==  foo(a,b,c)):
            pts +=1 
    except : 
        pass
        
    total +=1
    a,b,c = 10,10,10
    try :
        if (foo_corrige(a,b,c) ==  foo(a,b,c)):
            pts +=1 
    except : 
        pass
    
    return pts,total


## Q6
def is_rectangle_corrige(a:int, b:int, c:int) -> bool :
    if a*a == (b**b + c**c) :
        return True
    if b*b == (a**a + c**c) :
        return True
    if c*c == (b**b + a**a) :
        return True
    
    return False
    
def is_rectangle_test(foo,a,b,c):
    assert a > 0     
    assert b > 0
    assert c > 0
    if foo(a,b,c) == is_rectangle_corrige(a,b,c):
        print("Test réussi")
    else :
        print("Test échoué")

def test_q06(foo) :
    pts,total = 0,0
    
    foo_corrige = is_rectangle_corrige
    total +=1
    a,b,c = 10,1,1
    try :
        if (foo_corrige(a,b,c) ==  foo(a,b,c)):
            pts +=1 
    except : 
        pass

    total +=1
    a,b,c = 10,9,8
    try :
        if (foo_corrige(a,b,c) ==  foo(a,b,c)):
            pts +=1 
    except : 
        pass
        
    total +=1
    a,b,c = 10,10,9
    try :
        if (foo_corrige(a,b,c) ==  foo(a,b,c)):
            pts +=1 
    except : 
        pass
        
    total +=1
    a,b,c = 10,10,10
    try :
        if (foo_corrige(a,b,c) ==  foo(a,b,c)):
            pts +=1 
    except : 
        pass
    
    return pts,total


## Q7 Triangle
def triangle_corrige(a:int, b:int, c:int) -> bool :
    if not is_exists_corrige(a,b,c):
        return -1
    if is_equilateral_corrige(a,b,c):
        return 1
    if is_isocele_corrige(a,b,c) and is_rectangle_corrige(a,b,c):
        return 4
    if is_isocele_corrige(a,b,c) :
        return 2
    if is_rectangle_corrige(a,b,c):
        return 3
    return 0
    
def triangle_test(foo,a,b,c):
    assert a > 0     
    assert b > 0
    assert c > 0
    if foo(a,b,c) == triangle_corrige(a,b,c):
        print("Test réussi")
    else :
        print("Test échoué")    

def test_q07(foo) :
    pts,total = 0,0
    
    foo_corrige = triangle_corrige
    total +=1
    a,b,c = 10,1,1
    try :
        if (foo_corrige(a,b,c) ==  foo(a,b,c)):
            pts +=1 
    except : 
        pass

    total +=1
    a,b,c = 10,9,8
    try :
        if (foo_corrige(a,b,c) ==  foo(a,b,c)):
            pts +=1 
    except : 
        pass
        
    total +=1
    a,b,c = 10,10,9
    try :
        if (foo_corrige(a,b,c) ==  foo(a,b,c)):
            pts +=1 
    except : 
        pass
        
    total +=1
    a,b,c = 10,10,10
    try :
        if (foo_corrige(a,b,c) ==  foo(a,b,c)):
            pts +=1 
    except : 
        pass
    
    return pts,total

## Q8 Legende
def corrige_legende() -> int :
    case = 1
    res = 0
    for i in range(64):
        res = res + case
        case = case*2
    return res

def test_legende(foo) :
    if foo() == corrige_legende():
        print("Test réussi")
    else :
        print("Test échoué")

def test_q08(foo) :
    pts,total = 0,0
    
    foo_corrige = corrige_legende
    total +=2
    try :
        if (foo_corrige() ==  foo()):
            pts +=2 
    except : 
        pass
    
    return pts,total

## Q9 Masse
def corrige_calcul_masse():
    grains = corrige_legende()
    masse = grains *  0.02 / 1000
    return masse # en kg

def test_calcul_masse(foo) :
    if foo() == calcul_masse():
        print("Test réussi")
    else :
        print("Test échoué")    

def test_q09(foo) :
    pts,total = 0,0
    
    foo_corrige = corrige_calcul_masse
    total +=2
    try :
        if (foo_corrige() ==  foo()):
            pts +=2 
    except : 
        pass
    
    return pts,total

        
## Q10  Nb jours
def corrige_nb_jours():
    # Masse annuelle kg
    M = 757000000000
    # Masse journaliere
    mj = M/365

    #Masse légende 
    ml = corrige_legende()
    nb_j = int(ml/mj)+1
    return nb_j
    
def test_corrige_nb_jours(foo) :
    if foo() == corrige_nb_jours():
        print("Test réussi")
    else :
        print("Test échoué")    

def test_q10(foo) :
    pts,total = 0,0
    
    foo_corrige = corrige_nb_jours
    total +=2
    try :
        if (foo_corrige() ==  foo()):
            pts +=2 
    except : 
        pass
    
    return pts,total
    

## Q11 Nb mots
def corrige_nombre_lettres(mot:str) -> int:
    return len(mot)

def test_q11(foo) :
    pts,total = 0,0
    
    foo_corrige = corrige_nombre_lettres
    total +=1
    mot = ""
    try :
        if (foo_corrige(mot) ==  foo(mot)):
            pts +=1
    except : 
        pass
    
    total +=1
    mot = "a"
    try :
        if (foo_corrige(mot) ==  foo(mot)):
            pts +=1
    except : 
        pass
    
    total +=1    
    mot = "ab"
    try :
        if (foo_corrige(mot) ==  foo(mot)):
            pts +=1
    except : 
        pass
    
    total +=1    
    mot = "a b"
    try :
        if (foo_corrige(mot) ==  foo(mot)):
            pts +=1
    except : 
        pass
    
    return pts,total

## Q12 Premiere lettre
def corrige_premiere_lettre(mot:str) -> int:
    return mot[0]

def test_q12(foo) :
    pts,total = 0,0
    
    foo_corrige = corrige_premiere_lettre
    total +=1
    mot = "aa"
    try :
        if (foo_corrige(mot) ==  foo(mot)):
            pts +=1
    except : 
        pass
    
    total +=1
    mot = "a"
    try :
        if (foo_corrige(mot) ==  foo(mot)):
            pts +=1
    except : 
        pass

    total +=1    
    mot = "ab"
    try :
        if (foo_corrige(mot) ==  foo(mot)):
            pts +=1
    except : 
        pass
    
    total +=1
    mot = "a b"
    try :
        if (foo_corrige(mot) ==  foo(mot)):
            pts +=1
    except : 
        pass
    
    return pts,total
    
## Q13 Derniere lettre
def corrige_derniere_lettre(mot:str) -> int:
    return mot[-1]

def test_q13(foo) :
    pts,total = 0,0
    
    foo_corrige = corrige_derniere_lettre
    total +=1
    mot = "aa"
    try :
        if (foo_corrige(mot) ==  foo(mot)):
            pts +=1
    except : 
        pass
    
    total +=1
    mot = "a"
    try :
        if (foo_corrige(mot) ==  foo(mot)):
            pts +=1
    except : 
        pass
    
    total +=1
    mot = "ab"
    try :
        if (foo_corrige(mot) ==  foo(mot)):
            pts +=1
    except : 
        pass
        
    total +=1
    mot = "a b"
    try :
        if (foo_corrige(mot) ==  foo(mot)):
            pts +=1
    except : 
        pass
    
    return pts,total

## Q14 miroir
def corrige_miroir(mot:str) -> int:
    tom = ''
    for lettre in mot :
        tom = lettre+tom
    return tom
    

def test_q14(foo) :
    pts,total = 0,0
    
    foo_corrige = corrige_miroir
    total +=1
    mot = "aa"
    try :
        if (foo_corrige(mot) ==  foo(mot)):
            pts +=1
    except : 
        pass
    
    total +=1
    mot = "a"
    try :
        if (foo_corrige(mot) ==  foo(mot)):
            pts +=1
    except : 
        pass
        
    total +=1
    mot = "ab"
    try :
        if (foo_corrige(mot) ==  foo(mot)):
            pts +=1
    except : 
        pass
    
    total +=1
    mot = "a b"
    try :
        if (foo_corrige(mot) ==  foo(mot)):
            pts +=1
    except : 
        pass
    
    return pts,total
    

## Q15 remplace_lettre
def corrige_remplace_lettre(mot:str, old_lettre:str, new_lettre:str) -> str:
    new_mot = ""
    for lettre in mot :
        if lettre == old_lettre :
            new_mot = new_mot+new_lettre
        else :
            new_mot = new_mot+lettre
    return new_mot
    

def test_q15(foo) :
    pts,total = 0,0
    
    foo_corrige = corrige_remplace_lettre
    
    total +=1
    mot = "aa"
    old,new = 'a','b' 
    try :
        if (foo_corrige(mot,old,new) ==  foo(mot,old,new)):
            pts +=1
    except : 
        pass
    
    total +=1
    mot = "aa"
    old,new = 'c','c' 
    try :
        if (foo_corrige(mot,old,new) ==  foo(mot,old,new)):
            pts +=1
    except : 
        pass
    
    total +=1
    mot = "aba"
    old,new = 'a','b' 
    try :
        if (foo_corrige(mot,old,new) ==  foo(mot,old,new)):
            pts +=1
    except : 
        pass
    
    
    total +=1
    mot = "a a"
    old,new = ' ','a' 
    try :
        if (foo_corrige(mot,old,new) ==  foo(mot,old,new)):
            pts +=1
    except : 
        pass
    
    return pts,total
    
## GO
def go(foo1,foo2,foo3,foo4,foo5,foo6,foo7,foo8,foo9,foo10,foo11,foo12,foo13,foo14,foo15):
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
    
    pts = 0
    i += 1
    try :
        pts,tot = test_q12(foo12)
    except : 
        pass
    print("Question "+str(i)+" : ",str(pts),"/",str(tot))
    notes[i] = (pts,tot)
    
    pts = 0
    i += 1
    try :
        pts,tot = test_q13(foo13)
    except : 
        pass
    print("Question "+str(i)+" : ",str(pts),"/",str(tot))
    notes[i] = (pts,tot)
    
    pts = 0
    i += 1
    try :
        pts,tot = test_q14(foo14)
    except : 
        pass
    print("Question "+str(i)+" : ",str(pts),"/",str(tot))
    notes[i] = (pts,tot)
    
    pts = 0
    i += 1
    try :
        pts,tot = test_q15(foo15)
    except : 
        pass
    print("Question "+str(i)+" : ",str(pts),"/",str(tot))
    notes[i] = (pts,tot)  

