import sujet

import scipy.optimize as so
import scipy.integrate as si
from math import sqrt, sin, cos, atan
from numpy import array

def F (x,t) :
        return 3*cos(x) + t

def G (X,t) :
    a,b = X[0],X[1]
    return array([b,1+sin(t+a)])

def H (X,t) :
    a,b = X[0],X[1]
    return array([b,1+atan(t+a)])

def reponses(alpha) :
    t = sujet.cree_tableau(alpha)
    # Qu. 1 :
    N = len(t)
    # Qu. 2 :
    c1 = 0
    for x in t :
        if x >= 3000 : c1 += 1
    # Qu. 3 :
    c2 = 0
    for x in t :
        if x % 3 == 0 : c2 += 1
    # Qu. 4 :
    c3 = 0
    for i in range(N-1) :
        for j in range(i+1,N) :
            if t[i] < t[j] : c3 += 1
    u = 10 + alpha
    U = [u]
    for i in range(9999) :# invariant entrée : u = u_i
        u = (15091*u) % 64007
        U.append(u) # invariant sortie : u = u_{i+1}, U=[u_0,...,u_{i+1}]
    c4 = 0
    for x in U :
        if x % 17 == 0 : c4 += 1
    c5 = 0
    for i in range(9999) :
        if abs(U[i]-U[i+1]) <= 1000 : c5 += 1
    toto = open('zeta5.txt','r')
    toto.readline()
    toto.readline() # on élimine les deux premières lignes
    lignes = toto.readlines()
    toto.close()
    c6 = 0
    L50 = [] # en préparation de la question 11
    gen = (l for l in lignes if l != '\n')
    for  l in gen :
        L = l.split()
        B = ""  # en préparation de la question 11
        for b in L :
            if len(b) == 10 :
                B += b  # en préparation de la question 11
                for i in range(7) :
                    if b[i:i+4] == str(2000+alpha) : c6 += 1
        L50.append(B)  # en préparation de la question 11
    c7 = 0
    for b in L50:
        for i in range(47) :
            if b[i:i+4] == str(2000+alpha) : c7 += 1
    L500 = ["".join(L50[10*i:10*(i+1)]) for i in range(2000)]
    c8 = 0
    for b in L500 :
        for i in range(497) :
            if b[i:i+4] == str(2000+alpha) : c8 += 1
    Ltotale = "".join(L500)
    n = len(Ltotale)
    c9 = 0
    for i in range(n-3) :
        if Ltotale[i:i+4] == str(2000+alpha) : c9 += 1
    les_t = [i/10000 for i in range(10001)]
    les_t2 = [i*(1+alpha/10)/10000 for i in range(10001)]
    f = lambda beta : si.odeint(H,array([0,beta]),les_t2)[-1,0]-1-(2/3)*alpha
    titi = open('reponses.csv','a')
    titi.write(str(alpha)+',')
    titi.write(str(N)+',')
    titi.write(str(c1)+',')
    titi.write(str(c2)+',')
    titi.write(str(c3)+',')
    titi.write(str(U[42])+',')
    titi.write(str(U[-1])+',')
    titi.write(str(c4)+',')
    titi.write(str(c5)+',')
    titi.write(str(sum(x for x in U))+',')
    titi.write(str(c6)+',')
    titi.write(str(c7)+',')
    titi.write(str(c8)+',')
    titi.write(str(c9)+',')
    titi.write(str(so.brentq(lambda x : x**2 + sqrt(x) -10 -alpha,3,11))+',')
    titi.write(str(si.odeint(F,alpha,les_t)[-1,0])+',')
    titi.write(str(si.odeint(G,array([0,0]),les_t2)[-1,0])+',')
    titi.write(str(si.odeint(G,array([0,1]),les_t2)[-1,0])+',')
    titi.write(str(so.brentq(f,-2,2))+'\n')
    titi.close()


for alpha in range(44,100) :
    reponses(alpha)
