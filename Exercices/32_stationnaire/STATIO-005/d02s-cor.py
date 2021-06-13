import sujet

alpha = 10

t = sujet.cree_tableau(alpha)

Q = [None] * 24
# Q1

N = len(t)
Q[1] = N

Q[2] = len([x for x in t if x >= 3000])

Q[3] = len([x for x in t if x % 3 == 0])

Q[4] = len([(i,j) for j in range(N) for i in range(j) if t[i] < t[j]])

U = [None]*10000
U[0] = 10 + alpha
for i in range(10000-1):
    U[i+1] = 15091*U[i] % 64007

Q[5] = U[42]

Q[6] = U[-1]

Q[7] = len([x for x in U if x % 17 == 0])

Q[8] = len([i for i in range(10000-1) if abs(U[i]-U[i+1]) <= 1000])

Q[9] = sum(U)

# la chaîne à chercher :

v = str(2000 + alpha)

f = open("zeta5.txt")
lignes = f.readlines()
f.close()

# lignes découpées par les espaces :
lignes_decoupees = [L.split() for L in lignes]

# paquets de 10, rangés par lignes :
#paquets10 = [ L[0:5] for L in lignes_decoupees if len(L) == 7 and L[-2]==':']
paquets10 = [ L[0:5] for L in lignes_decoupees if len(L) == 7 and L[-2]==':']

def apparait(chaine, texte):
    n = len(texte)
    p = len(chaine)
    for i in range(n-p+1):
      if texte[i:i+p] == chaine:
        return True
    return False

# paquets_contenant_chaine = [ p for L in paquets10 for p in L if apparait(v, p)]
# Q[10] = len(paquets_contenant_chaine)

# Q[11] = len([''.join(L) for L in paquets10 if apparait(v, ''.join(L))])
