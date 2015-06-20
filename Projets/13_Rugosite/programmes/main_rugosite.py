#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__      = "Xavier Pessoles"
__email__ = "xpessoles.ptsi@free.fr"

import numpy as np
from scipy import fftpack
import matplotlib.pyplot as plt
import sys
sys.path.append('C:\\Enseignement\\GitHub\\Informatique\\Projets\\13_Rugosite\\programmes')

import math
import biblio_rugosite

x,y = biblio_rugosite.generate_profil(0.01,5,100,500,0.5,2000)

fourier = fftpack.fft(y)/np.size(y)
freq = np.arange(0,2001)*4000/2000
#plt.plot(x,y)
plt.plot(freq,np.abs(fourier),'b')
plt.plot(freq,np.abs(fourier),'r.')

plt.grid()
plt.show()














