

# On suppose a<b
## Q1

def disjoint(i1,i2):
    """ retourne True si les segment sont disjoints, false sinon """
    return(i1[1]<i2[0] or i2[1]<i1[0])

#print(disjoint([0,1],[-1,0.5]))
#False

## Q2

def fusion(i1,i2):
    """ fusionne les deux segments """
    return([min(i1[0],i2[0]),max(i1[1],i2[1])])

#print(fusion([-1,2],[0,0.5])) [-1, 2]
#print(fusion([-1,2],[0,5])) [-1, 5]


## Q3

#L = [[0,3],[6,7],[2,5]]
#non bien fondée
L = [[0,1],[2,3],[4,5]]
#bien fondée

def verif(L):
    """ vérifie si une liste est bien fondée """

    if len(L) == 1 :
        return(True)
    elif disjoint(L[0],L[1]) and L[0][1]<L[1][0] :
        return(True and (verif(L[1:])))
    else :
        return(False)
    
#print(verif(L))
#True
        
