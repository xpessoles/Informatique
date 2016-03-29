#Définition des constantes
ep = 0.40                # m
Tint = 20 + 273.15      # 
Text1 = 10 + 273.15     # 
Text2 = -10 + 273.15    # 
cp = 1000               # J kg-1 K-1
lambd = 1.65            # W m-1 K-1
rho = 2150              # kg m-3

N= 60
ItMax = 2000 
dt = 20 # pas de temps de 20 secondes
dx = ep / (N +1)


alpha = rho*cp/lambd
r = dt/(alpha *dx**2)





# Q1)
# T ne dépend que de x donc ∆(T)=∂^2T/∂x^2 
# on a donc pCp ∂T/∂t =(lambda) ∂^2T/∂x^2  

#Q2) cas 1 les limites (bords) sont 
# pour x=0 : T(0,t)=Tint
# et pour x=E : T(e,t):Text

#Cas 2 : conductivité faible = lambda très faible=  ∂T/∂t petit en x=e.
# on a toujours T(0,t)=Tint et en plus ∂T/∂t (e,t)=0

#Q3)En régime permanent on a ∂T/∂t=0 l'équation devient :
#∂^2T/∂x^2 =0 soit T(t,x)=a(t)x+b(t) 
# si t1<0, on a T(t1,0)=Tint et T(t1,e)=Text1
# On remplace et on trouve a(t_1)=(Text1-Tint)/e et b(t1)=Tint

#si t2<0 même calcul a(t_2)=(Text2-Tint)/e et b(t1)=Tint

#Q4) Numériquement on a T(t1,x)=-25x+20 (en deg)
# et T(t2,x)=-75x+20 (en deg)

#Q5)alpha= pCp/lambda

#Q6) On considère la situation t=0 comme la limite quand t->O^- 
# Ainsi avec Q3 : a=a(0)=(Text1-Tint)/e  et b=b(0)=Tint

#Q7) Il y a N+1 intervalles donc ∆x=e/(N+1)

#Q8) x(i+1)-x(i)=∆x (suite arithmétique) de raison ∆x
# donc x(i)=i∆x  (car x(0)=0), on vérifie que x(N+1)=e

#Q9)On somme les deux relations :
#T(x+∆x,t)+T(x-∆x,t)=2T(x,t)+(∆x)^2 ∂^2T/∂x^2 +o((∆x)^3)
#D'où ∂^2T/∂x^2(x,t)=(T(x+∆x,t)+T(x-∆x,t)-2T(x,t))/(∆x)^2  + o(∆x)
# Une valeur approchée à l'odre 1 en ∆x est donc :
# ∂^2T/∂x^2(x,t)=(T(x+∆x,t)+T(x-∆x,t)-2T(x,t))/(∆x)^2

#Q10) D'après 9, en remplaçant x=xi et t=tk (1<=i<=N) on a :
# ∂^2T/∂x^2(xi,tk)=(T(xi+∆x,tk)+T(xi-∆x,tk)-2T(xi,tk))/(∆x)^2
#soit ∂^2T/∂x^2(xi,tk)=(Ti+1,k + Ti-1,k - 2 Ti,k ) / (∆x)^2

#Q11) On utilise l'équation et Q10 :
#(Ti+1,k + Ti-1,k - 2 Ti,k ) / (∆x)^2= alpha (Ti,k+1-Ti,k)/(∆t)
# On isole Ti,k+1 :
# ∆t/(alpha (∆x)^2) (Ti+1,k + Ti-1,k - 2 Ti,k )=Ti,k+1-Ti,k
# et Ti,k+1=Ti,k + r(Ti+1,k + Ti-1,k - 2 Ti,k ) 
# avec r=∆t/(alpha (∆x)^2)
# puis Ti,k+1 = r Ti-1,k +  (1-2r) Ti,k + r Ti+1,k
# formule valable pour 1<=i<=N et k>=0

#Q12)On a deja répondu au début de la question 11 !
#Les conditionbs initiales donnent  (voir avant Q5)
# T0,k=T(0,tk)=Tint et TN+1,k=T(e,tk)=Text2 si k>0 
# et TN+1,0=T(e,0)=Text1.

#Q13)On constate que si l'on pose 
#M matrice N+1xN+1 avec 1-2r sur la diagonale 
#et des r sur la surdiagonale et sousdiagonale alors on a 
#grace à la formule de Q11) ,
# MTk est un vecteur de coordonnées :

# (1-2r) T1,k + r T2,k              = T1,k+1   -  r T0,k
#r T1,k +  (1-2r) T2,k + r T3,k     = T2,k+1
#  .....                            =....
#r TN-2,k +  (1-2r) TN-1,k + r TN,k = TN-1,k+1
#r TN-1,k +  (1-2r) TN,k            =TN,k+1    -  r TN+1,k
# On pose V=(T0,k , 0,..,0, TN+1,k)=
#V=(Tint,0,...,0,Text2) 
# on a bien Tk+1=MTk+rV

#Q14)
#On dispose de condition initiale :
#T0=(T0,0 , T1,0 ,....,  TN,0, TN+1,0)
# avec la formule T(x,0)=ax+b (Q6)
# et on dispose d'une formule de récurrence :
# Tk+1=MTk+rV  (M et V sont des constantes)
# On peut calculer de proche en proche les vecteurs Tk


#Q15) 
def euler_explicite(M,T_0,V,k):
    N=len(T_0)
    if k==0:
        return T_0
    return dot(M,euler_explicite(M,T_0,r,V,k-1))+r*V
            
#Q16) Changer cette question
#On dispose de condition initiale :
#T0=(T0,0 , T1,0 ,....,  TN,0, TN+1,0)
# avec la formule T(x,0)=ax+b (Q6)
# et on dispose d'une formule de récurrence :
# MTk+1=Tk+rV  (M et V sont des constantes)
# On peut calculer de proche en proche les vecteurs Tk en 
#inversant la matrice avec le pivot de Gauss C(n)=O(n^3)

#Q17
# Mu=d devient alors 
# u1+c1'u2=d1'
# u2+c2'u3=d3'
#...
# u(N-1)+c(N-1)'u(N)=dN'...
from numpy import *



def CalcTkp1(M,D):
    N=len(D)
    B=zeros([N])
    A=zeros([N])
    C=zeros([N])
    C1=zeros([N])
    D1=zeros([N])
    U=zeros([N])
    for k in range(0,N):
        B[k]=M[k,k]
        if k<N-1:
            C[k]=M[k,k+1]
        if k>0:
            A[k]=M[k,k-1]
    C1[0]=C[0]/B[0]
    D1[0]=D[0]/B[0]   
    for k in range(1,N):
        if k<N-1:
            C1[k]=C[k]/(B[k]-A[k]*C1[k-1])
        D1[k]=(D[k]-A[k]*D1[k-1])/(B[k]-A[k]*C1[k-1]) 
    U[N-1]=D1[N-1]
    for k in range(N-2,-1,-1):
        U[k]=D1[k]-C1[k]*U[k+1]
    return U

# Test de l'algo de Thomas:
# 
# In [13]: M=array([[7,2,0],[3,4,5],[0,6,7]])
# D=array([1,2,-2])
# 
# In [15]: U=CalcTkp1(M,D)
# 
# In [16]: U
# Out[16]: array([ 0.89285714, -2.625     ,  1.96428571])
# 
# In [17]: dot(M,U)-D
# Out[17]: array([ -8.88178420e-16,  -1.77635684e-15,   0.00000000e+00])
# Donc U vérifie bien MU=D (aux arrondis près !!!)


#Q18 a changer
#C(N)=7 (affectations) + N*(1+1+1+1+1)  +1+1+N*(1+1+1+1) + (N-1)
# C(N)=10N+8=O(N) on a une bien meileure complexité en profitant 
# du fait que la matrice est trigonale !



#Changer le baration de 3 nbIter est le "k"
            
#Q19) enlever les norme "2"
def calc_norme(V):
    longV=len(V)
    som=0
    for k in range(0,longV):
        som=som+V[k]**2
    return sqrt(som)

#Q20) Ecrire la fonction 
def schema_implicite(M,T,V):
    D=T+r*V
    return CalcTkp1(M,D)

#Q21) A voir rajout de "valeur de N connue" changer ItMax=5000
N=60
ItMax=5000
T_tous_k=zeros([N,ItMax])     
                            
                            
#Q22) a changer donner la réponse
def T0(Tint,Text,N):
    a=(Text-Tint)/ep
    b=Tint
    t0=zeros([N])
    for k in range(0,N):
        x=(k+1)*dx
        t0[k]=a*x+b
    return t0
    
#Q23) 
t0=T0(Tint,Text1,N)
for k in range(0,N):
    T_tous_k[k,0]=t0[k]
    
    
#Q24)
M=zeros([N,N])
V=zeros([N])
V[0]=Tint
V[N-1]=Text2
for k in range(0,N):
    M[k,k]=1+2*r
    if k>0:
        M[k-1,k]=-r
    if k<N-1:
        M[k+1,k]=-r

#Q25) T1 vérifie MT1=T0+rV
T1=schema_implicite(M,t0,V) 
for k in range(0,N):
    T_tous_k[k,1]=T1[k]
    
#Q26)Changer 

nbIter=1
while nbIter<ItMax-1 and calc_norme(T_tous_k[:,nbIter-1]-T_tous_k[:,nbIter])>=10**(-2):
    T_tous_k[:,nbIter+1]=schema_implicite(M,T_tous_k[:,nbIter],V)
    nbIter=nbIter+1
    
#Tracé des graphes On fait 10 graphes de 0 à k
from matplotlib.pyplot import *
#Création des 10 temps
NB=10
Temps=[]
DT=int(nbIter/NB)
for k in range(0,NB):
    Temps.append(k*DT)
Temps=array(Temps)
#Création des abscisses des points du mur:
X=array([i*dx for i in range(1,N+1)])
#Tracé des 10 courbes de température
for k in range(0,NB):
    plot(X,T_tous_k[:,Temps[k]])
# #Pour voir le début :
# for k in range(0,NB):
#     plot(X,T_tous_k[:,k])
show()       



        
    
    
    
                           
     
        
                                                    
        


