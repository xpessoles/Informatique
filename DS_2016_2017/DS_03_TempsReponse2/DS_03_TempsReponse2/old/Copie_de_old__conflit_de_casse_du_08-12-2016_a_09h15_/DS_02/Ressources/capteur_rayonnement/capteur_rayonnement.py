a = [1,4,3,3,5,4,1,2,3,5,5,5,1,3,5]
t = [10,20,30,40,50,60,70,80,90,100,110,120,130,140,150]

def compte(x,a):
    c=0
    for v in a:
        if x==v:
            c+=1
    return c

def occurrences(a):
    r=[]
    for v in a:
        r.append(compte(v,a))
    return r

def maxconstant(a,t):
    Tmax=0
    i=0
    k=1
    n=len(a)
    while  i<n-1:
        while k<n and a[k]==a[i]:
            k+=1
        T=t[k-1]-t[i]
        if T>Tmax:
            Tmax=T
        i=k
        k+=1
    return Tmax

def maxoccurrences(a,occ):
    m1=occ[0]
    i1=0
    n=len(occ)
    m2=occ[1]
    i2=1
    while i2<n and a[i2]==a[i1]:
        i2+=1
    if i2==n:
        i2=-1
    else:
        for k in range(i2,n):
            if occ[k]>m1:
                m2=m1
                i2=i1
                m1=occ[k]
                i1=k
            elif occ[k]>m2 and a[i1]!=a[k]:
                m2=occ[k]
                i2=k
    return i1,i2

def permute(a,i,j):
    a[i],a[j]=a[j],a[i]
   
def trier(a,t,m1,m2):
    b=0
    r=0
    q=len(a)-1
    while r<=q:
        if a[r]==m1:
            permute(a,r,b)
            permute(t,r,b)
            b+=1
            r+=1
        elif a[r]==m2:
            r+=1
        else:
            permute(a,r,q)
            permute(t,r,q)
            q-=1
            
    
    
    
    
