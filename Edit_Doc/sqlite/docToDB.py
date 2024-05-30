import sqlite3

#print(dir(sqlite3))
#connection = sqlite3.connection()
#cursor = connection.cursor()

db_name="my_db.db"

req1="""CREATE TABLE IF NOT EXISTS DU (
du_id INTERGER PRIMARY KEY,
name TEXT
) """

req2="""CREATE TABLE IF NOT EXISTS DOC (
doc_id INTEGER PRIMARY KEY,
name TEXT,
du_id INTEGER
) """

def execute_request(db_name,request):
    connection = sqlite3.connect(db_name)
    cursor = connection.cursor()
    #print(dir(cursor))
    cursor.execute(request)
    x=cursor.fetchall()
    connection.commit()
    connection.close()
    return x

def get_id(table):
    req="SELECT COUNT(*) FROM {0}".format(table)
    id=execute_request(db_name,req)
    print("###############################################")
    #print("id :",id[0])
    id=str(id)
    for i in id :
        if i == str(int()):
            print("i : ",i)
            id=i
    return id
class Item():
    id=get_id("DU")
    print(id)
    def __init__(self,name):
        self.name=name
        self.id=Item.id
        #Item.id +=1

class ChildItem():
    id=get_id("DOC")
    def __init__(self,name,parent):
        self.name=name
        self.parent=parent
        self.id=id
        ChildItem.id+=1



res1=execute_request(db_name,req1)
print(req1)
print("res1 : ",res1)
res2=execute_request(db_name,req2)
print(req2)
print("res2 : ",res2)

item1=Item("item1")
req3="INSERT INTO DU (du_id,name) VALUES ({0},\"{1}\")".format(item1.id,item1.name)
print(req3)
#res3=execute_request(db_name,req3)
#print("res3 : ",res3)

item2=Item("item2")
from_table="DU"

req4="SELECT * FROM {0}".format(from_table)
print(req4)
#res4=execute_request(db_name,req4)
#print("res4",res4)

"""
def insert_format_request(table,*args):
    req="INSERT INTO "
    req+=table
    req+=" VALUES "
    tmp_str=""
    for i in range(len(args)):
        tmp_str+="({"+str(i)+"}"
        if i != len(args)-1:
            tmp_str += ","
        #else:
        #    req+=")"
    tmp_str+=").format("
    for j in range(len(args)):
        tmp_str+=str(args[j])
        if j != len(args)-1:
            tmp_str+=","
    tmp_str+=")"
    print(tmp_str)
    tmp_str=eval(tmp_str)
    print(tmp_str)
    req+=tmp_str+")"
    print(req)
    return req
req4= insert_format_request("DU",item2.id,item2.name)
res4=execute_request(db_name,req4)
print("res4 : ",res4)
"""
