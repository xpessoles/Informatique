from numpy import *
import numpy.linalg as np
import matplotlib.pyplot as plt
from time import *

L=0.3
n=3
m=[0.1,0.2,0.1]
k=[20000,20000,1000]
c=[1000,10,10]

def creation_operateur(n,m,k,c):
    M=zeros((n,n),float)
    for i in range(n):
        M[i,i]=m[i]
    K=zeros((n,n),float)
    C=zeros((n,n),float)
    for i in range(1,n-1):
        K[i,i]=k[i]+k[i+1]
        C[i,i]=c[i]+c[i+1]
        K[i,i-1]=-k[i]
        C[i,i-1]=-c[i]
        K[i,i+1]=-k[i+1]
        C[i,i+1]=-c[i+1]
    K[0,0]=k[0]+k[1]
    K[0,1]=-k[1]
    C[0,0]=c[0]+c[1]
    C[0,1]=-c[1]
    K[n-1,n-1]=k[n-1]
    K[n-1,n-2]=-k[n-1]
    C[n-1,n-1]=c[n-1]
    C[n-1,n-2]=-c[n-1]
    return [M,K,C]

def calcul(n,M,K,C,npts,dt,fmax,omega):
    H=M/dt**2+C/dt+K
    F=zeros((n,1),float)
    X=[zeros((n,1),float),zeros((n,1),float)]
    for i in range(2,npts+2):
        F[n-1]=fmax*sin(omega*(i-1)*dt)
        G=dot((2*M/dt**2+C/dt),X[i-1])-dot(M/dt**2,X[i-2])+F
        #A=np.solve(H,G)
        A=resoud(H,G)
        X.append(A)
    return X[1:]

def resoud(H,G):
    G2=copy(G)
    H2=copy(H)
    n=len(G2)
    X=zeros((n,1),float)
    for i in range(1,n):
        a=H2[i-1,i-1]
        b=H2[i,i-1]
        H2[i]=H2[i]*a-H2[i-1]*b
        G2[i]=G2[i]*a-G2[i-1]*b
    X[n-1]=G2[n-1]/H2[n-1,n-1]
    for i in range(n-2,-1,-1):
        X[i]=(G2[i]-H2[i,i+1]*X[i+1])/H2[i,i]
    return X

npts=40
fmax=100
omega=1
dt=2*2*pi/omega/npts

[M,K,C]=creation_operateur(n,m,k,c)
X=calcul(n,M,K,C,npts,dt,fmax,omega)

def affiche_deplacement_pdt(q,X,L,n,ampl):
    T=[]
    for i in range(n):
        T.append((X[q][i]+(i+1)*L/n)*ampl)
    plt.plot(T,n*[0.5*q],'D')

ampl=1
for i in range(npts+1):
    affiche_deplacement_pdt(i,X,L,n,ampl)
    sleep(1)
plt.axis([0,0.5,-0.5,0.5*(npts+1)])
plt.ylabel(u'la poutre à chaque pas de temps')
plt.xlabel(u'les noeuds')
plt.grid()
plt.show()

"""
def lieu_temps_depl_max(X):
    k=0
    t=0
    for i in range(npts+1):
        for j in range(1,n):
            if abs(X[i][j])>abs(X[t][k]):
                t=i
                k=j
    return k+1,t,abs(X[t][k][0])

print (u"MAX : noeud, pas de temps, déplacement  ",lieu_temps_depl_max(X))

def calcul_energie(X,c,dt):
    m=len(X)
    n=len(X[0])
    E=0
    TE=[]
    TP=[]
    Tt=[]
    #calcul des vitesses
    V=[n*[0]]
    for i in range(1,m):
        T=[]
        for j in range(0,n):
            T.append((X[i][j][0]-X[i-1][j][0])/dt)
        V.append(T)
    for i in range(0,m):
        Ps=0
        for j in range(0,n):
            if j==0:
                Ps+=c[j]*(V[i][j])**2
            else:
                Ps+=c[j]*(V[i][j]-V[i][j-1])**2
        TP.append(Ps)
        E+=Ps*dt
        TE.append(E)
        Tt.append(i*dt)
    plt.grid()
    plt.ylabel(u"Energie dissipée")
    plt.xlabel("temps")
    plt.plot(Tt,TE)
    plt.figure(2)
    plt.plot(Tt,TP)
    plt.grid()
    plt.ylabel(u"Puissance dissipée")
    plt.xlabel("temps")
    plt.show()

calcul_energie(X,c,dt)

         


"""