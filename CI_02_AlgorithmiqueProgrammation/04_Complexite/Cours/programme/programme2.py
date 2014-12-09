from random import randint
import time
import matplotlib.pyplot as plt
import numpy as np


#Tri par sélection
def tri_selection(tab):
    op=0
    for i in range(0,len(tab)):
        indice = i
        op=op+1
        for j in range(i+1,len(tab)):
            if tab[j]<tab[indice]:
               indice = j
               op=op+1
        tab[i],tab[indice]=tab[indice],tab[i]
        op=op+1
    #return tab
    return op
    

    
#Tri par insertion
def tri_insertion(tab):
    op=0
    for i in range(1,len(tab)):
        a=tab[i]
        op=op+1
        j=i-1
        op=op+1
        while j>=0 and tab[j]>a:
            tab[j+1]=tab[j]
            op=op+1
            j=j-1
            op=op+1
        tab[j+1]=a
        op=op+1
    #return tab
    return op

def shellSort(array):
     "Shell sort using Shell's (original) gap sequence: n/2, n/4, ..., 1."
     "http://en.wikibooks.org/wiki/Algorithm_Implementation/Sorting/Shell_sort#Python"
     op=0
     gap = len(array) // 2
     op=op+1
     # loop over the gaps
     while gap > 0:
         # do the insertion sort
         for i in range(gap, len(array)):
             val = array[i]
             op=op+1
             j = i
             op=op+1
             while j >= gap and array[j - gap] > val:
                 array[j] = array[j - gap]
                 op=op+1
                 j -= gap
                 op=op+1
             array[j] = val
             op=op+1
         gap //= 2
         op=op+1
         return op


def recherche_dichotomique(x, a):
    op=0
    g, d = 0, len(a)-1
    #op=op+1
    while g <= d:
        m = (g + d) // 2
        op=op+1
        if a[m] == x:
            #return True
            #op=op+1
            return op
        if a[m] < x:
            #op=op+1
            g = m+1
        else:
            d = m-1
            #op=op+1
    #return False
    #op=op+1
    return op

def recherche(x,tab):
    op=0
    for i in range(len(tab)):
        op=op+1
        if tab[i]==x:
            #return True
            #op=op+1
            return op
    #return False
    #op=op+1
    return op

    
tabx=[]
taby1=[]
taby2=[]
taby3=[]
taby4=[]
tabop1=[]
tabop2=[]
tabop3=[]


def test_recherche():
    op1,op2=0,0
    for i in range(0,1000,5):
        tab = [randint(0,i) for j in range(i)]
        #print(i,op1,op2,len(tab))
        tab.sort()
        x = randint(0,1000)
        t1=time.time()
        op1=recherche(x,tab.copy())
        t2=time.time()
        op2=recherche_dichotomique(x,tab.copy())
        t3=time.time()
        tabx.append(i)
        taby1.append(t2-t1)
        taby2.append(t3-t2)
       
        tabop1.append(op1)
        tabop2.append(op2)
    
test_recherche()


plt.plot(tabx,tabop1,label='Recherche naïve')
plt.plot(tabx,tabop2,label='Recherche par dichotomie')
plt.legend(loc='upper center', shadow=True)
plt.show()

"""
print("Plot")

plt.plot(tabx,taby1,label='Selection')
plt.plot(tabx,taby2,label='Insertion')
plt.plot(tabx,taby3,label='Shell')
plt.plot(tabx,taby4,label='Python')
plt.plot(tabx,tabop1,label='Sélection')
plt.plot(tabx,tabop2,label='Insertion')
plt.plot(tabx,tabop3,label='Shell')

plt.legend(loc='upper center', shadow=True)
plt.show()
"""
