### concours blanc info 2017 : relevé de température

import matplotlib.pyplot as plt
import numpy as np

tp=[6,2,15,1,15,1]
t=[6,2,15,2,13,1,8,3,5]
t2D=[[6,2,15,2,13,1,8,3,5],[6,2,15,2,0,1,8,3,5],[6,2,15,2,13,-1,8,3,5]]
Tmin=[5,4,6,3,8,3,1,2,0,-1,-2,-6,-7,0,5,6,10,11,12]
Tmax=[15,14,16,13,12,13,11,12,10,5,1,0,1,3,6,10,15,20,25]
Ltemps=[i*360/18 for i in range(19)]

# question 1
def mini(t):
    if len(t)==0:
        return None
    p=t[0]
    for i in range(1,len(t)):
        if t[i]<p:
            p=t[i]
    return p
    
In [13]: mini([6,2,15,1,15,1])
pour i=1 mini=2
pour i=2 mini=2
pour i=3 mini=1
pour i=4 mini=1
pour i=5 mini=1

# question 2
# n-1 comparaisons soit une complexité en O(n)

# question 3
def max(t):
    if len(t)==0:
        return None
    m=t[0]
    for i in range(1,len(t)):
        if t[i]>=m:
            m=t[i]
    return (m)
    
# test    
# max(tp)
# Out[7]: 15
    
# question 4 : condition d'arret : quand la liste n'a qu'un élément alors cet élément est le mini
# boucle de recursivité : l'élément suivant dans la liste est comparé au mini de la liste tronquée 

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
        
# mini_recursive(tp)
# Out[9]: 1
    
# question 6
def position_mini(t):
    indice=0
    p=t[0]
    for i in range(1,len(t)):
        if t[i]<=p: #ou t[i]<p
            p=t[i]
            indice=i
    return i
    
# In [14]: position_mini(tp)
# Out[14]: 5
    
# question 7
def mini2D(t):
    p=mini(t[0])
    for i in range(1,len(t)):
        p1=mini(t[i])
        if p1<p:
            p=p1
    return p
    
# In [17]: mini2D(t2D)
# Out[17]: -1
    
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
    
# In [18]: majores_par(tp,10)
# Out[18]: 4
    
# question 10
def elements_majores_par(t,seuil):
    L1=[]
    for i in range(len(t)):
        if t[i]<seuil:
            L1.append(t[i])
    return L1
    
# In [19]: elements_majores_par(tp,10)
# Out[19]: [6, 2, 1, 1]


### partie 2
a=0.00390802
b=a/100
c=a/1000000
R=104
# question 11
def g(x):
    return 100*(1+a*x+b*x**2+c*x**3*(x-100))-R
    
# question 12
les_theta=[i*0.5 for i in range(101)]
les_g=[g(i) for i in les_theta]
plt.plot(les_theta,les_g)
plt.xlabel('les theta')
plt.ylabel('g(theta)')
plt.grid()
plt.show()

# question 13 dichotomie
def dichotomie(a, b, f, epsilon):
    g = a
    d = b
    while (d - g) > 2 * epsilon:
        m = (g + d)/2
        if f(g) * f(m) <= 0:
            d = m
        else:
            g = m
    return((d + g) / 2)

# la lecture de la courbe donne le zéro entre a=5 et b=10
# In [22]: dichotomie(0,15,g,10**-6)
# Out[22]: 9.423187673091888

# question 14
def tempinfrahoraire(Ltemps,Ltheta):
    s=0
    for i in range(1,len(Ltheta)):
        s=s+Ltheta[i]*(Ltemps[i]-Ltemps[i-1]) #intégration à droite, c'est la valeur de température mesurée à l'instant t{i+1} qui correspond à la température mesurée sur l'intervalle [t{i},t{i+1}]
    return s/(Ltemps[-1]-Ltemps[0]),Ltemps[-1]
    
# In [33]: tempinfrahoraire(Ltemps,Tmax)
# Out[33]: (10.38888888888889, 360.0)

# question 15
# les listes de temps en secondes et de theta ont la même longueur
# les_t_6min=[]
# les_theta_6min=[]
# for i in range(len(theta)):
#     s=0
#     Ltemps=[]
#     Ltheta=[]
#     while s<=360:
#         Ltemps.append(temps[i])
#         Ltheta.append(theta[i])
#         s=s+temps[i]-temps[i-1]
#     moy_theta,heure=tempinfrahoraire(Ltemps,Ltheta)
#     les_t_6min.append(heure)
#     les_theta_6min.append(moy_theta)

    
    
### partie 3
# question 16
# une clé primaire est la donnée qui permet d'identifier de manière unique un enregistrement dans une table
# pour la table ville, la clé primaire est le numéro d'insee
# pour la table mesures, il n'y a pas de clé primaire simple, il faut la construire à partir de deux colonnes ville,jour

# question 17
# SELECT * FROM mesures WHERE (Tmax+Tmin)/2<0;

# question 18
# SELECT INSEE,nom,dpt  FROM villes WHERE lat>47 AND lon>2;

# question 19
# SELECT DISTINCT nom FROM villes INNER JOIN mesures ON INSEE=ville WHERE Tmax>30;


### partie 4
# question 20
# nb de jours codage de 1 à 365 soit (9+2*90+3*265)caractères
# nb de ';' 2*365
# 4 caractères maxi pour la température mini et maxi : 4*2*365
# soit 4634 octets (ASCII 1 octet)

# question 21
def moyenne(a,b):
    Lm=[]
    for i in range(len(a)):
        Lm.append((a[i]+b[i])/2)
    return Lm
    
# question 22
Tmoy=moyenne(Tmin,Tmax)

# question 23
nb_jours_gel=majores_par(Tmoy,0)

# question 24
# ecart=[]
# for i in range(len(Tmin)):
#     ecart.append(Tmax,Tmin)
#ou
ecart=[Tmax[i]-Tmin[i] for i in range(len(Tmin))]

mini_ecart=mini(ecart)


# question 25
variation=0
for i in range(0,len(Tmax)-1):
    e=abs(Tmax[i+1]-Tmax[i])
    if e>variation:
        variation=e
print (variation)
        
### partie 5 modelisation physique

# question 26
def f(theta,t):
    return (mu*(1+eps*np.cos(omega*t))-alpha*(theta+T0)**4)

# question 27
# cours euler

# question 28
def euler(theta0,dt,tmax):
    temps=[0]
    theta=[theta0]
    t=dt
    while t<=tmax:
        temps.append(t)
        theta.append(theta[-1]+dt*f2(theta[-1],t))
        t=t+dt
    return temps,theta

    
    