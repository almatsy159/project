import mysql.connector as mc
import PyQt5.QtWidgets as qtw

# to devellop :create the class dynamicly (for new table ?) by getting all the colum of a table and cheking the existance of a key ?

class Form_Create_Block(qtw.QDialog):
    def __init__(self,parent=None):
        super().__init__()
        self.parent=parent
        self.id_block_created=""
        self.setWindowTitle("Create new block")
        self.main_layout=qtw.QGridLayout()


        self.l_Block_id=qtw.QLabel("Block ID :")
        self.e_Block_id=qtw.QLineEdit()
        self.e_Block_id.setText(str(db.next_id("block","block_id")))
        self.main_layout.addWidget(self.l_Block_id,0,0)
        self.main_layout.addWidget(self.e_Block_id,0,1)


        self.l_Block_name=qtw.QLabel("Block Name :")
        self.e_Block_name=qtw.QLineEdit()
        self.main_layout.addWidget(self.l_Block_name,1,0)
        self.main_layout.addWidget(self.e_Block_name,1,1)


        self.l_Type_id=qtw.QLabel("Type ID :")

        x0=db.select_all("block_type")
        self.type_cbb=qtw.QComboBox()
        y0=db.toDict_two_columnTable(x0)
        self.fill_cbb(self.type_cbb,y0)
        self.main_layout.addWidget(self.type_cbb,3,1)
        self.main_layout.addWidget(self.l_Type_id,3,0)
        #self.e_Type_id=qtw.QLineEdit()
        #self.main_layout.addWidget(self.e_Type_id,3,1)

        self.l_Parent_type=qtw.QLabel("Parent Type :")
        self.main_layout.addWidget(self.l_Parent_type,4,0)

        x3=db.select_all("block_type")
        self.parent_type_cbb=qtw.QComboBox()
        y3=db.toDict_two_columnTable(x3)
        self.fill_cbb(self.parent_type_cbb,y3)
        self.main_layout.addWidget(self.parent_type_cbb,4,1)


        self.l_Parent_id=qtw.QLabel("Parent ID:")
        self.e_Parent_id=qtw.QLineEdit()
        self.main_layout.addWidget(self.l_Parent_id,5,0)
        self.main_layout.addWidget(self.e_Parent_id,5,1)
        self.e_Parent_id.textChanged.connect(self.valid_parent_id)


        self.l_Theme_id=qtw.QLabel("Theme ID :")
        #self.e_Theme_id=qtw.QLineEdit()
        self.main_layout.addWidget(self.l_Theme_id,6,0)
        #self.main_layout.addWidget(self.e_Theme_id,5,1)

        x1=db.select_all("theme")
        self.theme_cbb=qtw.QComboBox()
        y1=db.toDict_two_columnTable(x1)
        self.fill_cbb(self.theme_cbb,y1)
        self.main_layout.addWidget(self.theme_cbb,6,1)


        self.l_Content_type_id=qtw.QLabel("Content Type ID :")
        #self.e_Content_type_id=qtw.QLineEdit()
        self.main_layout.addWidget(self.l_Content_type_id,7,0)
        #self.main_layout.addWidget(self.e_Content_type_id,6,1)
        x2=db.select_all("content_type")
        self.content_type_cbb=qtw.QComboBox()
        y2=db.toDict_two_columnTable(x2)
        self.fill_cbb(self.content_type_cbb,y2)
        self.main_layout.addWidget(self.content_type_cbb,7,1)

        self.l_Content_id=qtw.QLabel("Content ID :")
        self.e_Content_id=qtw.QLineEdit()
        self.main_layout.addWidget(self.l_Content_id,8,0)
        self.main_layout.addWidget(self.e_Content_id,8,1)


        self.l_lvl=qtw.QLabel("Level :")
        self.e_lvl=qtw.QLineEdit()

        self.main_layout.addWidget(self.l_lvl,9,0)
        self.main_layout.addWidget(self.e_lvl,9,1)

        self.valid=qtw.QPushButton("Valider",clicked=lambda : self.validate())
        self.main_layout.addWidget(self.valid,10,1)

        self.setLayout(self.main_layout)
        self.show()

    def fill_cbb(self,parent,dict):
        for i,j in dict.items():
            parent.addItem(j,i)

    def valid_parent_id(self):
        x=self.e_Parent_id.text()
        print("valeur de parent id :",x)
        if x != '':
            req=f"SELECT * FROM block WHERE block_id={x}"
            y=db.make_a_req(req)
            if y != None:
                for i in y:
                    z=i
                    self.get_parent_lvl(x)


    def get_parent_lvl(self,parent_id):
        req=f"SELECT lvl FROM block WHERE block_id = {parent_id}"
        x=db.make_a_req(req)
        for i in x:
            print(i)
        self.e_lvl.setText(str(i[0]+1))


    def validate(self):

        db.Connect_to_db()
        db.Open_Cursor()
        if self.e_Parent_id.text() == "":
            self.e_Parent_id.setText("Null")
        req=f"""INSERT INTO block (block_id,block_name,lvl,content_id,type_id,parent_id,theme_id,
        content_type_id) VALUES ({self.e_Block_id.text()},\"{self.e_Block_name.text()}\",{self.e_lvl.text()},
        {self.e_Content_id.text()},{self.type_cbb.currentText()},{self.e_Parent_id.text()},
        {self.theme_cbb.currentText()},{self.content_type_cbb.currentText()})
        """
        print(req)
        db.Exec_cursor(req)
        db.Conn_Close()
        self.id_block_created=self.e_Block_id.text()



class Form_Create_Content(qtw.QDialog):
    def __init__(self,parent=None):
        super().__init__()

        self.setWindowTitle("Create new content")
        self.main_layout=qtw.QGridLayout()

        self.l_Content_id=qtw.QLabel("Content ID :")
        self.e_Content_id=qtw.QLineEdit()
        self.main_layout.addWidget(self.l_Content_id,0,0)
        self.main_layout.addWidget(self.e_Content_id,0,1)

        self.l_Content_name=qtw.QLabel("Content Name :")
        self.e_Content_name=qtw.QLineEdit()
        self.main_layout.addWidget(self.l_Content_name,1,0)
        self.main_layout.addWidget(self.e_Content_name,1,1)

        self.l_Content=qtw.QLabel("Content :")
        self.e_Content=qtw.QTextEdit()
        self.main_layout.addWidget(self.l_Content,2,0)
        self.main_layout.addWidget(self.e_Content,2,1)

        self.l_Content_type_id=qtw.QLabel("Content Type ID :")
        self.e_Content_type_id=qtw.QLineEdit()
        self.main_layout.addWidget(self.l_Content_type_id,3,0)
        self.main_layout.addWidget(self.e_Content_type_id,3,1)

        self.l_Content_description=qtw.QLabel("Content Description :")
        self.e_Content_description=qtw.QTextEdit()
        self.main_layout.addWidget(self.l_Content_description,4,0)
        self.main_layout.addWidget(self.e_Content_description,4,1)

        self.valid=qtw.QPushButton("Valider",clicked=lambda : self.validate())
        self.main_layout.addWidget(self.valid,5,1)

        self.setLayout(self.main_layout)
        self.show()

    def validate(self):
        db.Connect_to_db()
        db.Open_Cursor()
        req=f"""INSERT INTO content (content_id,content_name,content,
        content_type_id,content_description) VALUES ({self.e_Content_id.text()},
        \"{self.e_Content_name.text()}\",\"{self.e_Content.toPlainText()}\",
        \"{self.e_Content_description.toPlainText()}\",{self.e_Content_type_id.text()})
        """
        db.Exec_cursor(req)
        db.Conn_Close()

class Form_Create_Theme(qtw.QDialog):
    def __init__(self,parent=None):
        super().__init__()

        self.setWindowTitle("Create new theme")
        self.main_layout=qtw.QGridLayout()

        self.l_Theme_id=qtw.QLabel("Theme ID :")
        self.e_Theme_id=qtw.QLineEdit()
        self.main_layout.addWidget(self.l_Theme_id,0,0)
        self.main_layout.addWidget(self.e_Theme_id,0,1)

        self.l_Theme_name=qtw.QLabel("Theme Name :")
        self.e_Theme_name=qtw.QLineEdit()
        self.main_layout.addWidget(self.l_Theme_name,1,0)
        self.main_layout.addWidget(self.e_Theme_name,1,1)

        self.valid=qtw.QPushButton("Valider",clicked=lambda : self.validate())
        self.main_layout.addWidget(self.valid,2,1)

        self.setLayout(self.main_layout)
        self.show()

    def validate(self):
        db.Connect_to_db()
        db.Open_Cursor()
        req=f"""INSERT INTO theme (theme_id,theme_name)
        VALUES ({self.e_Theme_id.text()},\"{self.e_Theme_name.text()}\")
        """
        db.Exec_cursor(req)
        db.Conn_Close()


class Form_Create_Block_Type(qtw.QDialog):
    def __init__(self,parent=None):
        super().__init__()

        self.setWindowTitle("Create new type of block")
        self.main_layout=qtw.QGridLayout()

        self.l_Type_id=qtw.QLabel("Type ID :")
        self.e_Type_id=qtw.QLineEdit()
        self.main_layout.addWidget(self.l_Type_id,0,0)
        self.main_layout.addWidget(self.e_Type_id,0,1)

        self.l_Type_name=qtw.QLabel("Type Name :")
        self.e_Type_name=qtw.QLineEdit()
        self.main_layout.addWidget(self.l_Type_name,1,0)
        self.main_layout.addWidget(self.e_Type_name,1,1)

        self.valid=qtw.QPushButton("Valider",clicked=lambda : self.validate())
        self.main_layout.addWidget(self.valid,2,1)

        self.setLayout(self.main_layout)
        self.show()

    def validate(self):
        db.Connect_to_db()
        db.Open_Cursor()
        req=f"""INSERT INTO block_type (type_id,type_name)
        VALUES ({self.e_Type_id.text()},\"{self.e_Type_name.text()}\")
        """
        db.Exec_cursor(req)
        db.Conn_Close()


class Form_Create_Content_Type(qtw.QDialog):
    def __init__(self,parent=None):
        super().__init__()

        self.setWindowTitle("Create new content type")
        self.main_layout=qtw.QGridLayout()

        self.l_Content_type_id=qtw.QLabel("Content_type ID :")
        self.e_Content_type_id=qtw.QLineEdit()
        self.main_layout.addWidget(self.l_Content_type_id,0,0)
        self.main_layout.addWidget(self.e_Content_type_id,0,1)

        self.l_Content_type_name=qtw.QLabel("Content_type Name :")
        self.e_Content_type_name=qtw.QLineEdit()
        self.main_layout.addWidget(self.l_Content_type_name,1,0)
        self.main_layout.addWidget(self.e_Content_type_name,1,1)

        self.valid=qtw.QPushButton("Valider",clicked=lambda : self.validate())
        self.main_layout.addWidget(self.valid,2,1)

        self.setLayout(self.main_layout)
        self.show()

    def validate(self):
        db.Connect_to_db()
        db.Open_Cursor()
        req=f"""INSERT INTO content_type (content_type_id,content_type_name)
        VALUES ({self.e_Content_type_id.text()},\"{self.e_Content_type_name.text()}\")
        """
        db.Exec_cursor(req)
        db.Conn_Close()

class DB():
    def __init__(self,pwd,user,db,host):
        self.pwd=pwd
        self.user=user
        self.host=host
        self.db=db

    def Connect_to_db(self):
        self.conn=mc.connect(password=self.pwd,user=self.user,database=self.db,host=self.host)

    def Open_Cursor(self):
        self.cursor=self.conn.cursor()

    def init_db(self):
        self.Connect_to_db()
        self.Open_Cursor()

    def end_db(self,bool=False):
        if bool==True:
            self.cursor.fetchall()
        self.Conn_Close()

    def Exec_cursor(self,req):
        self.cursor.execute(req)

    def Conn_Close(self):
        self.conn.close()

    def make_a_req(self,req):
        self.Connect_to_db()
        self.Open_Cursor()
        self.cursor.execute(req)
        x=self.cursor.fetchall()
        self.Conn_Close()
        return x

    def select_all(self,table,osef=0):
        req=f"SELECT * FROM {table}"
        x=self.make_a_req(req)
        if osef != 0:
            print(f"from {table} :")
            for i in x:
                print(i)
            print("\n ########################## \n")
        return x

    def select_one(self,table,cond):
        req=f"SELECT * FROM {table} WHERE {cond}"
        x=self.make_a_req(req)
        return x

    def toDict_two_columnTable(self,list,osef=0):
        dict={}
        for i in list:
            dict[i[0]]=i[1]
        if osef != 0:
            print(dict)
        return dict

    def next_id(self,table,column):
        req=f"SELECT MAX({column}) FROM {table}"
        x=self.make_a_req(req)
        for i in x:
            #print(i[0])
            #print(f"resultat de max id pour {table} : {i}")
            y=i[0]
        return y+1


        #return i+1

if __name__=="__main__":
    app=qtw.QApplication([])
    db=DB("","root","editDoc","localhost")
    form0=Form_Create_Block()
    #form1=Form_Create_Content()
    #form2=Form_Create_Theme()
    #form3=Form_Create_Block_Type()
    #form4=Form_Create_Content_Type()
    #x=db.select_all("block")
    #print(x)
    app.exec_()
else :
    db=DB("","root","editDoc","localhost")
