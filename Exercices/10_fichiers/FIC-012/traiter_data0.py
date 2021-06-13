with open('data0.txt','r',encoding='utf8') as f:
    data0=f.readlines()

with open('data0.txt','r',encoding='utf8') as f:
    #ligne=f.readline()
    k=0
    texte=''
    ligne='o'
    while ligne!='':
        k+=1
        ligne=f.readline()
        texte+=ligne.strip('\n')
        texte+=';'
        if k==16:
            k=0
            texte+='\n'


with open('data1.csv','w',encoding='utf8') as f:
    f.write(texte)

with open('data1.csv','r',encoding='utf8') as f:
    data=f.readlines()