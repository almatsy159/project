import mysql.connector as mc
import PyQt5.QtWidgets as qtw
import random as rd

import DB_Tree_Admin as dbadmin

listLambda=["item1","item2","item3"]
list_of_item=[]
doc1=["block1_d1","block2_d1","block3_d1"]
doc2=["block1_d2","block2_d2","block3_d2"]
doc3=["block1_d3","block2_d3","block3_d3"]
doc4=["block1_d4","block2_d4","block3_d4"]
doc5=["block1_d5","block2_d5","block3_d5"]
DU1={"doc1":doc1,"doc2":doc2}
DU2={"doc3":doc3,"doc4":doc4,"doc5":doc5}
DU_List={"DU1":DU1,"DU2":DU2}

class Connect_DB():
    def __init__(self,dbname,host='localhost',user='root',password=' '):
        self.db=dbname
        self.host=host
        self.user=user
        self.password=password

        #self.openConnexion()
        #self.closeConnexion()
    def openConnexion(self):
        self.connexion=mc.connect(database=self.db,host=self.host,user=self.user,password=self.password)
        self.cursor=self.connexion.cursor()

    def getNextId(self,table):
        x=dbadmin.getLastId(table)
        print("next_id : ",x)
        print(x,type(x))
        if x ==None:
            x=0
        return x+1
    def addItemIntoDB(self):
        x=self.getNextId("du")
        dbadmin.closeConnexion()
        dbadmin.openConnexion()

        name="DU"+str(self.getNextId("du"))
        dbadmin.insert_block("DU1")
        dbadmin.closeConnexion()
        dbadmin.openConnexion()

        name="Doc"+str(self.getNextId("doc"))
        dbadmin.insert_block(name,x,"doc")
        dbadmin.closeConnexion()
        dbadmin.openConnexion()

        name="Block"+str(self.getNextId("block"))
        dbadmin.insert_block(name,x)

        dbadmin.closeConnexion()

    def closeConnexion(self):
        self.connexion
        self.connexion.close()

#print(dir())
class DB_Tree(qtw.QWidget):
    def __init__(self):
        super().__init__()

        self.list_TreeViewItem=[]

        self.hbox1=qtw.QHBoxLayout()

        self.tree_layout=qtw.QVBoxLayout()
        self.tree_groupBox=qtw.QGroupBox("Tree")
        self.tree_groupBox.setLayout(self.tree_layout)
        self.hbox1.addWidget(self.tree_groupBox)

        #Tabs
        self.tree_tabwidget=qtw.QTabWidget()
        #Tab 1
        self.tree_tab1=qtw.QWidget()
        self.tree_tabwidget.addTab(self.tree_tab1,"UD")
        self.tree_tab_vbox1=qtw.QVBoxLayout()
        self.tree_tab_vbox1.setSpacing(0)
        self.tree_tab1.setLayout(self.tree_tab_vbox1)
        # Widget tab1
        self.dbView=qtw.QTreeWidget()
        self.dbView.setColumnCount(1)
        #dbView.expandAll()

        #Tab 2
        self.tree_tab2=qtw.QWidget()
        self.tree_tabwidget.addTab(self.tree_tab2,"DB")
        self.tree_tab_vbox2=qtw.QVBoxLayout()
        self.tree_tab_vbox2.setSpacing(0)
        self.tree_tab2.setLayout(self.tree_tab_vbox2)
        # Widget tab1
        self.dbView=qtw.QTreeWidget()
        self.dbView.setColumnCount(1)
        """
        self.tabDB=qtw.QTabWidget(self.dbView)
        #self.tabDB.setTabsClosable(True)
        self.tab1DB=qtw.QWidget()
        self.tabDB.addTab(self.tab1DB,"")
        self.tab2DB=qtw.QWidget()
        self.tabDB.addTab(self.tab2DB,"")
        """
        # Can't do better ??? maybe wait for db and structure of document ??
        for i,j in DU_List.items():
            x=self.fillTree(self.dbView,i)
            for k,l in j.items():
                sub_name=str(k)
                y=self.fillTree(x,k)
                for m in l:
                    self.fillTree(y,m)

        self.tree_tab_vbox1.addWidget(self.dbView)
        self.setLayout(self.hbox1)
        self.tree_layout.addWidget(self.tree_tabwidget)
        self.show()
        #print(__name__)
        if __name__=="__main__":
            #here tool inside vbox
            pass
        else:
            #here tool inside tools menu
            pass

    def fillTree(self,parent,name):
        item=qtw.QTreeWidgetItem(parent)
        item.setText(0,name)
        self.list_TreeViewItem.append(item)
        return item

if __name__ == "__main__":
    app=qtw.QApplication([])
    db=Connect_DB("du_db")
    #db.openConnexion()
    db.addItemIntoDB()
    #db.closeConnexion()
    main=DB_Tree()
    app.exec_()
