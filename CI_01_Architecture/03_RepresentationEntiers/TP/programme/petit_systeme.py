# -*- coding: utf-8 -*-
"""
Created on Wed Jul 31 14:49:18 2013

@author: Damien
"""

#import cProfile, pstats, io
#pr = cProfile.Profile()
#pr.enable()

import numpy as np


A=np.array([[0.2161001, 0.1441],[1.2969001, 0.8648]],dtype=np.float64)


#b=np.array([[ 2*A[0,0]-2*A[0,1]],[ 2*A[1,0]-2*A[1,1]]],dtype=np.float64)
b=np.array([[ 0.144] ,[0.8642002]],dtype=np.float64)

print('A')
print(A)
print('b')
print(b)
#Résolution du problème
N = A.shape[1]
M = A.shape[0]

for k in range(N):
    # Mise à zéros 
    for i in range(k+1,M):
        #On modifie le second membre avant de modifier A        
        b[i] -= b[k]*A[i,k]/A[k,k]        
        A[i,:] -= A[k,:]*A[i,k]/A[k,k]
print('A et b')
print(A)  
print(b)       

#remontée
for k in range(N-1,0,-1):   #-1 pour pas negatif
        for i in range(k):
            b[i] -= b[k]*A[i,k]/A[k,k]        
            A[i,:] -= A[k,:]*A[i,k]/A[k,k]


#fin de la résolution
solution= np.zeros((1,N))
for k in range(N):
    solution[0,k]=b[k]/A[k,k]
print('solution')
print(solution)


residu=b-np.dot(A,solution.T)
print('residu')
print(residu)

##pr.disable()
#pr.create_stats()
#pr.print_stats()

##f = open('x.pstats', 'a')
##sortby = 'time'
##pstats.Stats(pr, stream=f).strip_dirs().sort_stats(sortby).print_stats()
##f.close()



