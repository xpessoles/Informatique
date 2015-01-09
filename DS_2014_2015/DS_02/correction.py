
notes=[9.5, 11.7, 15.3, 12.1]
coefficients=[2, 1, 4, 3]

#Question 1

def verifie(notes,coefficients):
    if len(notes)==len(coefficients):
        return True
    else :
        return False


#Question 2

def noteMaxi(notes):
    max=notes[0]
    for element in notes :
        if element>max :
            max=element
    return max

print("Note maxi :",noteMaxi(notes))


#Question 3

def moyenne(notes,coefficients) :
    a=0
    b=0
    for i in range(len(notes)):
        a=a+notes[i]*coefficients[i]
        b=b+coefficients[i]
    return a/b

print("Moyenne :",moyenne(notes,coefficients))

#Question 4

n=0
m=moyenne(notes,coefficients)
for element in notes :
    if element<m :
        n=n+1
        
print(n,"notes sont inférieures à la moyenne")

#Table de Pythagore

lignes=7
colonnes=7
print("  ",end=" ")
for i in range(1,colonnes) :
    print(i,end="  ")
print(lignes)
for i in range(1,lignes+1) :
    print(i,end=" ")
    for j in range(1,colonnes+1) :
        txt=str(i*j)
        if len(txt)==1 :
            txt=" "+txt
        print(txt,end=" ")
    print("")
    


#Factorielle

def factorielle(n) :
    if type(n)!=int :
        return False
    elif n==0 :
        return 1
    else :
        a=1
        for i in range(1,n+1) :
            a=a*i
        return a


#Nuage de points

x=[2.21, 3.34, -5.4, 0.03]
y=[-3.02, 0.7, 1.2, 4.33]
X=[]
Y=[]
for i in range(len(x)) :
    if (x[i]**2+y[i]**2)<=16 :
        X.append(x[i])
        Y.append(y[i])

#Tracé

import matplotlib.pyplot as plt
from math import cos,sin,pi
cotesCercle=200
rayon=4
cx=[]
cy=[]
for i in range(cotesCercle+1):
    cx.append(rayon*cos(2*pi*i/cotesCercle))
    cy.append(rayon*sin(2*pi*i/cotesCercle))
plt.scatter(X,Y)
plt.plot(cx,cy)
plt.axis("equal")
plt.show()
