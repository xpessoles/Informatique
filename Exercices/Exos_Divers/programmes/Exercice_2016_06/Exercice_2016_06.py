import matplotlib.pyplot as plt
import numpy as np
import random as rdm

####Exercice 6 ####

A=[1,5]
B=[2,8]
C=[7,1]

##question 1:

def triangle(a,b,c):
    plt.plot([a[0],b[0],c[0]],[a[1],b[1],c[1]],'r')
    
    plt.plot([c[0],a[0]],[c[1],a[1]],'r')


triangle(A,B,C)
plt.show()
##question 2:

def milieu(a,b):
    I=[(a[0]+b[0])/2,(a[1]+b[1])/2]
    return(I)

print(milieu(A,B))

##question 3:

def cal_milieu(p):
    L=[A,B,C]
    a=L[rdm.randint(0,2)]
    I=milieu(a,p)
    
    return(I)

## question 4 :

p=[1,1] # point p choisi arbitrairement

L=[]
for k in range(1000):
    L.append(cal_milieu(p))

les_x=[]
les_y=[]

for l in range(len(L)):
    les_x.append(L[l][0])
    les_y.append(L[l][1])

triangle(A,B,C)
plt.xlim(0,10)
plt.ylim(0,10)
plt.plot([p[0]],[p[1]],'*')
plt.plot(les_x,les_y,'+-g')
plt.show()

