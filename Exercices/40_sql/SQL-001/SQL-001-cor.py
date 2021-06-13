import sqlite3

def traitement_sol(L) :
    return [x[0] for x in L]



conn = sqlite3.connect('medocs.sqlite')
cur = conn.cursor()
req1 = """SELECT code_CIS from CIS_bdpm ;"""
cur.execute(req1)
codes =[ str(r[0]) for r in cur.fetchall()]
conn.close()



def qu_sql(alpha) :
    conn = sqlite3.connect('medocs.sqlite')
    cur = conn.cursor()
    req= [ """SELECT laboratoire  
              FROM LABORATOIRES 
              WHERE id = ? ;""",
           """SELECT COUNT(code_CIS) 
              FROM CIS_bdpm 
              WHERE titulaire = ?;""",
           """SELECT COUNT(date_AMM) 
              FROM CIS_bdpm  
              WHERE titulaire = ? 
                    AND 
                    date_AMM >= DATE("2000-01-01") ; """,
           """SELECT MIN(code_CIS) 
              FROM (SELECT MIN(date_AMM) AS min_date 
                    FROM CIS_bdpm 
                    WHERE titulaire = ?
                   ), CIS_bdpm
              WHERE date_AMM=min_date 
                    AND
                    titulaire = ? ;""",
           """SELECT SUM(numéro_liaison)
              FROM CIS_COMPO, CIS_bdpm
              WHERE CIS_COMPO.code_CIS = CIS_bdpm.code_CIS
                    AND titulaire = ? ; """,
           """select min(CIS_COMPO.code_CIS) 
            from CIS_COMPO,
                    (SELECT CIS_COMPO.code_CIS  as coco,  count(code_substance) as cosubst
                    from CIS_COMPO, CIS_bdpm
                    where CIS_COMPO.code_CIS = CIS_bdpm.code_CIS and titulaire = ?
                    group by CIS_COMPO.code_CIS) ,
                             (select max(cosubs) as maxcosub
                             from
                                       (SELECT count(code_substance) as cosubs
                                       from CIS_COMPO, CIS_bdpm
                                       where CIS_COMPO.code_CIS = CIS_bdpm.code_CIS and titulaire = ?
                                       group by CIS_COMPO.code_CIS) )
                             where CIS_COMPO.code_CIS = coco and cosubst = maxcosub ;""" ,
           """SELECT lien 
              FROM CIS_HAS_SMR, HAS_Liens, (SELECT MIN(code_CIS) AS coco 
                                            FROM (SELECT MIN(date_AMM) AS min_date 
                                                  FROM CIS_bdpm 
                                                  WHERE titulaire = ?), CIS_bdpm 
                                            WHERE date_AMM=min_date 
                                                  AND 
                                                  titulaire = ?
                                           )
              WHERE coco = code_CIS 
                    AND 
                    CIS_HAS_SMR.code_HAS = HAS_Liens.code_HAS ;
           """
         ]
    q = [] # reponses
    p = [(alpha,),(alpha,),(alpha,),(alpha,alpha),(alpha,),(alpha,alpha),(alpha,alpha)] # paramètres
    for i,r in enumerate(req) : 
        cur.execute(r,p[i])
        q.append(cur.fetchone()[0])
    q9=q[6]
    s = q9[-6:]
    if q9[-7].isdigit() :
        s = q9[-7]+s
    q[6] = s
    conn.close()
    compteur = 0
    beta = str(alpha)
    if alpha < 10 :
        beta = '0'+beta
    for e in codes :
        if beta in e :
            compteur += 1
    q.append(compteur)
    return q
    

def reponses():
    "Génère le csv des réponses"
    header = ('alpha;R1;R2;R3;R4;R5;R6;R7;R8;R9;R10\n')
    with open('d04s_reponses.csv','w') as f:
        f.write(header)
        for alpha in range(1,101):
            L = [alpha,'Oui','Non'] + qu_sql(alpha)
            ligne = ';'.join([str(t) for t in L])+'\n'
            f.write(ligne)
    return None

if __name__ == '__main__':
    reponses()
           

