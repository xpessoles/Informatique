def fact_recursif(n):
    if n==0:
        res=1
    else:
        res=n*fact_recursif(n-1)
    return res