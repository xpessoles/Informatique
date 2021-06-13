import random

L=[]

for i in range(1,200) :
    L.append((i,random.randrange(3,4+i//2-25*(i//50))))

L1=[]

for e in L :
    for i in range(e[1]) :
        L1.append((e[0],random.randrange(e[0]+1,201)))


L = []
for e in L1:
    i,j = e
    if ( (i,j) not in L) and ( (j,i) not in L):
        L.append(e)

random.shuffle(L)
L2 = L[:len(L)//2]
L3 = L[len(L)//2:]

L4 = [e[::-1] for e in L2]
L5 = L3+L4
random.shuffle(L5)

toto = open('amis.csv','w')

for e in L5 :
    toto.write(str(e[0])+','+str(e[1])+'\n')

toto.close()
