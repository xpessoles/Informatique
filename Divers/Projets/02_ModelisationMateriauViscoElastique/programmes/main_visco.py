#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__      = "Xavier Pessoles"
__email__ = "xpessoles.ptsi@free.fr"

import matplotlib.pyplot as plt
import numpy as np
import sys
sys.path.append('C:\\Enseignement\\GitHub\\Informatique\\Projets\\02_ModelisationMateriauViscoElastique\\programmes')
import math
import biblio_visco

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

temps = [i*h for i in range(int(T/h)+1)]
#ff = [biblio.f_sin(1,2*math.pi,x) for x in temps]

