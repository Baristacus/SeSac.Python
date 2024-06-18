import sqlite3

conn = sqlite3.connect("example.db")

cur = conn.cursor()

cur.execute("SELECT * FROM users")

rows = cur.fetchall()

for row in rows:
    print(f"이름: {row[1]}")

conn.close()
