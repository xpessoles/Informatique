#procedure de decryptage
def decryptage_cesar(code):
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