import sqlite3

conn=sqlite3.connect('veekun-pokedex.sqlite')

cur=conn.cursor()

#cur.execute('SELECT * FROM pokemon')

cur.execute('SELECT * FROM pokemon')

print(cur.fetchall())
