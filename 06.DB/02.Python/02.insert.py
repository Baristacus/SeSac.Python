import sqlite3

conn = sqlite3.connect("example.db")

cur = conn.cursor()

cur.execute("SELECT COUNT(*) FROM users")
count = cur.fetchone()[0]
print(f"현재 데이터 갯수: {count}")

if count == 0:
    cur.execute("INSERT INTO users (name, age) VALUES ('Alice', 25)")
    cur.execute("INSERT INTO users (name, age) VALUES (?, ?)", ("Bob", 30))
else:
    print("데이터가 이미 있음")

conn.commit()

conn.close()
