def fact_iterative(n):
    res=1 
    for k in range(n):
        res=res*(k+1)
    return res