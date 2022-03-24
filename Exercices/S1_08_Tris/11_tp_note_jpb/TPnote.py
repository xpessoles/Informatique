#####PROBLEME I


##### PROBLEME 2

## 1

import random as r

def random_list(n,k):
    return([r.randrange(k) for i in range(n)])

## 2

def counting_sort(k,t):
    u=[0]*k
    n=len(t)
    r=[]
    for i in range(n):
        u[t[i]]+=1
    for i in range(k):
        if u[i]!=0:
            for j in range(u[i]):
                r.append(i)
    return(r)

## 3

# Pour chaque valeur de f(x) trouvee, on incremente u[f(x)]
# On cree simultanement une liste des antecedents de f(x) dans t

def f(x):
    if x==0:
        return(3)
    elif x==1:
        return(2)
    elif x==2:
        return(1)
    elif x==3:
        return(4)
    elif x==4:
        return(0)
    elif x==5:
        return(2)
    elif x==6:
        return(0)

t=random_list(10,7)


def bucket_sort(f,k,t):
    u=[[] for i in range(k)]
# u[f(i)] contient la liste des antécédents de f(i).
    n=len(t)
    r=[]
    for i in range(n):
        j=f(t[i])
        u[j].append(t[i])
    for i in range(k):
        if u[i]!=[]:
            r=r+u[i]
    return(r)

## 4

def radix_sort(k,t):
    # t est compose d'entiers dans range(k**2)
    def lp(x):
        return x//k
    def rp(x):
        return x%k
    u=bucket_sort(rp,k,t)
    r=bucket_sort(lp,k,u)
    return (r)

## 5

def radix_sort2(k,t):
    # t est compose d'entiers dans range(k**3)
    def lp(x):
        return x//k
    def rp(x):
        return x%k
    u=bucket_sort(rp,k,t)
    v=bucket_sort(lp,k**2,u)
    return (u,v)

t=random_list(10,7**3)

## 6

# On choisit n nombres aleatoires, chacun de complexite à temps constant. On obtient un O(n).
#


# Dans la première boucle, il y a n tours.
# Pour la deuxième, il y a k tours et dans le pire des cas (chaque ui non nul), il y a 1 affectation dans r. Au total, cela donne une complexite en n+k, soit en max(n,k).
#


# meme chose.
#


# Pour u, la complexite est de O(max(n,k))
# Pour r, aussi.
# Cela donne encore une complexite en max(n,k).
#


# On realise l'ordre du dictionnaire. Pour k=10, on regarde d'abord les unites et on ordonne le tableau selon les unites croissantes.
# Puis on regarde les dizaines et on ordonne par tri stable suivant les dizaines croissantes. On a ordonne le tableau.
# Pour une autre valeur de k, le principe est le même mais en base k. On remarque que rp(x) et lp(x) sont bien compris entre 0 et k-1 pour x compris entre 0 et k**2-1
# En effet, on a x<=y lorsque (lp(x)<lp(y)) ou (lp(x)=lp(y) et rp(x)<=rp(y))
