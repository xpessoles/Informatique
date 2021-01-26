###Exo Banque PT
# Lucie Bathie

##Exo 10: palindrome
#1.
def inverse(mot):
    """renvoie la chaine de caractères écrite à l'envers"""
    liste = []
    for k in range(len(mot)):
        liste.append(mot[k])
    inverse = ''
    for i in range(1,len(liste)+1):
        inverse = inverse + liste[-i]
    return(inverse)

#print(inverse('bonjour'))
#ruojnob

#2.

def palindrome(mot):
    return(inverse(mot)==mot)

#print(palindrome('kayak'))
#True
#print(palindrome('bonjour'))
#False

#3.
def pat_nombre(N):
    """renvoie la liste de palindromes inférieurs ou égaux à N"""
    L =[]
    for n in range(N+1):
        if palindrome(str(n)) == True:
            L.append(n)
    return(L)

#print(pat_nombre(100))
#[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 22, 33, 44, 55, 66, 77, 88, 99]
