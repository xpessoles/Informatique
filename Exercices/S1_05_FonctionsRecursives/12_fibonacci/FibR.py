def FibR(n):
    if n<=1:
        return n
    else:
        return FibR(n-1)+FibR(n-2)