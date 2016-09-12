import numpy as np
from math import pi,floor,cos,sin
import matplotlib.pyplot as plt
from random import randint

e = 0.40                # cm
Tint = 20 + 273.15      # 
Text1 = 10 + 273.15     # 
Text2 = -10 + 273.15    # 
cp = 1000               # J kg-1 K-1
lambd = 1.65            # W m-1 K-1
rho = 2150              # kg m-3

ItMax_k = 4000


Tps_simu = 30000
Nech_tps = 10000
Nech_e = 5

dx = e/(Nech_e-1)
dt = Tps_simu/(Nech_tps)
dt = 10

def T1(x):
    k1 = (Text1-Tint)/e
    k2 = Tint
    T = k1*x + k2
    return T
    
def T2(x):
    k1 = (Text2-Tint)/e
    k2 = Tint
    T = k1*x + k2
    return T

x = np.linspace(0,e,Nech_e)
t1 = T1(x)
t2 = T2(x)

alpha = rho*cp/lambd

## Front de température à t<<0 et à t>>0
"""
plt.plot(x,t1)
plt.plot(x,t2)
plt.show()
"""

r = dt/(alpha *dx**2)

# Création de la matrice M_expl : 
Mexpl = np.zeros((Nech_e,Nech_e))
Mexpl[0][0] = 1-2*r
Mexpl[0][1] = r
Mexpl[Nech_e-1][Nech_e-1] = 1-2*r
Mexpl[Nech_e-1][Nech_e-2] = r


for i in range(1,Nech_e-1):
    Mexpl[i][i]=1-2*r
    Mexpl[i][i+1]=r
    Mexpl[i][i-1]=r

T_k=np.zeros((Nech_e,1))

#Création de la matrice des température initiales : 
for i in range(Nech_e):
    #T_k[i]=((i)*dx*(Text1-Tint)/(e)+Tint)
    x = i*dx
    T_k[i]=x*(Text1-Tint)/(e)+Tint
    
#Création de la matrice v
v = np.zeros((Nech_e,1)) 
v[0]=Tint
v[-1]=Text2

    
res=[]
res.append(np.array(T_k))
t=0

print(Mexpl,res[-1],r,v)
while len(res)<ItMax_k:
#    t=t+dt
    #res.append(somme(prod(M_expl,res[-1]),prodv(r,v)))
    res.append(np.dot(Mexpl,np.array(res[-1]))+r*v)
#print(Mexpl,res[0],r,v)


"""
# Affichage des résultats EXPLICITES
#définition des abscisses:
x = [i*(e/(Nech_e-1)) for i in range(Nech_e)]
#print(t)

for i in range(len(res)):
    if i%200 == 0:
        plt.plot(x,res[i],label=i)
        
        
plt.plot(x,res[0],linewidth=2.0)
plt.plot(x,res[-1],linewidth=2.0)
plt.legend()
plt.show()
"""

"""
# Création de la matrice Mimpl : 
Mimpl = np.zeros((Nech_e,Nech_e))
Mimpl[0][0] = 1+2*r
Mimpl[0][1] = -r
Mimpl[Nech_e-1][Nech_e-1] = 1+2*r
Mimpl[Nech_e-1][Nech_e-2] = -r


for i in range(1,Nech_e-1):
    Mimpl[i][i]=1+2*r
    Mimpl[i][i+1]=-r
    Mimpl[i][i-1]=-r

Vimpl = np.zeros((Nech_e,1)) 
Vimpl[0] = Tint
Vimpl[-1] = Text2

Timpl=np.zeros((Nech_e,1))
#Création de la matrice des température initiales : 
for i in range(Nech_e):
    #T_k[i]=((i)*dx*(Text1-Tint)/(e)+Tint)
    x = i*dx
    Timpl[i]=x*(Text1-Tint)/(e)+Tint



def CalcTkp1(M,d):
    N=len(d)
    L = np.copy(M)
    L[0,1] = L[0,1]/L[0,0]
    d[0] = d[0]/L[0,0]
    for i in range(1,N-1):
        temp = L[i,i]-L[i,i-1]*L[i-1,i]
        L[i,i+1] = L[i,i+1]/temp
        d[i] = (d[i]-L[i,i-1]*d[i-1])/temp
    d[-1] = (d[-1]-L[-1,-2]*d[-2])/(L[-1,-1]-L[-1,-2]*L[-2,-1])
    u = np. zeros(N)
    u[-1] = d[-1]
    for i in range(N-2,-1,-1):
        u[i] = d[i]-L[i,i+1]*u[i+1]
    return(u)
    

UU = CalcTkp1(Mimpl,Timpl)
VV = CalcTkp1(Mimpl,r*Vimpl)

resimpl = []
resimpl.append(UU+VV)

      
t=0        
while t<Tps_simu:
    t=t+dt
    print(t)
    #res.append(somme(prod(M_expl,res[-1]),prodv(r,v)))
    UU = CalcTkp1(Mimpl,resimpl[-1])
    VV = CalcTkp1(Mimpl,r*Vimpl)
    resimpl.append(UU+VV)

x = [i*(e/(Nech_e-1)) for i in range(Nech_e)]
print(t)

for i in range(len(res)):
    if i%500 == 0:
        plt.plot(x,resimpl[i],label=i)
        
        
plt.plot(x,resimpl[0],linewidth=2.0)
plt.plot(x,resimpl[-1],linewidth=2.0)
plt.legend()
plt.show()


"""