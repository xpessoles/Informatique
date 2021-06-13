from sqlite3 import *
from random import *

def cree_bdd_vide(nom_de_bdd,script_creation = "cree_table.sql"):
    """Crée une base de donnée vide avec la structure"""
    with open(script_creation,"r") as f:
        r = f.read().strip(';').split(';')
    c = connect(nom_de_bdd)
    for req in r :
        c.execute(req)
    c.commit()
    c.close()

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

def cree_moyen():
    """Tire au hasard un moyen de paiement"""
    return choice(['CB','CB','Liquide','Liquide','Cheque'])

def cree_liste_produits(nom_de_fichier = 'produits.csv'):
    """Crée la liste des produits"""
    with open(nom_de_fichier,'r',encoding='utf8') as f :
        f.readline()
        L = f.readlines()
    for i in range(len(L)):
        ligne = L[i].split(';')
        produit = ligne[0]
        pmin = float(ligne[1].replace(',','.'))
        pmax = float(ligne[2].replace(',','.'))
        prix = randrange(10*pmin, 10*pmax+1)/10
        L[i] = (produit,prix)
    shuffle(L)
    id = 0
    for i,x in enumerate(L):
        id = id + randrange(1,4)
        L[i] = (id,) + L[i]
    shuffle(L)
    return L

def cree_liste_tickets():
    """Crée la liste des temps"""
    t = 6*3600 + 45*60
    dt = randrange(30,300)
    tps_fin = 20*3600
    L = []
    while t+dt <= tps_fin :
        t = t+dt
        dt = randrange(30,150)
        paiement = cree_moyen()
        L.append((conv_time(t),paiement))
    shuffle(L)
    id = 0
    for i,x in enumerate(L):
        id = id + randrange(1,4)
        L[i] = (id,) + L[i]
    shuffle(L)
    return L
        
def cree_liste_lignes_tickets(liste_produits,liste_tickets):
    """Créée le contenu des tickets"""
    liste_idp = [p[0] for p in liste_produits]
    nb_prod = [1,1,1,2,2,3,4]
    L = []
    for t in liste_tickets :
        idt = t[0]
        n = choice(nb_prod)
        liste_idprod = []
        for i in range(n):
            idp = choice(liste_idp)
            while idp in liste_idprod : 
                idp = choice(liste_idp)
            liste_idprod.append(idp)
        for idp in liste_idprod :
            quantite = randrange(1,4)
            L.append((idt,idp,quantite))
    shuffle(L)
    id = 0
    for i,x in enumerate(L):
        id = id + randrange(1,4)
        L[i] = (id,) + L[i]
    shuffle(L)
    return L

def remplir_produits(nom_de_bdd,liste_produits):
    """Remplit la table des produits"""
    r = "INSERT INTO produits VALUES (?,?,?)"
    c = connect(nom_de_bdd)
    for j in liste_produits:
        c.execute(r,j)
    c.commit()
    c.close()

def remplir_tickets(nom_de_bdd,liste_tickets):
    """Remplit la table des tickets"""
    r = "INSERT INTO tickets VALUES (?,?,?)"
    c = connect(nom_de_bdd)
    for j in liste_tickets:
        c.execute(r,j)
    c.commit()
    c.close()
    
def remplir_lignes_tickets(nom_de_bdd,liste_lignes_tickets):
    """Remplit la table des lignes des tickets"""
    r = "INSERT INTO lignes_tickets VALUES (?,?,?,?)"
    c = connect(nom_de_bdd)
    for j in liste_lignes_tickets:
        c.execute(r,j)
    c.commit()
    c.close()

def cree_bdd(nom_de_bdd,graine=1):
    """Crée une bdd"""
    seed(graine)
    cree_bdd_vide(nom_de_bdd)
    liste_produits = cree_liste_produits()
    liste_tickets = cree_liste_tickets()
    liste_lignes_tickets = cree_liste_lignes_tickets(liste_produits,liste_tickets)
    remplir_produits(nom_de_bdd,liste_produits)
    remplir_tickets(nom_de_bdd,liste_tickets)
    remplir_lignes_tickets(nom_de_bdd,liste_lignes_tickets)
    
def cree_plein_bdd(nb,graine=1):
    """Crée nb bdd, chacune avec environ nbparties"""
    for i in range(nb):
        nom_de_bdd = './bdd/bdd_boulangerie_'+convert(i+1)+'.sqlite'
        print('Génération de : ' + nom_de_bdd)
        cree_bdd(nom_de_bdd, graine = i+1)
    return None

# Pour créer un exemple : cree_bdd('ex.sqlite')
# Pour créer les 99 bdd du DS: cree_plein_bdd(99)
