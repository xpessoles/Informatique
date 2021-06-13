CREATE TABLE tickets (
	-- table des tickets
	id INTEGER,
	heure TIME NOT NULL,
	paiement VARCHAR(10) NOT NULL,
	PRIMARY KEY (id)
	);

CREATE TABLE produits (
	-- table des produits
	id INTEGER,
	nom VARCHAR(50) NOT NULL,
	prix FLOAT,
	PRIMARY KEY (id)
	);

CREATE TABLE lignes_tickets (
	-- table des lignes des tickets
	id INTEGER,
	idt INTEGER,
	idp INTEGER,
	quantite INTEGER NOT NULL,
	PRIMARY KEY (id),
	FOREIGN KEY (idt) REFERENCES tickets,
	FOREIGN KEY (idp) REFERENCES produits
	);
