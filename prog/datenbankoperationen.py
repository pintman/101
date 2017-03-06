import sqlite3

# In die Datenbank schreiben
conn = sqlite3.connect("datenbank.db")
c = conn.cursor()

c.execute("CREATE TABLE Person(id int, name varchar(50))")
c.execute("""INSERT INTO Person VALUES (1, "Max")""")

conn.commit()
conn.close()

# Aus der Datenbank lesen
conn = sqlite3.connect("datenbank.db")
c = conn.cursor()

zeilen = c.execute("SELECT * FROM Person")
for z in zeilen:
    print(z)
    
