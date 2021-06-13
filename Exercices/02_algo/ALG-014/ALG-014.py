def fonction(x) :
    y=1.1
    i=0
    while x!=y and i <10:
        x=x+0.1
        i=i+1
        print('i='+str(i)+' x='+str(round(x*100)/100)+'\n')
        # print('i='+str(i)+' x='+str(x)+'\n')
    return i

fonction(0.1)

fonction(0.3)