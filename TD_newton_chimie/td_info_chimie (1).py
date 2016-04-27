### chimie calcul du pH d'une solution
import numpy as np
import matplotlib.pyplot as plt
import scipy.optimize as sco

def pH_1(C):
    return -np.log10(C)
    
def pH_2(C,pKa):
    return 0.5*(pKa-np.log10(C))
    

   
def pH_3(C,pKa):
    return -np.log10(0.5*(-Ka+np.sqrt(Ka*(Ka+4*C))))


### equation 4 avec recherche du zéro d'une fonction    
def f(h,Ka):
    Ke=10**-14
    return h**3+Ka*h**2-(Ke+Ka*C)*h-Ka*Ke
    
def der_f(h,Ka):
    Ke=10**-14
    return 3*h**2+2*Ka*h-Ke-Ka*C
    
# pKa=4.8
# Ka=10**-pKa  
# Ke=10**-14
les_C=[10**-2,10**-4,10**-6,10**-8]

C=10**-2
plt.figure(1)
les_h=np.linspace(-10**-11,10**-11,50)
les_y=f(les_h,10**-3.2)
# les_y_bis=der_f(les_h,10**-3.2)
plt.plot(les_h,les_y,label='fonction f(h)')
plt.grid()
plt.legend()
plt.show()
plt.figure(2)
les_h=np.linspace(-1,1,50)
les_y=f(les_h,10**-3.2)
plt.plot(les_h,les_y)
les_y_bis=der_f(les_h,10**-3.2)
plt.plot(les_h,les_y_bis)
plt.grid()
plt.show()

    
def dichotomie(f,a,b,epsilon,Ka):
    g=a
    d=b
    while (d-g)>2*epsilon:
        m=(d+g)/2
        if f(m,Ka)*f(g,Ka)<=0:
            d=m
        else:
            g=m
    return ((d+g)/2)
    

def newton(f,der_f,a0,epsilon,Ka):
    y=a0
    y1=y-f(y,Ka)/der_f(y,Ka)
    while np.abs(y1-y)>epsilon:
        y=y1
        y1=y-f(y,Ka)/der_f(y,Ka)
    return y
    
# la valeur de h est negative ???? et n'est pas dans le domaine de validité du logarithme décimal...
# In [5]: newton(f,der_f,-1,10**-15,10**-3.2)
# Out[5]: -0.0006309673443219599
# In [6]: dichotomie(f,-1,0,10**-15,10**-3.2)
# Out[6]: -0.0006309673443221087

def f1(h):
    Ka=10**-3.2
    Ke=10**-14
    return h**3+Ka*h**2-(Ke+Ka*C)*h-Ka*Ke
    
C=10**-4    
print ('scipy donne '+str(sco.newton(f1,1)))
#C=10**-2 : scipy donne 0.002216141417218524
#C=10**-4 scipy donne 8.778626688056297e-05

def pH_4(Concentration,pKa,methode):
    Ka=10**(-pKa)
    Ke=10**-14
    C=Concentration
    if methode=="dichotomie":
        h=dichotomie(f,0,1,10**-15,Ka)
    if methode=="newton":
        h=newton(f,der_f,0,10**-15,Ka)
    if methode=="scipy":
        h=sco.newton(f1,1)
    return -np.log10(h)

les_C=[10**-2,10**-4,10**-6,10**-8]
for C in les_C:
    print (pH_4(C,3.2,"dichotomie"))
    print (pH_4(C,3.2,"newton"))
    print (pH_4(C,3.2,"scipy"))

    