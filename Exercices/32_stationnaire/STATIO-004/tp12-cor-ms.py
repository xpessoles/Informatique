import numpy as np
from math import exp, log
import matplotlib.pyplot as pl
## Question 1

xmin = 0
xmax = 20
f = lambda x : 0.02*x*(x-5)


def trace_fonction(xmin,xmax,f,nom_de_fichier,lab=""):
    """Trace la courbe de f sur [xmin,xmax]
    Enregistre dans nom_de_fichier"""
    pl.clf()
    les_x = np.linspace(xmin,xmax,1000)
    les_y = [f(t) for t in les_x]
    pl.plot(les_x,les_y,label=lab)
    if lab != '' :
        pl.legend()
    pl.savefig(nom_de_fichier)
    pl.clf()
    return None

trace_fonction(xmin,xmax,f,'fig_ex_fonction.png')

## Question 2

T = [0, 7, 18, 27, 37, 56, 102]
C = [34.83, 32.14, 28.47, 25.74, 23.14, 18.54, 11.04]
g = lambda x : 34 - 0.2*x

def trace_ajustement(X,Y,f,nom_de_fichier,lab="Courbe d'ajustement"):
    """Trace la courbe de f et les points (X,Y)
    Enregistre dans nom_de_fichier"""
    pl.clf()
    pl.plot(X,Y, 'rx',label='Mesures expérimentales')
    les_x = np.linspace(min(X),max(X),1000)
    les_y = [f(t) for t in les_x]
    pl.plot(les_x,les_y,label=lab)
    pl.xlabel('Temps (s)')
    pl.ylabel('Concentration (mol / L)')
    pl.title('Évolution de la concentration en fonction du temps')
    pl.legend()
    pl.savefig(nom_de_fichier)
    pl.clf()
    return None

trace_ajustement(T,C,g,'fig_ex_ajustement.png')

## Question 3

# L1 = lambda k : sum((C-C[0]*np.exp(-k*t))**2)/7
def L1(k):
    """L1(k)"""
    S = 0
    for i in range(len(T)) :
        S = S + (C[i]-C[0]*exp(-k*T[i]))**2
    return S / 7

## Question 4

trace_fonction(0,0.12,L1,'fig_L1.png','$L_1$')

## Question 5

# dL1 = lambda k : 2 * C[0] * sum(t * (C-C[0]*np.exp(-k*t)) * np.exp(-k*t))/7
def dL1(k):
    """L1'(k)"""
    S = 0
    for i in range(len(T)) :
        S = S + T[i] * (C[i]-C[0]*exp(-k*T[i])) * exp(-k*T[i])
    return 2*C[0]*S / 7
trace_fonction(0,0.12,dL1,'fig_dL1.png',"$L_1'$")


## Question 6

# ddL1 = lambda k : 2*C[0] * sum(t**2 * (2*C[0]*np.exp(-k*t) - C) * np.exp(-k*t))/7
def ddL1(k):
    """L1''(k)"""
    S = 0
    for i in range(len(T)) :
        S = S + T[i]**2 * (2*C[0]*exp(-k*T[i]) - C[i]) * exp(-k*T[i])
    return 2*C[0]*S / 7
trace_fonction(0,0.12,ddL1,'fig_ddL1.png',"$L_1''$")

## Question 7

def newton(f,fp,x0,eps):
    """Zéro de f par la méthode de Newton, critère d'arret eps
    fp : dérivée de f
    x0 : point initial"""
    u = x0
    v = u - f(u)/fp(u)
    while abs(v-u) > eps:
        u, v = v, v - f(v)/fp(v)
    return u

## Question 8

def val_k1() :
    """Valeur de k1"""
    return newton(dL1, ddL1, 0.01, 10**-10)

k1 = val_k1()

## Question 9

def f1(x) :
    """Fonction d'ajustement pour le modèle d'ordre 1"""
    return  C[0]*exp(-k1*x)

trace_ajustement(T,C,f1,'regression_ordre_1.png',"Modèle d'ordre 1, méthode de Newton")

## Question 10

# L2 = lambda k : sum((C-C[0]/(C[0]*k*t+1))**2)/7

def L2(k):
    """L2(k)"""
    S = 0
    for i in range(len(T)) :
        S = S + (C[i]-C[0]/(C[0]*k*T[i]+1))**2
    return S / 7


## Question 11

trace_fonction(0,0.05,L2,'fig_L2.png',"$L_2$")

## Question 12

# dL2 = lambda k : 2 * C[0]**2 * sum(T[i] * (C[i]*C[0]*T[i]*k+C[i]-C[0]) / (C[0]*T[i]*k+1)**3)/7
def dL2(k):
    """L2'(k)"""
    S = 0
    for i in range(len(T)) :
        S = S + T[i] * (C[i]*C[0]*T[i]*k+C[i]-C[0]) / (C[0]*T[i]*k+1)**3
    return  2*S*C[0]**2 / 7



trace_fonction(0,0.01,dL2,'fig_dL2.png',"$L_2'$")

## Question 13

def secante(f,x0,x1,eps):
    """Zéro de f par la méthode de la sécante"""
    u,v = x0,x1
    while abs(u-v) > eps :
        p = (f(u)-f(v)) / (u-v)
        u,v = v,u - f(u)/p
    return u

## Question 14

def val_k2() :
    """Valeur de k2"""
    return secante(dL2,0.0005,0.0001,10**-10)
k2 = val_k2()

## Question 15

def f2(x) :
    """Fonction d'ajustement pour le modèle d'ordre 2"""
    return  C[0]/(C[0]*k2*x+1)

trace_ajustement(T,C,f2,'regression_ordre_2.png',"Modèle d'ordre 2, méthode de la sécante")

## Question 16

# ddL2 = lambda k : 2*C[0]**3 * sum(T[i]**2 * (3*C[0]-2*C[i]-2*C[i]*C[0]*T[i]*k) / (C[0]*T[i]*k+1)**4)/7
def ddL2(k):
    """L2''(k)"""
    S = 0
    for i in range(len(T)) :
        S = S + T[i]**2 * (3*C[0]-2*C[i]-2*C[i]*C[0]*T[i]*k) / (C[0]*T[i]*k+1)**4
    return  2*C[0]**3 *S / 7

trace_fonction(0,0.12,ddL2,'fig_ddL2.png',"$L_2''$")

def val_k2_bis() :
    return newton(dL2, ddL2, 0.0001, 10**-10)


k2_bis = val_k2_bis()

def f2_bis(x) :
    """Fonction d'ajustement pour le modèle d'ordre 2"""
    return  C[0]/(C[0]*k2_bis*x+1)

trace_ajustement(T,C,f2_bis,'regression_ordre_2_bis.png',"Modèle d'ordre 2, méthode de Newton")

## Question 19
def val_kp1():
    """Valeur de k1'"""
    S1,S2 = 0,0
    for i in range(len(T)):
        S1 = S1 + T[i]*log(C[i]/C[0])
        S2 = S2 + T[i]**2
    return -S1/S2

kp1 = val_kp1()

def fp1(x) :
    """Fonction d'ajustement pour le modèle d'ordre 1
    Régression linéaire sur les logarithmes de C"""
    return  C[0]*exp(-kp1*x)


trace_ajustement(T,C,fp1,'regression_ordre_1_lin.png',"Modèle d'ordre 1, régression linéaire")

## Question 20

## Newton : on optimise directement le critère pertinent. Linéaire : forme close pour la solution mais on n'optimise pas directement le critère pertinent.


