import random
a=[random.randint(1,100) for x in range (20)]
a=[1,2,3,4,5,6,7,9,8]
print(a)

def maximum(tab):
    maxi =  float("-infinity")
    for i in range(0,len(tab)):
        if tab[i]>maxi:
            maxi=tab[i]
    return maxi

def tri_naif(tab):
    for i in range(0,len(tab)-1):
        min=i
        for j in range(i+1,len(tab)):
            if tab[j]<tab[min]:
                min=j
        tmp = tab[i]
        tab[i]=tab[min]
        tab[min]=tmp
        print(tab)
    return tab
                

print(tri_naif(a))

        
