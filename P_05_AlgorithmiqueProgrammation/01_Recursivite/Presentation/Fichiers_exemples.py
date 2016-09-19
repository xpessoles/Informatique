"""
def fonction_recursive():
    return fonction_recursive()

def fonction_recursive_2(n):
    n=n+1
    print(n)
    return fonction_recursive_2(n)
    


def fonction_recursive_3(n):
    n=n+1
    print(n)
    if n==3:
        return 3
    else :
        return fonction_recursive_3(n)
    
    
fonction_recursive_3(0)
"""

def explicite_2n(n):
    return 2**n
    
def iteratif_2n(n):
    if n==0:
        return 1
    else :
        i=0
        res = 1
        while i<n:
            res = res*2
            i=i+1 #
        return res
        
def recursif_2n(n):
    if n==0:
        return 1
    else :
        return 2*recursif_2n(n-1)
    
#u_n = f(u(n-1))

print(explicite_2n(5))
print(iteratif_2n(5))
print(recursif_2n(5))

    