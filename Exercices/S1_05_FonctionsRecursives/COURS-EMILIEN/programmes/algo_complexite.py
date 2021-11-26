def u(n):
    if n==0:
        return 2.
    else: 
        x=u(n-1)
        return 0.5*(x+3./x)
