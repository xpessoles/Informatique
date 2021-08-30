###Tri par insertion :
def tri_Insertion_v3(t) :
    '''Trie la liste t
    Entrée :
        Une liste
    Sortie :
        La liste est modifiée mais n’est pas renvoyée'''
    for i in range(1,len(t)) :
        element=t[i]
        x=t[i][-1]
        k=0
        while (k<i and x>t[k][-1]) :
            k=k+1
        for j in range(i,k,-1) :
            t[j]=t[j-1]
        t[k]=element