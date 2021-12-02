L=[-3,5,7,10,11,14,17,21,30]

def dichotomie(x0,L):
    g=0
    d=len(L)-1
    m=(g+d)//2
    print(g,d,m,L[m]<x0,L[m]==x0)
    while g<=d:
        if L[m]==x0:
            return True
        elif L[m]<x0:
            g=m+1
        else:
            d=m-1
        m=(g+d)//2
        print(g,d,m,L[m]<x0,L[m]==x0)
    return False
