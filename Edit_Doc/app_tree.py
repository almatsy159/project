import PyQt5.QtWidgets as qtw

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

class Tree(qtw.QWidget):
    def __init__(self,parent):
        self.parent=parent
        super().__init__()
        self.list_TreeViewItem=[]

        #self.setWindowTitle("Edit Doc Menu")
        self.main_grid=qtw.QGridLayout()
        self.main_grid.setSpacing(0)
        #Tree items
        self.tree_layout=qtw.QVBoxLayout()
        self.tree_groupBox=qtw.QGroupBox("Tree")
        self.tree_groupBox.setLayout(self.tree_layout)
        self.main_grid.addWidget(self.tree_groupBox)

        #Tabs
        self.tree_tabwidget=qtw.QTabWidget()
        #Tab 1
        self.tree_tab1=qtw.QWidget()
        self.tree_tabwidget.addTab(self.tree_tab1,"UD List")
        self.tree_tab_vbox1=qtw.QVBoxLayout()
        self.tree_tab_vbox1.setSpacing(0)
        self.tree_tab1.setLayout(self.tree_tab_vbox1)
        # Widget tab1
        self.dbView=qtw.QTreeWidget()
        self.dbView.setColumnCount(1)
        #dbView.expandAll()
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
        #Tab2
        self.tree_tab2=qtw.QWidget()
        self.tree_tab_vbox2=qtw.QVBoxLayout()
        self.tree_tab_vbox2.setSpacing(0)
        self.tree_tab2.setLayout(self.tree_tab_vbox2)
        self.tree_tabwidget.addTab(self.tree_tab2,"DB")
        # Widget tab2

        #change tab text : self."tabWidget".setTabText(<name>)

        #add Tabs to vbox
        self.tree_layout.addWidget(self.tree_tabwidget)
        self.tree_tabwidget.currentChanged.connect(self.changingTreeTab)


        self.setLayout(self.main_grid)
        self.show()

    def fillTree(self,parent,name):
        item=qtw.QTreeWidgetItem(parent)
        item.setText(0,name)
        self.list_TreeViewItem.append(item)
        return item
            #exec("self."+name+"=item")

    def changingTreeTab(self):
        print("index of Tree tab changed to :", self.tree_tabwidget.currentIndex())

if __name__=="__main__":

    app = qtw.QApplication([])
    tree=Tree()
    app.exec_()
