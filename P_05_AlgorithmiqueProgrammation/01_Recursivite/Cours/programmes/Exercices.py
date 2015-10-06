def f(n) :
    if n>100 : 
        return n-10
    return f(f(n+11))
    
print(f(1))
print(f(2))
print(f(3))
print(f(4))


print(f(101))
print(f(102))
print(f(103))
print(f(104))
