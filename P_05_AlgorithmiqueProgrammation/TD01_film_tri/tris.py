
### tri insertion
def tri_insertion(tab):
    """ 
    Trie une liste de nombre en utilisant la méthode du tri par insertion.
    En Python, le passage se faisant par référence, il n'est pas indispensable
    de retourner le tableau.
    Keyword arguments:
    Entrées :
        tab -- liste de nombres
    """
    for i in range (1,len(tab)):
        x=tab[i]
        j=i
        while j>0 and tab[j-1]>x:
            tab[j]=tab[j-1]
            j = j-1
        tab[j]=x

# Exemple :
#liste = [1,8,7,6,5]
#print(liste)
#tri_insertion_02(liste)
#print(liste)


### tri rapide
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
    p=tab[i]
    while g<=d :
        while d>=0 and tab[d]>p:
            d=d-1
        while g<=j and tab[g]<=p:
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
#Exemple
#import random
#tab1 = [random.randint(0,100) for i in range(100)]
#tab2 = tab1[:]
#tab2.sort()
#tri_quicksort(tab1,0,99)
#for i in range(len(tab1)):
#    if tab1[i]!=tab2[i]:
#        print("Perdu")
#        break



### tri fusion
def fusion_listes(tab,g,d,m):
    """
    Fusionne deux listes triées.
    Keyword arguments:
    Entrées :
        tab (list) -- liste : une liste de nombres tab[g:d] avec g indice de la 
            valeur de gauche, d indice de la valeur de droite
        g,d,m (int) -- entiers : indices tels que g<=m<d et tel que les 
            sous-tableaux tab[g:m] et tab[m+1:d] soient ordonnés
    Sorties :
        tab (list) : liste triée entre les indices g et d
    """
    n1 = m-g+1
    n2 = d-m
    G,D = [],[]
    for i in range (n1):
        G.append(tab[g+i])
    for j in range (n2):
        D.append(tab[m+j+1])
    i,j=0,0
    G.append(99999999999)
    D.append(99999999999)
    for k in range (g,d+1):
        if i<=n1 and  G[i]<=D[j]:
            tab[k]=G[i]
            i=i+1
        elif j<=n2 and G[i]>D[j]:
            tab[k]=D[j]
            j=j+1
            
def tri_fusion(tab,g,d):
    """
    Tri d'une liste par la méthode du tri fusion
    Keyword arguments:
    Entrées : 
        tab (list) -- liste : une liste de nombres non triés tab[g:d]
        g,d (int) -- entiers : indices de début et de fin de liste si on veut trier
                           tout le tableau g=0, d=len(tab)-1
    Sortie :
        tab (list) : liste triée entre les indices g et d
    """
    if g<d:
        m=(g+d)//2
        tri_fusion(tab,g,m)
        tri_fusion(tab,m+1,d)
        fusion_listes(tab,g,d,m)
#Exemple
#import random
# tab = [random.randint(0,20) for i in range(20)]
#print(tab)
#tri_fusion(tab)  
#print(tab)