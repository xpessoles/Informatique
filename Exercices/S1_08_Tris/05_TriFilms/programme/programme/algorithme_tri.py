### tri TD01 Xavier
### exercice 2 : tri à bulles
#question 2 algorithme naif 

def triBulleNaif(L):
    n=len(L)
    j=0
    while j!=n-1:
        j=0
        for i in range(n-1):
            if L[i+1]<L[i]:
                L[i+1],L[i]=L[i],L[i+1]
            else:
                j+=1
    return L
    
    
# L=[3,5,7,1,4,0,3,9]
# triBulleNaif(L)
# [0, 1, 3, 3, 4, 5, 7, 9]

def triBulleMoinsNaif(L):
    n=len(L)
    j=0
    k=0
    while j!=n-k:
        j=0
        k=k+1
        for i in range(n-k):
            if L[i+1]<L[i]:
                L[i+1],L[i]=L[i],L[i+1]
            else:
                j+=1
    return L
    
# L=[3,5,7,1,4,0,3,9]
# triBulleMoinsNaif(L)
# [0, 1, 3, 3, 4, 5, 7, 9]