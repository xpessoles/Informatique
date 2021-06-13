CREATE TABLE joueurs (
	idj INTEGER,
	pseudo VARCHAR(50),
	datenaiss DATE,
	classe VARCHAR(50),
	PRIMARY KEY (idj)
	);

CREATE TABLE parties (
	idp INTEGER,
	idj1 INTEGER, 
	idj2 INTEGER,
	res INTEGER,
	coups INTEGER,
	date DATETIME,
	PRIMARY KEY(idp),
	FOREIGN KEY(idj1) REFERENCES joueurs,
	FOREIGN KEY(idj2) REFERENCES joueurs
	);
