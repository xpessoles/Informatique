def ajouteUnFor(L):
    '''prend comme argument une liste L de flottants et ajoute 1 à chaque élément de la liste avec un boucle for'''
    for i in range(len(L)):
        L[i]+=1
        
        
def ajouteUnWhile(L):
    '''prend comme argument une liste L de flottants et ajoute 1 à chaque élément de la liste avec une boucle while'''
    i=0
    while i<len(L):
        L[i]+=1
        i+=1
        
L=[1,2,3,4,5]
ajouteUnFor(L)
print(L)
ajouteUnWhile(L)
print(L)

        

        