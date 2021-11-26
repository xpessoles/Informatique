def FibI(n):
    u=0
    v=1
    if n<=1:
        v=n
    for k in range(2,n+1):
        u,v=v,u+v
    return v