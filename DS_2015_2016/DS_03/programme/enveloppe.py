from random import randint

import matplotlib.pyplot as plt 


def orientation(tab,i,j,k):
    p1 = tab[i]
    p2 = tab[j]
    p3 = tab[k]
    p12 = [p2[0]-p1[0],p2[1]-p1[1]]
    p13 = [p3[0]-p1[0],p3[1]-p1[1]]
    det = p12[0]*p13[1]-p12[1]*p13[0]
    if det <0 :
        return -1
    elif det >0 :
        return 1
    else :
        return 0

def enveloppe_Sup_rec(tab,Es,i):
    if est_vide(Es):
        push(Es,i)
    else :
        p1 = i
        p2 = pop(Es)
        if est_vide(Es):
            push(Es,p2)
            push(Es,p1)
        else :
            p3 = top(Es)
            if orientation(tab,p1,p2,p3)>0:
                push(Es,p2)
                push(Es,p1)
            else :
                enveloppe_Sup_rec(tab,Es,i)
                
def enveloppe_Sup_it(tab,Es,i):
    if est_vide(Es):
        push(Es,i)
    else :
        p1 = i
        p2 = pop(Es)
        if est_vide(Es):
            push(Es,p2)
            push(Es,p1)
        else :
            ori=1
            while (not(est_vide(Es))) or ori>0.00001:
                print(Es,ori)
                p3 = top(Es)
                ori = orientation(tab,p1,p2,p3)
                if ori>0:
                    push(Es,p2)
                    push(Es,p1)
                else :
                    pop(Es)
                
                

def creer_pile():
    return[]

def est_vide(p):
    return len(p)==0

def push(p,e):
    p.append(e)

def pop(p):
    return p.pop()
    
def top(p):
    return p[-1]



def segmente(tab,i,j):
    """
    Segmentation d'un tableau par rapport à un pivot.
    Keyword arguments: 
    Entrées :
        tab (list) -- liste de nombres
        i,j (int) -- indices de fin et de début de la segmantation
    Sorties :    
        tab (list) -- liste de nombres avec le pivot à sa place définitive
        k (int) -- indice de la place du pivot
    """
    g =i+1
    d=j
    p=tab[i][0]
    while g<=d :
        while d>=0 and tab[d][0]>p:
            d=d-1
        while g<=j and tab[g][0]<=p:
            g=g+1
        if g<d :
            tab[g],tab[d]=tab[d],tab[g]
            d=d-1
            g=g+1
    k=d
    tab[i],tab[d]=tab[d],tab[i]
    return k
    
def tri_quicksort(tab,i,j):
    """
    Tri d'une liste par l'utilisation du tri rapide (Quick sort).
    Keyword arguments:
    Entrées :
        tab (list) -- liste de nombres
        i,j (int) -- indices de fin et de début de la zone de tri
    Sorties :    
        tab (list) -- liste de nombres avec le pivot à sa place définitive
    """
    if i<j :
        k = segmente(tab,i,j)
        tri_quicksort(tab,i,k-1)
        tri_quicksort(tab,k+1,j)



                

nuage = [[randint(0,20),randint(0,20)] for i in range(20)]

x=[nuage[i][0] for i in range(len(nuage))]
y=[nuage[i][1] for i in range(len(nuage))]
plt.axis("equal")
plt.grid()
a = max(x)
b = max(y)
maxi = max(a,b)
plt.plot(x,y,".")

nuagetrie = nuage.copy()
tri_quicksort(nuagetrie,0,len(nuage)-1)

Es=creer_pile()
for i in range(len(nuagetrie)):
    enveloppe_Sup_rec(nuagetrie,Es,i)
xenv =[]
yenv = []
for i in Es:
    xenv.append(nuagetrie[i][0])
    yenv.append(nuagetrie[i][1])
plt.plot(xenv,yenv)

# Es=creer_pile()
# for i in range(len(nuagetrie)):
#     enveloppe_Sup_it(nuagetrie,Es,i)
# xenv =[]
# yenv = []

plt.show()

