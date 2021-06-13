a,b,n = 0,1,0
while a!=b:
    b,n = (a+b)/2,n+1
    print(b)


#5e-324 est le nombre le plus petit que l'on peut représenter car on peut le représenter avec un nombre dénormalisé égal à 1/2**52*2**(-1022)=5e-324
print(5e-324.hex())