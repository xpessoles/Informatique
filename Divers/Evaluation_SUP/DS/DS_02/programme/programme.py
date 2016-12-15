from random import randint
from math import sqrt
"""
def solve(a,b,c):
    # Calcul du discriminant :
    delta = b*b - 4*a*c
    if delta == 0 :
        return [-b/(2*a)]
    elif delta > 0 :
        return [(-b-sqrt(delta))/(2*a),(-b+sqrt(delta))/(2*a)]


def verif(tab,a,b,c) :
    if len(tab)==2:
        print(a*tab[0]*tab[0]+b*tab[0]+c)
        print(a*tab[1]*tab[1]+b*tab[1]+c)
    if len(tab)==1:
        print(a*tab[0]*tab[0]+b*tab[0]+c)


a,b,c=1.0,0.,0.
tab = solve(a,b,c)
print(tab)
verif(tab,a,b,c)
"""


def tri(tab):
    for i in range(0,len(tab)):
        indice = i
        for j in range(i+1,len(tab)):
            if tab[j]<tab[indice]:
               indice = j
        permute(tab,i,indice)
    return tab
    
def permute(tab,i,j):
    tab[i],tab[j]=tab[j],tab[i]

def is_sorted_for(tab):
    for i in range(0,len(tab)-1):
        if tab[i+1]<tab[i]:
            return False
    return True

def is_sorted_while(tab):
    i=1
    print(tab[i-1],tab[i])
    while tab[i-1]<=tab[i] and i<len(tab)-1:
        
        i=i+1
    return tab[i-1]<=tab[i]

        
#tab=[2,10,5,8,2,11,20,6,1]
tab=[2,5,10,9]
#tab=[10,0]#,5,8,2,11,20,6,13]
print(tab)
print(is_sorted_while(tab))
tri(tab)
print(tab)
print(is_sorted_while(tab))

