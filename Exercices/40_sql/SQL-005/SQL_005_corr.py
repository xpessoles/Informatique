import sqlite3
conn = sqlite3.connect('veekun-pokedex.sqlite')
conn.close()
#c = conn.cursor()

"""
for i in range(1,25):
    print("## Question "+str(i))
    print("sol_Q"+str(i)+'_req = ""')
    print("sol_Q"+str(i)+'_res = ""')
    print("")
"""
    
## Question 1
sol_Q1_res = "172"

## Question 2
sol_Q2_res = 'pokemon(id : integer, identifier : string, species_id : integer, height : integer, weight : integer, base_experience : integer, order : integer, is_default : boolean)'

## Question 3
sol_Q3_res = "La clé primaire d'une table est une contrainte d'unicité, composée d'une ou plusieurs colonnes et qui permet d'identifier de manière unique chaque ligne de la table."

## Question 4
sol_Q4_req = "SELECT height FROM pokemon WHERE identifier = 'pikachu';"
sol_Q4_res = "4"

## Question 5
sol_Q5_req = "SELECT weight FROM pokemon WHERE identifier = 'pikachu';"
sol_Q5_res = "60"

## Question 6
sol_Q6_req = "SELECT identifier FROM pokemon WHERE height> 4;"

## Question 7
sol_Q7_req = "SELECT identifier FROM pokemon WHERE height > (SELECT height FROM pokemon WHERE identifier = 'pikachu');"

## Question 8
sol_Q8_req = "SELECT count(*) FROM pokemon WHERE height > (SELECT height FROM pokemon WHERE identifier = 'pikachu');"
sol_Q8_res = "678"

## Question 9
sol_Q9_req = "SELECT count(*) FROM pokemon WHERE height = (SELECT height FROM pokemon WHERE identifier = 'pikachu');"
sol_Q9_res = "63"

## Question 10
sol_Q10_req = "SELECT identifier,max(weight) FROM pokemon WHERE height = (SELECT height FROM pokemon WHERE identifier = 'pikachu');"
sol_Q10_res = "aron,600"

## Question 11
sol_Q11_req = "SELECT identifier, height, weight FROM pokemon WHERE height = (SELECT max(height) FROM pokemon);"
sol_Q11_res = "wailord,145,3980"

## Question 12
sol_Q12_req = "SELECT identifier FROM pokemon WHERE height = (SELECT min(height) FROM pokemon); "
sol_Q12_res = "joltik,flabebe"

## Question 13
sol_Q13_req = "SELECT height,count(height) FROM pokemon GROUP BY height order BY height DESC"

## Question 14
sol_Q14_req = "SELECT height,MAX(ch) FROM (SELECT height,count(height) AS ch FROM pokemon GROUP BY height)"
sol_Q14_res = "6,68"

## Question 15
sol_Q15_req = "SELECT identifier,max(height) FROM (SELECT identifier,height FROM pokemon WHERE height!=(SELECT max(height) from pokemon))"

## Question 16
sol_Q16_req = "SELECT avg(height) FROM pokemon;"
sol_Q16_res = "12.2503082614057"

## Question 17
sol_Q17_req = "SELECT count(*) FROM pokemon WHERE height <= 8.5 AND height >= 7.5;"
sol_Q17_res = "44"

## Question 18
sol_Q18_req = "SELECT S.identifier,H.identifier FROM pokemon_species AS S JOIN pokemon_habitats AS H ON S.habitat_id = H.id;"

## Question 19
sol_Q19_req = "SELECT count(*) FROM pokemon_species AS S JOIN pokemon_habitats AS H ON S.habitat_id = H.id WHERE H.identifier = 'forest';"
sol_Q19_res = "71"

## Question 20
sol_Q20_req = "SELECT count(*) FROM pokemon_species AS S JOIN pokemon_habitats AS H ON S.habitat_id = H.id WHERE H.identifier = 'forest' AND S.generation_id = 3;"
sol_Q20_res = "29"
