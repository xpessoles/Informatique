#! /usr/bin/env python3

from math import sqrt, floor, ceil, log

def u(alpha,n):
    """u_n, u_0 = alpha"""
    x = alpha
    for i in range(n):
        x = (15091 * x) % 64007
    return x

def liste_u(alpha,n):
    """Donne la liste des u_k pour 0 <= k < n"""
    L = [0]*n
    L[0] = u(alpha,0)
    for i in range(1,n):
        L[i] = (15091 * L[i-1]) % 64007
    return L

def imax(T):
    im = 0
    for j in range(1,len(T)):
        if T[j] > T[im]:
            im = j
    return im

def u_atteint(alpha,k):
    x = alpha
    i = 0
    while x != k:
        x = (15091 * x) % 64007
        i = i+1
    return i


def compte(alpha,n):
    """Compte le nombre de u(k) <= 10000 pour 0<= k < n"""
    x = alpha
    c = 0
    for k in range(n):
        # Invariant : x = u(k)
        if x <= 10000:
            c = c+1
        x = (15091 * x) % 64007
    return c

def pgcd(a,b):
    r0 = a
    r1 = b
    while r1 != 0:
        r0, r1 = r1, (r0 % r1)
    return r0

def moy_elaguee(T):
    M = max(T)
    m = min(T)
    t = []
    for x in T:
        if (x != M) and (x != m):
            t.append(x)
    return sum(t) / len(t)

def S(alpha,n):
    x = alpha
    somme  = 1/(x**2)
    for i in range(n):
        x  = (15091 * x) % 64007
        somme  = somme + 1/(x**2)
    return somme


def Snaif(alpha,n):
    return sum([1/(u(alpha,k)**2) for k in range(n+1)])


a = 1

def v(alpha,n):
    """Calcule v_n"""
    L = [0]*(n+1)
    L[0] = u(alpha,0)
    for i in range(n):
        L[i+1] = sum([(i+1-k)*L[k] for k in range(i+1)])
    return L[-1]

def nbmax_val(L,x):
    """Nombre max de x consécutifs de L"""
    i = 0
    nx = 0
    m = 0
    # Idée : on parcourt L
    # Tant que l'on rencontre un zéro, on augmente le compteur.
    # Si l'on rencontre autre chose que 0, on le met à 0.
    for i in range(len(L)):
        if L[i] == x:
            nx = nx + 1
            if nx > m:
                m = nx
        else :
            nx = 0
    return m

def est_premier(n):
    """Booléen indiquant si n est premier"""
    if n < 2:
        return False
    for i in range(2,ceil(sqrt(n))+1):
        if n % i == 0:
            return False
    return True

def compte_premier(L):
    """Compte le nombre de nombres premiers dans L"""
    c = 0
    for n in L:
        if est_premier(n):
            c = c+1
    return c

def u_atteint_liste(les_u,k):
    i = 0
    while les_u[i] != k:
        i = i+1
    return i

def compte_liste(les_u,n):
    """Compte le nombre de u(k) <= 10000 pour 0<= k < n"""
    c = 0
    for i in range(n):
        if les_u[i] <= 10000:
            c = c+1
    return c

def pyramide(alpha,n):
    """Construit la pyramide a n ligne"""
    p = []
    x = alpha
    for i in range(n):
        l = []
        for j in range(i+1) :
            y = x % 10
            l.append(y)
            x = (15091 * x) % 64007
        p.append(l)
    return p


def total_pyramide(p) :
    """Calcule la somme maximale dans la pyramide p"""
    n = len(p)
    m = 0
    for ligne in range(n) :
        for j in range(n-ligne-1) :
            p[n-ligne-2][j] += max(p[n-ligne-1][j],p[n-ligne-1][j+1])
    return p[0][0]

def reponses():
    "Génère le csv des réponses"""
    header = ('alpha,R1 (reste), R1 (quotient),R2,R3,R4,R5,R6,R7,R8,R9,R10,R11,R12,R13,R14\n')
    with open('d01s_reponses.csv','w') as f:
        f.write(header)
        for a in range(1,100):
            les_u = liste_u(a,4000)
            r1r = les_u[2]*les_u[3] % les_u[4]
            r1q = les_u[2]*les_u[3] // les_u[4]
            r2 = imax([les_u[k] for k in range(1000)])
            r3 = log(les_u[2],10)
            r4 = u_atteint(a,100)
            r5 = compte_liste(les_u,1000)
            r6 = pgcd(les_u[6],les_u[7])
            r7 = moy_elaguee([ les_u[k] % 100 for k in range(1000,2000)])
            r8 = S(a,987)
            x = S(a,10**6)
            r9 = x - floor(x)
            r10 = v(a,15)
            r11 = nbmax_val([les_u[k] % 5 for k in range(2000,3000)],0)
            r12 = compte_premier([les_u[k] for k in range(3000,4000)])
            p20 = pyramide(a,20)
            p100 = pyramide(a,100)
            r13 = total_pyramide(p20)
            r14 = total_pyramide(p100)
            L = [a,r1r,r1q,r2,r3,r4,r5,r6,r7,r8,r9,r10,r11,r12,r13,r14]
            ligne = ','.join([str(t) for t in L])+'\n'
            f.write(ligne)
    return None

if __name__ == '__main__':
    reponses()
