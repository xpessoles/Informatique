--Q1
SELECT count(quantite) FROM lignes_tickets;


--Q2
SELECT count(pq) FROM (SELECT quantite, prix, prix*quantite as pq FROM lignes_tickets JOIN produits ON lignes_tickets.idp=produits.id);

--Q3
SELECT lignes_tickets.idp, count(*) as nbpdt FROM lignes_tickets GROUP BY lignes_tickets.idp ORDER BY nbpdt DESC limit 1;

SELECT idp, max(nbpdt) FROM (SELECT lignes_tickets.idp, count(*) as nbpdt FROM lignes_tickets GROUP BY lignes_tickets.idp);

--Q4
--liste des tickets avec le nombre de produits différentes vendus
SELECT lignes_tickets.idt, count(*) as nbpdt FROM lignes_tickets GROUP BY lignes_tickets.idt;

--liste des tickets avec un nombre de type produits vendus égal à 1
select idt from (SELECT lignes_tickets.idt, count(*) as nbpdt FROM lignes_tickets GROUP BY lignes_tickets.idt) where nbpdt=1;


--liste des tickets avec le nombre de produits vendus sans tenir compte s'ils sont différents ou non
SELECT idt, SUM(quantite) as qt FROM lignes_tickets GROUP BY lignes_tickets.idt;

--liste des tickets avec le nombre de produits vendus sans tenir compte s'ils sont différents ou non égal à 1
select idt from (SELECT idt, SUM(quantite) as qt FROM lignes_tickets GROUP BY lignes_tickets.idt) where qt=1;


--Q5
select idt, nbpdt from (SELECT idt, SUM(quantite) as qt, count(*) as nbpdt FROM lignes_tickets GROUP BY lignes_tickets.idt) where qt=nbpdt;






--Q5
SELECT count(quantite) FROM lignes_tickets;

--Q6
SELECT count(quantite) FROM lignes_tickets;

--Q7
SELECT count(quantite) FROM lignes_tickets;

--Q8
SELECT count(quantite) FROM lignes_tickets;

--Q9
SELECT count(quantite) FROM lignes_tickets;

