def chercheMax(L):
    '''prend comme argument une liste L d'entiers int et qui renvoie le plus grand élément de la liste'''
    max=L[0]
    for i in range(1,len(L)):
        if L[i]>max:
            max=L[i]
    return max
        
        
def chercheMaxIndice(L):
    '''prend comme argument une liste L d'entiers int et qui renvoie l'indice du plus grand élément de la liste'''
    max=L[0]
    indmax=0
    for i in range(1,len(L)):
        if L[i]>max:
            max=L[i]
            indmax=i
    return indmax
        
L=[1,2,10,3,4,10,5]
a=chercheMax(L)
b=chercheMaxIndice(L)

        

        