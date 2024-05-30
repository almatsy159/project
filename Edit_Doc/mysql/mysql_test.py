import mysql.connector as mc
import mysql

print(dir(mysql))
print("#######################################################################")
db_name = "tests"
def try_db(db_name):
    flag_db=0
    try:
        connection=mc.connect(user="root",password="",host="localhost")
        cursor=connection.cursor()
        cursor.execute("SHOW DATABASES;")
        x=cursor.fetchall()
        print(x)
        for i in x:
            for j in i:
                if j == db_name:
                    flag_db = 1
        connection.close()
    except mc.Error as err:
        print(err)
    finally:
        print("flag =",flag_db)
    return flag_db

def try_table(db_name,table_name):
    flag_table=0
    try:
        connection=mc.connect(user="root",password="",host="localhost",database=db_name)
        cursor=connection.cursor()
        cursor.execute("SHOW TABLES;")
        x=cursor.fetchall()
        print(x)
        for i in x:
            for j in i:
                if j == table_name:
                    flag_table = 1
        connection.close()
    except mc.Error as err:
        print(err)
    finally:
        #print("flag =",flag_table)
        pass
    return flag_table

def execute_request(req,db):

    connection=mc.connect(user="root",password="",host="localhost",database=db)
    cursor=connection.cursor()
    cursor.execute(req)
    x=cursor.fetchall()
    connection.commit()
    connection.close()
    return x

flag_db=try_db(db_name)

if flag_db == 0:
    req0= "CREATE DATABASE  {0};".format(db)
    res0=execute_request(req0)
    print(res0)


table_name="test1"
flag_table=try_table(db_name,table_name)
if flag_table ==0:

    req1="CREATE TABLE test1 (id INT PRIMARY KEY, name VARCHAR(50) NOT NULL);"
    res1=execute_request(req1,db_name)
    print(res1)

req3="SELECT * FROM test1"
res3=execute_request(req3,db_name)
print(res3)

req4="SELECT COUNT(*) FROM test1"
res4=execute_request(req4,db_name)
print(res4)
for i in res4:
    for j in i:
        print(j)
        next_id=j+1
row_name="\"row{0}\"".format(next_id)
req2="INSERT INTO test1 (id,name) VALUES ({0},{1});".format(next_id,row_name)
res2=execute_request(req2,db_name)
print(res2)
