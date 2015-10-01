def P2_rapide(n):
    if n == 0:
        return 1
    if n%2 == 0 :
        tmp = P2_rapide(n/2)
        return tmp*tmp
    else : 
       return (2*P2_rapide(n-1))
       

print(P2_rapide(7))
print(2**7)