### version PT
### tri insertion
def tri_insertion(tab):
    for p in range(1,len(tab)):
        x=tab[p]
        k=0
        while k<p and x>tab[k]:
            k=k+1
        for i in range(p,k,-1):
            tab[i]=tab[i-1]
        tab[k]=x
        
        
### tri rapide
def tri_rap(tab):
    if len(tab)<2:
        return (tab)
    else:
        x=tab[-1]
        a=[]
        b=[]
        for i in range(0,len(tab)-1):
            if tab[i]<x:
                a.append(tab[i])
            else:
                b.append(tab[i])
        return (tri_rap(a)+[x]+tri_rap(b))
        
        
### tri fusion
def placer(tab,p,x):
    k=p
    while k<len(tab) and x>tab[k]:
        k=k+1
    tab.insert(k,x)
    return (k)
    
def fusion(a,b):
    p=0
    for x in a:
        p=placer(b,p,x)+1
    return (b)
    
def tri_fus(tab):
    if len(tab)<2:
        return (tab)
    else:
        m=len(tab)//2
        return fusion(tri_fus(tab[:m]),tri_fus(tab[m:]))
        
        
        
        
        
        
        