SELECT SUM(quantite) AS qtt_vendue
FROM lignes_tickets;

SELECT SUM(quantite * prix) as chiffre_affaire
FROM lignes_tickets
JOIN produits ON lignes_tickets.idp = produits.id;

SELECT idp, SUM(quantite) AS qtt_vendue
FROM lignes_tickets
GROUP BY idp
ORDER BY qtt_vendue DESC, idp ASC
LIMIT 1;

SELECT COUNT(*) AS nb_tickets_1_produit
FROM (SELECT idt, COUNT(*) AS nb_produits
	  FROM lignes_tickets
	  GROUP BY idt
	  HAVING nb_produits = 1
	  );
	  
SELECT COUNT(*) AS nb_tickets_qtt1
FROM tickets
WHERE NOT EXISTS (SELECT * 
                  FROM lignes_tickets
				  WHERE lignes_tickets.idt = tickets.id
				        AND 
						quantite >= 2
				  );
				  
SELECT MAX(heure) AS heure_dernier_ticket
FROM tickets;

SELECT SUM(quantite*prix) AS valeur_premier_ticket
FROM tickets
JOIN lignes_tickets ON tickets.id = idt
JOIN produits ON idp = produits.id
WHERE heure = (SELECT MIN(heure)
			   FROM tickets
			   );

SELECT 0.01 * SUM(quantite * prix) AS commission
FROM tickets
JOIN lignes_tickets ON tickets.id = idt
JOIN produits ON idp = produits.id
WHERE paiement = 'CB';

SELECT COUNT(*) AS nb_tickets_plus_10euros
FROM (SELECT tickets.id, SUM(quantite * prix) AS prix_ticket
	  FROM tickets
	  JOIN lignes_tickets ON tickets.id = idt
	  JOIN produits ON idp = produits.id
	  GROUP BY idt
	  HAVING prix_ticket >= 10
	  );
