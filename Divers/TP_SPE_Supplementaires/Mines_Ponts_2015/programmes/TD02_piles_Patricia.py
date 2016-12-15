### TD02 - piles
# question 1 : fonction est_vide
def est_vide(pile):
    return len(pile)==0
    
# >>> est_vide((1,2,3))
# False
# >>> est_vide(())
# True   

# question 2 : fonction est pleine
def est_pleine(pile,nb):
    return len(pile)==nb
    
# >>> est_pleine((1,2,3),3)
# True
# >>> est_pleine((1,2,3),6)
# False

# question 3 : ajouter un element (un peu tiré par les cheveux)
def push(pile,el):
    pile=pile+(el,0)#je ne peux pas concatener un tuple avec un seul élément, minimum 2
    pile=pile[:-1]
    return(pile)
    
# >>> push((1,2,3),(94))
# (1, 2, 3, 94)

def pop(pile):
    dernier=pile[-1]
    pile=pile[:-1] #je n'arrive pas à changer le tuple qui est non mutable
    return dernier,pile
    
# >>> pop((1,2,3,4,5))
# 5
# >>> pop((1,2,3,4,5))
# (5, (1, 2, 3, 4))

### Exercice 2 : notation polonaise inversee
# est-ce un element au hasard ?
# la pile est un tuple de strings
def est_nombre(pile,i):
    return pile[i] not in ['+','-','*','/']
    
# >>> est_nombre(('+','1','3','*'),1)
# True  

def est_operation(pile,i):
    return pile[i] in ['+','-','*','/']
    
# >>> est_operation(('+','1','3','*'),0)
# True
# >>> est_operation(('+','1','3','*'),1)
# False


def evaluer(exp):
    ''' l'expression exp doit être postfixée '''
    pile=()
    for element in exp:
        pile=push(pile,element)
#     return pile resultat OK
    res=()
    for elt in pile:
        if elt == '+':
            b = float(pop(res)[0])
            res=pop(res)[1]
            a=float(pop(res)[0])
            res=pop(res)[1]
            res=push(res,(a+b))
        elif elt == '*':
            b = float(pop(res)[0])
            res=pop(res)[1]
            a=float(pop(res)[0])
            res=pop(res)[1]
            res=push(res,(a*b))
        elif elt == '-':
            b = float(pop(res)[0])
            res=pop(res)[1]
            a=float(pop(res)[0])
            res=pop(res)[1]
            res=push(res,(a-b))
        elif elt == '/':
            b = float(pop(res)[0])
            res=pop(res)[1]
            a=float(pop(res)[0])
            res=pop(res)[1]
            res=push(res,(a/b))
        else:
            res=push(res,(float(elt)))
    return res[0]
    
# NE fonctionne pas

# Question 4 : '12+4*3-5+'

### Exercice 3 - croisement routier
#creation de listes aléatoires
import random as rd
f1=[rd.randint(0,1) for i in range(10)]
f2=[rd.randint(0,1) for i in range(8)]

def croisement(f1,f2):
    f3=[]
    while len(f1)!=0 and len(f2)!=0:
        if f1[-1]==1: # si un véhicule dans la file 1 il est prioritaire
            f3.append(1) # la file 3 reçoit le véhicule de la file 1
            f1.pop() #la file 1 est dépilée
            if f2[-1]==0:
                f2.pop() #si pas de voiture sur la file 2 du stop avancer d'un véhicule
        else: # si pas de véhicule sur la file 1 dépiler la file 2
            if f2[-1]==1: 
                f3.append(1)
                f1.pop()
                f2.pop()
            else:
                f3.append(0)
                f1.pop()
                f2.pop()
    if len(f1)!=0: #quand une file est vide les véhicules de la file suivant ese vide dans file 3
        for i in range(len(f1)):
            f3.append(f1.pop())
    else:
        for i in range(len(f2)):
            f3.append(f2.pop())
    f3.reverse() #inverser la file 3 pour avoir les véhicules dans l'ordre d'arrivée
    return f3
    
# >>> croisement([0, 1, 1, 0, 0, 1, 1, 0, 1, 1],[0, 1, 0, 1, 1, 1, 1, 0])
# [0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
        
    
    
    
