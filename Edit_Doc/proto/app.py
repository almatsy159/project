import PyQt5.QtWidgets as qtw
import sys
import os

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



class MainWindow(qtw.QWidget):
    def __init__(self):
        super().__init__()
        self.list_TreeViewItem=[]
        self.setWindowTitle("Edit Doc App")
        self.main_layout=qtw.QGridLayout()
        self.main_groupBox=qtw.QGroupBox()

        self.grid=qtw.QGridLayout()
        self.menu=qtw.QMenuBar()
        self.action1=qtw.QAction("File")
        self.action2=qtw.QAction("As")
        self.menu_file=qtw.QMenu("File_QMenu")
        self.menu_file.addAction(self.action1)
        self.sub_menu_file=qtw.QMenu("Open")
        self.sub_menu_file.addAction(self.action2)
        #self.menu_file.setObjectName("File_ObjectName")
        self.menu.addMenu(self.menu_file)
        self.menu_file.addMenu(self.sub_menu_file)
        self.main_layout.addWidget(self.menu)
        self.message_label=qtw.QLabel()
        self.main_layout.addWidget(self.message_label)

        vbox1=qtw.QVBoxLayout()
        gp1=qtw.QGroupBox("Doc Data Base")
        vbox2=qtw.QVBoxLayout()
        gp2=qtw.QGroupBox("Unik Doc")
        vbox3=qtw.QHBoxLayout()
        gp3=qtw.QGroupBox("ManAger")
        hbox1=qtw.QHBoxLayout()
        gp4=qtw.QGroupBox("Terminal")
        hbox2=qtw.QGridLayout()
        gp5=qtw.QGroupBox("Tools")

        self.dbView=qtw.QTreeWidget()
        self.dbView.setColumnCount(1)
        #dbView.expandAll()
        self.tabDB=qtw.QTabWidget(self.dbView)
        #self.tabDB.setTabsClosable(True)
        self.tab1DB=qtw.QWidget()
        self.tabDB.addTab(self.tab1DB,"")
        self.tab2DB=qtw.QWidget()
        self.tabDB.addTab(self.tab2DB,"")

        for i,j in DU_List.items():
            x=self.fillTree(self.dbView,i)
            for k,l in j.items():
                sub_name=str(k)
                y=self.fillTree(x,k)
                for m in l:
                    self.fillTree(y,m)
        """
        item0=qtw.QTreeWidgetItem(dbView)
        item0.setText(0,"DU1")
        sub_item0=qtw.QTreeWidgetItem(item0)
        sub_item0.setText(0,"doc1")
        sub_sub_item0=qtw.QTreeWidgetItem(sub_item0)
        sub_sub_item0.setText(0,doc1[0])

        for i in range(len(doc1)):
            name=str(doc1[i])
            xname=name
            exec(name +"=qtw.QTreeWidgetItem(dbView)")
            #print(help(qtw.QTreeWidgetItem))
            exec(name+".setText(int(i),"+xname+")")
        """

        #print(dir(qtw.QTreeView()))
        vbox1.addWidget(self.dbView)

        self.editDoc=qtw.QTextEdit()
        vbox2.addWidget(self.editDoc)

        self.manager_list=qtw.QListWidget()
        self.btn_add_item=qtw.QPushButton("Add Item")
        self.btn_remove_item=qtw.QPushButton("Remove Item")
        self.entry_item=qtw.QLineEdit()

        vbox3.addWidget(self.entry_item)
        vbox3.addWidget(self.btn_add_item)
        vbox3.addWidget(self.btn_remove_item)
        vbox3.addWidget(self.manager_list)

        self.terminalOutput=qtw.QTextEdit()
        self.terminalInput=qtw.QLineEdit()
        self.terminalValid=qtw.QPushButton("Enter",clicked=lambda : self.enter())
        self.terminalClear=qtw.QPushButton("Clear",clicked=lambda : self.clear())
        hbox1.addWidget(self.terminalOutput)
        hbox1.addWidget(self.terminalInput)
        hbox1.addWidget(self.terminalValid)
        hbox1.addWidget(self.terminalClear)

        self.tool1=qtw.QPushButton("tool1")
        self.tool2=qtw.QPushButton("tool2")
        hbox2.addWidget(self.tool1)
        hbox2.addWidget(self.tool2)

        self.main_groupBox.setLayout(self.grid)
        gp1.setLayout(vbox1)
        gp2.setLayout(vbox2)
        gp3.setLayout(vbox3)
        gp4.setLayout(hbox1)
        gp5.setLayout(hbox2)

        self.main_layout.addWidget(self.main_groupBox)
        self.grid.addWidget(gp1,0,0)
        self.grid.addWidget(gp2,0,1)
        self.grid.addWidget(gp3,0,2)
        self.grid.addWidget(gp4,1,0)
        self.grid.addWidget(gp5,1,2)

        self.action1.triggered.connect(lambda: self.message_label.setText("action1 triggered"))
        self.action2.triggered.connect(lambda: self.clicker())

        #self.setLayout(self.grid)
        self.setLayout(self.main_layout)
        self.show()

    def fillTree(self,parent,name):
        item=qtw.QTreeWidgetItem(parent)
        item.setText(0,name)
        self.list_TreeViewItem.append(item)
        return item
        #exec("self."+name+"=item")

    def clicker(self):
        buffer=""
        fname=qtw.QFileDialog.getOpenFileName(self,"Open File","","TXT Files (*.txt)") # All FIles (*)
        #C:\\\Users\\gaeta\\OneDrive\\Documents\\prog\\Edit_Doc\\
        #print(fname[0])
        with open(fname[0],"r+") as file:
            #lines=file.readlines()
            #print(file)
            for line in file :
                print(line)
                buffer += line
            print(buffer)
            self.editDoc.setPlainText(buffer)

    def enter(self):
        #print(dir(qtw.QLineEdit))
        if self.terminalInput.text() != "":
            x=os.popen(self.terminalInput.text())
            self.terminalInput.clear()
            #print(x.read())
            #self.terminalOutput.setText(x.read())
            self.terminalOutput.insertPlainText(x.read())

    def clear(self):
        self.terminalOutput.clear()
app=qtw.QApplication(sys.argv)
mw=MainWindow()

app.exec_()
