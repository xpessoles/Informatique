# -*- coding: utf-8 -*-
"""
Created on Thu Jul  6 12:47:07 2023

@author: xavier.pessoles2
"""

    
## Question 1
def cor_q01_min():
    return 0
    
def cor_q01_max():
    return 2**8 - 1

## Question 2
def cor_q02_min():
    return -2**7
def cor_q02_max():
    return 2**7-1
    
## Question 3
def cor_q03_bin():
    return "11011000"
def cor_q03_hex():
    return "d8"
    
## Question 4
def cor_q04_01():
    return "01101111"
def cor_q04_02():
    return "10010001"
    
## Question 5
def cor_q05():
    return -77
    
## Question 6
def cor_moyenne(a):
    return (sum(a))/len(a)
    
## Question 7
def cor_variance(a):
    n = len(a)
    m = cor_moyenne(a)
    return 1/n*sum([i-m for i in a])

## Question 8
def cor_moyennes(a,b):
    return [0.5*(a[i]+b[i]) for i in range(len(a))]    
    
    
## Question 9
def cor_moyenneGlissante(a,n):
    def cor_moyenne(a):
        return (sum(a))/len(a)
    mg = a[:n-1]
    for i in range(len(a)-n+1):
        mg.append(cor_moyenne(a[i:i+n]))
    return mg
    
## TESTS ##
def test_q01_min(foo):
    pts = 0
    total = 0
    total +=1
    try :
        if (cor_q01_min() ==  foo):
            pts +=1 
    except : 
        pass
    return pts,total

def test_q01_max(foo):
    pts = 0
    total = 0
    total +=1
    try :
        if (cor_q01_max() ==  foo):
            pts +=1 
    except : 
        pass
    return pts,total

def test_q02_min(foo):
    pts = 0
    total = 0
    total +=1
    try :
        if (cor_q02_min() ==  foo):
            pts +=1 
    except : 
        pass
    return pts,total

def test_q02_max(foo):
    pts = 0
    total = 0
    total +=1
    try :
        if (cor_q02_max() ==  foo):
            pts +=1 
    except : 
        pass
    return pts,total    

def test_q03_bin(foo):
    pts = 0
    total = 0
    total +=1
    try :
        if (cor_q03_bin() ==  foo):
            pts +=1 
    except : 
        pass
    return pts,total    

def test_q03_hex(foo):
    pts = 0
    total = 0
    total +=1
    try :
        if (cor_q03_hex() ==  foo):
            pts +=1 
    except : 
        pass
    return pts,total    

def test_q04_01(foo):
    pts = 0
    total = 0
    total +=1
    try :
        if (cor_q04_01() ==  foo):
            pts +=1 
    except : 
        pass
    return pts,total   

def test_q04_02(foo):
    pts = 0
    total = 0
    total +=1
    try :
        if (cor_q04_02() ==  foo):
            pts +=1 
    except : 
        pass
    return pts,total  

def test_q05(foo):
    pts = 0
    total = 0
    total +=1
    try :
        if (cor_q05() ==  foo):
            pts +=1 
    except : 
        pass
    return pts,total  

    
def test_q06(foo):
    pts = 0
    total = 0
    
    import random as rd
    import numpy as np
    
    nb,L = 0, [rd.randrange(1,20) for i in range(100)]
    total +=1
    try :
        L1 = cor_moyenne(L)
        L2 = foo(L)
        if (np.allclose(L1,L2)):
            pts +=1 
    except : 
        pass
    
    nb,L = 0, [rd.randrange(1,20) for i in range(100)]
    total +=1
    try :
        L1 = cor_moyenne(L)
        L2 = foo(L)
        if (np.allclose(L1,L2)):
            pts +=1 
    except : 
        pass
        
    return pts,total

def test_q07(foo):
    pts = 0
    total = 0
    
    import random as rd
    import numpy as np
    
    nb,L = 0, [rd.randrange(1,20) for i in range(100)]
    total +=1
    try :
        L1 = cor_variance(L)
        L2 = foo(L)
        if (np.allclose(L1,L2)):
            pts +=1 
    except : 
        pass
    
    nb,L = 0, [rd.randrange(1,20) for i in range(100)]
    total +=1
    try :
        L1 = cor_variance(L)
        L2 = foo(L)
        if (np.allclose(L1,L2)):
            pts +=1 
    except : 
        pass
        
    return pts,total

def test_q08(foo):
    pts = 0
    total = 0
    
    import random as rd
    import numpy as np
    
    nb,La,Lb = 0, [rd.randrange(1,20) for i in range(100)], [rd.randrange(1,20) for i in range(100)]
    total +=1
    try :
        L1 = cor_moyennes(La,Lb)
        L2 = foo(La,Lb)
        if (np.allclose(L1,L2)):
            pts +=1 
    except : 
        pass
    
    nb,La,Lb = 0, [rd.randrange(1,20) for i in range(100)], [rd.randrange(1,20) for i in range(100)]
    total +=1
    try :
        L1 = cor_moyennes(La,Lb)
        L2 = foo(La,Lb)
        if (np.allclose(L1,L2)):
            pts +=1 
    except : 
        pass
        
    return pts,total

def test_q09(foo):
    pts = 0
    total = 0
    
    import random as rd
    import numpy as np
    
    nb,L = 0, [rd.randrange(1,20) for i in range(100)]
    n = rd.randrange(1,20)
    total +=1
    try :
        L1 = cor_moyenneGlissante(L,n)
        L2 = foo(L,n)
        if (np.allclose(L1,L2)):
            pts +=1 
    except : 
        pass
    
    nb,L = 0, [rd.randrange(1,20) for i in range(100)]
    n = rd.randrange(1,20)
    total +=1
    try :
        L1 = cor_moyenneGlissante(L,n)
        L2 = foo(L,n)
        if (np.allclose(L1,L2)):
            pts +=1 
    except : 
        pass
        
    return pts,total



    
    
def go(foo1,foo2,foo3,foo4,foo5,foo6,foo7,foo8,foo9,foo10,foo11,foo12,foo13):
    i = 0
    notes = {}
    tot = 2
    
    pts = 0
    i += 1
    try :
        pts,tot = test_q01_min(foo1)
    except : 
        pass
    
    try :
        pts,tot = test_q01_max(foo2)[0]+1,test_q01_max(foo2)[1]+1
    except : 
        pass
        
    print("Question "+str(i)+" : ",str(pts),"/",str(tot))
    notes[i] = (pts,tot)

    
    
    pts = 0
    i += 1
    try :
        pts,tot = test_q02_min(foo3)
    except : 
        pass
    
    try :
        pts,tot = test_q02_max(foo4)[0]+1,test_q02_max(foo4)[1]+1
    except : 
        pass
        
    print("Question "+str(i)+" : ",str(pts),"/",str(tot))
    notes[i] = (pts,tot)
    
    
    pts = 0
    i += 1
    try :
        pts,tot = test_q03_bin(foo5)
    except : 
        pass
    
    try :
        pts,tot = test_q03_hex(foo6)
    except : 
        pass
        
    print("Question "+str(i)+" : ",str(pts),"/",str(tot))
    notes[i] = (pts,tot)
    
    pts = 0
    i += 1
    try :
        pts,tot = test_q04_01(foo7)
    except : 
        pass
    
    try :
        pts,tot = test_q04_02(foo8)
    except : 
        pass
        
    print("Question "+str(i)+" : ",str(pts),"/",str(tot))
    notes[i] = (pts,tot)
    
    
    pts = 0
    i += 1
    try :
        pts,tot = test_q05(foo9)
    except : 
        pass
        
    print("Question "+str(i)+" : ",str(pts),"/",str(tot))
    notes[i] = (pts,tot)
    

    pts = 0
    i +=1
    try :
        pts,tot = test_q06(foo10)
    except : 
        pass
    print("Question "+str(i)+" : ",str(pts),"/",str(tot))
    notes[i] = (pts,tot)
    
    pts = 0
    i +=1
    try :
        pts,tot = test_q07(foo11)
    except : 
        pass
    print("Question "+str(i)+" : ",str(pts),"/",str(tot))
    notes[i] = (pts,tot)
    
    pts = 0
    i +=1
    try :
        pts,tot = test_q08(foo12)
    except : 
        pass
    print("Question "+str(i)+" : ",str(pts),"/",str(tot))
    notes[i] = (pts,tot)
    
    pts = 0
    i +=1
    try :
        pts,tot = test_q09(foo13)
    except : 
        pass
    print("Question "+str(i)+" : ",str(pts),"/",str(tot))
    notes[i] = (pts,tot)
    

    
    #bilan : 
    points,total = 0,0
    for n in notes.values() :
        points = points + n[0]
        total = total + n[1]
    print(points,total)