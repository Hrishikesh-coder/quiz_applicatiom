import sqlite3

db = sqlite3.connect(f'quiz_db.db')

cursor = db.cursor()