#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__      = "Xavier Pessoles"
__email__ = "xpessoles.ptsi@free.fr"

import matplotlib.pyplot as plt
import numpy as np
import sys
sys.path.append('C:\\Enseignement\\GitHub\\Informatique\\Projets\\01_ModelisationAmortisseur\\Programme')
import math
import biblio

from scipy import *
from scipy.integrate import odeint

global k,c,m
# Raideur du ressort en N/m
k = 1000000
# Coefficient d'amortissement en N.s/m
c = 10000
# Masse en kg
m = 1000
# Pas de temps en seconde
h = 0.0001
# Temps total en s
T = 2*math.pi
# Initialisation 
x0,v0 = 0,0
# Nombre d'éléments viscoélastiques 
n = 5


temps = [i*h for i in range(int(T/h)+1)]
#ff = [biblio.f_sin(1,2*math.pi,x) for x in temps]



""" 
# ECHELON
f_echelon = [biblio.echelon(10) for x in temps]
x_newton_echelon = biblio.solve_eq(m,k,c,x0,v0,h,temps,f_echelon)

conditions_ini=[x0,v0]
solution=odeint(syst_diff_echelon,conditions_ini,temps)
x_ode = solution[:,0]
v_ode = solution[:,1]

plt.plot(temps,x_newton_echelon)
plt.plot(temps,x_ode)

plt.show()
"""

# SINUS
f_sinus = [biblio.f_sin(1,1,x) for x in temps]
x_newton_sinus = biblio.solve_eq(m,k,c,x0,v0,h,temps,f_sinus)
conditions_ini=[x0,v0]
solution=odeint(syst_diff_sinus,conditions_ini,temps)
x_ode = solution[:,0]
v_ode = solution[:,1]
#plt.plot(temps,f_sinus)
plt.plot(temps,x_newton_sinus)
plt.plot(temps,x_ode)

plt.grid()
plt.show()














