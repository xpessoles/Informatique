#question 1

def dédoublement(L):
    n =len(L)
    k=0
    P=[]
    while k < n :
        v=L[k]
        S=0
        while k<n and L[k] == v:
            S=S+1
            k=k+1
        P.append(S)
        P.append(v)
    return(P)

##print(dédoublement([1,1,1,2,2,2]))
##>>> 
##[3, 1, 3, 2]

#question2

def chaine(P):
    C=str(P[0])
    n=len(P)
    for k in range(1,n):
        C=C+','+str(P[k])
    return(C)

##print(chaine(dédoublement([1,1,1,2,2,2])))
##>>> 
##3,1,3,2

def dédoubl_recurence(L,n):
    for k in range(n):
        L=dédoublement(L)
    return(L)


def dédouble_recursive(L,n):
    if n == 0:
        return(L)
    else:
        L=dédoublement(L)
        return(dédouble_recursive(L,n-1))

##print(dédouble_recursive([1],3))
##print(dédoubl_recurence([1],3))
##>>> 
##[1, 2, 1, 1]
##[1, 2, 1, 1]
