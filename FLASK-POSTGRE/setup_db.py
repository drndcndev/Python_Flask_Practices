import sqlite3

conn = sqlite3.connect('sample.db')
c = conn.cursor()

c.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        hobby TEXT NOT NULL
    )
''')

conn.commit()
conn.close()