def tri_Insertion(t) :
    '''Trie la liste t
    Entrée :
        Une liste
    Sortie :
        La liste est modifiée mais n'est pas renvoyée'''
    for i in range(1,len(t)) :
        cle=t[i]
        k=i-1
        while (k>=0 and t[k]>cle) :# on peut comparer avec l'élément précédent
            t[k+1]=t[k]
            k=k-1
        t[k+1]=cle

L=[2,5,1,6,9,4]
tri_Insertion(L)
print (L)


etudiants=[('Julie','PTS1',15),('Elio','PTS2',14),('Jules','PTS1',17),('Adam','PTS2',16)]

a = sorted(etudiants, key=lambda etudiants: etudiants[2])

# >>> a
# [('Elio', 'PTS2', 14), ('Julie', 'PTS1', 15), ('Adam', 'PTS2', 16), ('Jules', 'PTS1', 17)]

couple=[(3,3),(3,6),(3,1)]

