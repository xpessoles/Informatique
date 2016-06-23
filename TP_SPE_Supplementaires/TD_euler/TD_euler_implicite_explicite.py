### TD sur les méthodes d'Euler explicite et implicite et étude de la stabilité et rapidité
#Importation des modules
import matplotlib.pyplot as plt
import math
import numpy as np
import time

### question 1
#relation de récurrence de la méthode d'Euler explicite yk+1=yk+hf(yk,tk)
# pour l'équation choisie domega/dt=(Kc*U-omega)/tau
# donc omega=omega+h*(Kc*U-omega)/tau

#Définition des paramètres

T=2
U0=5
omega0=0


### question 2
def euler1_explicite(T,h,U0,omega0):
    ''' Renvoie une liste des ordonnées pour un premier ordre
    soumis à un échelon u de tension '''
    s=omega0
    sortie=[omega0]
    for i in range(1,int(T/h)):
        f=(0.5*U0-s)/0.2
        s=s+f*h
        sortie.append(s)
    return sortie

### question 3    
### tracé de la solution exacte et des solutions approchées
def ordre1(t):
    return (0.5*5*(1-np.exp(-t/0.2)))
    
#trace des solutions pour différents pas de temps
marqueurs = ['^', '+', '*', '.', '', 'o'] #Les marqueurs
plt.figure(1)
k=0
for i in (0.5,0.2,0.1,0.01,0.005):
    x=np.linspace(0,T,int(T/i))
    y=euler1_explicite(T,i,U0,omega0)
    plt.plot(x,y,'--',color='b',marker=marqueurs[k],label='euler, pas= '+str(i))
    k=k+1
x=np.linspace(0,2,100)
y=ordre1(x)
plt.plot(x,y,'r',label='exacte')
plt.title('Euler explicite ordre 1')
plt.legend()
plt.show()

# La rapidité de la méthode d’Euler explicite ne dépends que des opérations de l’équation de récurrence et du nombre d’itérations souhaitées n. Ainsi, nous aurons un temps de calcul directement proportionnel au facteur n.


# En conclusion, le pas de temps d’un schéma explicite doit être choisi suffisamment petit devant les constantes de temps de l’équation différentielle pour éviter des instabilités numériques.
#facteur h/tau... qui crée l'instabilité

### question 4 sur un intervalle de temps de 2s
T=2
temps=[]
for i in (0.1,0.01,0.001,0.0001,0.00001,0.000001):
    x=np.linspace(0,T,int(T/i))
    td=time.clock()
    y=euler1_explicite(T,i,U0,omega0)
    tf=time.clock()-td
    temps.append(tf)
    
# print (temps)
# [2.7479030685469386e-05, 0.0001433544612868463, 0.001265690774825897, 0.013448171402936946, 0.08863642759358183, 0.8244762016695993]

### question 5 erreur de consistance
# Calcul de de l’erreur locale (ou erreur de consistance) :
# ci=h**2/2*deriveesecondefexacte(ti)

def consistance(t,h):
    return (-(h**2)/2*5*0.5/(0.2**2)*np.exp(-t/0.2))

T=2
erreur=[]
for h in (0.1,0.01,0.001,0.0001,0.00001,0.000001):
    erreur.append(consistance(T-h,h))
    
# print (erreur)
# [-2.3391196839906476e-05, -1.4914885605250613e-07, -1.4258593080448336e-09, -1.4194573563532274e-11, -1.4188187442413721e-13, -1.4187548988344106e-15]

### question 6...
fichier=open('euler_explicite.csv','w')
fichier.write("pas de temps h"+'\;'+"10**(-1)"+'\;'+'10**(-2)'+'\;'+'10**(-3)'+'\;'+'10**(-4)'+'\;'+'10**(-5)'+'\;'+'10**(-6)'+'\n')
fichier.write("N pas de temps"+'\;'+str(2//0.1)+'\;'+str(2//0.01)+'\;'+str(2//0.001)+'\;'+str(2//0.0001)+'\;'+str(2//0.00001)+'\;'+str(2//0.000001)+'\;'+'\n')
fichier.write("erreur"+'\;'+'\n')
fichier.write("temps de calcul"+'\;'+'\n')
fichier.close()

pas_de_temps=[1e-01, 1e-02, 1e-03,1e-04, 1e-05, 1e-06]

fichier=open('euler_explicite2.csv','w')
fichier.write("pas de temps h"+';'+"N pas de temps"+';'+"erreur"+';'+"temps de calcul"+'\n')
for i in range(len(pas_de_temps)):
    N=2//pas_de_temps[i]
    fichier.write(str(pas_de_temps[i])+';'+str(N)+';'+str(erreur[i])+';'+str(temps[i])+';'+'\n')
fichier.close()

### euler explicite pour une equation différentielle du second ordre
### question 7 sur feuille

### question 8
#Données
J=0.015
mu=0.01
dmg=0.6
theta0=np.pi/4

def euler2_explicite(T,Dt):
    #intervalle de temps
    n=int(T/Dt)
    
    #initialisation
    theta=[theta0,theta0]
    
    #résolution
    for i in range(2,n):
        theta.append((2-Dt*mu/J)*theta[i-1]+(Dt*mu/J-1)*theta[i-2]-(dmg*Dt**2/J)*np.sin(theta[i-2]))
    return theta


### avec l'exemple de sup 2014    
def ordre2_euler(w_0,xi,K,u,temps):
    ''' Renvoie une liste des ordonnées pour un premier ordre
    soumis à un échelon u de tension 
    pour une liste abscisse des temps fournie'''
    v=0
    a=0
    vitesse=[0]
    acc=[0]
    for i in range(1,len(temps)):
        f1=(K*u-v-2*xi*a/w_0)*((w_0)**2)
        f2=a
        a2=a+f1*(temps[i]-temps[i-1])
        v2=v+f2*(temps[i]-temps[i-1])
        vitesse=vitesse + [v2]
        acc=acc+[a2]
        v=v2
        a=a2
    return vitesse, acc
    
#Question 9
def ordre2_exacte(t):
    '''pour un theta petit solution de J*(theta..)+mu*(theta.)+dmg*theta=0'''
    z=0.01/(2*np.sqrt(1.5*10**(-2)*0.6))
    om=np.sqrt(0.6*100/1.5)
    return (np.pi/4*np.exp(-z*om*t)*np.cos((np.sqrt(1-z**2))*om*t)+z/(np.sqrt(1-z**2))*np.sin((np.sqrt(1-z**2))*om*t))
    
    
    

T=15
Dt=0.001 #prendre aussi Dt=0.1 pour une divergence de la fonction


plt.figure(2)
for i in [0.001,0.01]:
    temps=np.linspace(0,T,int(T/i))
    plt.plot(temps,euler2_explicite(T,i))
les_t=np.linspace(0,T,1000)
y=ordre2_exacte(les_t)
plt.plot(les_t,y,'r',label='exacte')
plt.title('Euler explicite ordre 2')
plt.legend()
plt.show()

### partie 3 methode d'euler implicite - utilisation de la méthode de newton
### question 10
### relation de recurrence de la méthode d'euler implicite Yi+1 = Yi + hF(ti+1;Yi+1)


### question 11
# Yi+1 - Yi - hF(ti+1;Yi+1) = 0
#si la fonction n'est pas linéaire il faut approcher le zéro de la fonction par la méthode de Newton
# si la fonction est linéaire mais avec des matrices (ou vecteurs) il faut inverser la matrice (coût temporel important)

#définition de la fonction dérivée
def dP(x):
    return 3*x**2-8*x+2
    
def zero_newton(f,df,u0,epsilon):
    x=float(u0)
    y=float(u0)-f(u0)/df(u0)
    i=0
    while abs(y-x)>epsilon:
        x=y
        y=y-f(y)/df(y)
        i=i+1
    return [y,f(y),i]
    
    
# Dans les cas linéaires, il faut au moins une inversion, ce qui est aussi très lourd pour les problèmes de grande dimension. Il faut donc retenir qu’une méthode implicite est généralement plus coûteuse qu’une méthode explicite à pas de temps égal.
 ### question 12   
### euler implicite
def euler1_implicite(T,h,U0,omega0):
    s=omega0
    sortie=[omega0]
    for i in range(1,int(T/h)):
        s=(s*0.2+h*0.5*U0)/(0.2+h)
        sortie.append(s)
    return sortie


### question 13    
marqueurs = ['^', '+', '*', '.', '', 'o'] #Les marqueurs
plt.figure(3)
k=0
T=3
for i in (1,0.5,0.2,0.1,0.01,0.005):
    x=np.linspace(0,T,int(T/i))
    y=euler1_implicite(T,i,U0,omega0)
    plt.plot(x,y,'--',color='b',marker=marqueurs[k],label='euler, pas= '+str(i))
    k=k+1
x=np.linspace(0,T,100)
y=ordre1(x)
plt.plot(x,y,'r',label='exacte')
plt.title('Euler implicite')
plt.legend()
plt.show()

### question 14
#pas de divergence de courbe et s=(s*0.2+h*0.5*U0)/(0.2+h) on a h+tau au dénominateur
    
    