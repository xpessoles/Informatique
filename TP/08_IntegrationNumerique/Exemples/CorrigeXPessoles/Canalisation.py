# -*- coding: utf-8 -*-
#! /usr/bin/env python

from math import pi,exp
def erf(x,nb):
    if x>=0:
        return trapeze(fexp,0,x,nb)
	else :
	    return None

def fexp(u):
    return (2/pi)*exp(-u*u)

def trapeze(f,a,b,nb):
    res = 0
	pas = abs(b-a)/nb
	for i in range(nb):
	    x0 = a+pas*i
		x1 = a+pas*(i+1)
	    res = res + (x1-x0)*0.5*(f(x0)+f(x1))

D=2.8*10**(-7)
T0=278
T1=258
tf=10


