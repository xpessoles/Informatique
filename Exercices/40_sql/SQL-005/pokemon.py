import sqlite3
conn = sqlite3.connect('veekun-pokedex.sqlite')
c = conn.cursor()

c.execute('SELECT height FROM pokemon WHERE identifier = "pikachu"')
a = c.fetchone()[0]
#print(a)

c.execute('SELECT weight FROM pokemon WHERE identifier = "pikachu"')
a = c.fetchone()[0]
#print(a)

c.execute('SELECT identifier FROM pokemon WHERE height> 4')
a = c.fetchone()[0]

c.execute('SELECT identifier FROM pokemon WHERE height> (SELECT height FROM pokemon WHERE identifier = "pikachu")')
#print(c.fetchall())


c.execute('SELECT identifier FROM pokemon WHERE height= (SELECT height FROM pokemon WHERE identifier = "pikachu")')
print(c.fetchall())
