import numpy as np
import matplotlib.pyplot as plt
from math import sqrt

e = 0.40                # cm
Tint = 20 + 273.15      # 
Text1 = 10 + 273.15     # 
Text2 = -10 + 273.15    # 
cp = 1000               # J kg-1 K-1
lambd = 1.65            # W m-1 K-1
rho = 2150              # kg m-3

Tps_simu = 30000        # s
Nech_tps = 10000
Nech_e = 60
ItMax_k = 4000 
dt = 25 # pas de temps de 10 secondes
dx = e / (Nech_e +1)

N=Nech_e
alpha = rho*cp/lambd
r = dt/(alpha *dx**2)


def calc_norme(v):
    res = 0
    for i in range(len(v)):
        res = res+v[i]**2
    return sqrt(res)        


def T0(Ti,Tf,N):
    tt =  np.zeros((N,1))
    for i in range(N):
        tt[i] = ((Tf-Ti)/(N))*i+Ti
    return tt


def calcTkp1(M,d):
    L=np.copy(M) # copie pour ne pas affecter M
    L[0,1] = L[0,1]/L[0,0]
    d[0] = d[0]/L[0,0]

    for i in range(1,N-1):
        temp = L[i,i] - L[i,i-1] * L[i-1,i]
        L[i,i+1] = L[i,i+1]/temp
        d[i] = (d[i] - L[i,i-1] * d[i-1])/temp

    d[-1] = (d[-1] - L[-1,-2] * d[-2])/(L[-1,-1] - L[-1,-2] * L[-2,-1])

    u = np.zeros(N)
    u[-1] = d[-1]
    for i in range(N-2, -1, -1):
        u[i] = d[i] - L[i,i+1] * u[i+1]
    return(u)
    
    
t0 = T0(Tint,Text1,N)    


M = np.zeros((N,N))
M[0][0]=1+2*r
M[0][1]=-r

M[N-1][N-1]=1+2*r
M[N-1][N-2]=-r
for i in range(1,N-1):
    M[i][i]=1+2*r
    M[i][i+1]=-r
    M[i][i-1]=-r

V = np.zeros((N,1))
V[0][0]=Tint
V[N-1][0]=Text2

NN = np.linalg.inv(M)
T_tous_k = []
T_tous_k.append(t0)
Tk =  np.dot(NN,t0)+r*np.dot(NN,V)
T_tous_k.append(Tk)

while calc_norme(T_tous_k[-1]-T_tous_k[-2])>0.01 and len(T_tous_k)<ItMax_k:
    T_tous_k.append(np.dot(NN,T_tous_k[-1])+r*np.dot(NN,V))

x = [i*(e/(Nech_e-1)) for i in range(Nech_e)]
    
plt.plot(x,t0,label="Temp. ini.")


for i in range(1,len(T_tous_k)):
    if i%int(7200/dt) == 0:
        plt.plot(x,T_tous_k[i],label=str(int(i*dt/3600))+" heures")
    
print(len(T_tous_k)*dt/3600)

t0 = T0(Tint,Text1,N)    
tf = T0(Tint,Text2,N)    
#plt.plot(x,T_tous_k[int(3600*12/25)],label="12 heures")

#plt.plot(x,tf,label="Temp. fin.")
plt.grid()
plt.xlabel("Température (K)")
plt.xlabel("Abscissse mur (m)")

plt.legend()
plt.show()
