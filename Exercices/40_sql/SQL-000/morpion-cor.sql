.header ON
-- q1

SELECT pseudo AS pseudo_42
FROM joueurs
WHERE idj = 42;

-- q2

SELECT idj AS id_Galois
FROM joueurs
WHERE pseudo = "Galois";

-- q3

SELECT count(*) AS nb_parties
FROM parties;

-- q4

SELECT count(*) AS nb_matchs_nuls
FROM parties
WHERE res = 0;

-- q5

SELECT count(DISTINCT coups) AS nb_coups_distincts
FROM parties;

-- q6

SELECT idj AS id_jeune
FROM joueurs
WHERE datenaiss = (SELECT max(datenaiss)
                   FROM joueurs
                  );
   

-- q7

SELECT count(*) AS nb_parties_Tux
FROM parties
JOIN joueurs ON pseudo = "Tux"
WHERE idj1 = idj -- Tux = j1
      OR 
      idj2 = idj -- Tux = j2
      ;

-- q8 

SELECT count(*) AS nb_defaites_Tux
FROM  parties
JOIN joueurs ON pseudo = "Tux"
WHERE (idj = idj1 AND res = 2) -- Tux = j1 et j2 gagne
      OR 
      (idj = idj2 AND res = 1) -- Tux = j2 et j1 gagne
;
      

-- q9

SELECT count(*) AS nb_victoires_MPS1
FROM parties
JOIN joueurs AS j1 ON j1.idj = parties.idj1
JOIN joueurs AS j2 ON j2.idj = parties.idj2
WHERE (j1.classe = "MPS1" AND j2.classe = "MPS2" AND res = 1)
      OR 
      (j1.classe = "MPS2" AND j2.classe = "MPS1" AND res = 2);

-- q10

SELECT pseudo AS pseudo_max_j1
FROM joueurs, (SELECT max(nbj1) AS maxi
               FROM (SELECT idj1, count(*) AS nbj1
                     FROM parties
                     GROUP BY idj1
                    )
              )
JOIN (SELECT idj1, count(*) AS nbj1
      FROM parties
      GROUP BY idj1)
      ON idj = idj1
WHERE nbj1 = maxi ;   

-- q11

SELECT count(*) AS rep_q11
FROM parties
JOIN joueurs AS j1 ON j1.idj = parties.idj1
JOIN joueurs AS j2 ON j2.idj = parties.idj2
WHERE j1.classe = j2.classe
      AND
      coups < 10000000
      AND
      res > 0
      AND
      date >= "2018-01-01 00:00:00"
      AND
      date < "2019-01-01 00:00:00";
