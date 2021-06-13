import matplotlib.pyplot as plt
import numpy as np

T = [0, 7, 18, 27, 37, 56, 102]
C = [34.83, 32.14, 28.47, 25.74, 23.14, 18.54, 11.04]

#Q1
xmin = 0
xmax = 20
def f(x) :
    return 0.02* x*(x-5)

def trace_fonction(xmin,xmax,f,nom_de_fichier):
    plt.clf()
    lx=np.linspace(xmin,xmax,1000)
    y=[f(x) for x in lx]
    plt.plot(lx,y)
    plt.savefig(nom_de_fichier)

trace_fonction(xmin,xmax,f,'fig_ex_fonction.png')

#Q2
def trace_ajustement(X,Y,f,nom_de_fichier):
    plt.clf()
    plt.plot(X,Y,'b*',label='Mesures expérimentales')
    les_x = np.linspace(min(X),max(X),1000)
    les_y = [f(t) for t in les_x]
    plt.plot(les_x,les_y)
    plt.xlabel('Temps (s)')
    plt.ylabel('Concentration (mol / L)')
    plt.title('Évolution de la concentration en fonction du temps')
    plt.legend()
    plt.savefig(nom_de_fichier)
    plt.clf()

def g(x) :
    return 34 - 0.2*x
trace_ajustement(T,C,g,'fig_ex_ajustement.png')

#Q3
def L1(k):
    S=0
    for i in range(len(T)):
        S+=(C[i]-C[0]*np.exp(-k*T[i]))**2
    return S/7

#Q4
trace_fonction(0,0.12,L1,'tp12_durif_q4.png')

#Q5
# dL1 = lambda k : 2 * C[0] * sum(t * (C-C[0]*np.exp(-k*t)) * np.exp(-k*t))/7
def dL1(k):
    """L1'(k)"""
    S = 0
    for i in range(len(T)) :
        S = S + T[i] * (C[i]-C[0]*np.exp(-k*T[i])) * np.exp(-k*T[i])
    return 2*C[0]*S / 7
trace_fonction(0,0.12,dL1,'fig_dL1.png')


## Question 6
def ddL1(k):
    """L1''(k)"""
    S = 0
    for i in range(len(T)) :
        S = S + T[i]**2 * (2*C[0]*np.exp(-k*T[i]) - C[i]) * np.exp(-k*T[i])
    return 2*C[0]*S / 7
trace_fonction(0,0.12,ddL1,'fig_ddL1.png')

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
    return  C[0]*np.exp(-k1*x)

trace_ajustement(T,C,f1,'tp12_durif_q9.png')

## Question 10
# L2 = lambda k : sum((C-C[0]/(C[0]*k*t+1))**2)/7

def L2(k):
    """L2(k)"""
    S = 0
    for i in range(len(T)) :
        S = S + (C[i]-C[0]/(C[0]*k*T[i]+1))**2
    return S / 7

## Question 11

trace_fonction(0,0.05,L2,'tp12_durif_q11.png')

## Question 12

# dL2 = lambda k : 2 * C[0] * sum(t * ( C/(C[0]*k*t+1)**2 - C[0]/(C[0]*k*t+1)**3) )/7
def dL2(k):
    """L2'(k)"""
    S = 0
    for i in range(len(T)) :
        S = S + T[i] * ( C[i]/(C[0]*k*T[i]+1)**2 - C[0]/(C[0]*k*T[i]+1)**3)
    return  2*C[0]**2*S / 7


def dL2_bis(k):
    """L2'(k)"""
    S = 0
    for i in range(len(T)) :
        #print(S)
        S = S + C[0]**2*T[i]*(C[i]+C[0]/(C[0]*k*T[i]+1))/(1+C[0]*k*T[i])**2
    return  2*S / 7

def dL2_ms(k):
    """L2'(k)"""
    S = 0
    for i in range(len(T)) :
        S = S + T[i] * (C[i]*C[0]*T[i]*k+C[i]-C[0]) / (C[0]*T[i]*k+1)**3
    return  2*S*C[0]**2 / 7


trace_fonction(0,0.01,dL2,'tp12_durif_q12.png')


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
    return secante(dL2,0.00005,0.0001,10**-10)
k2 = val_k2()


## Question 15

def f2(x) :
    """Fonction d'ajustement pour le modèle d'ordre 2"""
    return  C[0]/(C[0]*k2*x+1)

trace_ajustement(T,C,f2,'tp12_durif_q15.png')


## Question 16

# ddL2 = lambda k : 2*C[0]**2 * sum(t**2 * (3*C[0]/(C[0]*k*t+1)**4 -  2*C/(C[0]*k*t+1)**3) )/7
def ddL2(k):
    """L2''(k)"""
    S = 0
    for i in range(len(T)) :
        S = S + T[i]**2 * (3*C[0]/(C[0]*k*T[i]+1)**4 -  2*C[i]/(C[0]*k*T[i]+1)**3)
    return  2*C[0]**2 *S / 7

trace_fonction(0,0.12,np.vectorize(ddL2),'tp12_durif_q16.png')

def val_k2_bis() :
    return newton(dL2, ddL2, 0.0001, 10)


## Question 17
def val_kp1():
    """Valeur de k1'"""
    S1,S2 = 0,0
    for i in range(len(T)):
        S1 = S1 + T[i]*np.log(C[i]/C[0])
        S2 = S2 + T[i]**2
    return -S1/S2

kp1 = val_kp1()

def fp1(x) :
    """Fonction d'ajustement pour le modèle d'ordre 1
    Régression linéaire sur les logarithmes de C"""
    return  C[0]*np.exp(-kp1*x)


trace_ajustement(T,C,fp1,'tp12_durif_q17.png')
