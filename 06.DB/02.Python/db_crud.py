import sqlite3


def connect_db():
    conn = sqlite3.connect("example.db")
    return conn


def create_table():
    conn = connect_db()
    cur = conn.cursor()
    cur.execute(
        "CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT NOT NULL, age INTEGER NOT NULL)"
    )
    conn.commit()
    conn.close()


def insert_data(name, age):
    conn = connect_db()
    cur = conn.cursor()
    cur.execute("INSERT INTO users (name, age) VALUES (?, ?)", (name, age))
    conn.commit()
    conn.close()


def fetch_users():
    conn = connect_db()
    cur = conn.cursor()
    cur.execute("SELECT * FROM users")
    users = cur.fetchall()
    conn.close()

    return users


def update_user(name, age):
    conn = connect_db()
    cur = conn.cursor()
    cur.execute("UPDATE users SET age = ? WHERE name = ?", (age, name))
    conn.commit()
    conn.close()


def delete_user(name):
    conn = connect_db()
    cur = conn.cursor()
    cur.execute("DELETE FROM users WHERE name = ?", (name,))
    conn.commit()
    conn.close()
