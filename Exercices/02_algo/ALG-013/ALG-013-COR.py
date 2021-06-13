def fonctionMystere(n) :
    if n==0 or n==1:
         return 1
    else :
        res = 1
    for i in range (2,n+1) :
        res = res * i
    return res

print('fonctionMystere(5) renvoie '+str(fonctionMystere(5))+'\n')

def fonctionMystere(n) :
    if n==0 or n==1:
         return 1
    else :
        res = 1
    for i in range (2,n+1) :
        res = res * i
        print('i='+str(i)+' res='+str(res)+'\n')
    return res

fonctionMystere(4)