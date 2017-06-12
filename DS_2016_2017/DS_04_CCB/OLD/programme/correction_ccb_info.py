### concours blanc info 2017 : relevé de température

import matplotlib.pyplot as plt
import numpy as np


t=[6,2,15,2,13,1,8,3,5]
t2D=[[6,2,15,2,13,1,8,3,5],[6,2,15,2,0,1,8,3,5],[6,2,15,2,13,-1,8,3,5]]
Tmin=[5,4,6,3,8,3,1,2,0,-1,-2,-6,-7,0,5,6,10,11,12]
Tmax=[15,14,16,13,12,13,11,12,10,5,1,0,1,3,6,10,15,20,25]

# question 1
def mini(t):
    if len(t)==0:
        return None
    p=t[0]
    for i in range(1,len(t)):
        if t[i]<p:
            p=t[i]
    return p

# question 2
# n-1 comparaisons soit une complexité en O(n)

# question 3
def max(t):
    m=t[0]
    for i in range(1,len(t)):
        if t[i]>=m:
            m=t[i]
    return (m)
    
# question 4 : condition d'arret et boucle de recursivité


    
# question 5
def mini_recursive(t):
    n=len(t)
    if n==1:
        return t[0]
    else:
        p=mini_recursive(t[0:n-1])
        if t[-1]<p:
            p=t[-1]
        return p
    
# question 6
def position_mini(t):
    indice=0
    p=t[0]
    for i in range(1,len(t)):
        if t[i]<=p: #ou t[i]<p
            p=t[i]
            indice=i
    return p,i
    
# question 7
def mini2D(t):
    p=mini(t[0])
    for i in range(1,len(t)):
        p1=mini(t[i])
        if p1<p:
            p=p1
    return p
    
# question 8
def chaine_mini(L):
    nom=L[0][0]
    valeur=L[0][1]
    for i in range(1,len(t)):
        if L[i][1]<=valeur:
            valeur=L[i][1]
            nom=L[i][0]
    return nom
    
# question 9
def majores_par(t,seuil):
    k=0
    for i in range(len(t)):
        if t[i]<seuil:
            k+=1
    return k
    
# question 10
def elements_majores_par(t,seuil):
    L1=[]
    for i in range(len(t)):
        if t[i]<seuil:
            L1.append(t[i])
    return L1


### partie 2
a=0.00390802
b=a/100
c=a/1000000
R=104

def f(x):
    return 100*(1+a*x+b*x**2+c*x**3*(x-100))-R
    
def g(x):
    return 100*(1+a*x)-R
    
    
les_theta=[i*0.5 for i in range(101)]
les_f=[f(i) for i in les_theta]
les_g=[g(i) for i in les_theta]
plt.plot(les_theta,les_f)
#plt.plot(les_theta,les_g)
plt.xlabel('les theta')
plt.ylabel('f(theta)')
plt.grid()
plt.show()

### partie 3



### partie 4
# question 18
# nb de jours codage de 1 à 365 soit (9+2*90+3*265)caractères
# nb de ';' 2*365
# 4 caractères maxi pour la température mini et maxi : 4*2*365
# soit 4634 octets (ASCII 1 octet)

# question 19
def moyenne(L1,L2):
    Lm=[]
    for i in range(len(L1)):
        Lm.append((L1[i]+L2[i])/2)
    return Lm
    
# question 20
Tmoy=moyenne(Tmin,Tmax)
print (Tmoy)
# question 21
nb_jours_gel=majores_par(Tmoy,0)
print (nb_jours_gel)

# question 22
# ecart=[]
# for i in range(len(Tmin)):
#     ecart.append(Tmax,Tmin)
    
#ou
ecart=[Tmax[i]-Tmin[i] for i in range(len(Tmin))]
print (ecart)

mini_ecart=mini(ecart)
print(mini_ecart)

# question 23
variation=0
for i in range(0,len(Tmax)-1):
    e=abs(Tmax[i+1]-Tmax[i])
    if e>variation:
        variation=e
print (variation)
        
### partie 5 modelisation physique

# question 24
def f2(theta,t):
    return (mu*(1+eps*np.cos(omega*t))-alpha*(theta+T0)**4)

# question 25
# cours euler

# question 26
def euler(theta0,dt,tmax):
    temps=[0]
    theta=[theta0]
    t=dt
    while t<=tmax:
        temps.append(t)
        theta.append(theta[-1]+dt*f2(theta[-1],t))
        t=t+dt
    return temps,theta

    
    