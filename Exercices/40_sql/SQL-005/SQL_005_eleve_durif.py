NOM = "DURIF"
Prenom = "Emilien"
Classe = "MPSI2"

## Question 1
Q1_res = "172"

## Question 2
Q2_res = "pokemon(id : INTEGER, identifier : VARCHAR(79), species_id : INTEGER, height : INTEGER, weight : INTEGER, base_experience : INTEGER,order : INTEGER, is_default : BOOLEAN)"

## Question 3
Q3_req = "Un clé primaire est unique pour chaque donnée d'une table et permet de bien différencier chaque donnée. Il s'agit d'un entier"

## Question 4
Q4_req = "SELECT IDENTIFIER, height FROM pokemon where lower(identifier)='pikachu';"
Q4_res = "4"

## Question 5
Q5_req = "SELECT IDENTIFIER, weight FROM pokemon where lower(identifier)='pikachu';"
Q5_res = "60"

## Question 6
Q6_req = "SELECT IDENTIFIER, height FROM pokemon where height>=4;"


## Question 7
Q7_req = "SELECT IDENTIFIER, height FROM pokemon where height>=(SELECT height FROM pokemon where lower(identifier)='pikachu');"


## Question 8
Q8_req = "SELECT COUNT(*) FROM (SELECT IDENTIFIER, height FROM pokemon where height>(SELECT height FROM pokemon where lower(identifier)='pikachu'));"

Q8_res = "678"

## Question 9
Q9_req = "SELECT COUNT(*) FROM (SELECT IDENTIFIER, height FROM pokemon where height=(SELECT height FROM pokemon where lower(identifier)='pikachu'));"

Q9_res = "9"

## Question 10
Q10_req = "SELECT identifier, max(weight) FROM (SELECT IDENTIFIER, height, weight FROM pokemon where height=(SELECT height FROM pokemon where lower(identifier)='pikachu'));"

Q10_res = "aron,600"

## Question 11
Q11_req = "SELECT identifier, max(height), weight from pokemon;"
Q11_res = "wailord,145,3980"

## Question 12
Q12_req = "SELECT identifier FROM POKEMON where weight=(SELECT min(height) from pokemon);"
Q12_res = "gastly, haunter flabebe"

## Question 13
Q13_req = "SELECT identifier, height from pokemon order by height DESC;"

## Question 14
Q14_req = "SELECT max(nb_meme_taille), height FROM (SELECT count(*) as nb_meme_taille, height from pokemon group by height);"
Q14_res = "(68,6)"

## Question 15
Q15_req = "select identifier, max(height) from (select * from pokemon EXCEPT select * from pokemon where height=(select max(height) from pokemon));"

Q15_res ="rayquaza-mega,108"
## Question 16
Q16_req = "SELECT AVG(height) from pokemon;"
Q16_res = "12.25"

## Question 17
Q17_req = "SELECT count(*) from (SELECT identifier from pokemon where height<=8.5 and height>=7.5);"
Q17_res = "44"

## Question 18
Q18_req = "SELECT pokemon_species.identifier, pokemon_habitats.identifier from pokemon_species JOIN pokemon_habitats ON pokemon_species.habitat_id=pokemon_habitats.id ;"

## Question 19
Q19_req = "SELECT count(*) FROM (SELECT pokemon_species.identifier, pokemon_habitats.identifier from pokemon_species JOIN pokemon_habitats ON pokemon_species.habitat_id=pokemon_habitats.id WHERE pokemon_habitats.identifier='forest' ) ;"
Q19_res = "71"

## Question 20
Q20_req = "SELECT count(*) FROM (SELECT pokemon_species.identifier, pokemon_habitats.identifier from pokemon_species JOIN pokemon_habitats ON pokemon_species.habitat_id=pokemon_habitats.id WHERE pokemon_habitats.identifier='forest' and pokemon_species.generation_id=3) ;"
Q20_res = "29"