
n = 30

def crible(n):
    tab=[]
    for i in range(2,n):
        tab.append(i)
    for i in range(0,len(tab)):
        for j in range(len(tab)-1,i,-1):
            if (tab[j]%tab[i]==0):
                tab.remove(tab[j])
    return tab
    
            
            

import cProfile            
cProfile.run('crible(10000)')
