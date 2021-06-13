import sqlite3



conn = sqlite3.connect('bdd/bdd_morpion_01.sqlite')
c = conn.cursor()

def traitement_sol(l) :
    return [x[0] for x in l]

req=["""select pseudo from joueurs where idj = 42 ;""",\
     """select idj from joueurs where pseudo = 'Galois' ;""",\
     """select count(*) from parties ;""",\
     """select count(*) from parties where res = 0;""",\
     """select count(distinct coups) from parties;""",\
     """select idj from (select idj, max(datenaiss) from joueurs);""",\
     """select count(*) from joueurs, parties where pseudo='Tux' and \
           (idj = idj1 or idj = idj2);""",\
     """select count(*) from joueurs, parties where pseudo='Tux' and \
           ((idj = idj1 and res = 2) or (idj = idj2 and res = 1));""",\
     """select count(*) from parties, joueurs,\
           (select idj as idj22, pseudo as pseudo2, classe as classe2\
           from joueurs as joueur2) where\
           (idj =  idj1 and idj22 = idj2 and \
               classe="MPS1" and classe2="MPS2" and res = 1)\
           or (idj =  idj1 and idj22 = idj2 and \
             classe="MPS2" and classe2="MPS1" and res = 2);""",\
    """SELECT pseudo
FROM joueurs, 
     (SELECT idj1, count(*) AS nbj1
      FROM parties
      GROUP BY idj1)
WHERE idj = idj1
      AND nbj1 = (SELECT max(nbj1)
                  FROM (SELECT idj1, count(*) AS nbj1
                        FROM parties
                        GROUP BY idj1)
                 );""",\
     """select count(idp) from joueurs,\
         (select idj as idj22, pseudo as pseudo2, classe as classe2\
           from joueurs as joueur2),\
           parties where date >= "2016-01-01" and coups < 9999999\
           and idj1 = idj and idj2 = idj22 and classe = classe2 ;"""
     ]

n=len(req)


q=[]

for requete in req :
    c.execute(requete)
    q.append(traitement_sol(c.fetchall()))



