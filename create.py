import sqlite3

db = sqlite3.connect('test.db')

try:
    cur = db.cursor()
    cur.execute('''CREATE TABLE student (StudentID INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT (20) NOT NULL, age INTEGER, marks REAL);''')

    print('successful')

except:

    print('error')
    db.rollback()

db.close()
