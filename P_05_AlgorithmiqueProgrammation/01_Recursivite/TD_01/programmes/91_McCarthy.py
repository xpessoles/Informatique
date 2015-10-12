def f(n) :
    if n>100 : 
        print("retour")
        return n-10
    print("appel")
    return f(f(n+11))
    
print(f(91))
