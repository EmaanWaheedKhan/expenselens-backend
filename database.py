import sqlite3

conn = sqlite3.connect("expense.db")

cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS receipts (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    filename TEXT
)
""")

conn.commit()

print("Database Created")