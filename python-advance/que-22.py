import sqlite3

connect = sqlite3.connect('table.db')

cursor = connect.cursor()

sql = """
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    age INTEGER,
    email TEXT UNIQUE
);"""
cursor.execute(
   sql
)
cursor.execute('INSERT INTO users(name, age) values ("aliash", 21)')

connect.commit()

connect.close()