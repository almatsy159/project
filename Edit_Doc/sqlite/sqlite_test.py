import sqlite3

connection = sqlite3.connect("my_db")
cursor=connection.cursor()
x1=cursor.execute("SELECT COUNT(*) FROM DU")
y1=cursor.fetchone()
connection.commit()
connection.close()
#print("x1 :",x1)
#print("y1[0] :",y1[0])

connection = sqlite3.connect("my_db")
cursor=connection.cursor()
cursor.execute("SELECT * FROM DU")
y2=cursor.fetchall()
print("y2 :",y2)
connection.commit()
connection.close()
