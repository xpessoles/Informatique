def parseMaxpidFile(nom_file):
    fid = open(nom_file,'r')
    donnees_fichier=fid.readlines()
    fid.close()
    temps=[]
    valeur=[]
    for ligne in donnees_fichier:
        s = ligne.split()
        if len(s)==3:
            temps.append(float(s[0]))
            valeur.append(float(s[2]))
    res=[temps,valeur]
    return res

def ordre(temps,mesures):
    j=0
    for i in range(len(mesures)-1):
        j=i
        if abs(mesures[i]-mesures[i+1])>0.1:
            break
    pente = (abs(mesures[j+1]-mesures[j]))/(temps[j+1]-temps[j])
    if pente <0.1:
        return 2
    else : 
        return 1
    
def calculGain(mesures,E0):
    gain = (mesures[len(mesures)-1]-mesures[0])/E0
    return gain

def calculGainMoyen(mesures,E0):
    gain = (calculValeurFinale(mesures)-mesures[0])/E0
    return gain

def calculDebut(mesures):
    j=0
    for i in range(len(mesures)-1):
        j=i
        if abs(mesures[i]-mesures[i+1])>0.1:
            break
    return j

def calculValeurFinale(mesures):
    i_ini=int(0.8*len(mesures))
    res = 0
    for i in range(i_ini,len(mesures)):
        res = res + mesures[i]
    return res/(len(mesures)-i_ini)
        

def calculTau(temps,mesures,E0):
    i0 = calculDebut(mesures)               # Index du depart de la mesure
    ifin = len(mesures)                     # Index de la derniere mesures   
    mes0 = mesures[i0]                     # Valeur initiale
    mesf = calculValeurFinale(mesures)     # Calcul de la valeur finale
    mes_63 = 0.63*(mesf-mes0)+mes0
    print(mes_63)
    ind_g = i0
    ind_d = ifin-1
    mes_g=mesures[ind_g]
    mes_d=mesures[ind_d]

    ind_m=ind_g

    
    while ind_d-ind_g>2:
        ind_m = int((ind_g+ind_d)/2)
        mes_m =mesures[ind_m]
        if mes_m <= mes_63 :
            ind_g = ind_m
            mes_g = mes_m
        else :
            ind_d = ind_m
            mes_d = mes_m
    print(temps[i0])
    return temps[ind_m]-temps[i0]

def identificationOrdre1(temps,mesures,E0):
    K = calculGainMoyen(mesures,E0)
    tau = calculTau(temps,mesures,E0)
    return K,tau
    

##########

nom_fichier="Echelon1.Txt"
res = parseMaxpidFile(nom_fichier)
temps = res[0]
mesures = res[1]
E0=22
# Test ordre
# print(ordre(res[0],res[1]))

# Test Calcul gain
# print(calculGain(res[1],22.))
# print(calculTau(temps,mesures,22.))
print(identificationOrdre1(temps,mesures,E0))

# Affichage des courbes
import matplotlib.pyplot as plt
import numpy as np
p1=plt.plot(res[0],res[1],linewidth=3)
plt.grid(True, which="both", linestyle="dotted")
plt.show()

