# -*- coding: utf-8 -*-
"""
Created on Fri Oct 10 13:46:40 2014

@author: pessoles
"""

#Création de la liste incidence

#Question 2
incidence = []
u0 = -9
for i in range(14):
    un = u0+3*i
    incidence.append(un)
    

#Question 3
#import matplotlib.pyplot as plt
trainee = [7,5,4,3,3,4,5,7,10,13,16,18,19,20]
portance = [-20,-18,0,13,37,47,60,74,83,90,87,80,75,52]

#plt.plot(trainee,portance)
#plt.show()

# Question 4
finesse=[]
for i in range(len(trainee)):
    finesse.append(portance[i]/trainee[i])


#Question 5 : Trouver le maximum de la liste : 
maxi = finesse[0]
for i in range(1,len(finesse)):
    if finesse[i]>maxi:
        maxi = finesse[i]


#Question 5 : Trouver l'indice du maximum de la liste : 
maxi = finesse[0]
indice_maxi=0
for i in range(1,len(finesse)):
    if finesse[i]>maxi:
        maxi = finesse[i]
        indice_maxi = i
#Question 5 : Quelle est l'incidence pour laquelle la finesse est maximale : 
print("L'incidence est maximale pour une incidence de "+str(incidence[indice_maxi])+" degrés")
