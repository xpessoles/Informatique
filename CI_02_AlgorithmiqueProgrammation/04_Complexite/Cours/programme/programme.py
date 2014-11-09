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

    
tabx=[]
taby1=[]
taby2=[]
taby3=[]
taby4=[]
tabop1=[]
tabop2=[]
tabop3=[]
# compréhensions de liste
def test_tri():
    for i in range(0,1001,50):
        print(i)
        tab = [randint(0,2**1024) for j in range(i)]
        t1=time.time()
        op1=tri_selection(tab.copy())
        t2=time.time()
        op2=tri_insertion(tab.copy())
        t3=time.time()
        op3=shellSort(tab.copy())
        t4=time.time()
        tab.sort()
        t5=time.time()
        tabx.append(i)
        taby1.append(t2-t1)
        taby2.append(t3-t2)
        taby3.append(t4-t3)
        taby4.append(t5-t4)
        tabop1.append(op1)
        tabop2.append(op2)
        tabop3.append(op3)
test_tri()

print("Plot")

plt.plot(tabx,taby1,label='Selection')
plt.plot(tabx,taby2,label='Insertion')
plt.plot(tabx,taby3,label='Shell')
plt.plot(tabx,taby4,label='Python')
"""plt.plot(tabx,tabop1,label='Sélection')
plt.plot(tabx,tabop2,label='Insertion')
plt.plot(tabx,tabop3,label='Shell')
"""
plt.legend(loc='upper center', shadow=True)
plt.show()
