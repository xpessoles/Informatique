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
