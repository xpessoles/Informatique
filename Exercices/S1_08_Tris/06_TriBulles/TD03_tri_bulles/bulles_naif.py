def tri_bulles_naif(l):
    for i in range(len(l)):
        for j in range(len(l)-1): #on ne peut pas comparer le dernier élément avec un suivant
            if l[j]>l[j+1]:
                l[j],l[j+1]=l[j+1],l[j]

L=[10,3,7,5,9,7,8,0,8]