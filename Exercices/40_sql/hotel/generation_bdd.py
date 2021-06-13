from sqlite3 import *
from random import *
import os


def convert(k):
    """Entier -> str avec un zéro devant"""
    if k<10:
        return '0'+str(k)
    else :
        return str(k)

def conv_time(t):
    """Convertit un temps t en seconde (depuis minuit) au format hh:mm:ss"""
    h,m = t // 3600, t % 3600
    m,s = m // 60, m % 60
    return convert(h) + ':' + convert(m) + ':' + convert(s)



def copie_bdd(nb):
    """Copie nb bdd à partir de hotel, chacune avec environ nbparties"""
    if os.path.exists('./bdd/') == False:
        os.mkdir('./bdd/')
    for i in range(nb):
        nom_de_bdd = './bdd/hotel_'+convert(i+1)+'.db'
        os.system('cp hotel.db '+ nom_de_bdd)
    return None

def supprimer_client(nom_de_bdd,id_clients):
    """supprime toutes les donnees liees à tous les id_clients contenu dans id_clients"""
    reqs=[]
    reqs.append("DELETE FROM T_CLIENT WHERE CLI_ID=")
    reqs.append("DELETE FROM T_EMAIL WHERE CLI_ID=")
    reqs.append("DELETE FROM T_TELEPHONE WHERE CLI_ID=")
    reqs.append("DELETE FROM T_ADRESSE WHERE CLI_ID=")
    reqs.append("DELETE FROM T_FACTURE WHERE CLI_ID=")
    c = connect(nom_de_bdd)
    for id_client in id_clients:
        for req in reqs:
            c.execute(req+str(id_client)+";")
    c.commit()
    c.close()

def supprimer_facture(nom_de_bdd,id_factures):
    """supprime toutes les donnees liees à tous les id_clients contenu dans id_clients"""
    reqs=[]
    reqs.append("DELETE FROM T_LIGNE_FACTURE WHERE FAC_ID=")
    reqs.append("DELETE FROM T_FACTURE WHERE FAC_ID=")
    c = connect(nom_de_bdd)
    for id_facture in id_factures:
        for req in reqs:
            c.execute(req+str(id_facture)+";")
    c.commit()
    c.close()

def generer_clients_a_effacer(i):
    if i%2==0:
        id_clients=[]
    else:
        id_clients=[22,98]
    if i%5==0:
        id_clients.append(2)
    if i%6==0:
        id_clients.append(94)
    for k in range(i//7+1):
        dec=(k+1)*11
        if i+dec==100:
            id_clients.append(i+11)
        else:
            id_clients.append((i+dec)%100)
    return id_clients


def generer_facture_a_effacer(i):
    id_factures=[]
    dec=1
    while dec+i<=2374:
        dec+=7+i//10
        id_factures.append(dec)
    return id_factures


def modifier_montant_remise(nom_de_bdd,i):
    """supprime toutes les donnees liees à tous les id_clients contenu dans id_clients"""
    req1="UPDATE T_LIGNE_FACTURE SET LIF_REMISE_POURCENT="+str(i+16)+" WHERE LIF_REMISE_POURCENT=15"
    req2="UPDATE T_LIGNE_FACTURE SET LIF_REMISE_MONTANT="+str(i+50)+" WHERE LIF_REMISE_MONTANT=50"
    c = connect(nom_de_bdd)
    c.execute(req1+";")
    c.commit()
    c.close()
    c = connect(nom_de_bdd)
    c.execute(req2+";")
    c.commit()
    c.close()


nb=99
copie_bdd(nb)

for i in range(nb):
    nom_de_bdd = './bdd/hotel_'+convert(i+1)+'.db'
    id_clients=generer_clients_a_effacer(i+0)
    id_factures=generer_facture_a_effacer(i+0)
    supprimer_client(nom_de_bdd,id_clients)
    supprimer_facture(nom_de_bdd,id_factures)
    modifier_montant_remise(nom_de_bdd,i)






# Pour créer un exemple : cree_bdd('ex.sqlite')
# Pour créer les 99 bdd du DS: cree_plein_bdd(99)
