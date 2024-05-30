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

"""
to do :
    create fct "log" => a ajouter a chaque fonction qui fait evoluer le message global
    ne pas oublier d'ajouter et retirer les infos en DB aussi !
    system de reste :
        exemple =>  fichier="my file\nsecond line"
                    cmd = cat fichier| grep $$ (fin de ligne)
                    process = take the file to read it(t0), filter with grep(t1)
                    result =  "my file\n"
                    rest = "second line"
                    solution : passer par un fichier json(dont un dico pour chaque fichier) + (temporaire ?)
    add prefix to terminal + path +suffix
    add liste
    add context menu
    create block (cf doc_UI.py and doc.py)
    doucle click on listItem => does it have a doc linked ? No => Does It have a link ? (No => does it exist somewhere in db ?) => No => search on default engine.
    add link to doc to item /block / (list is a block ?) or url
    self.... with "with self"?
"""

class MainWindow(qtw.QWidget):
    def __init__(self):

        super().__init__()
        self.list_TreeViewItem=[]
        self.buffer=""

        # Window general items
        self.setWindowTitle("Edit Doc App")
        self.main_grid=qtw.QGridLayout()
        self.main_groupBox=qtw.QGroupBox("Main Group Box")
        self.main_layout=qtw.QVBoxLayout()
        self.hbox1=qtw.QHBoxLayout()
        self.gp_hbox1=qtw.QGroupBox()
        self.hbox2=qtw.QHBoxLayout()
        self.gp_hbox2=qtw.QGroupBox()

        #Top of the window

        #Menu
        self.menu=qtw.QMenuBar()

        self.action1=qtw.QAction("File")
        self.action2=qtw.QAction("In")
        self.action12=qtw.QAction("New Tab")
        self.action3=qtw.QAction("New Doc")
        self.action4=qtw.QAction("New Block")
        self.action5=qtw.QAction("New Unik Doc")

        self.action6=qtw.QAction("Tools")
        self.action7=qtw.QAction("Terminal")
        self.action8=qtw.QAction("Doc")
        self.action9=qtw.QAction("Helper")
        self.action10=qtw.QAction("App")
        self.action11=qtw.QAction("DB")


        self.menu_file=qtw.QMenu("File")
        self.menu_setting=qtw.QMenu("Setting")

        self.menu_file.addAction(self.action1)
        self.menu_file.addAction(self.action3)
        self.menu_file.addAction(self.action4)
        self.menu_file.addAction(self.action5)

        self.menu_setting.addAction(self.action6)
        self.menu_setting.addAction(self.action7)
        self.menu_setting.addAction(self.action8)
        self.menu_setting.addAction(self.action9)
        self.menu_setting.addAction(self.action11)
        self.menu_setting.addAction(self.action10)

        self.sub_menu_file=qtw.QMenu("Open")
        self.sub_menu_file.addAction(self.action12)
        self.sub_menu_file.addAction(self.action2)
        #self.menu_file.setObjectName("File_ObjectName")
        self.menu_file.addMenu(self.sub_menu_file)

        self.menu.addMenu(self.menu_file)


        self.menu.addMenu(self.menu_setting)


        self.main_grid.addWidget(self.menu)

        #Tree items
        self.tree_layout=qtw.QVBoxLayout()
        self.tree_groupBox=qtw.QGroupBox("Tree")
        self.tree_groupBox.setLayout(self.tree_layout)
        self.hbox1.addWidget(self.tree_groupBox)

        #Tabs
        self.tree_tabwidget=qtw.QTabWidget()
        #Tab 1
        self.tree_tab1=qtw.QWidget()
        self.tree_tabwidget.addTab(self.tree_tab1,"UD List")
        self.tree_tab_vbox1=qtw.QVBoxLayout()
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
        self.tree_tab2.setLayout(self.tree_tab_vbox2)
        self.tree_tabwidget.addTab(self.tree_tab2,"DB")
        # Widget tab2

        #change tab text : self."tabWidget".setTabText(<name>)

        #add Tabs to vbox
        self.tree_layout.addWidget(self.tree_tabwidget)

        #Doc items
        self.doc_layout=qtw.QVBoxLayout()
        self.doc_groupBox=qtw.QGroupBox("Doc")
        self.doc_groupBox.setLayout(self.doc_layout)
        self.hbox1.addWidget(self.doc_groupBox)

        self.doc_tabwidget=qtw.QTabWidget()

        #Tab 1
        self.tab1=qtw.QWidget()
        self.doc_tabwidget.addTab(self.tab1,"DU1")
        self.tab_hbox1=qtw.QHBoxLayout()
        self.tab1.setLayout(self.tab_hbox1)
        # Widget tab1


        #Tab2
        self.tab2=qtw.QWidget()
        self.tab_hbox2=qtw.QHBoxLayout()
        self.tab2.setLayout(self.tab_hbox2)
        self.doc_tabwidget.addTab(self.tab2,"DU1/doc2")
        # Widget tab2

        #Tab3
        self.tab3=qtw.QWidget()
        self.tab_hbox3=qtw.QHBoxLayout()
        self.tab3.setLayout(self.tab_hbox3)
        self.doc_tabwidget.addTab(self.tab3,"DU1/doc2/block3")
        # Widget tab3

        #add Tabs to vbox
        self.doc_layout.addWidget(self.doc_tabwidget)

        self.editDoc=qtw.QTextEdit()
        self.tab_hbox1.addWidget(self.editDoc)

        # Help items
        self.help_layout=qtw.QVBoxLayout()
        self.help_groupBox=qtw.QGroupBox("Helper")
        self.help_groupBox.setLayout(self.help_layout)
        #### !!!!
        self.hbox1.addWidget(self.help_groupBox)

        ##################################""
        # Tabs
        self.helper_tabwidget=qtw.QTabWidget()
        #Tab Manager
        self.helper_tab1=qtw.QWidget()
        self.helper_tabwidget.addTab(self.helper_tab1,"ManAger")
        self.helper_tab_vbox1=qtw.QVBoxLayout()
        self.helper_tab1.setLayout(self.helper_tab_vbox1)

        # Widget ManAger
        #self.btn=qtw.QPushButton("Hi i'm in tab1")
        #self.helper_tab_hbox1.addWidget(self.btn)
        """
        change name here !!
        """
        self.manager_tabwidget=qtw.QTabWidget()
        #Lister
        self.lister=qtw.QWidget()
        self.manager_tabwidget.addTab(self.lister,"Lister")
        self.m_tab_vbox1=qtw.QVBoxLayout()
        self.lister.setLayout(self.m_tab_vbox1)
        # Widget Lister
        # Tabs
        self.manager_list=qtw.QListWidget()
        self.btn_add_item=qtw.QPushButton("Add Item",clicked=lambda: self.add_list_item())
        self.entry_item=qtw.QLineEdit()
        self.tab_list=qtw.QTabWidget()
        #Tab 1
        self.list1=qtw.QWidget()
        self.tab_list.addTab(self.list1,"list1")
        self.tab_hbox1=qtw.QHBoxLayout()
        self.list1.setLayout(self.tab_hbox1)
        # Widget list1

        #add Tabs to vbox
        self.m_tab_vbox1.addWidget(self.tab_list)

        self.m_tab_vbox1.addWidget(self.entry_item)
        self.m_tab_vbox1.addWidget(self.btn_add_item)
        self.tab_hbox1.addWidget(self.manager_list)

        #Tab Info (Manager)
        self.info=qtw.QWidget()
        self.m_tab_vbox2=qtw.QVBoxLayout()
        self.info.setLayout(self.m_tab_vbox2)
        self.manager_tabwidget.addTab(self.info,"Info")
        # Widget Info

        self.editInfo=qtw.QTextEdit()
        self.m_tab_vbox2.addWidget(self.editInfo)
        self.editInfo.setText("Here the info of your system or else (see setup)")

        #Tab Note (Manager)
        self.note=qtw.QWidget()
        self.m_tab_vbox3=qtw.QVBoxLayout()
        self.note.setLayout(self.m_tab_vbox3)
        self.manager_tabwidget.addTab(self.note,"Note")
        # Widget tab2

        self.editNote=qtw.QTextEdit()
        self.m_tab_vbox3.addWidget(self.editNote)
        self.editNote.setText("Here you can take some note")

        #Tab ShortCut (Manager)
        self.shortcut=qtw.QWidget()
        self.m_tab_vbox4=qtw.QVBoxLayout()
        self.shortcut.setLayout(self.m_tab_vbox4)
        self.manager_tabwidget.addTab(self.shortcut,"ShortCut")
        # Widget shortucut
        self.label=qtw.QLabel("Show the shortCuts \n(maybe in a tree(env,apps...))")
        self.m_tab_vbox4.addWidget(self.label)

        #add Tabs to vbox
        self.helper_tab_vbox1.addWidget(self.manager_tabwidget)

        # Helpinguin
        self.helper_helpin=qtw.QWidget()
        self.helper_tab_vbox2=qtw.QVBoxLayout()
        self.helper_helpin.setLayout(self.helper_tab_vbox2)
        self.helper_tabwidget.addTab(self.helper_helpin,"Hel Pinguin")

        self.hp_tabwidget=qtw.QTabWidget()
        #Tab Error Handler
        self.hp_tab1=qtw.QWidget()
        self.hp_tabwidget.addTab(self.hp_tab1,"Err. Handler")
        self.hp_tab_vbox1=qtw.QVBoxLayout()
        self.hp_tab1.setLayout(self.hp_tab_vbox1)
        # Widget Error Handler
        self.error_list=qtw.QListWidget()
        self.error_text=qtw.QTextEdit()
        self.error_text.setText("Here you can set up my comportement\nin case of error in terminal\n(list of error managed add item/comment/comportement)")
        self.error_cbb=qtw.QComboBox(self)
        self.error_cbb.addItem("Error List Handler",0)#Qtw.Object()
        self.error_cbb.addItem("Error printing",1)
        self.error_list_btn=qtw.QPushButton("Add new error (print only if list)")# if prefix == "python" =>handle python error!
        # topLevel => name , comment ,type , comportement,(context ?)
        """
        if "state" of cbb = 0:
            btn + list visible"
            text not
        elif "state" =1:
            text visible
            btn + list not
        """
        self.hp_tab_vbox1.addWidget(self.error_cbb)
        self.hp_tab_vbox1.addWidget(self.error_list_btn)
        self.hp_tab_vbox1.addWidget(self.error_list)
        self.hp_tab_vbox1.addWidget(self.error_text)
        #Tab Displayer
        self.hp_tab2=qtw.QWidget()
        self.hp_tab_vbox2=qtw.QVBoxLayout()
        self.hp_tab2.setLayout(self.hp_tab_vbox2)
        self.hp_tabwidget.addTab(self.hp_tab2,"Displayer")
        # Widget Displayer
        self.label=qtw.QLabel("There are displayed possibilities\n(at the moment for Terminal and Doc (by type ?))\n need to know where cursor is!\n add extension system .py = python\n related to bin and var env ")
        self.hp_tab_vbox2.addWidget(self.label)

        #Tab Watcher
        self.hp_tab3=qtw.QWidget()
        self.hp_tabwidget.addTab(self.hp_tab3,"Watcher")
        self.hp_tab_vbox3=qtw.QVBoxLayout()
        self.hp_tab3.setLayout(self.hp_tab_vbox3)
        # Widget Watcher
        self.label1=qtw.QLabel("Here you can watch file change")
        self.hp_tab_vbox3.addWidget(self.label1)
        # Tabs
        self.watchers=qtw.QTabWidget()
        #Tab 1
        self.w_tab1=qtw.QWidget()
        self.watchers.addTab(self.w_tab1,"file1")
        self.w_tab_hbox1=qtw.QHBoxLayout()
        self.w_tab1.setLayout(self.w_tab_hbox1)
        # Widget tab1
        self.btn=qtw.QPushButton("Hi i'm in tab1")
        self.w_tab_hbox1.addWidget(self.btn)

        #Tab2
        self.w_tab2=qtw.QWidget()
        self.w_tab_hbox2=qtw.QHBoxLayout()
        self.w_tab2.setLayout(self.w_tab_hbox2)
        self.watchers.addTab(self.w_tab2,"file2")
        # Widget tab2
        self.label=qtw.QLabel("Hi i'm in tab2")
        self.w_tab_hbox2.addWidget(self.label)

        #add Tabs to vbox
        self.hp_tab_vbox3.addWidget(self.watchers)

        #Tab Manual
        self.hp_tab4=qtw.QWidget()
        self.hp_tabwidget.addTab(self.hp_tab4,"Help")
        self.hp_tab_vbox4=qtw.QVBoxLayout()
        self.hp_tab4.setLayout(self.hp_tab_vbox4)
        # Widget Manual
        self.label3=qtw.QLabel("Here manual is displayed")
        self.hp_tab_vbox4.addWidget(self.label3)

        self.helper_tab_vbox2.addWidget(self.hp_tabwidget)
        #Tab Modification
        self.hp_tab5=qtw.QWidget()
        self.hp_tabwidget.addTab(self.hp_tab5,"Mod Follower")
        self.hp_tab_vbox5=qtw.QVBoxLayout()
        self.hp_tab5.setLayout(self.hp_tab_vbox5)
        # Widget Manual
        self.label3=qtw.QLabel("Here the previous state of the current doc are displayed")
        self.hp_tab_vbox5.addWidget(self.label3)

        self.helper_tab_vbox2.addWidget(self.hp_tabwidget)

        # Widget helpinguin
        #self.label=qtw.QLabel("Hi i'm in the tab helpinguin")
        #self.helper_tab_hbox2.addWidget(self.label)



        #add Tabs to layout
        self.help_layout.addWidget(self.helper_tabwidget)

        ##############################################
        #Terminal items
        self.terminal_layout=qtw.QVBoxLayout()
        self.terminal_groupBox=qtw.QGroupBox("Terminal")
        self.terminal_groupBox.setLayout(self.terminal_layout)
        self.hbox2.addWidget(self.terminal_groupBox)

        self.terminalOutput=qtw.QTextEdit()
        self.terminalInput=qtw.QLineEdit()
        self.terminalValid=qtw.QPushButton("Enter",clicked=lambda : self.enter())
        self.terminal_layout.addWidget(self.terminalOutput)
        self.terminal_layout.addWidget(self.terminalInput)
        self.terminal_layout.addWidget(self.terminalValid)

        #Tool items
        #self.tool_layout=qtw.QGridLayout()

        self.tool_layout=qtw.QVBoxLayout()
        self.tool_groupBox=qtw.QGroupBox("Tool")
        self.tool_groupBox.setLayout(self.tool_layout)
        self.hbox2.addWidget(self.tool_groupBox)

        self.tool_tabwidget=qtw.QTabWidget()
        #Tab Tool tree
        self.tool_tab1=qtw.QWidget()
        self.tool_tabwidget.addTab(self.tool_tab1,"Tree Tool")
        self.tool_tab_vbox1=qtw.QVBoxLayout()
        self.tool_tab1.setLayout(self.tool_tab_vbox1)
        # Widget tab tree


        #Tab Tool Doc
        self.tool_tab2=qtw.QWidget()
        self.tool_tab_vbox2=qtw.QVBoxLayout()
        self.tool_tab2.setLayout(self.tool_tab_vbox2)
        self.tool_tabwidget.addTab(self.tool_tab2,"Doc Tool")
        # Widget tab doc

        # Tab tool Helper
        self.tool_tab3=qtw.QWidget()
        self.tool_tabwidget.addTab(self.tool_tab3,"Helper Tool")
        self.tool_tab_vbox1=qtw.QVBoxLayout()
        self.tool_tab3.setLayout(self.tool_tab_vbox1)
        # Widget tab helper
        self.btn_remove_item=qtw.QPushButton("Remove Item")
        self.tool_tab_vbox1.addWidget(self.btn_remove_item)
        # Tab tool Terminal
        self.tool_tab1=qtw.QWidget()
        self.tool_tabwidget.addTab(self.tool_tab1,"Terminal Tools")
        self.tool_tabwidget.setObjectName("ToolTabWidget")
        self.tool_tab_vbox1=qtw.QVBoxLayout()
        self.tool_tab1.setLayout(self.tool_tab_vbox1)
        # Widget tab terminal
        self.terminalClear=qtw.QPushButton("Clear",clicked=lambda : self.clear())
        self.tool_tab_vbox1.addWidget(self.terminalClear)
        #add Tabs to vbox
        self.tool_layout.addWidget(self.tool_tabwidget)

        #Global tools maybe in a status bar ? !!! sure!(not the cbb)
        self.target_cbb=qtw.QComboBox()
        self.target_cbb.addItem("Current Doc")
        self.target_cbb.addItem("Terminal")
        self.global_tool_grid=qtw.QGridLayout()
        self.global_tool_gb=qtw.QGroupBox("Global Tools")
        self.global_tool_gb.setLayout(self.global_tool_grid)
        self.tool_layout.addWidget(self.global_tool_gb)
        self.tool1=qtw.QPushButton("tool1")
        self.tool2=qtw.QPushButton("tool2")

        #Message
        self.message_label=qtw.QLabel()

        self.global_tool_grid.addWidget(self.target_cbb,0,1)
        self.global_tool_grid.addWidget(self.message_label,0,0)
        self.global_tool_grid.addWidget(self.tool1,1,0)
        self.global_tool_grid.addWidget(self.tool2,1,1)

        # here current index of each tabs
        # to update !!!
        self.tool_tabwidget.currentChanged.connect(self.changingToolTab)
        self.hp_tabwidget.currentChanged.connect(self.changingHelPinguinTab)
        self.manager_tabwidget.currentChanged.connect(self.changingManagerTab)
        self.tree_tabwidget.currentChanged.connect(self.changingTreeTab)
        self.helper_tabwidget.currentChanged.connect(self.changingHelperTab)
        self.doc_tabwidget.currentChanged.connect(self.changingDocTab)


        # Event
        self.action1.triggered.connect(lambda: self.message_label.setText("action1 triggered"))
        self.action2.triggered.connect(lambda: self.clicker())
        self.action3.triggered.connect(lambda: self.new_doc_in_new_tab(self.doc_tabwidget))
        self.action4.triggered.connect(lambda: self.new_block_in_new_tab(self.doc_tabwidget))
        self.action5.triggered.connect(lambda: self.new_UD(self.doc_tabwidget))
        #to layout add group box AND to group box set a layout(child)
        # <LAYOUT>.addWidget(<GroupBox>)
        # <GroupBox>.setLayout(<Child Layout>)
        self.main_layout.addWidget(self.gp_hbox1)
        self.main_layout.addWidget(self.gp_hbox2)

        self.gp_hbox1.setLayout(self.hbox1)
        self.gp_hbox2.setLayout(self.hbox2)

        self.main_grid.addWidget(self.main_groupBox)
        self.main_groupBox.setLayout(self.main_layout)
        self.setLayout(self.main_grid)
        self.print_name()
        self.show()

    def fillTree(self,parent,name):
        item=qtw.QTreeWidgetItem(parent)
        item.setText(0,name)
        self.list_TreeViewItem.append(item)
        return item
        #exec("self."+name+"=item")

    def clicker(self):
        fname=qtw.QFileDialog.getOpenFileName(self,"Open File","","TXT Files (*.txt)") # All FIles (*)
        #C:\\\Users\\gaeta\\OneDrive\\Documents\\prog\\Edit_Doc\\
        #print(fname[0])
        if fname[0] != '':
            with open(fname[0],"r+") as file:
                #lines=file.readlines()
                #print(file)
                for line in file :
                    print(line)
                    self.buffer += line
                print(self.buffer)
                self.editDoc.setPlainText(self.buffer)

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

    def changingTreeTab(self):
        print("index of Tree tab changed to :", self.tree_tabwidget.currentIndex())
    def changingHelperTab(self):
        print("index of Helper tab changed to :", self.helper_tabwidget.currentIndex())
    def changingToolTab(self):
        print("index of Tool tab changed to :", self.tool_tabwidget.currentIndex())
    def changingManagerTab(self):
        print("index of ManAdagertab changed to :", self.manager_tabwidget.currentIndex())
    def changingHelPinguinTab(self):
        print("index of HP tab changed to :", self.hp_tabwidget.currentIndex())
    def changingDocTab(self):
        print("index of Doc tab changed to :", self.doc_tabwidget.currentIndex())

    def print_name(self):
        # recursively to load list_of_objects !!! this allow to load the combo of object to target
        for child in self.findChildren(qtw.QTabWidget):
            print(child.objectName())
            #print(f'get check state : {child.checkState()}')

    def auto_name(self):
        #x="object"+str(self.id)
        x="object"
        return x
    def new_tab(self,parent):
        print("adding a new tab")
        parent.addTab(qtw.QWidget(),"New tab")
    def new_doc_in_new_tab(self,parent):
        x=self.new_tab(parent)
        # +doc type param doc()
        return x
    def new_block_in_new_tab(self,parent):
        x=self.new_tab(parent)
        # + Block type param Block()
    def new_UD(self,parent):
        x=self.new_tab(parent)
        # + UD type param UD()
        return x
    def add_list(self):
        #add a list in a new tab to the lister
        pass
    def add_list_item(self):
        if self.entry_item.text() != '':
            item = self.entry_item.text()
            self.manager_list.addItem(item)
            self.entry_item.clear()

app=qtw.QApplication(sys.argv)
mw=MainWindow()
app.exec_()