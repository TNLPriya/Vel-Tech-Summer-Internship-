import sqlite3

# Connect database
conn = sqlite3.connect('students.db')

cursor = conn.cursor()

# Create table
cursor.execute('''
CREATE TABLE IF NOT EXISTS students (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    age INTEGER,
    gender INTEGER,
    marital_status INTEGER,
    debtor INTEGER,
    tuition INTEGER,
    scholarship INTEGER,
    first_sem_approved REAL,
    first_sem_grade REAL,
    second_sem_approved REAL,
    second_sem_grade REAL,
    prediction TEXT,
    confidence REAL
)
''')

conn.commit()
conn.close()

print("Database Created Successfully!")