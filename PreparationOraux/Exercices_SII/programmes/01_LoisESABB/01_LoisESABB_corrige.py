
# Import du module d'optiomisation 
from scipy.optimize import fsolve
# Import de fonctions mathématiques
from math import cos,sin,pi

# Pas de calcul de la loi entrée sortie (en degrés)
pas_calcul = .5

global t1,t1_ini,t1_fin

t1_ini = -90*pi/180
t1_fin =  0*pi/180
t1 = t1_ini


# Définition du système d'équations 
# =================================
global a,b,c,d,e,ff
a,b,c,d,e,ff = 265,280,280,89.5,25,13

def systeme(x,t1):
    t2,t3,t4 = x[0],x[1],x[2]
    eq1 = a*cos(t1)+b*cos(t2)*cos(t1)-b*sin(t2)*sin(t1)-c*cos(t4)+d+ff*sin(t1)
    eq2 = a*sin(t1)+b*cos(t2)*sin(t1)+b*sin(t2)*cos(t1)-c*sin(t4)+e-ff*cos(t1)
    eq3 = t1+t2+t3-t4
    res = [eq1,eq2,eq3]
    return res


# Résolution du système :
# =======================
def resoudre():
    res = []
    t1 = t1_ini
    sol_ini = [-2,1,-2]  
    while t1<=t1_fin :
        res.append(fsolve(systeme,sol_ini,t1))
        sol_ini = res[-1]
        t1 = t1 + pas_calcul*pi/180    
    t1_res = []
    t2_res = []
    t3_res = []
    t4_res = []
    for i in range(len(res)):
        t4_res.append(-res[i][2]*180/pi-44.04)
        t2_res.append((res[i][0]*180/pi))
        t3_res.append((res[i][1]*180/pi))
        t1_res.append(-(t1_ini*180/pi + i*pas_calcul))

    return [t1_res,t2_res,t3_res,t4_res]


# Affichage des courbes :
# =======================
from scipy import *
from pylab import *
t1_res,t2_res,t3_res,t4_res = resoudre()

#plot(t1_res,t2_res,'r.-',label="$\\theta_2$")
plt.plot(t1_res,t4_res,'g.-',label="$\\theta_4$")
#plot(t1_res,t3_res,'b.-',label="$\\theta_3$")


# Lecture des mesures
# ===================
#import os
#os.chdir("C:\\Enseignement\\GitHub\\Informatique\\PreparationOraux\\Exercices_SII\\programmes\\01_LoisESABB")
fid = open("data/mesures.txt","r")
tps_mes = []
t1_mes =[]
t4_mes =[]
for ligne in fid :
    ligne = ligne.split("\t")
    tps_mes.append(float(ligne[0]))
    t4_mes.append(float(ligne[1]))
    t1_mes.append(float(ligne[2]))
    
    
plt.plot(t1_mes,t4_mes,label = "Mesure")    

#plt.legend()
plt.show()