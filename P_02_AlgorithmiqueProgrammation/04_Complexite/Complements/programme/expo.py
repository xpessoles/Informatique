def expo_naive(x,n):
    i=1
    res = x
    while i<n:
        res = res *x
        i=i+1

    print(x,n,res)
    print()

def expo(x,n):
    """ Calcul de x^n """
    res = 1
    puiss = x 
    while n!=0:
        if n%2 == 0 :
            #res = res*res
            n=int(n/2)
        else :
            res = res*puiss
            n=int((n-1)/2)

        puiss = puiss * puiss
            
    print(x,n,res)


print()
expo(2,30)
expo_naive(2,30)
