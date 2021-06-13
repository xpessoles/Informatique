#Importation des modules
import matplotlib.pyplot as plt
import numpy as np

#Programme principal


##Q2

fichier='premier_ordre.csv'
f=open(fichier)
texte=f.readlines()
temps=[]
V=[]
for k in range(len(texte)):
    ligne=texte[k].split(";")
    temps.append(float(ligne[0]))
    V.append(float(ligne[1]))




##Q3
t=np.asarray(temps)
V=np.asarray(V)
theta_inf=3
Y=np.log((theta_inf-V)/theta_inf)
    
plt.figure()   
plt.plot(t,V)

plt.title('Reponse indicielle')
plt.xlabel('temps (s)')
plt.ylabel('Vitesse angulaire (rad/s)')


plt.figure()
plt.plot(t,Y,'b*')



##Q5
def calcul_alpha(t,Y):
    S1=0
    S2=0
    for k in range(len(t)):
        S1+=t[k]*Y[k]
        S2+=t[k]**2
    alpha=S1/S2
    return alpha
    
alpha=calcul_alpha(t,Y)
Y_sol=alpha*t
K=theta_inf

plt.plot(t,Y_sol,'r')
plt.xlabel('temps (s)')
plt.ylabel('log((theta_inf-V)/theta_inf)')
V_th=K*(1-np.exp(alpha*t))

plt.figure()
plt.plot(t,V,label='donnees experimentales')
plt.plot(t,V_th,label='Modele identifie')

plt.title('Reponse indicielle')
plt.xlabel('temps (s)')
plt.ylabel('Vitesse angulaire (rad/s)')
plt.legend(loc='lower right')
plt.show()
# 
# ##Q8
def residu(t,V,V_th):
    res=0
    for k in range(len(t)):
        res+=(V[k]-V_th[k])**2
    return res

print("\n le residu pour la determination de alpha au sens des moindres carres vaut "+str(residu(t,V,V_th))+"\n")
# 
# 
# ##Q9
def derivee(t,V):
    dV=np.zeros([len(t)])
    for k in range(len(t)-1):
        dV[k]=(V[k+1]-V[k])/(t[k+1]-t[k])
    k=len(t)-1
    dV[k]=(V[k]-V[k-1])/(t[k]-t[k-1])
    return dV
#     
# 
# 
# 
##Q16
plt.figure()
plt.plot(t,derivee(t,V))
plt.title('Reponse indicielle')
plt.xlabel('temps (s)')
plt.ylabel('derivee de la vitesse angulaire (rad/s^2)')
plt.legend(loc='lower right')
plt.show()
# 
# 
# ##Q11
dV=derivee(t,V)
phi=np.transpose([list(dV),list(V)])
E0=4
E=E0*np.ones([len(t)])
X=np.dot(np.dot(np.linalg.inv(np.dot(np.transpose(phi),phi)),np.transpose(phi)),E)
K1=1/X[1]
tau1=K1*X[0]
V_th1=K1*(1-np.exp(-t/tau1))*E0

plt.figure()
plt.plot(t,V,label='donnees experimentales')
plt.plot(t,V_th,label='Modele identifie')
plt.plot(t,V_th1,label='Modele identifie')

plt.title('Reponse indicielle')
plt.xlabel('temps (s)')
plt.ylabel('Vitesse angulaire (rad/s)')
plt.legend(loc='lower right')
plt.show()


#  ##Q12 Calcul d'integrale
# def integ1(t,V):
#     dt=t[1]-t[0]
#     iV=np.cumsum(V)*dt
#     return iV
#     
def integ2(t,V):
    dt=t[1]-t[0]
    iV=0
    LiV=[0]
    for k in range(1,len(t)):
        iV+=dt*V[k]
        LiV.append(iV)
    return LiV
    
##Q13
iV=integ2(t,V)
iE=integ2(t,E)
iphi=np.transpose([list(V),list(iV)])
X=np.dot(np.dot(np.linalg.inv(np.dot(np.transpose(iphi),iphi)),np.transpose(iphi)),iE)
K2=1/X[1]
tau2=K2*X[0]
V_th2=K2*(1-np.exp(-t/tau2))*E0

plt.figure()
plt.plot(t,V,label='donnees experimentales')
plt.plot(t,V_th,label='Modele identifie 1')
plt.plot(t,V_th1,label='Modele identifie 2')
plt.plot(t,V_th2,label='Modele identifie 3')

plt.title('Reponse indicielle')
plt.xlabel('temps (s)')
plt.ylabel('Vitesse angulaire (rad/s)')
plt.legend(loc='lower right')
plt.show()
#     
# 
# 
# ## Q19 Methode des moindres carres integree
# iV1=integ1(t,V)
# iV2=integ2(t,V)
# iE=integ2(t,E)   
# plt.figure()
# plt.plot(t,V,label='theta')
# plt.plot(t,iV1,label='Integralle 1')
# plt.plot(t,iV2,label='Integralle 2')
# 
# iphi=np.transpose([list(V),list(iV1)])
# X2=np.dot(np.dot(np.linalg.inv(np.dot(np.transpose(iphi),iphi)),np.transpose(iphi)),iE)
# K2=1/X2[1]
# tau2=K2*X2[0]
# 
# 
# V_th2=K2*(1-np.exp(-t/tau2))*E0
# 
# ## Q20 Comparaison des residus
# 
print("\n le residu pour la determination de alpha au sens des moindres carres vaut "+str(residu(t,V,V_th))+"\n")
print("\n le residu pour la determination de alpha au sens des moindres carres (methode 2) vaut "+str(residu(t,V,V_th1))+"\n")
print("\n le residu pour la determination de alpha au sens des moindres carres (methode 3 integre) vaut "+str(residu(t,V,V_th2))+"\n")
# 
# plt.figure()
# plt.plot(t,V,label='donnees experimentales')
# plt.plot(t,V_th,label='Moindres carres sur un coefficient')
# plt.plot(t,V_th1,label='Moindres carres sur deux coefficients')
# plt.plot(t,V_th2,label='Moindres carres sur deux coefficients avec methode integrale')
# 
# plt.title('Reponse indicielle')
# plt.xlabel('temps (s)')
# plt.ylabel('Vitesse angulaire (rad/s)')
# plt.legend(loc='lower right')
# 
# plt.show()
    