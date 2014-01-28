
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

def val_moy_n(temps,tab,n):
    """
    Retourne une liste de couple[temps,tab_f]
    ou tab_f est une valeur moyenne de tab sur n éléments
    """
    tab_f=[]
    for i in range(0,len(temps),n):
        tmp=0
        if i+n<len(temps):
            for j in range(i,i+n):
                tmp = tmp+tab[j]
            tab_f.append([temps[i],tmp/n])
    return tab_f


def int_rect_n(temps,tab,n):
    """
    Retourne une liste de couple[temps,tab_f]
    ou tab_f est une intégration du signal numérique
    """
    tab_f=[]
    pas=temps[n]-temps[0]
    for i in range(0,len(temps),n):
        tmp=0
        if i+n<len(temps):
            tab_f.append([temps[i], pas*tab[i]])
    return tab_f




malte_f=val_moy_n(temps,malte,50)
maneton_f=val_moy_n(temps,maneton,50)
#malte_f=int_rect_n(temps,malte,50)
mm=[]
tt=[]
mama=[]
for i in range(len(malte_f)):
    tt.append(malte_f[i][0])
    mm.append(malte_f[i][1])
    mama.append(maneton_f[i][1])
    
#plt.plot(temps,malte,'r.')
plt.plot(tt,mm,linewidth=2)
plt.plot(tt,mama,linewidth=2)
plt.grid(True, which="both", linestyle="dotted")
#plt.show()

fid=open('Mesure_Traitee.txt','w')
for i in range(len(tt)):
    ch=str(tt[i])+','+str(mm[i])+'\n'
    fid.write(ch)
fid.close()
