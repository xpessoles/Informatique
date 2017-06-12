# -*- coding: utf-8 -*-
"""
@auteur: David Fournier
"""

s = [3,4,8,11,1,5,2,7,9,0,10,0]

def scm(s):
    r = []
    d, f = 0, 0
    for i in range(len(s)-1):
        if s[i] <= s[i+1]:
            f += 1
        else:
            r.append((d,f))
            d = f = f+1
    r.append((d,f))
    return r

r = scm(s)
#print(r)

def fusionner(s, r1, r2):
    d1, f1 = r1
    d2, f2 = r2
    s1, i1 = s[d1:f1+1], 0
    s2, i2 = s[d2:f2+1], 0
    for i in range(d1,f2+1):
        if i1 > len(s1)-1:
            s[i] = s2[i2]
            i2 += 1
        elif i2 > len(s2)-1:
            s[i] = s1[i1]
            i1 += 1
        elif s1[i1] <= s2[i2]:
            s[i] = s1[i1]
            i1 += 1
        else:
            s[i] = s2[i2]
            i2 += 1

#print(s)
#fusionner(s, r[0], r[1])
#print(s)

def depileFusionneRemplace(s, pile):
    r2 = d2, f2 = pile.pop()
    r1 = d1, f1 = pile.pop()
    fusionner(s, r1, r2)
    pile.append((d1, f2))
    print("Fusion des scm:",r1,"et",r2,". Etat de la liste:",s)
    print('Etat de la pile:',pile)

#print(s)
#depileFusionneRemplace(s, r)
#print(s)

def alphaTri(s):
    print('** Première phase **')
    r = scm(s)
    pile = []
    pile.append(r[0])
    print('Etat de la pile:',pile)
    for i in range(1,len(r)):
        pile.append(r[i])
        print('Etat de la pile:',pile)
        dz, fz = pile[-1] # z
        dy, fy = pile[-2] # y
        while len(pile)>=2 and (fy-dy+1) < 2*(fz-dz+1):
            depileFusionneRemplace(s, pile)
            if len(pile)>=2:
                dz, fz = pile[-1] # z
                dy, fy = pile[-2] # y
    print('** Deuxième phase **')
    while len(pile)>=2:
        depileFusionneRemplace(s, pile)
                
print('** Découpage en scm **')
print('Liste à trier:',s)
print('Liste des scm:',scm(s))
alphaTri(s)
print("La liste triée:",s)
           
        
        
       
    
    









