import sqlite3

conn = sqlite3.connect('password.sqlite')
cur = conn.cursor()

try:
    cur.execute('CREATE TABLE pass (user VARCHAR, pass VARCHAR, web VARCHAR, key VARCHAR)')
except:
    print("")
cur.execute('INSERT INTO pass (user,pass,web,key) values ("alexandru","admin","testing","root")')
#cur.execute ("DROP TABLE pass")
cur.execute ("SELECT * FROM pass")
ans=cur.fetchall()
print(ans)
conn.commit()
conn.close()