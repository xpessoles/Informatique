def division(a,b):
    reste = a
    quotient = 0
    while reste > b:
        reste = reste -b
        quotient = quotient + 1
    print("reste ", reste)
    print("quotient ", quotient)



def fonction(n):
    i=0
    res=1
    while i<n:
        res = res*2
        i=i+1
    return res

def fonction2(n):
    i=n
    res=1
    while i!=0:
        res = res*2
        i=i-1
    return res

print(fonction(0))
print(fonction2(0))
print(fonction(1))
print(fonction2(1))
print(fonction(2))
print(fonction2(2))
print(fonction(3))
print(fonction2(3))
