
trame = "45000028586e400080060000c0a9faf6c72fd9ac"

def liste_16bits(t) :
    print("trame brute :",t)
    l=[]
    n=len(t)
    if n==40 :
        for i in range(0,n,4) :
            l.append(hex(int(t[i:i+4],16)))
    print("liste 16 bits :",l)
    return l

def add_16bits(a, b):
    if a+b>65535:
        return a+b-65536+1
    else :
        return a+b

def complement(s):
    chaine=bin(s)
    print(chaine)
    res=""
    for i in range(2,len(chaine)) :
        if chaine[i] == "0":
            res = res+"1"
        else :
            res=res+"0"
        #print(res)
    return int(res,2)

def checksum(t):
    s = 0
    for i in t:
        s = add_16bits(s, int(i,16))
        #print(s)
    print("somme",s)
    cs = complement(s)
    print("complement",cs)
    return cs

#l'émetteur calcul le checksum
print("Calcul checksum :")
res=hex(checksum(liste_16bits(trame)))
print("Checksum:",res)

#définition de la trame envoyée avec checksum
trame2=trame
trame2=trame2[0:20]+res[2:6]+trame2[24:40]

#le récepteur vérifie
print("")
print("Vérification :")
print("Checksum:",hex(checksum(liste_16bits(trame2))))

