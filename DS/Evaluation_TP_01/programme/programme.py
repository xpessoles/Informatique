"""tab = [17, 38, 10, 25, 72, 4, 98, 32, 11]
print (tab)

N = len (tab)
tampon = tab [N - 1]
for i in range (0, N - 1, 1) :
    tab [N - 1 - i] = tab [N - 2 - i]
tab [0] = tampon
print (tab)

tab = [17, 38, 10, 25, 72, 4, 98, 32, 11]
N = len (tab)
tampon = tab [0]
for i in range (1, N) :
    if tab [i] > tampon :
        tampon=tab[i]
print (tampon)
"""

def recherche(mot,texte):
    nb_mot=0
    for i in range(0,len(texte)):
        if texte[i]==mot[0]:
            j=0
            while j!=len(mot):
                if (i+j)>=len(texte):
                    return nb_mot
                elif texte[i+j]!=mot[j]:
                    break
                j=j+1
            if j==len(mot):
                nb_mot+=1
    return nb_mot

texte = "abcabcabcabcabcabc"
mot="abc"
print(recherche(mot,texte))
