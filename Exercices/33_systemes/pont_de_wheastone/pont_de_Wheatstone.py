#-*- coding: utf-8 -*-
import random
import numpy as np
from numpy import array,zeros
import matplotlib.pyplot as plt

#Q1
#a
R1,R3,R2,R4,R=10**4,10**4,10**3,10**3,10**3
E=10
A=np.array([[1,-1,0,0,-1],[0,0,1,-1,-1],[R1,R2,0,0,0],[0,0,R3,R4,0],[R1,0,0,-R4,R]])
B=np.array([[0],[0],[E],[E],[0]])
Xa=np.linalg.solve(A,B)
print(Xa)

#b
R1,R3,R2,R4,R=4*1e3,4*1e3,2*1e3,8*1e3,2*1e3
E=10
A=np.array([[1,-1,0,0,-1],[0,0,1,-1,-1],[R1,R2,0,0,0],[0,0,R3,R4,0],[R1,0,0,-R4,R]])
B=np.array([[0],[0],[E],[E],[0]])
Xb=np.linalg.solve(A,B)

R2=(random.randrange(11)+5)*500


# donnees
R1,R4,R=10**3,2*10**3,10**3
R2=(random.randrange(11)+5)*500
E=10

t=np.linspace(10**3,2*10**4,100) # valeurs de R3
i=[]
for R3 in t:
    A=np.array([[1,-1,0,0,-1],[0,0,1,-1,-1],[R1,R2,0,0,0],[0,0,R3,R4,0],[R1,0,0,-R4,R]])
    B=np.array([[0],[0],[E],[E],[0]])
    X=np.linalg.solve(A,B)
    i=i+[X[4,0]*1000] # *1000 pour recuperer une intensite en mA
plt.plot(t,i)
plt.axhline()
plt.ylabel('i en A')
plt.xlabel('R3 en $\Omega$')
plt.savefig('tp13_durif_q7.png')
