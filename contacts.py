import sqlite3

db = sqlite3.connect("contacts.sqlite")
db.execute("CREATE TABLE IF NOT EXISTS contacts (name TEXT, phone INTEGER, email TEXT)")
db.execute("INSERT INTO contacts(name, phone, email) VALUES ('Georgios', 123, 'helloworld@gmail.com')")
db.execute("INSERT INTO contacts VALUES ('Martine', 456, 'whoareyou@gmail.com')")


columns =["Name:", "Phone:", "Email:"]

cursor = db.cursor() # Cursor is a pointer in sorts to the location of the db query, there are no data loaded at memory
cursor.execute("SELECT * FROM contacts")

for row in cursor:
    rows = 0
    for data in row:
        print(columns[rows], data)
        rows += 1
    print("*" * 80)

print("-" * 80)

cursor.execute("SELECT * FROM contacts")
for name, phone, email in cursor:
    print("Name:", name)
    print("Phone:", phone)
    print("Email:", email)
    print("*" * 80)

db.commit()

cursor.close()
db.close()


