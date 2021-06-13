def mystere():
    a,b,n = 1,1.,0
    while a==b:
        a,b,n = 2*a,2*b,n+1
    return n
