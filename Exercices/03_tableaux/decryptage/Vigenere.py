global alphabet,N,cle,L
alphabet= "abcdefghijklmnopqrstuvwxyz"
N=len(alphabet)
cle="roue"
L=len(cle)


def code_vigenere(ch):
    code=""
    for i in range(len(ch)):
        d=i
        while d>L-1:
            d=d-L
        index=alphabet.index(ch[i])+alphabet.index(cle[d])
        if index>N-1:
            index=index-N
        j=alphabet[index]
        code=code+j
    return code
    
def decode_vigenere(ch):
    decode=""
    for i in range(len(ch)):
        d=i
        while d>L-1:
            d=d-L
        index=alphabet.index(ch[i])-alphabet.index(cle[d])
        if index<0:
            index=index+N
        j=alphabet[index]
        decode=decode+j
    return(decode)
        
c1=code_vigenere("anticonstitutionnellement")
print(c1)
c2=decode_vigenere(c1)
print(c2)