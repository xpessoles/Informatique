#Programme principal
#definition des chaines de caracteres
mess="la metamorphose"
alphabet="abcdefghijklmnopqrstuvwxyz"
code=""


def decalage(c,n):
    ind=alphabet.index(c)
    return alphabet[(ind+n)%26]

def chiffrement_cesar(mess,n):
    code=""
    for i in range(len(mess)):
        if mess[i].isalpha():
            ind=alphabet.index(mess[i])
            newind=(ind+n)%26
            code=code+decalage(mess[i],n)
        else:
            code=code+mess[i]
    return code

def decryptage_cesar(code):
    for n in range(len(alphabet)):
        decrypt_mess=""
        for i in range(len(code)):
            if code[i].isalpha():
                decrypt_mess+=decalage(code[i],-n)
            else:
                decrypt_mess+=code[i]
        print(decrypt_mess," avec n= ",n)
    return None

def decryptage_cesar0(code):
    for n in range(26):
        decrypt_mess=""
        for i in range(len(code)):
            if code[i].isalpha():
                ind=alphabet.index(code[i])
                newind=(ind-n)%26
                decrypt_mess=decrypt_mess+alphabet[newind]
            else:
                decrypt_mess=decrypt_mess+code[i]
        print(decrypt_mess," avec n= ",n)


def cryptage_cesar(mess,n):
    code=""
    for i in range(len(mess)):
        if mess[i].isalpha():
            ind=alphabet.index(mess[i])
            newind=(ind+n)%26
            code=code+alphabet[newind]
        else:
            code=code+mess[i]
    return code