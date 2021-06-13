from sqlite3 import *
from random import *

def cree_bdd(nom_de_bdd):
    """Crée une base de donnée vide"""
    with open("cree_table.sql","r") as f:
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

def cree_datenaiss():
    """Tire au hasard une date de naissance"""
    a = choice(['1999','2000','2001'])
    m = choice([convert(k) for k in range(1,13)])
    j = choice([convert(k) for k in range(1,29)])
    return a+'-'+m+'-'+j

def cree_classe():
    """Tire au hasard une classe"""
    return 'MPS'+choice(['1','2'])

def cree_table_joueurs():
    """Crée la liste des joueurs"""
    with open("pseudos.csv","r") as f:
        joueurs = f.readlines()
    shuffle(joueurs)
    if joueurs[41] == "Galois" :
        # Pb questions 1 et 2
        joueurs[23] , joueurs[41] = joueurs[41], joueurs[23]
    elif joueurs[41] == "Tux" :
        # Pb questions 7 et 8
        joueurs[69] , joueurs[41] = joueurs[41], joueurs[69]
    for i,p in enumerate(joueurs):
        p = p.strip('\n')
        idj = i+1
        datenaiss = cree_datenaiss()
        classe = cree_classe()
        joueurs[i] = (idj,p,datenaiss,classe)
    shuffle(joueurs) # inutile : sqlite présente la bdd par id ?
    return joueurs

def cree_liste_parties(nom_de_fichier):
    """Crée la liste des coups possibles"""
    with open(nom_de_fichier,'r') as f:
        p = f.readlines()
    return [int(x.strip('\n')) for x in p]

def cree_date():
    """Crée une date de partie aléatoire"""
    a = choice(['2017','2018'])
    m = choice([convert(k) for k in range(1,13)])
    j = choice([convert(k) for k in range(1,29)])
    h = choice([convert(k) for k in range(24)])
    mm = choice([convert(k) for k in range(60)])
    s = choice([convert(k) for k in range(60)])
    return a+'-'+m+'-'+j+' '+h+':'+mm+':'+s

def cree_table_parties(joueurs,nb):
    """Crée une liste de nb parties à partir de la liste des joueurs"""
    parties = [0]*nb
    parties0 = cree_liste_parties('./parties0.csv')
    parties1 = cree_liste_parties('./parties1.csv')
    parties2 = cree_liste_parties('./parties2.csv')
    L = [parties0,parties1,parties2]
    idp = 0
    for i in range(nb):
        idp = idp+randrange(1,3)
        j1 = choice(joueurs)
        j2 = choice(joueurs)
        while j2 == j1:
            j2 = choice(joueurs)
        (idj1,_,_,_) = j1
        (idj2,_,_,_) = j2
        res = choice([0,1,2])
        coups = choice(L[res])
        date = cree_date()
        parties[i] = (idp,idj1,idj2,res,coups,date)
    shuffle(parties) # inutile, sqlite présente la bdd par id ? 
    return parties

def remplir_joueurs(nom_de_bdd,joueurs):
    """Remplit la table des joueurs"""
    with open("insert_joueur.sql","r") as f:
        r = f.read().strip('\n')
    c = connect(nom_de_bdd)
    for j in joueurs:
        c.execute(r,j)
    c.commit()
    c.close()

def remplir_parties(nom_de_bdd,parties):
    """Remplit la table des joueurs"""
    with open("insert_partie.sql","r") as f:
        r = f.read().strip('\n')
    c = connect(nom_de_bdd)
    for p in parties:
        c.execute(r,p)
    c.commit()
    c.close()
    
def cree_plein_bdd(nb,nbparties,graine=1):
    """Crée nb bdd, chacune avec environ nbparties"""
    for i in range(nb):
        nom_de_bdd = './bdd/bdd_morpion_'+convert(i+1)+'.sqlite'
        seed(graine+i)
        print(nom_de_bdd)
        cree_bdd(nom_de_bdd)
        Tj = cree_table_joueurs()
        Tp = cree_table_parties(Tj,nbparties+randrange(50))
        remplir_joueurs(nom_de_bdd,Tj)
        remplir_parties(nom_de_bdd,Tp)
    return None
    
if __name__ == '__main__':
    cree_plein_bdd(99,10**4)
