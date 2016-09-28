# Multiplication
def fonc_01(a,b):
    if b==0:
        return 0
    else :
        return a+(fonc_01(a,b-1))

#print(fonc_01(3,2))
# Réponse +6 -14 -5 -1

# Multiplication avec erreur
def fonc_02(a,b):
    if b==0:
        return 1
    else :
        return a+(fonc_02(a,b-1))

print(fonc_02(3,2))
# Réponse -14  -6  +15  -9  -5


# Inversion d'une chaine de caracteres
def fonc_03(ch):
    n=len(ch)
    if n==0 :
        return ch
    else :
        return ch[n-1] + fonc_03(ch[0:n-1])

# print(fonc_03("resu"))
# Réponse  +user -usre -resu

# Inversion d'une chaine de caraceres avec erreur
def fonc_04(ch):
    n=len(ch)
    if n == 2:
        return ch
    else :
        return ch[n-1] + fonc_04(ch[0:n-1])

# print(fonc_04("resu"))
# Réponse +usre -resu -user

# x^n avec erreur
def fonc_05(x,n):
    if n==0:
        return 1
    else :
        return fonc_05(x,n-1)
        
#print(fonc_05(3,3))
# Reponses : +1  -0 -9 - 27


# x^n sans erreur
def fonc_06(x,n):
    if n==0:
        return 1
    else :
        return x*fonc_06(x,n-1)
        
print(">>>"+str(fonc_06(3,3)))
# Reponses : +27  -0 -9 -6 

# x^n avec erreur
def fonc_07(x,n):
    if n==0:
        return 0
    else :
        return x*fonc_07(x,n-1)
        
#print(fonc_07(3,3))
# Reponses : -27  +0 -9 -6 

 
def fonc_08(n):
    return (n+fonc_08(n-1))
    
# print(fonc_08(4))
# Reponses : -4 +Autre  -10 - 3 

def fonc_09(n):
    if n==0:
        return 0
    else :
        return (n+fonc_09(n-1))
    
#print(fonc_09(4))
# Reponses : -4 -Autre  +10 - 3



# PGCD
def fonc_10(a,b):
    if b==0:
        return a
    else:
        r=a%b
        return fonc_10(b,r)

#print(fonc_10(4))
# Reponses : + Autre -8 -4 -2 -0

# PGCD
def fonc_11(a,b):
    if b==0:
        return a
    else:
        r=a%b
        return fonc_11(b,r)

print(fonc_11(8,4))
# Reponses : - Autre -8 +4 -2 -0