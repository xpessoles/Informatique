from math import *
import matplotlib.pyplot as plt
#Calcul de la distance de freinage d'un vehicule
##Methode : Tangent amelioree
print("Calcul e la distance de freinage d'un vehicule de masse m")
print("Vitesse initiale v0")
print("coefficient de frottement sol-roue sur sol sec f=0.8+0.2e(-V/Vref)")
print("position initiales x0=0")
##
V0=float(input("vitesse initiale v0=? en m/s"))
# h=float(input("pas de temps d'integration h=? en s"))
##====================
##Donnees
g=9.81#m/s2
##parametre du coefficient de frottement f=a+b*e(-V/Vref)
a=0.8
b=0.2
Vref=5#m/s
##===============
##t-temps (discretise avace le pas h)
##y1 - abscisse x calcul au pas i-1
##y2 - vitesse horizontale calculee au pas i-1
##y1n - abscisse x calcule au pas i
##y2n -  vitesse horizontale calculee au pas i
##===============
##Conditions initiales

Lh=[1,0.01,0.0001]
for k in range(len(Lh)):
    t=0
    x0=0
    y1=x0
    y2=V0
    Lt=[t]
    V=[y2]
    xG=[y1]
    h=Lh[k]
    ##===============
    while y2>0:        #ZONEA
        t=t+h
        ##=====
        ##Euler
                    #Debut Zone B
        y1n=y1+h*y2
        y2n=y2+h*(-g*(a+b*exp(-y2/Vref)))            
                    
                    
                    #Fin Zone B
        ##=====
        y1=y1n
        y2=y2n
        Lt.append(t)
        V.append(y2)
        xG.append(y1)
    ##===============
    #Debut de la zone C
    DA=y1
    Vf=y2
    tf=t
    
    #Fin de la zone C
    ##===============
    
    print("Temps de freinage"+"tf="+str(tf))
    print("Distance d'arret"+"DA="+str(DA))
    print("Verification vitesse nulle"+"Vf="+str(Vf))
    
    plt.plot(Lt,xG,label='Position avec h='+str(h))
    plt.plot(Lt,V,label='Vitesse avec h='+str(h))
    
plt.xlabel('Temps (en s)')
plt.ylabel('Position en (m) et Vitesse (en m/s)')
plt.grid()
plt.legend(loc='upper left')
plt.show()