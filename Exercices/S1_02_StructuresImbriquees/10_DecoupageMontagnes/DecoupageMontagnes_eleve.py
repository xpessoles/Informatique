# -*- coding: utf-8 -*-
"""
@author: xpessoles@lamartin.fr
"""
# === Import des Modules === 
import math as m
import random as rd
import numpy as np
import matplotlib.pyplot as plt

# === Génération d'un profil de montagne ===
les_x = np.linspace(-1.1,1.3,1000)
les_y1 = 0.6366 * np.cos(6.2813*les_x-np.pi/2)
les_y2 = 0.2122 * np.cos(18.85*les_x-np.pi/2)
les_y = les_y1+les_y2-0.4*les_x*les_x

les_x = np.linspace(0,60*14,1000)
les_y = 800*les_y + 1500
alt = les_y 

plt.ylabel("Altitude [m]")
plt.plot(les_x,les_y,label = "Profil")
plt.legend()
plt.grid()
plt.show()

# ==========================================