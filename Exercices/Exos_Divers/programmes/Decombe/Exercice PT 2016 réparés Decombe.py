import numpy as np
import random as rd
import matplotlib.pyplot as plt

###### Exercice 1 ######
## 1 ##
def mots(n):
    L=[]
    for i in range(n):
        L1=[0]*n
        L1[i]=1
        L.append(L1)
    return(L)
#print(mots(4)) [[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 1, 0], [0, 0, 0, 1]]
        
## 2 ##
def bon_mot(mot):
    i=0
    x= False
    while i < len(mot)-1 and x == False:
        m=mot[i]
        n=mot[i+1]
        if m==n:
            x=True
            return(x)
        else:
            i+=1
            print(i)
    return(x)
    
##print(bon_mot([0,1,2,3,5,1,1]))    #True
##print(bon_mot([1,3,2,3,5]))        #False

###### Exercice 2 ######

## 1 ##
zo=2 + 1j
def zn1(zn):
    return((zn+abs(zn))/2)

#print(zn1(zo))
z=zo
for i in range(12):
    z=zn1(z)
    
#print(z)  2.1568104230797602+0.000244140625j)
    
## 2 ##
    
def les_zn(zo,n):
    L=[zo]
    z=zo
    for i in range(n):
        L.append(zn1(z))
        z=zn1(z)
    return(L)
#print(les_zn(2+1j,2))

# [(2+1j), (2.118033988749895+0.5j), (2.1471424441163585+0.25j)]



###### Exercice 4 ######

## 1 ##
def pol(L,x):
    s=0
    for i in range(len(L)-1,-1,-1): # pas de -1 pour parcourir le range à l'envers
        s+=L[(len(L)-1)-i]*(x**i)
   
    return(s)

# print(pol([1,2,1],-2))  #1 bien égal à (-2)²+2*(-2)+1


## 2 ##

M=np.array([[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]])
# print(M)
# [[0 0 0 0]
#  [0 0 0 0]
#  [0 0 0 0]
#  [0 0 0 0]]

## 3 ##
# ici la relation de récurrence est bk+1 = bk**2 + I4
I4=np.array([[1,0,0,0],[0,1,0,0],[0,0,1,0],[0,0,0,1]])
def Bk(M,k):
    M1=np.copy(M)
    for i in range(k):
        M1=M1*M1 + I4
    return(M1)
# print(Bk(M,4))
# [[26  0  0  0]
#  [ 0 26  0  0]
#  [ 0  0 26  0]
#  [ 0  0  0 26]]
        
######## Exercice 5 ######
## 1 ##
def divise(n):
    L=[]
    i=1
    while i*i<=n:
        if n%i==0:
            L.append(i)
        i+=1
    return(L)

#print(divise(100)) [1, 2, 4, 5, 10]
    
## 2 ##
def est_premier(n):
    return((len(divise(n))==1))
##print(est_premier(27))    False
##print(est_premier(25))    False
##print(est_premier(41))    True

## 3 ##
def nbp(n):
    i=0
    for j in range(2,n+1):
        if est_premier(j)==True:
            i+=1
    return(i)
# print(nbp(25))
# 9 cela correspond(2, 3, 5, 7, 11, 13, 17, 19, 23)


###### Exercice 6 ######

## 1 ##
def h(t):
    if t>0:
        return(1)
    else:
        return(0)
    
def ro(t):
    return(np.sqrt(h(np.cos(2*t))*np.cos(2*t)))

    
## 2 ##
def pts(n):
    les_xy=[]
    les_ti=np.linspace(0,2*np.pi,n+1)
    for t in les_ti:
        les_xy.append((ro(t)*np.cos(t),ro(t)*np.sin(t)))
    return(les_xy)
# print(pts(2))
# [(1.0, 0.0), (-1.0, 1.2246467991473532e-16), (1.0, -2.4492935982947064e-16)]

les_x1=[]
les_y1=[]
les_x2=[]
les_y2=[]

for i in range(len(pts(50))):
    les_x1.append(pts(50)[i][0])
    les_y1.append(pts(50)[i][1])

for i in range(len(pts(1000))):
    les_x2.append(pts(1000)[i][0])
    les_y2.append(pts(1000)[i][1])

#plt.plot(les_x1,les_y1,label=' n = 50 ')
#plt.plot(les_x2,les_y2,label=' n = 1000 ')
#plt.legend()
#plt.savefig('courbe_exo_6')
#plt.show()

## 3 ##
def longueur(L):
    l=0
    for i in range(len(L)-1):
        l=l+np.sqrt((L[i+1][1]-L[i][1])**2+(L[i+1][0]-L[i][0])**2)
    return(l)

## print(longueur(pts(50)))              5.21854299262

## print(longueur(pts(1000)))            5.24403702161



######## Exercice 7 ########
## 1 ##
def trec(n):
    if n==0:
        return(0)
    elif n == 1:
        return(1-trec(0))
    elif n%2==0:
        j=n-2
        return(trec(j))
    else:
        j=n-2
        return(1-trec(j))

##print(trec(0)) 0
##print(trec(4)) 0
##print(trec(5)) 1

## 2 ##
def mot(n):
    m=''
    for i in range(n):
        m+=str(trec(i))
    return(m)
#print(mot(10))

## 3 ##

def nbseq(n,seq):
    l=len(seq)
    nb=0
    for i in range(n-l+1):
        if seq==mot(n)[i:i+l]:
            nb+=1
    return(nb)

## 4 ##
# attention a ne pas trop augmenter la valeur de n, l'algorithme recursif plante
#print(nbseq(1000,'0')/1000)       #0.75
#print(nbseq(1000,'1')/1000)       #0.25
#print(nbseq(1000,'01')/1000)      #0.25
#print(nbseq(1000,'10'))           #0.25
#print(nbseq(1000,'010')/1000)     #0.25
#trop de temps de calcul les autres ne sont pas fait

######## Exercice 8 ########

## 1 ##
f=open('pi.txt','r')
les_lignes=f.readlines()
deci=les_lignes[0]
f.close()

## 2 ##
#print(deci[:10])     1415926535
#print(len(deci))      50

## 3 ##
def tirer(n,C,p):
    l=[]
    N=len(C)
    for i in range(n):
        if p+i<N:
            l.append(C[p+i])
        else:
            l.append(C[p+i-N-1])
    return(l)
                
# print(tirer(5,deci,48))
# ['1', '0', '0', '1', '4']

###### Exercice 10 ######
valeurs=["7","8","9","10","V","D","R","A"]
couleurs=["trefle","coeur","carreau","pique"]

## 1 ##

jeu=[]
for val in valeurs:
    for cou in couleurs:
        jeu.append([val,cou])
#print(jeu)
        
## 2 ##
        
def tirermain():
    rand=[]
    while len(rand)<5:
        if rd.randint(0,31) not in rand:
            rand.append(rd.randint(0,31))
    main=[jeu[x] for x in rand]
    return(main)

#print(tirermain())
main1=[['R', 'trefle'], ['9', 'coeur'], ['8', 'carreau'], ['9', 'pique'], ['7', 'pique']]

    
## 3 ##

import numpy as np
def LV(main):
    l=[0,0,0,0,0,0,0,0]
    for x in main:
        for i in range(8):
            if x[0]==valeurs[i]:
                l[i]=l[i]+1
    l1=[]
    for i in range(7):
        if l[i]!=0:
            l1.append(l[i])
    
    return(l1)
# print(LV(tirermain()))
# [1, 1, 2, 1]       [1, 1, 1, 1, 1]     [2,3]

## 4 ##
def probabrelan(n):
    p=0
    for i in range(n):
        var=False
        for x in LV(tirermain()):
            if x>=3:
                var=True
        if var == True:
            p+=1
    return(p/n)
    

def probapaire(n):
    p=0
    for i in range(n):
        var=False
        for x in LV(tirermain()):
            if x>=2:
                var=True
        if var == True:
            p+=1
    return(p/n)
    
def probacarre(n):
    p=0
    for i in range(n):
        var=False
        for x in LV(tirermain()):
            if x>=4:
                var=True
        if var == True:
            p+=1
    return(p/n)


######## Exercice 11 ########

## 1 ##

def bin(d):
    i=0
    m=1
    while d>m:
        m=m*2
        i+=1
    return(i)

#print(bin(31))     5
#print(bin(3))      2

## 2 ##

def f(a):
    n=bin(a)
    return(a**(n+1)-2**(n+1))

#print(f(1))      -1
#print(f(2))       0


## 3 ##

def les_un(n,uo):
    l=[uo]
    for i in range(n):
        l.append(f(l[i]))
    return(l)

#print(les_un(3,1))     [1, -1, -3, -5]4


######## Exercice 12 ########



## 1 ##


def listes1(n):
    l=[]
    nb=2**n
    for i in range(0,nb):
        
        l1=[int(bin(i)[j]) for j in range(2,len(bin(i)))]
        l2=l1[:]
        while len(l2)<n:
            l2=[0]+l2
        l3=l2[:]
        for i in range(len(l2)):
            if l2[i] == 0:
                l3[i]=-1
        l.append(l3)
    return(l)

# il y a 2**n combinaison possible , on utilise l'ecriture en binaire de tout
# les nombres de 1 a 2**n en remplacant les 0 par des -1 et on obtient toutes
# les listes possibles


######## Exercice 13 ########

## 1 ##

def inversé(n):
    l=[]
    i=1
    while n >10:
        l.append(n%10)
        n=n//10
    l.append(n)
    #l contient les chiffres du nombre n dans l'ordre inverse [8, 7, 6, 5, 2, 1]
    s=0
    for i in range(len(l)):
        s+=l[i]*10**(len(l)-i-1)
    # s contient le nombre inversé
    return(s)

# print(inversé(125678))                   876521

## 2 ##

def palindrome(n):
    return(n==inversé(n))

#print(palindrome(121))   True
#print(palindrome(1212))  False

     
## 3 ##

def palindromes(n):
    l=[]
    for i in range(n+1):
        if palindrome(i) == True:
            l.append(i)
    return(l)

# print(palindromes(111))
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 22, 33, 44, 55, 66, 77, 88, 99, 111]

## 4 ##

l=[]
def inversérec(n):
    if n<10:
        l.append(n)
        s=0
        for i in range(len(l)):
            s+=l[i]*10**(len(l)-i-1)
        return(s)
    else:
        l.append(n%10)
        return(inversérec(n//10))

# print(inversérec(124))  421    
# De même mais on crée la liste de facon récursive, meme méthode pour finir

######## Exercice 14 ########

## 1 ##
import random as rd
def bonbonmang(n1,n2):
    bonbon=0
    while n1 >0 and n2 > 0 :
        poche=rd.randint(0,1)
        if poche==0:
            n1=n1-1
            bonbon+=1
        else:
            n2=n2-1
            bonbon+=1
    boitevide=1
    if n2==0:
        boitevide=2
    return(bonbon,boitevide)

# print(bonbonmang(5,5))
# (7,a)=(bonbons mangés , poche 1 vide)
# evolution (na,nb) : (5,4) (4,4) (3,4) (3,3) (3,2) (3,1) (3,0)

## 2 ##

def probamangé(na,nb,n):
    l=[0]*(na+nb)
    l2=[0,0]
    for i in range(n):
        l[bonbonmang(na,nb)[0]-1]+=1
        if bonbonmang(na,nb)[1]==1:
            l2[0]+=1
        else:
            l2[1]+=1
            
    for i in range(len(l)):
        l[i]=(l[i]/n)*100
    l2[0]=(l2[0]/n)*100
    l2[1]=(l2[1]/n)*100
    
    return(l2,l)

# print(probamangé(5,5,100)) renvoie deux listes : la preimiere donne les proba
# que les poche 1 puis 2 soient vides; la deuxieme liste donne la proba de chaque
# nombre de bonbon mangé de 1 a na+nb 
    

