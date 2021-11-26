def u(n):
    if n==0:
        return 2.
    else: 
        return 0.5*(u(n-1)+3./u(n-1))
