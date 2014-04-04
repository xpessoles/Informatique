
from math import log, sqrt

def ph_1(C):
    return -log(C)

def ph_2(C,pKa):
    return 0.5*(pKa - log(C))

def ph_3(C,pKa):
    Ka = -log(pKa)
    return -log((-Ka+sqrt(Ka*(Ka+4*C)))/(2))
    

def f(h,C,PKa):
    Ka = -log(pKa)
    return h**3 + Ka*h**2 - (Ke+Ka*C)*h-Ka*Ke
    