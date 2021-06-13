import sqlite3

conn=sqlite3.connect('hotel.db')

cur=conn.cursor()


#Q1
print("\n Q1 : \n")

cur.execute('SELECT CLI_NOM, CLI_PRENOM, TIT_CODE FROM T_CLIENT')

print(cur.fetchall())

#Q2
print("\n Q2 : \n")

cur.execute('SELECT COUNT(*) FROM T_CLIENT ;')

print(cur.fetchall())

#Q3
print("\n Q3 : \n")

cur.execute("SELECT CLI_NOM, CLI_PRENOM, TIT_CODE FROM T_CLIENT WHERE TIT_CODE='Mme.'")

# cur.execute('SELECT CLI_NOM, CLI_PRENOM FROM T_CLIENT JOIN T_TITRE ON T_CLIENT.TIT_CODE=T_TITRE.TIT_CODE WHERE T_TITRE.TIT_LIBELLE="Madame"')

print(cur.fetchall())


#Q4
print("\n Q4 : \n")

cur.execute("SELECT CLI_NOM, CLI_PRENOM, TIT_CODE FROM T_CLIENT WHERE TIT_CODE='Mme.' OR TIT_CODE='Melle.'")



print(cur.fetchall())

#Q5
print("\n Q5 : \n")

cur.execute("SELECT count(*) FROM T_CLIENT WHERE TIT_CODE='Mme.' OR TIT_CODE='Melle.'")



print(cur.fetchall())


#Q6
print("\n Q6 : \n")

cur.execute("SELECT CLI_NOM as noms, CLI_PRENOM as prenoms FROM T_CLIENT WHERE TIT_CODE='Mme.' OR TIT_CODE='Melle.' ORDER BY noms, prenoms")

# cur.execute('SELECT CLI_NOM as Nom, CLI_PRENOM as Prénom FROM T_CLIENT JOIN T_TITRE ON T_CLIENT.TIT_CODE=T_TITRE.TIT_CODE WHERE T_TITRE.TIT_LIBELLE="Monsieur" ORDER BY Nom, Prénom')

print(cur.fetchall())
#Q3
print("\n Q3 : \n")
cur.execute('SELECT Nom1, T_CLIENT.CLI_PRENOM FROM T_CLIENT JOIN (SELECT Nom1, Prenom FROM (SELECT CLI_NOM as Nom1, CLI_PRENOM as prenom, COUNT(*) as nb_nom FROM T_CLIENT GROUP BY Nom1) WHERE nb_nom>1) ON T_CLIENT.CLI_NOM=Nom1')


print(cur.fetchall())



#Q4
print("\n Q4 : \n")
cur.execute('SELECT FAC_ID FROM T_LIGNE_FACTURE EXCEPT SELECT FAC_ID FROM T_LIGNE_FACTURE WHERE LIF_REMISE_POURCENT>0 OR LIF_REMISE_MONTANT>0')


print(cur.fetchall())


#Q5
print("\n Q5 : \n")
cur.execute('SELECT  DISTINCT T_FACTURE.CLI_ID FROM T_FACTURE JOIN(SELECT T_LIGNE_FACTURE.FAC_ID as id1 FROM T_LIGNE_FACTURE EXCEPT SELECT FAC_ID FROM T_LIGNE_FACTURE WHERE LIF_REMISE_POURCENT>0 OR LIF_REMISE_MONTANT>0) ON id1=T_FACTURE.FAC_ID;')


print(cur.fetchall())


#Q6
print("\n Q6 : \n")
cur.execute('SELECT T_CLIENT.CLI_NOM, T_CLIENT.CLI_PRENOM FROM T_CLIENT JOIN (SELECT  DISTINCT T_FACTURE.CLI_ID as client_id FROM T_FACTURE JOIN (SELECT T_LIGNE_FACTURE.FAC_ID as id1 FROM T_LIGNE_FACTURE EXCEPT SELECT FAC_ID FROM T_LIGNE_FACTURE WHERE LIF_REMISE_POURCENT>0 OR LIF_REMISE_MONTANT>0)ON id1=T_FACTURE.FAC_ID)ON T_CLIENT.CLI_ID=client_id')


print(cur.fetchall())


#Q7
print("\n Q7 : \n")

cur.execute('SELECT COUNT(*) FROM (SELECT TJ_CHB_PLN_CLI.PLN_JOUR, TJ_CHB_PLN_CLI.CHB_PLN_CLI_OCCUPE, TJ_CHB_PLN_CLI.CHB_PLN_CLI_RESERVE FROM TJ_CHB_PLN_CLI WHERE TJ_CHB_PLN_CLI.PLN_JOUR="2001-01-28" AND CHB_PLN_CLI_RESERVE=0)')

print(cur.fetchall())


#Q8
print("\n Q8 : \n")

cur.execute('SELECT T_CLIENT.CLI_NOM, T_TELEPHONE.TEL_NUMERO FROM T_CLIENT JOIN T_TELEPHONE ON T_CLIENT.CLI_ID=T_TELEPHONE.CLI_ID')

print(cur.fetchall())

#Q9
print("\n Q9 : \n")

cur.execute('SELECT CHB_ETAGE, count(*) FROM T_CHAMBRE GROUP BY CHB_ETAGE')

print(cur.fetchall())


#Q10
print("\n Q10 : \n")

cur.execute('SELECT T_CHAMBRE.CHB_ETAGE, count(*) FROM T_CHAMBRE  JOIN TJ_CHB_PLN_CLI ON TJ_CHB_PLN_CLI.CHB_ID=T_CHAMBRE.CHB_ID  WHERE TJ_CHB_PLN_CLI.PLN_JOUR="2001-01-28" GROUP BY T_CHAMBRE.CHB_ETAGE')

print(cur.fetchall())


#Q11
print("\n Q11 : \n")

cur.execute('SELECT etage1, nbetage1-nbetage2 FROM (SELECT CHB_ETAGE as etage1, count(*) as nbetage1 FROM T_CHAMBRE GROUP BY CHB_ETAGE) JOIN (SELECT T_CHAMBRE.CHB_ETAGE as etage2, count(*) as nbetage2 FROM T_CHAMBRE  JOIN TJ_CHB_PLN_CLI ON TJ_CHB_PLN_CLI.CHB_ID=T_CHAMBRE.CHB_ID  WHERE TJ_CHB_PLN_CLI.PLN_JOUR="2001-01-28" GROUP BY T_CHAMBRE.CHB_ETAGE) on etage1=etage2')

print(cur.fetchall())









