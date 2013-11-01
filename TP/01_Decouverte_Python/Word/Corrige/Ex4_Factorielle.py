#! /usr/bin/env python
# -*- coding: utf-8 -*-

# Calcul de factorielle n

n=10

# Boucle for
fact = 1
for i in range(1,n+1):
    fact=fact*i

print("Boucle for : "+str(fact))

# Boucle while
fact = 1
i=1
while i<=n:
    fact=fact*i
    i=i+1
    
print("Boucle while : "+str(fact))


# Prise en cas de n=0
fact = 1
i=1
if n==0:
    fact = 1
else :
    while i<=n:
        fact=fact*i
        i=i+1
    
print("Boucle while + IF: "+str(fact))
