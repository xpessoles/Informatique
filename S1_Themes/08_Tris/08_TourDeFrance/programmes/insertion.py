def tri_insertion_modifie(tab):
    '''Trie la liste t
    Entree :
        Une liste
    Sortie :
        La liste est modifiee mais n est pas renvoyee'''
    for i in range(1,len(t)) :
        element=t[i]
        x=t[i][-1]
        k=0
        while (k<i and x>t[k][-1]) :
            k=k+1
        for j in range(i,k,-1) :
            t[j]=t[j-1]
        t[k]=element
