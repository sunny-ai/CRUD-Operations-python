import sqlite3
db=sqlite3.connect('test.db')
qry="DELETE from student where name=?;"
try:
    cur=db.cursor()
    cur.execute(qry, ('sunny',))
    db.commit()
    print("record deleted")
except:
    print("error")
    db.rollback()
db.close()
