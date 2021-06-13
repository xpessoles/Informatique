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
h=float(input("pas de temps d'integration h=? en s"))
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
t=0
x0=0
y1=x0
y2=V0
V=[y2]
T=[0]
X=[y1]
##===============
while y2>0:         #ZONEA
    t=t+h
    ##=====
    ##Euler
                #Debut Zone B
    y2n=y2-h*(a+b*exp(-y2/Vref))*g
    y1n=y1+h*y2
                
                
                #Fin Zone B
    ##=====
    y1=y1n
    y2=y2n
    X.append(y1)
    V.append(y2)
    T.append(t)
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
fig1=plt.figure()
plt.plot(T,V,label="Vitesse en m/s")
plt.plot(T,X,label="position en m")
plt.xlabel("Temps en s")
plt.legend()
plt.show()
fig1.savefig('figure_finale.pdf')