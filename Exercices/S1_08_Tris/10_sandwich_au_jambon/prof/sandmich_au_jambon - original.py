# -*- coding: utf-8 -*-
"""
@auteur: David
"""

######################################################
print('\n'+'Réponse 1 : calculIndiceMaximum(tab,a,b)')
######################################################

# David
def calculIndiceMaximum(tab,a,b):
    for indice, valeur in enumerate(tab[a-1:b]):
        if valeur == max(tab[a-1:b]):
            return a-1+indice+1

exemple = [3,2,5,8,1,34,21,6,9,14,8]
print(exemple)

resultat = calculIndiceMaximum(exemple,1,11)
print(str(resultat)+' --> '+str(exemple[resultat-1]))
# doit retourner 6
resultat = calculIndiceMaximum(exemple,3,9)
print(str(resultat)+' --> '+str(exemple[resultat-1]))
# doit retourner 6

######################################################
print('\n'+'Réponse 2 : nombrePlusPetit(tab,a,b,val)')
######################################################

def nombrePlusPetit(tab,a,b,val):
    compteur = 0
    for valeur in tab[a-1:b]:
        if valeur <= val:
            compteur += 1
    return compteur

exemple = [3,2,5,8,1,34,21,6,9,14,8]
print(exemple)

resultat = nombrePlusPetit(exemple,1,11,8)
print(str(resultat))
# doit retourner 7
resultat = nombrePlusPetit(exemple,3,9,8)
print(str(resultat))
# doit retourner 3

########################################################
print('\n'+'Réponse 3 : partition(tab,a,b,indicePivot)')
########################################################

def partition(tab,a,b,indicePivot):
    assert indicePivot >= a or indicePivot <= b
    tab1 = []; tab2 = []; tab3 = []; pivot = tab[indicePivot-1]
    tabini = tab[:a-1]; tabfin = tab[b:]
    for valeur in tab[a-1:b]:
        if    valeur <  pivot: tab1.append(valeur)
        elif  valeur == pivot: tab2.append(valeur)
        else                 : tab3.append(valeur)
    del(tab[:])
    for valeur in tabini + tab1 + tab2 + tab3 + tabfin:
        tab.append(valeur)
    return a-1+len(tab1)+1

exemple = [3,2,5,8,1,34,21,6,9,14,8]
print(exemple)

exemple = [3,2,5,8,1,34,21,6,9,14,8]
print(partition(exemple,1,11,4))
print(exemple)
# doit retourner 6 car [6, 1, 5, 2, 3, 8, 8, 14, 9, 21, 34]
exemple = [3,2,5,8,1,34,21,6,9,14,8]
print(partition(exemple,3,9,4))
print(exemple)
# doit retourner 6 car [3, 2, 5, 1, 6, 8, 34, 21, 9, 14, 8]


#############################################
print('\n'+'Réponse 4 : elementK(tab,a,b,k)')
#############################################

def elementK(tab,a,b,k):
    if k==1 and a==b: return tab[a-1]
    else:
        i = partition(tab,a,b,a)
        if i-a+1 >  k: return elementK(tab,a,i-1,k)
        if i-a+1 == k: return tab[i-1]
        if i-a+1 <  k: return elementK(tab,i+1,b,k-i+a-1)

exemple = [3,2,5,8,1,34,21,6,9,14,8]
print(exemple)

exemple = [3,2,5,8,1,34,21,6,9,14,8]
print(elementK(exemple,1,11,4))
print(exemple)
# doit retourner 5 car [1,2,3,5,6,8,8,9,14,21,34]
exemple = [3,2,5,8,1,34,21,6,9,14,8]
print(elementK(exemple,3,9,4))
print(exemple)
# doit retourner 8 car [3,2, 1,5,6,8,9,21,34 ,14,8]
# Selon moi, cela devrait plutôt retourner 5 pour ne pas être en relatif

#############################################
print('\n'+'Réponse 6 : ChoixPivot(tab,a,b)')
#############################################






