###Exo Banque PT
# Lucie Bathie

##Exo 12: vecteur creux

v = [1,2,0,4,7,0,0,0,0]

def creux(v):
    """renvoie True si le vecteur est creux, false sinon"""
    nombre_zeros = 0
    for k in range(len(v)):
        if v[k] == 0:
            nombre_zeros +=1
    return(nombre_zeros >= (len(v)-nombre_zeros)/2)

#print(creux(v))
#True

#2.
def coder(v):
    code = [len(v)]
    indices = []
    valeurs = []
    for k in range(len(v)):
        if v[k] != 0:
            indices.append(k)
            valeurs.append(v[k])
    code.append(valeurs)
    code.append(indices)
    return(code)

#print(coder(v))
#[9, [1, 2, 4, 7], [0, 1, 3, 4]]

#3.

def decoder(code):
    """permet de décoder un codage creux"""
    v=[0]*code[0]
    for k in range(len(code[2])):
        v[code[2][k]] = code[1][k]
    return(v)

code1=[9,[1,2,4,7],[0,1,3,4]]
##print(decoder(code1))
##[1, 2, 0, 4, 7, 0, 0, 0, 0]

#4.
def simul(C,a):
    """C  codage de v
renvoie le codage de av"""
    v = decoder (C)
    for k in range(len(v)):
        v[k] = a*v[k]
    return(coder(v))

#print(simul(code1,2))
#[9, [2, 4, 8, 14], [0, 1, 3, 4]]

def coefficient(j,C):
    vecteur = decoder(C)
    return(vecteur[j])

#print(coefficient(1,code1))
#2
