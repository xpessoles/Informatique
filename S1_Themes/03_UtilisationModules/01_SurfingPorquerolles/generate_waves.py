# -*- coding: utf-8 -*-
"""
Created on Wed Jun  9 22:55:28 2021

@author: xpess
"""
import numpy as np
import matplotlib.pyplot as plt
import random

les_t = np.linspace(-40,40,10000)

les_vagues = 5*np.sin(les_t*.5)+2

#plt.plot(les_t,les_vagues)

les_vagues2 = les_vagues + np.sin(les_t*2+10)

#plt.plot(les_t,les_vagues2)

les_vagues3 = les_vagues2 * np.sin(0.001*les_t+2)*.01
les_vagues4 = les_vagues3+0.00002*les_t*les_t
#plt.plot(les_t,les_vagues4*100)

les_v = 100*les_vagues4[2500:-200]
les_t = np.linspace(0,40,len(les_v))

plt.grid()
plt.xlabel("Temps ($t$ en s.)")
plt.ylabel("Niveau de vague ($\\eta$ en m.)")

m = sum(les_v)/len(les_v)
plt.plot(les_t,les_v,label="Niveau des vagues")
xx = [0,40]
yy = [m,m]
plt.plot(xx,yy,label="Niveau moyen")
plt.legend()
fid = open('vague.txt',"w")
for i in range(len(les_t)):
    s = str(les_t[i])+","+str(les_v[i])+"\n"
    fid.write(s)
fid.close()
plt.savefig("fig_00.pdf")