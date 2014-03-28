def expo(x,n):
    res = 1
    for i in range(n):
        res =res*x 
    return res


def evaluer(a,x):
    res=0
    for i in range(len(a)):
        res = res+a[i]*expo(x,i) 
    return res

def expo2(x,n):
    j=n
    res = 1
    while j>=1:
        res = res * x
        j=j-1
    return res

def horner(a,x):
    res=0
    n = len(a)-1
    while n>=0:
        res = a[n]+x*res
        n=n-1 
    return res

print(evaluer([0,1,2,3],2))
print(horner([0,1,2,3],2))
