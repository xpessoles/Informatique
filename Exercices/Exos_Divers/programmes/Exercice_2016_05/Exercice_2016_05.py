#### Exercice 5

##question 1:

#cette fonction crée une liste de chiffre à partir d'un nombre, les elements de la liste sont les chiffres qui composent le nombre


##question 2:

def chiffres (n):
    L=[]
    for k in range(len(str(n))):
        if n == 0:
            return[0]
        if n != 0:
            L.append(n%10)
            n=n//10
    return(L)

def calcul_narcissique(n):
    p=len(str(n))
    L=chiffres(n)
    S=0
    for k in range (p):
        S=S+L[k]**p 
    return(S)

# print(calcul_narcissique(93084))
# 93084

##question 3:

def verif_narcissique(n):
    return(calcul_narcissique(n)==n)
    
# print(verif_narcissique(93084))
# True

##question 4

l=[]
for k in range(100000):
    if verif_narcissique(k) == True:
        l.append(k)
        
# print(l)
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 153, 370, 371, 407, 1634, 8208, 9474, 54748, 92727, 93084]

