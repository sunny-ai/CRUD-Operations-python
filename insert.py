import sqlite3
db=sqlite3.connect('test.db')
qry="insert into student (name, age, marks) values(?, ?, ?);"

students = [('maria', 1000, 29), ('SUNNY', 5666, 28), ('King', 25556, 566)]
try:
    cur=db.cursor()
    cur.executemany(qry,students)
    db.commit()
    print ("record added")

except:
    print ("error")
    db.rollback()
db.close()

