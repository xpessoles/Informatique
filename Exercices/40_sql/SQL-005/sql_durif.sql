/*Q4*/

SELECT IDENTIFIER, height FROM pokemon where lower(identifier)='pikachu';

/*Q5*/
SELECT IDENTIFIER, weight FROM pokemon where lower(identifier)='pikachu';

/*Q6*/
SELECT IDENTIFIER, height FROM pokemon where height>4;
/*Q7*/
SELECT IDENTIFIER, height FROM pokemon where height>(SELECT height FROM pokemon where lower(identifier)='pikachu');

/*Q8*/
SELECT COUNT(*) FROM (SELECT IDENTIFIER, height FROM pokemon where height>(SELECT height FROM pokemon where lower(identifier)='pikachu'));

/*Q9*/
SELECT COUNT(*) FROM (SELECT IDENTIFIER, height FROM pokemon where height=(SELECT height FROM pokemon where lower(identifier)='pikachu'));

/*Q10*/
SELECT identifier, max(weight) FROM (SELECT IDENTIFIER, height, weight FROM pokemon where height=(SELECT height FROM pokemon where lower(identifier)='pikachu'));

/*Q11*/
SELECT identifier, max(height), weight from pokemon;

/*Q12*/
SELECT identifier FROM POKEMON where height=(SELECT min(height) from pokemon);
/*XAvier*/

SELECT identifier
FROM pokemon
WHERE height =
(SELECT min(height) FROM pokemon);

/*Q13*/
SELECT identifier, height from pokemon order by height DESC;

/*Q14*/
SELECT max(nb_meme_taille), height FROM (SELECT count(*) as nb_meme_taille, height from pokemon group by height);

/*Q15*/
select * from pokemon where height=(select max(height) from pokemon);

select * from pokemon EXCEPT select * from pokemon where height=(select max(height) from pokemon);

select identifier, max(height) from (select * from pokemon EXCEPT select * from pokemon where height=(select max(height) from pokemon));

/*Q16*/

SELECT AVG(height) from pokemon;


/*Q17*/

SELECT count(*) from (SELECT identifier from pokemon where height<=8.5 and height>=7.5);


/*Q18*/

SELECT pokemon_species.identifier, pokemon_habitats.identifier from pokemon_species JOIN pokemon_habitats ON pokemon_species.habitat_id=pokemon_habitats.id ;

/*Q19*/
SELECT count(*) FROM (SELECT pokemon_species.identifier, pokemon_habitats.identifier from pokemon_species JOIN pokemon_habitats ON pokemon_species.habitat_id=pokemon_habitats.id WHERE pokemon_habitats.identifier='forest' ) ;

/*Q20*/
SELECT count(*) FROM (SELECT pokemon_species.identifier, pokemon_habitats.identifier from pokemon_species JOIN pokemon_habitats ON pokemon_species.habitat_id=pokemon_habitats.id WHERE pokemon_habitats.identifier='forest' and pokemon_species.generation_id=3) ;