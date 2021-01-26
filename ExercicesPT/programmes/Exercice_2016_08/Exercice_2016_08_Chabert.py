import random as r

##Q1

def lancer():
    """ Simule un lancer de dés """
    return(r.randint(1,6))
    
#print(lancer())
#1
    
##Q2

def liste(n) :
    """ Renvoie une liste pour le lancer de n dés """
    return([lancer() for i in range(n)])
    
#print(liste(10)); [5, 3, 3, 2, 4, 6, 4, 5, 1, 1]
L = [5, 3, 3, 2, 4, 6, 4, 5, 1, 1]

##Q3

def arrivee(k,L) :
    """ Simule l'avancée comme proposé """
    
    c = k 
    
    while c < len(L) and c + L[c] < len(L) :
        c += L[k]
        
    return(c)
    
#print(arrivee(2,L)) ,5

L_15 = liste(15)
L_20 = liste(20)
L_25 = liste(25)
La_15 = []
La_20 = []
La_25 = []


for k in range (len(L_15)) :
    La_15.append(arrivee(k,L_15))

#print(La_15),[12, 15, 12, 15, 12, 15, 12, 15, 18, 17, 12, 14, 12, 14, 14]

for k in range (len(L_20)) :
    La_20.append(arrivee(k,L_20))

#print(La_20),[18, 19, 20, 17, 18, 20, 18, 17, 18, 18, 19, 17, 17, 17, 17, 17, 17, 17, 18, 19]

for k in range (len(L_25)) :
    La_25.append(arrivee(k,L_25))

#print(La_25),[24, 25, 22, 21, 21, 25, 24, 23, 22, 21, 22, 21, 22, 23, 22, 21, 21, 21, 21, 21, 22, 21, 22, 23, 24]

##Q4

def commun(L) :
    """ renvoie le plus grand entier tel que l'arrivee de 0,1,2,k soit le même """
    a,b,c = arrivee(0,L),arrivee(1,L),arrivee(2,L)
    k = 0
    res = True
    
    while res and k < len(L) :
        if arrivee(k,L) == a and arrivee(k,L) == b and arrivee(k,L) == c :
            k +=1
        else :
            res = False
        
    return(k-1)
        
#print(commun([6,5,4,3,2,1,1]))
#6
