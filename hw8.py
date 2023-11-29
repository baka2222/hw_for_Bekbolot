import sqlite3
with sqlite3.connect('venv/hw_8') as db:
    cursor = db.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS students(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    hobby TEXT,
    name TEXT,
    surname TEXT,
    year_birth INTEGER,
    point_hw INTEGER DEFAULT 0
    )''')

    # cursor.execute('''INSERT INTO students(hobby, name, surname, year_birth, point_hw)
    # VALUES("djudo", "Abirhan", "Atabaev", 2008, 88)''')


    cursor.execute("""UPDATE students SET name = 'genius' WHERE point_hw>10""")
    prnt = cursor.execute('''SELECT * FROM students WHERE name LIKE "genius"''')
    for i in prnt:
        print(i)
    cursor.execute("DELETE FROM students WHERE id%2=0")