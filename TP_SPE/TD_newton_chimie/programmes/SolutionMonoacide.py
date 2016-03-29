from math import log10,sqrt
from scipy.optimize import newton

global pKa,c
pKa = 3.2
c=1*10**(-2)

def pH_1(c):
    return -log10(c) 

def pH_2(c,pKa):
    return 0.5*(pKa-log10(c))
    

def pH_3(c,pKa):
    Ka = 10**(-pKa)
    return -log10(0.5*(-Ka*sqrt(Ka*(Ka+4*c))))

    
def f(x):
    Ka = 10**(-pKa)
    Ke = 10**(-14)
    return x**3 +Ka*x*x-(Ke+Ka*c)*x-Ka*Ke


def pH_4(c):
    # ph compris entre 0 et 14
    h = 10**(0)
    sol =  newton(f,h)
    return -log10(sol)
    
    
    