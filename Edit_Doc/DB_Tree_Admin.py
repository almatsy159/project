import mysql.connector as mc

# select du.name,doc.parent_id,doc.name from doc left outer join du on doc.parent_id=du.id;
#select du.name,block.parent_id,block.name from block left outer join du on block.parent_id=du.id;
if __name__=="__main__":

    conn = mc.connect(host='localhost',user='root',password='',database='du_db')
    c = conn.cursor()
else :
    conn = mc.connect(host='localhost',user='root',password='',database='du_db')
    c = conn.cursor()
    print("Connected")
#c.execute("CREATE TABLE if not exists {0}(id INT PRIMARY,name )".format())
def openConnexion():
    print("opening connexion")
    conn = mc.connect(database='du_db',user='root',password='',host='localhost')
    c = conn.cursor()
def insert_du(name):
    x="INSERT INTO du (name) VALUES (\"{0}\");".format(name)
    print(x)
    c.execute(x)
    print("DU inserted")

def getLastId(table):
    print("getting id")
    c.execute("SELECT COUNT(*) FROM {0};".format(table))
    x=c.fetchone()
    for i in x:
        print(i,type(i))
        return i
def insert_doc(name,parent_id):
    print("INSERT INTO doc (name,parent_id) VALUES (\"{0}\",{1})".format(name,parent_id))
    x="INSERT INTO doc (name,parent_id) VALUES (\"{0}\",{1})".format(name,parent_id)
    c.execute(x)
    print("Doc inserted")

def insert_block(name,parent_id=None,type=None):
    if parent_id == None :
        type="DU"
        insert_du(name)
        c.execute("INSERT INTO block (name,type) values (\"{0}\",\"{1}\")".format(name,type))
    elif type==None :
        type="Block"
        c.execute("INSERT INTO block (name,parent_id,type) values (\"{0}\",{1},\"{2}\")".format(name,parent_id,type))
    else:
        c.execute("INSERT INTO block (name,parent_id,type) values (\"{0}\",{1},\"{2}\")".format(name,parent_id,type))
        if type == "doc":
            insert_doc(name,parent_id)
        elif type == "DU":
            insert_du(name)
        else :
            pass
    print("Block inserted")

x=getLastId("du")+1
name="DU"+str(x)
insert_block(name)


x=getLastId("doc")
name="Doc"+str(x)
insert_block(name,x,"doc")

x=getLastId("block")
name="Block"+str(x)
insert_block(name,x)

def closeConnexion():

    if __name__=="__main__":

        conn.commit()
        conn.close()
    else:
        print("closing connexion")
        conn.commit()
        conn.close()

closeConnexion()
