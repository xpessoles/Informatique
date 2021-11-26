def Pow2_recursive(n):
    if n==0:
        return 1
    else:
        return 2*Pow2_recursive(n-1)