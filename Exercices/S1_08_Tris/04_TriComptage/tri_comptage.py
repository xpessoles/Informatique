def tri_comptage(L:list,k:int):
    C=k*[0]
    a=[]
    for x in L:
        for i in range(k):
            if x==i:
                C[i]+=1
    for i in range(k):
        a+=C[i]*[i]
    return a


def tri_comptage2(L,k):
    C=[0]*k
    for i in range(len(L)):
        C[L[i]]=C[L[i]]+1
    p=0
    for i in range(k):
        for j in range(C[i]):
            L[p]=i
            p+=1

L=[2,1,4,1]

a=tri_comptage(L,5)
