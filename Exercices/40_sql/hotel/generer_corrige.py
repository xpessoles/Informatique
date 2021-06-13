from sqlite3 import *
from random import *
import os

def convv(v):
    """Convertis la valeur v en chaîne de caractère. Dans le cas d'un
       flottant, on arrondit à 3 chiffres après la virgule."""
    if isinstance(v, float):
        return "{:.3f}".format(v)
    return str(v)

def conv(v):
    """Convertis la valeur v en chaîne de caractère. Dans le cas d'un
       flottant, on arrondit à 5 chiffres après la virgule."""
    if isinstance(v, float):
        return "{:.5f}".format(v)
    return str(v)

def print_line(l):
    """Affiche les valeurs de la ligne l, séparées par des ";". """
    print(';'.join(conv(v) for v in l))

def renvoie_line(l):
    """Affiche les valeurs de la ligne l, séparées par des ";". """
    return(';'.join(conv(v) for v in l))

def convert(k):
    """Entier -> str avec un zéro devant"""
    if k<10:
        return '0'+str(k)
    else :
        return str(k)

from DS08_corrige import *
reqs=[Q1_req,Q2_req,Q3_req,Q4_req,Q5_req,Q6_req,\
Q7_req,Q8_req,Q9_req,Q10_req,Q11_req,Q12_req,\
Q13_req,Q14_req,Q15_req]

reqs_res=[Q2_req,Q5_req,Q9_req,Q10_req,Q11_req,Q15_req]
res=[Q2_res,Q5_res,Q9_res,Q10_res,Q11_res,Q15_res]
question_num=['alpha','Q2','Q5','Q9','Q10','Q11','Q15']

nb=99

texte=renvoie_line(question_num)+'\n'
for i in range(nb):
    nom_de_bdd = './bdd/hotel_'+convert(i+1)+'.db'
    c = connect(nom_de_bdd)
    for req in reqs:
        cur=c.cursor()
        cur.execute(req)
    sol=[]
    for req in reqs_res:
        cur=c.cursor()
        cur.execute(req)
        resultat=cur.fetchall()
        if len(resultat)>1:
            sol.append(resultat)
        else:
            resultat=resultat[0]
            if len(resultat)==1:
                sol.append(resultat[0])
            else:
                sol.append(resultat)
    texte+=convert(i+1)+';'+renvoie_line(sol)+'\n'

with open('DS08_responses.csv','w') as f:
    f.write(texte)









# Pour créer un exemple : cree_bdd('ex.sqlite')
# Pour créer les 99 bdd du DS: cree_plein_bdd(99)
