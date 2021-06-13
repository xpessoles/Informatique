import sqlite3



conn = sqlite3.connect('bdd/bdd_boulangerie_01.sqlite')
c = conn.cursor()

def traitement_sol(l) :
    return [x[0] for x in l]


req=["""SELECT sum(quantite) FROM lignes_tickets;""",\
     """SELECT sum(pq) FROM (SELECT quantite, prix, prix*quantite as pq FROM lignes_tickets \
JOIN produits ON lignes_tickets.idp=produits.id);""",\
     """SELECT idp FROM (SELECT lignes_tickets.idp, sum(quantite) as nbpdt FROM lignes_tickets GROUP BY lignes_tickets.idp)\
ORDER BY nbpdt DESC limit 1;""",\
     """SELECT count(*) from (select idt from \
(SELECT idt, SUM(quantite) as qt FROM lignes_tickets GROUP BY lignes_tickets.idt) where qt=1);""",\
     """SELECT count(*) from (select idt, nbpdt from (SELECT idt, SUM(quantite) as qt, count(*) as nbpdt \
FROM lignes_tickets GROUP BY lignes_tickets.idt) where qt=nbpdt);""",\
     """SELECT max(heure) FROM tickets;""",\
     """SELECT sum(quantite*prix) \
FROM (SELECT heure, quantite, prix, idt FROM tickets JOIN lignes_tickets JOIN produits ON tickets.id=lignes_tickets.idt and lignes_tickets.idp=produits.id) \
JOIN (SELECT min(heure), id as premier FROM tickets) ON idt=premier; """,\
      """SELECT SUM(0.01*prix*quantite) FROM (SELECT id, prix FROM produits) \
JOIN (SELECT idp, quantite FROM (SELECT id as id0 FROM tickets WHERE paiement='CB') JOIN lignes_tickets ON id0=idt) ON id=idp;
""",\
      """SELECT COUNT(*) FROM(SELECT idt, SUM(quantite*prix) as valeur FROM \
(SELECT idt, idp, quantite FROM lignes_tickets join tickets on idt=tickets.id ORDER BY idt ASC) \
JOIN produits ON idp=id GROUP BY idt HAVING valeur>=10);""" 
     ]



n=len(req)


q=[]

for requete in req :
    c.execute(requete)
    q.append(traitement_sol(c.fetchall()))



