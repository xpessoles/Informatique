from tri import *
import time as t
import matplotlib.pyplot as plt


def chargeClassement(fichier):
    f=open(fichier,'r',encoding='utf8')
    fichier=f.readlines()
    f.close() #ne pas oublier de fermer le fichier...
    L=[]
    for ligne in fichier:
        ligne=ligne.split('\t') # coupe aux tabulations
        L1=[]
        L1.append(ligne[1])
        L1.append(ligne[2])
        L1.append(ligne[4])
        L.append(L1)
    return L


def convertirTemps(temps:str):
    '''temps est un str de la forme "06h 09' 39''" '''
    t_course=temps.split('h') #on peut aussi couper à h
    #print (t_course)
    heure=int(t_course[0])
    t_course2=t_course[1].split("'")
    #print (t_course2)
    duree=int(t_course2[1])+60*int(t_course2[0])+3600*heure
    return duree



def classement(fichier):
    L=chargeClassement(fichier)
    for element in L:
        element[2]=convertirTemps(element[2])
    return L

LG=classement('classement_general.txt')
L18=classement('etape_18.txt')


#Q4
def ajoutTemps(liste1:list,liste2:list)->list:
    LGN=[]
    for x in liste1:
        for y in liste2:
            if x[1]==y[1]:
                LGN+=[[x[0],x[1],y[2]+x[2]]]
    return LGN

#Q5
####Tri par insertion modifié
def tri_insertion_modifie(T):
    n=len(T)
    for i in range(1,n):
        j=i
        v=T[i][-1]
        v2=T[i]
        while j>0 and v<T[j-1][-1]:
            T[j]=T[j-1]
            j=j-1
        T[j]=v2
    return T

####Tri rapide modifié
def partition_modifie(a,g,d):
    assert g<d
    v=a[g][-1]
    v2=a[g]
    ainf=[]
    asup=[]
    for x in a[g+1:d]:
        if x[-1]<=v:
            ainf.append(x)
        else:
            asup.append(x)
    a=a[0:g]+ainf+[v2]+asup+a[d:len(a)]
    m=len(ainf)+g
    return m,a



def tri_rapide_modifie(a,g,d):
    if g>=d-1:
        return
    else:
        m,a=partition_modifie(a,g,d)
        tri_rapide_modifie(a,g,m)
        tri_rapide_modifie(a,m+1,d)

####Tri par fusion modifié
def fusion_modifie(a0,a,g,m,d):
    i,j=g,m
    for k in range(g,d):
        if i<m and (j==d or a0[i][-1]<=a0[j][-1]):
            a[k]=a0[i]
            i=i+1
        else:
            a[k]=a0[j]
            j=j+1


def tri_fusion_modifie(a,g,d):
    a0=a[:]
    if g>=d-1:
        return
    else:
        m=(g+d)//2
        tri_fusion_modifie(a,g,m)
        tri_fusion_modifie(a,m,d)
        a0[g:d]=a[g:d]
        fusion_modifie(a0,a,g,m,d)





def test_tri_modifie1():
    LGN=ajoutTemps(LG,L18)
    LGN0=LGN[:]
    LGN=sorted(LGN,key=lambda colonnes:colonnes[2])
    LGN1=tri_insertion_modifie(LGN0)
    print(LGN[0:6],'\n\n',LGN1[0:6])
    assert LGN==LGN1


def test_tri_modifie2():
    LGN=ajoutTemps(LG,L18)
    LGN1=LGN[:]
    LGN=sorted(LGN,key=lambda colonnes:colonnes[2])
    tri_fusion_modifie(LGN1,0,len(LGN1))
    print(LGN[0:6],'\n\n',LGN1[0:6])
    assert LGN==LGN1

def test_tri_modifie3():
    LGN=ajoutTemps(LG,L18)
    LGN1=LGN[:]
    LGN=sorted(LGN,key=lambda colonnes:colonnes[2])
    tri_rapide_modifie(LGN1,0,len(LGN1))
    print(LGN[0:6],'\n\n',LGN1[0:6],'\n\n',ajoutTemps(LG,L18)[0:6])
    assert LGN==LGN1




def update_classement_general(liste1:list,liste2:list)->list:
    LGN=ajoutTemps(LG,L18)
    sorted(LGN,key=lambda colonnes:colonnes[2])
    return LGN






#LGN=update_classement_general(LG,L18)


####Comparaison des temps de calcul
def comparer_tri(LGN,nom_de_fichier):
    temps_insertion=[]
    temps_rapide=[]
    temps_fusion=[]
    temps_sorted=[]
    liste_k=[]
    for k in range(2,len(LGN),100):
        liste_k.append(k)
        LGT1=LGN[:k+1]
        LGT2=LGN[:k+1]
        LGT3=LGN[:k+1]
        LGT4=LGN[:k+1]
        tic=t.time()
        tri_fusion(LGT1,0,len(LGT1))
        toc=t.time()
        temps_fusion.append(toc-tic)
        tic=t.time()
        tri_insertion(LGT2)
        toc=t.time()
        temps_insertion.append(toc-tic)
        tic=t.time()
        tri_rapide(LGT3,0,len(LGT3))
        toc=t.time()
        temps_rapide.append(toc-tic)
        tic=t.time()
        sorted(LGT4)
        toc=t.time()
        temps_sorted.append(toc-tic)

    plt.clf()
    #pdb.set_trace()
    plt.plot(liste_k,temps_fusion,'g-',label='fusion')
    plt.plot(liste_k,temps_rapide,'b*-',label='rapide')
    plt.plot(liste_k,temps_insertion,'r--',label='insertion')
    plt.plot(liste_k,temps_sorted,'k.-',label='sorted')
    plt.legend()
    plt.savefig(nom_de_fichier)



def comparer_tri_liste(LGN,nom_de_fichier):
    temps_insertion=[]
    temps_rapide=[]
    temps_fusion=[]
    temps_sorted=[]
    for k in range(2,len(LGN)):
        LGT1=LGN[:k+1]
        LGT2=LGN[:k+1]
        LGT3=LGN[:k+1]
        LGT4=LGN[:k+1]
        tic=t.time()
        tri_fusion_modifie(LGT1,0,len(LGT1))
        toc=t.time()
        temps_fusion.append(toc-tic)
        tic=t.time()
        tri_insertion_modifie(LGT2)
        toc=t.time()
        temps_insertion.append(toc-tic)
        tic=t.time()
        tri_rapide_modifie(LGT3,0,len(LGT3))
        toc=t.time()
        temps_rapide.append(toc-tic)
        tic=t.time()
        sorted(LGT4,key=lambda colonnes:colonnes[2])
        toc=t.time()
        temps_sorted.append(toc-tic)

    plt.clf()
    plt.plot(list(range(2,len(LGN))),temps_fusion,'g-',label='fusion')
    plt.plot(list(range(2,len(LGN))),temps_rapide,'b*-',label='rapide')
    plt.plot(list(range(2,len(LGN))),temps_insertion,'r--',label='insertion')
    plt.plot(list(range(2,len(LGN))),temps_sorted,'k.-',label='sorted')
    plt.legend()
    plt.savefig(nom_de_fichier)

LGN=update_classement_general(LG,L18)
comparer_tri_liste(LGN,'tp09_durif_compare_tri1.png')


import random
def generer_liste(n,N):
    x = [random.randint(0, n) for p in range(0, N)]
    return(x)

N=int(1e3)
# for k in range(1,N,100):
#     L=generer_liste(N,N)

L=generer_liste(N,N)
comparer_tri(L,'tp09_durif_compare_tri2.png')






