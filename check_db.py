import sqlite3

db = sqlite3.connect("contacts.sqlite")

name_querry = input("Give eme the name you are searching:\n")

# We use parenthesis and coma sit sbecause of tuple rules
for row in db.execute("SELECT * FROM contacts WHERE name LIKE ? ", (name_querry,)):
    print(row)
    print("*" * 40)

db.close()