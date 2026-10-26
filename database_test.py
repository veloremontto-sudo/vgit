import sqlite3


connection = sqlite3.connect("bikes.db")
cursor = connection.cursor()


cursor.execute("""
CREATE TABLE IF NOT EXISTS repairs (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    client TEXT,
    problem TEXT,
    status TEXT
)
""")

cursor.execute(
    "INSERT INTO repairs (client, problem, status) VALUES (?, ?, ?)",
    ("Анна", "Прокол колеса", "Новая")
)
cursor.execute(
    "INSERT INTO repairs (client, problem, status) VALUES (?, ?, ?)",
    ("Иван", "Не работают тормоза", "Новая")
)

connection.commit()

cursor.execute(
    "UPDATE repairs SET status = ? WHERE id = ?",
    ("В ремонте", 1)
)

connection.commit()

cursor.execute(
    "DELETE FROM repairs WHERE id = ?",
    (1,)
)

connection.commit()

cursor.execute("SELECT * FROM repairs")
rows = cursor.fetchall()

cursor.execute("SELECT * FROM repairs")
print(cursor.fetchall())


connection.close()

print(rows)