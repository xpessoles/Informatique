from copy import *
def Carre_vide(n):
    if n%2==0:
        print("Erreur n doit être impair")
        return None
    else:
        carre=[]
        for i in range(n):
            carre.append([0]*n)
        return carre

def Remplir_carre(carre):
    n=len(carre)
    carre_magique=deepcopy(carre)
    x,y=(n-1)//2-1,(n-1)//2
    for i in range(1,n**2+1):
        carre_magique[y][x]=i
        print(carre_magique)
        if i%(n)==0:
            x=(x-2)%n
        else:
            x,y=(x-1)%n,(y-1)%n
    return carre_magique

def Verif_carre(carre_magique):
    n=len(carre)
    dens=int(n*(n**2 + 1)/2)
    for i in range(n):
        d1=0
        d2=0
        for j in range(n):
            d1+=carre_magique[j][i]
            d2+=carre_magique[i][j]
        if d1!=dens or d2!=dens:
            return False
    d1=0
    d2=0
    for i in range(n):
        d1+=carre_magique[i][i]
        d2+=carre_magique[n-1-i][i]
    if d1!=dens or d2!=dens:
        return False
    return True


n=5
carre=Carre_vide(n)
print(carre)
carre_magique=Remplir_carre(carre)
print(carre_magique)
Bool=Verif_carre(carre_magique)
print(Bool)
