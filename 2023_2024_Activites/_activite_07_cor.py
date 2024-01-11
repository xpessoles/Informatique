import matplotlib.pyplot as plt
import random as rd
import numpy as np
import math as m

## Question 1
def cor_new_image(nl,nc):
    # Pixel blanc : 1
    # Pixel noir : 0
    im = []
    for i in range(nl):
        L = []
        for j in range(nc):
            L.append(1)
        im.append(L)
    return im

## Question 2	
def cor_hauteur(im:[[int]]) :
    return len(im)

## Question 3
def cor_largeur(im:[[int]]) -> int :
    return len(im[0])

## Question 4
def cor_in_img(im:[[int]],pt:[int]) -> [[int]] :
    x,y = pt
    ht = cor_hauteur(im)
    la = cor_largeur(im)
    if x < 0 or y < 0 or x >= ht or y >= la :
        return False
    return True
## Question 5
def cor_trace_point(im:[[int]],pt:[int]) -> [[int]] :
    assert cor_in_img(im,pt)
    x,y = pt
    im[x][y] = 0
    return im

## Question 6
def cor_ligne_h(im:[[int]],pt1,pt2) -> [[int]] :
    assert cor_in_img(im,pt1)
    assert cor_in_img(im,pt2)
    assert pt1[0] == pt2[0]
    
    jdep = min(pt1[1],pt2[1])
    jfin = max(pt1[1],pt2[1])
    i = pt1[0]
    for j in range(jdep,jfin+1) :
        cor_trace_point(im,[i,j])
    return im

## Question 7
def cor_ligne_v(im:[[int]],pt1,pt2) -> [[int]] :
    assert cor_in_img(im,pt1)
    assert cor_in_img(im,pt2)
    assert pt1[1] == pt2[1]
    
    idep = min(pt1[0],pt2[0])
    ifin = max(pt1[0],pt2[0])
    j = pt1[1]
    for i in range(idep,ifin+1) :
        cor_trace_point(im,[i,j])
    return im

def cor_rectangle(im:[[int]],pt1,pt2) -> [[int]] :
    assert cor_in_img(im,pt1)
    assert cor_in_img(im,pt2)
    
    pt_hg = pt1
    pt_hd = [pt1[0],pt2[1]]
    pt_bd = pt2
    pt_bg = [pt2[0],pt1[1]]
  
    im = ligne_h(im,pt_hg,pt_hd)
    im = ligne_v(im,pt_hd,pt_bd)
    im = ligne_h(im,pt_bd,pt_bg)
    im = ligne_v(im,pt_bg,pt_hg)
    return im
    
def test_q01(foo):
    pts = 0
    total = 0
    
    total +=1
    nl,nc = 5,3
    try :
        L1 = cor_new_image(nl,nc)
        L2 = foo(nl,nc)
        if (np.allclose(L1,L2)):
            pts +=1 
    except : 
        pass
    
    total +=1
    nl,nc = 2,6
    try :
        L1 = cor_new_image(nl,nc)
        L2 = foo(nl,nc)
        if (np.allclose(L1,L2)):
            pts +=1 
    except : 
        pass
    
    total +=1
    nl,nc = 4,4
    try :
        L1 = cor_new_image(nl,nc)
        L2 = foo(nl,nc)
        if (np.allclose(L1,L2)):
            pts +=1 
    except : 
        pass
    
    return pts,total

    
def test_q02(foo):
    pts = 0
    total = 0
    
    total +=1
    nl,nc = 5,3
    try :
        L = cor_new_image(nl,nc)
        L1 = cor_hauteur(L)
        L2 = foo(L)
        if (np.allclose(L1,L2)):
            pts +=1 
    except : 
        pass
    
    total +=1
    nl,nc = 2,6
    try :
        L = cor_new_image(nl,nc)
        L1 = cor_hauteur(L)
        L2 = foo(L)
        if (np.allclose(L1,L2)):
            pts +=1 
    except : 
        pass
    
    total +=1
    nl,nc = 4,4
    try :
        L = cor_new_image(nl,nc)
        L1 = cor_hauteur(L)
        L2 = foo(L)
        if (np.allclose(L1,L2)):
            pts +=1 
    except : 
        pass
    
    return pts,total

def test_q03(foo):
    pts = 0
    total = 0
    
    total +=1
    nl,nc = 5,3
    try :
        L = cor_new_image(nl,nc)
        L1 = cor_largeur(L)
        L2 = foo(L)
        if (np.allclose(L1,L2)):
            pts +=1 
    except : 
        pass
    
    total +=1
    nl,nc = 2,6
    try :
        L = cor_new_image(nl,nc)
        L1 = cor_largeur(L)
        L2 = foo(L)
        if (np.allclose(L1,L2)):
            pts +=1 
    except : 
        pass
    
    total +=1
    nl,nc = 4,4
    try :
        L = cor_new_image(nl,nc)
        L1 = cor_largeur(L)
        L2 = foo(L)
        if (np.allclose(L1,L2)):
            pts +=1 
    except : 
        pass
    
    return pts,total
    

def test_q04(foo):
    pts = 0
    total = 0
    
    nl,nc = 2,4
    les_pt = [[i,j] for i in range(-1,4) for j in range(-1,6)]  

    for pt in les_pt :         
        total +=1
        try :
            L = cor_new_image(nl,nc)
            L1 = cor_in_img(L,pt)
            L2 = foo(L,pt)
            if (np.allclose(L1,L2)):
                pts +=1 
        except : 
            pass
    
    return pts,total

    
def test_q05(foo):
    pts = 0
    total = 0
    
    nl,nc = 2,4
    les_pt = [[i,j] for i in range(-1,4) for j in range(-1,6)]  

    for pt in les_pt :         
        total +=1
        L = cor_new_image(nl,nc) 
        L1 = 1
        L2 = 2
        flag1 = None
        flag2 = None
        try :
            L1 = cor_trace_point(L,pt)
        except AssertionError :
            flag1 = True
        except :
            pass
        try :
            L2 = foo(L,pt)
        except AssertionError :
            flag2 = True
        except :
            pass
        if (np.allclose(L1,L2)) or (flag1 and flag2) :
                pts +=1 
        
    return pts,total


def test_q06(foo):
    pts = 0
    total = 0
    
    nl,nc = 1,3
    les_pt1 = [[i,j] for i in range(-1,3) for j in range(-1,5)]  
    les_pt2 = [[i,j] for i in range(-1,3) for j in range(-1,5)]
    
    for pt1 in les_pt1 :
        for pt2 in les_pt2 :
            total +=1
            L = cor_new_image(nl,nc) 
            L1 = 1
            L2 = 2
            flag1 = None
            flag2 = None
            try :
                L1 = cor_ligne_h(L,pt1,pt2)
            except AssertionError :
                flag1 = True
            except :
                pass
            try :
                L2 = foo(L,pt1,pt2)
            except AssertionError :
                flag2 = True
            except :
                pass
            if (np.allclose(L1,L2)) or (flag1 and flag2) :
                    pts +=1
        
    return pts,total


def test_q07(foo):
    pts = 0
    total = 0
    
    nl,nc = 1,3
    les_pt1 = [[i,j] for i in range(-1,3) for j in range(-1,5)]  
    les_pt2 = [[i,j] for i in range(-1,3) for j in range(-1,5)]
    
    for pt1 in les_pt1 :
        for pt2 in les_pt2 :
            total +=1
            L = cor_new_image(nl,nc) 
            L1 = 1
            L2 = 2
            flag1 = None
            flag2 = None
            try :
                L1 = cor_ligne_v(L,pt1,pt2)
            except AssertionError :
                flag1 = True
            except :
                pass
            try :
                L2 = foo(L,pt1,pt2)
            except AssertionError :
                flag2 = True
            except :
                pass
            if (np.allclose(L1,L2)) or (flag1 and flag2) :
                    pts +=1
        
    return pts,total

def test_q08(foo):
    pts = 0
    total = 0
    
    nl,nc = 1,3
    les_pt1 = [[i,j] for i in range(-1,3) for j in range(-1,5)]  
    les_pt2 = [[i,j] for i in range(-1,3) for j in range(-1,5)]
    
    for pt1 in les_pt1 :
        for pt2 in les_pt2 :
            total +=1
            L = cor_new_image(nl,nc) 
            L1 = 1
            L2 = 2
            flag1 = None
            flag2 = None
            try :
                L1 = cor_ligne_h(L,pt1,pt2)
            except AssertionError :
                flag1 = True
            except :
                pass
            try :
                L2 = foo(L,pt1,pt2)
            except AssertionError :
                flag2 = True
            except :
                pass
            if (np.allclose(L1,L2)) or (flag1 and flag2) :
                    pts +=1
        
    return pts,total

def go(foo1,foo2,foo3,foo4,foo5,foo6,foo7,foo8):
    i = 0
    notes = {}
    tot = 2
    
    tests = [[test_q01,foo1],[test_q02,foo2],[test_q03,foo3],[test_q04,foo4],[test_q05,foo5],[test_q06,foo6],[test_q07,foo7],[test_q08,foo8]]
    
    for t in tests : 
        tq,f = t
        pts = 0
        i +=1
        try :
            pts,tot = tq(f)
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