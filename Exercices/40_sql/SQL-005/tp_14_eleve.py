NOM = "DANIS"
Prenom = "Ludovic"
Classe = "PSI*"

## Question 1
Q1_res = "Il y a 172 tables."

## Question 2
Q2_res = "pokemon(id : INTEGER, identifier : VARCHAR(79), species_id : INTEGER, height : INTEGER, weight : INTEGER, base_experience : INTEGER, order : INTEGER, is_default : BOOLEAN)"

## Question 3
Q3_res = "La clé primaire permet d'identifier de façon unique chaque occurence d'une table."

## Question 4
Q4_req = "SELECT height FROM pokemon WHERE identifier = 'pikachu' ; "
Q4_res = "4"

## Question 5
Q5_req = "SELECT weight FROM pokemon WHERE identifier = 'pikachu' ;"
Q5_res = "60"

## Question 6
Q6_req = "SELECT identifier FROM pokemon WHERE height > 4 ;"

## Question 7
Q7_req = "SELECT identifier FROM pokemon WHERE height > (SELECT height FROM pokemon WHERE identifier = 'pikachu') ;"

## Question 8
Q8_req = "SELECT count(*) FROM pokemon WHERE height > 4 ; "
Q8_res = "678"

## Question 9
Q9_req = "SELECT count(*) FROM pokemon WHERE height = 4 ;"
Q9_res = "63"

## Question 10
Q10_req = "SELECT identifier, weight FROM pokemon WHERE height = 4 AND weight = (SELECT max(weight) FROM pokemon WHERE height = 4) ;"
Q10_res = "aron,600"

## Question 11
Q11_req = "SELECT identifier, height FROM pokemon WHERE height = (SELECT max(height) FROM Pokemon) ;"
Q11_res = "wailord,145"

## Question 12
Q12_req = "SELECT identifier FROM pokemon WHERE height = (SELECT min(height) FROM Pokemon) ;"
Q12_res = "joltik & flabebe"

## Question 13
Q13_req = "SELECT height, count(*) AS amount FROM pokemon GROUP BY height ORDER BY height DESC ;"

## Question 14
Q14_req = "SELECT height, max(amount1) AS amount FROM (SELECT height, count(*) AS amount1 FROM pokemon GROUP BY height ORDER BY height DESC) ;"
Q14_res = "6,68 "

## Question 15
Q15_req = "SELECT identifier, max(height) FROM pokemon WHERE NOT height = (SELECT max(height) FROM pokemon) ;"

## Question 16
Q16_req = "SELECT AVG(height) FROM pokemon ;" # Je ne vois pas comment limiter à 2 décimales après la virgule
Q16_res = "12.25"

## Question 17
Q17_req = "SELECT count(*) FROM pokemon WHERE height >= 7.5 AND height <= 8.5 ;"
Q17_res = "44"

## Question 18
Q18_req = "SELECT p.identifier AS name, ph.identifier AS habitat FROM pokemon AS p JOIN pokemon_species AS ps ON species_id = ps.id JOIN pokemon_habitats AS ph ON habitat_id = ph.id ;"

## Question 19
Q19_req = "SELECT count(*) FROM pokemon AS p JOIN pokemon_species AS ps ON species_id = ps.id JOIN pokemon_habitats AS ph ON habitat_id = ph.id WHERE ph.identifier = 'forest' ;"
Q19_res = "87"

## Question 20
Q20_req = "SELECT count(*) FROM pokemon AS p JOIN pokemon_species AS ps ON species_id = ps.id JOIN pokemon_habitats AS ph ON habitat_id = ph.id WHERE ph.identifier = 'forest' AND ps.generation_id = 3 ;"
Q20_res = "31"