
fid = open("MesureBrute.lvm")
fichier = fid.readlines()
fid.close()
mesures=fichier[22:]
temps=[]
maneton=[]
malte=[]

import numpy as np
import matplotlib.pyplot as plt

for i in range(len(mesures)):
    tt = str(mesures[i][0:8]).replace(',','.')
    man = str(mesures[i][9:18]).replace(',','.')
    mal = str(mesures[i][19:29]).replace(',','.')
    temps.append(float(tt))
    maneton.append(float(man))
    malte.append(float(mal))

p1=plt.plot(temps,malte)
plt.grid(True, which="both", linestyle="dotted")
plt.show()
