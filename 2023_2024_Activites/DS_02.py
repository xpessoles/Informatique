import random as rd
import numpy as np
import math as m

def _factorielle(n):
    res = 1
    j = 0
    while  j < n :
        j = j+1
        res = res*j
    return res

def _binomial(n : int, p : int) -> int :
    return _factorielle(n)//(_factorielle(p)*_factorielle(n-p))

def _binomial_rec(n : int, p : int) -> int :
    if p > n : 
        return 0
    if p == 0  or p == n : 
        return 1
    else : 
        return n * _binomial_rec(n-1,p-1)//p

def _bernstein(n : int, i : int, t : float) -> float :
    return _binomial(n,i)*t**i*(1-t)**(n-i)

def _calcule_t(n: int) -> []:
    les_t = []
    for i in range(n) :
        les_t.append(i/(n-1))
    return les_t

def _calcule_M(P0: [], P1: [], P2: [], P3: [], les_t: []) -> ([],[]) :
    les_x = []
    les_y = []
    for t in les_t:
        les_x.append((1-t)**3*P0[0]+3*t*(1-t)**2*P1[0]+3*(t**2)*(1-t)*P2[0]+(t**3)*P3[0])
        les_y.append((1-t)**3*P0[1]+3*t*(1-t)**2*P1[1]+3*(t**2)*(1-t)*P2[1]+(t**3)*P3[1])
    return les_x,les_y

def _milieu(A,B):
    return [(A[0]+B[0])/2,(A[1]+B[1])/2]

def _etape_casteljau(P):
    p0, p1, p2, p3=P
    M = _milieu(p1, p2)
    a1 = _milieu(p0, p1)
    a2 = _milieu(a1, M)
    b2 = _milieu(p2, p3)
    b1 = _milieu(M, b2)
    a3 = _milieu(a2, b1)
    return [p0, a1, a2, a3], [a3, b1, b2, p3]

def _distance(A,B):
    return sqrt((B[0]-A[0])**2+(B[1]-A[1])**2)

def _cond_arret(P):
    for i in range(len(P)-1):
        if _distance(P[i],P[i+1])>=0.1:
            return False
    return True

def _trace_ligne_brisee(P):
    return None

def _bezier_casteljau(P):
    P=[np.array(x) for x in P]
    if _cond_arret(P):
        _trace_ligne_brisee(P)
    else:
        a,b=_etape_casteljau(P)
        _bezier_casteljau(a)
        _bezier_casteljau(b)




def test_q01(foo,verbose):
    pts = 0
    total = 0
    
    coef = 2
    nb_tests = 10
    liste_n = [rd.randrange(2,100) for i in range(nb_tests)]
    
    for n in liste_n :
        total +=1
        try :
            fcor =  _factorielle(n)
            fel = foo(n)
            
            if fcor == fel :
                pts +=1 
            else : 
                if verbose :
                    print('n :',n)
                    print('Corrigé :',fcor)
                    print('Votre fonction :',fel)
                    print()
        except : 
            pass
    
    return pts*coef/nb_tests,total*coef/nb_tests

def test_q02(foo,verbose):
    pts = 0
    total = 0
    
    coef = 2
    nb_tests = 10
    liste_n = [rd.randrange(11,20) for i in range(nb_tests)]
    liste_p = [rd.randrange(0,10) for i in range(nb_tests)]
    nb_tests = nb_tests*nb_tests
    
    for n in liste_n :
        for p in liste_p :
            total +=1
            try :
                fcor =  _binomial(n,p)
                fel = foo(n,p)

                if fcor == fel:
                    pts +=1 
                else : 
                    if verbose :
                        print('n :',n)
                        print('Corrigé :',fcor)
                        print('Votre fonction :',fel)
                        print()
            except : 
                pass

    return pts*coef/nb_tests,total*coef/nb_tests

def test_q03(foo,verbose):
    pts = 0
    total = 0
    
    coef = 2
    nb_tests = 10
    liste_n = [rd.randrange(11,20) for i in range(nb_tests)]
    liste_p = [rd.randrange(0,10) for i in range(nb_tests)]
    nb_tests = nb_tests*nb_tests
    
    for n in liste_n :
        for p in liste_p :
            total +=1
            try :
                fcor =  _binomial_rec(n,p)
                fel = foo(n,p)

                if fcor == fel:
                    pts +=1 
                else : 
                    if verbose :
                        print('n :',n)
                        print('Corrigé :',fcor)
                        print('Votre fonction :',fel)
                        print()
            except : 
                pass

    return pts*coef/nb_tests,total*coef/nb_tests


def test_q04(foo,verbose):
    pts = 0
    total = 0
    
    coef = 2
    nb_tests = 6
    liste_n = [rd.randrange(11,20) for i in range(nb_tests)]
    liste_p = [rd.randrange(0,10) for i in range(nb_tests)]
    les_t = [i/(nb_tests-1) for i in range(nb_tests) ]
    nb_tests = nb_tests*nb_tests*nb_tests
    
    for n in liste_n :
        for p in liste_p :
            for t in les_t :
                total +=1
                try :
                    fcor =  _bernstein(n,p,t)
                    fel = foo(n,p,t)

                    if m.isclose(fcor,fel):
                        pts +=1 
                    else : 
                        if verbose :
                            print('n :',n)
                            print('Corrigé :',fcor)
                            print('Votre fonction :',fel)
                            print()
                except : 
                    pass

    return pts*coef/nb_tests,total*coef/nb_tests

def test_q05(foo,verbose):
    pts = 0
    total = 0
    
    coef = 2
    nb_tests = 10
    liste_n = [rd.randrange(2,100) for i in range(nb_tests)]
    
    for n in liste_n :
        total +=1
        try :
            fcor =  _calcule_t(n)
            fel = foo(n)
            
            if np.isclose(fcor,fel) :
                pts +=1 
            else : 
                if verbose :
                    print('n :',n)
                    print('Corrigé :',fcor)
                    print('Votre fonction :',fel)
                    print()
        except : 
            pass
    
    return pts*coef/nb_tests,total*coef/nb_tests

def test_q06(foo,verbose):
    pts = 0
    total = 0
    
    coef = 2
    nb_tests = 10
    
    for i in range(nb_tests):
        total +=1
        try :
            P0 = [rd.randint(-10,10),rd.randint(-10,10)]
            P1 = [rd.randint(-10,10),rd.randint(-10,10)]
            P2 = [rd.randint(-10,10),rd.randint(-10,10)]
            P3 = [rd.randint(-10,10),rd.randint(-10,10)]
            les_t = _calcule_t(50)
            fcor = _calcule_M(P0,P1,P2,P3,les_t)
            fel = foo(P0,P1,P2,P3,les_t)

            if np.isclose(fcor,fel) :
                pts +=1 
            else : 
                if verbose :
                    print('n :',n)
                    print('Corrigé :',fcor)
                    print('Votre fonction :',fel)
                    print()
        except : 
            pass

    return pts*coef/nb_tests,total*coef/nb_tests

def test_q08(foo,verbose):
    pts = 0
    total = 0
    
    coef = 2
    nb_tests = 10
    
    for i in range(nb_tests):
        total +=1
        try :
            P0 = [rd.randint(-10,10),rd.randint(-10,10)]
            P1 = [rd.randint(-10,10),rd.randint(-10,10)]
            
            fcor = _milieu(P0,P1)
            fel = foo(P0,P1)

            if np.isclose(fcor,fel) :
                pts +=1 
            else : 
                if verbose :
                    print('n :',n)
                    print('Corrigé :',fcor)
                    print('Votre fonction :',fel)
                    print()
        except : 
            pass

    return pts*coef/nb_tests,total*coef/nb_tests

def test_q09(foo,verbose):
    pts = 0
    total = 0
    
    coef = 2
    nb_tests = 10
    
    for i in range(nb_tests):
        total +=1
        try :
            P0 = [rd.randint(-10,10),rd.randint(-10,10)]
            P1 = [rd.randint(-10,10),rd.randint(-10,10)]
            P2 = [rd.randint(-10,10),rd.randint(-10,10)]
            P3 = [rd.randint(-10,10),rd.randint(-10,10)]
            
            poly = (P0,P1,P2,P3)
            fcor = _etape_casteljau(poly)
            fel = foo(poly)

            if np.isclose(fcor,fel) :
                pts +=1 
            else : 
                if verbose :
                    print('n :',n)
                    print('Corrigé :',fcor)
                    print('Votre fonction :',fel)
                    print()
        except : 
            pass

    return pts*coef/nb_tests,total*coef/nb_tests


def test_q10(foo,verbose):
    pts = 0
    total = 0
    
    coef = 2
    nb_tests = 10
    
    for i in range(nb_tests):
        total +=1
        try :
            P0 = [rd.random(),rd.random()]
            P1 = [rd.random(),rd.random()]
            
            fcor = _distance(P0,P1)
            fel = foo(P0,P1)

            if np.isclose(fcor,fel) :
                pts +=1 
            else : 
                if verbose :
                    print('n :',n)
                    print('Corrigé :',fcor)
                    print('Votre fonction :',fel)
                    print()
        except : 
            pass

    return pts*coef/nb_tests,total*coef/nb_tests

def test_q11(foo,verbose):
    pts = 0
    total = 0
    
    coef = 2
    nb_tests = 10
    
    for i in range(nb_tests):
        total +=1
        try :
            P0 = [rd.randint(-10,10),rd.randint(-10,10)]
            P1 = [rd.randint(-10,10),rd.randint(-10,10)]
            
            poly = (P0,P1)
            fcor = _cond_arret(poly)
            fel = foo(poly)

            if np.isclose(fcor,fel) :
                pts +=1 
            else : 
                if verbose :
                    print('n :',n)
                    print('Corrigé :',fcor)
                    print('Votre fonction :',fel)
                    print()
        except : 
            pass

    return pts*coef/nb_tests,total*coef/nb_tests
    
def go(foo1,foo2,foo3,foo4,foo5,foo6,foo8,foo9,foo10,foo11,verbose = False):
    i = 0
    notes = {}
    tot = 2
    
    tests = [[test_q01,foo1],[test_q02,foo2],
             [test_q03,foo3],[test_q04,foo4],
             [test_q05,foo5],[test_q06,foo6],
             #[test_q07,foo7],
             [test_q08,foo8],
             [test_q09,foo9],
             [test_q10,foo10],
             [test_q11,foo11]]
    
    for t in tests : 
        tq,f = t
        pts = 0
        i +=1
        try :
            pts,tot = tq(f,verbose)
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
    print(points*20/total,20) 
 