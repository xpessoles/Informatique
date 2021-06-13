# def pgcd(m,n):
#     """
#     Retourne le PGCD de deux nombres entiers en utilisant l'algorythme d'Euclide
#     m > n
#     Keywords arguments :
#     m : nombre entier
#     n: nombre entier
#     """
#     x,y=m,n
#     r=0
#     while y!=0:
#         r = x%y
#         x=y
#         y=r
#     return x
# 
# def pgcd_python(m,n):
#     """
#     Retourne le PGCD avec "plus de style" (voirfractions.py)
#     """
#     while n:
#         m, n = n, m%n
#     return m
# 
# # Détermination du PGCD avec Python 
# from fractions import gcd
# #print(gcd(a,b))
# 




## Algorithme du rendu de monnaie
## Attention : on pourra vérifier que travailler avec des flottants n'est pas
## une bonne idée ... avec les approximations, le client peut perdre 1 centime ...

valeurs=[20,10,5,2,1,0.5,0.2,0.1,0.05,0.02,0.01]

valeurs2=[]
for v in valeurs:
    valeurs2.append(v*100)
    
valeurs=[2000, 1000, 500, 200, 100, 50, 20, 10, 5, 2, 1]

def rendre_monnaie(cout,somme_client,valeurs):
    """
    Retourne une liste nombre_billets donnant le nombre de billets ou pièce à rendre selon le type de billet ou pièce
    Keywords arguments :
    cout : somme à payer
    somme_client : argent donné par le client
    """
    nombre_billets=[0]*len(valeurs)
    montant_a_rendre = somme_client - cout
    k=0#Indice du billet dans la liste valeur
    while montant_a_rendre>0:
        nombre_billets[k]=montant_a_rendre//valeurs[k]
        montant_a_rendre-=nombre_billets[k]*valeurs[k]
        k+=1
    return nombre_billets

            
def afficher_rendu_monnaie(cout,somme_client,valeurs):
    cout=round(100*cout)
    somme_client=round(100*somme_client)
    nombre_billets=rendre_monnaie(cout,somme_client,valeurs)
    for k in range(len(nombre_billets)):
        if valeurs[k]>200:
            print(str(int(nombre_billets[k]))+' : billet de '+str(int(valeurs[k]/100))+' euros')
        elif valeurs[k]>=100:
            print(str(int(nombre_billets[k]))+' : pièce de '+str(int(valeurs[k]/100))+' euros')
        else:
            print(str(int(nombre_billets[k]))+' : pièce de '+str(int(valeurs[k]))+' centimes')

def rendre_monnaie_dico(cout,somme_client):
    """
    Retourne un dictionnaire contenant le type de billets
    ou pièces à rendre ainsi que le nombre de chacun d'entre eux
    
    Keywords arguments :
    cout : somme à payer
    somme_client : argent donné par le client
    """
    dico_monnaie={}
    montant_a_rendre = somme_client - cout
    if montant_a_rendre < 0:
        print("Le client doit ajouter au moins :"+str(montant_a_rendre*(-1)))
        return dico_monnaie 

    #Liste des différentes valeurs
    valeurs=[20,10,5,2,1,0.5,0.2,0.1,0.05,0.02,0.01]

    #Ditionnaire contenant le type de monnaie et la valeur
    dico_valeurs={}
    dico_valeurs[20]="Billet 20 euros"
    dico_valeurs[10]="Billet 10 euros"
    dico_valeurs[5]="Billet 5 euros"
    dico_valeurs[2]="Pièce 2 euros"
    dico_valeurs[1]="Pièce 1 euros"
    dico_valeurs[0.5]="Pièce 50 centimes"
    dico_valeurs[0.2]="Pièce 20 centimes"
    dico_valeurs[0.1]="Pièce 10 centimes"
    dico_valeurs[0.05]="Pièce 5 centimes"
    dico_valeurs[0.02]="Pièce 2 centimes"
    dico_valeurs[0.01]="Pièce 1 centime"

    decompte=montant_a_rendre
    for i in range(0,len(valeurs)):
        nb_billet=nb_billets(decompte,valeurs[i])
        print(valeurs[i],nb_billet)
        if nb_billets!=0:
            dico_monnaie[dico_valeurs[valeurs[i]]]=nb_billet
        decompte = decompte-nb_billet*valeurs[i]
        print(montant_a_rendre,decompte)

    for elements in dico_monnaie:
        if dico_monnaie[elements]!=0:
            print(elements+" : "+str(dico_monnaie[elements]))
    return dico_monnaie

         
def nb_billets(montant,valeur):
    """
    Calcule le nombre de billets ou de pièce à rendre pour un
    un montant donné
    Keywords arguments :
    montant : montant à payer
    valuer : valeur de la pièce ou du billet
    """
    return montant//valeur

def rendre_monnaie_entier(cout,somme_client):
    """
    On travaille ici avec des nombres entiers
    
    Retourne un dictionnaire contenant le type de billets
    ou pièces à rendre ainsi que le nombre de chacun d'entre eux
    
    Keywords arguments :
    cout : somme à payer
    somme_client : argent donné par le client
    """
    dico_monnaie={}
    montant_a_rendre = int(100*somme_client) - int(100*cout)
    if montant_a_rendre < 0:
        print("Le client doit ajouter au moins :"+str(montant_a_rendre*(-1)))
        return dico_monnaie 

    #Liste des différentes valeurs
    valeurs=[2000,1000,500,200,100,50,20,10,5,2,1]

    #Ditionnaire contenant le type de monnaie et la valeur
    dico_valeurs={}
    dico_valeurs[2000]="Billet 20 euros"
    dico_valeurs[1000]="Billet 10 euros"
    dico_valeurs[500]="Billet 5 euros"
    dico_valeurs[200]="Pièce 2 euros"
    dico_valeurs[100]="Pièce 1 euros"
    dico_valeurs[50]="Pièce 50 centimes"
    dico_valeurs[20]="Pièce 20 centimes"
    dico_valeurs[10]="Pièce 10 centimes"
    dico_valeurs[5]="Pièce 5 centimes"
    dico_valeurs[2]="Pièce 2 centimes"
    dico_valeurs[1]="Pièce 1 centime"

    decompte=montant_a_rendre
    for i in range(0,len(valeurs)):
        nb_billet=nb_billets(decompte,valeurs[i])
        #print(valeurs[i],nb_billet)
        if nb_billets!=0:
            dico_monnaie[dico_valeurs[valeurs[i]]]=nb_billet
        decompte = decompte-nb_billet*valeurs[i]
        #print(montant_a_rendre,decompte)

    for elements in dico_monnaie:
        if dico_monnaie[elements]!=0:
            print(elements+" : "+str(dico_monnaie[elements]))
    return dico_monnaie



# rendre_monnaie_dico(23.32,30)
# print()
# rendre_monnaie_entier(23.32,30)


afficher_rendu_monnaie(15.99,17.5,valeurs)





    