import PyQt5.QtWidgets as qtw
import sys
#import os
#import re
#import time
#import create as cr
import app_menu as am
import app_helper as ah
import app_tree as atr
import app_editDoc as ae
import app_terminal as ate
import app_tools as ato
#import asyncio

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

def comment():
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
    pass

class MainWindow(qtw.QWidget):
    def __init__(self):

        super().__init__()
        self.list_TreeViewItem=[]
        self.buffer=""
        self.top_window_info={}

        # Window general items
        self.setWindowTitle("Edit Doc App V4")
        self.main_grid=qtw.QGridLayout()
        self.main_grid.setSpacing(0)
        self.main_groupBox=qtw.QGroupBox("Main Group Box")

        self.main_layout=qtw.QVBoxLayout()
        self.main_layout.setSpacing(0)
        self.hbox1=qtw.QHBoxLayout()
        #print(self.hbox1.spacing())
        self.hbox1.setSpacing(0)
        self.gp_hbox1=qtw.QGroupBox()
        self.hbox2=qtw.QHBoxLayout()
        self.hbox2.setSpacing(0)
        self.gp_hbox2=qtw.QGroupBox()

        self.menu=am.Menu(self)
        self.helper=ah.Helper(self)
        self.tree=atr.Tree(self)
        self.editDoc=ae.EditDoc(self)
        self.terminal=ate.Terminal(self)
        self.tools=ato.Tools(self)

        self.main_layout.addWidget(self.menu)
        self.hbox1.addWidget(self.tree)
        self.hbox1.addWidget(self.editDoc)
        self.hbox1.addWidget(self.helper)
        self.hbox2.addWidget(self.terminal)
        self.hbox2.addWidget(self.tools)

        self.main_layout.addWidget(self.gp_hbox1)
        self.main_layout.addWidget(self.gp_hbox2)

        self.gp_hbox1.setLayout(self.hbox1)
        self.gp_hbox2.setLayout(self.hbox2)

        self.main_grid.addWidget(self.main_groupBox)
        self.main_groupBox.setLayout(self.main_layout)
        self.setLayout(self.main_grid)
        self.print_name()
        self.show()

    def addLog(self,event):
        self.helper.helpinguin.watcher.app_log.addItem(event)
        with open("log.txt","a") as log:
            #add time
            str_to_write=event + "\n"
            log.write(str_to_write)
    """
    def fillTree(self,parent,name):
        item=qtw.QTreeWidgetItem(parent)
        item.setText(0,name)
        self.list_TreeViewItem.append(item)
        return item
        #exec("self."+name+"=item")


    def clear(self):
        self.terminalOutput.clear()
    """
    def add_item_to_list(self,list,toAdd):
        list.addItem(toAdd)
        event="item added to "+list.objectName()
        self.addLog(event)
    """
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
    """
    def print_name(self):
        # recursively to load list_of_objects !!! this allow to load the combo of object to target
        for child in self.findChildren(qtw.QTabWidget):
            print(child.objectName())
            #print(f'get check state : {child.checkState()}')

    def auto_name(self):
        #x="object"+str(self.id)
        x="object"
        return x

    def new_tab(self,parent,name):
        print(f"adding a new tab to : {parent}")
        parent.addTab(qtw.QWidget(),name)
    """
    def new_BlockType(self,parent):
        print("adding a block type !")
        form = cr.Form_Create_Block_Type(self)
        # +doc type param doc()
        #return x

    def last_block_created(self):
        self.new_block_in_new_tab(self.doc_tabwidget,True)

    def new_block_in_new_tab(self,parent,id_exist=False):
        if id_exist == False:
            form = cr.Form_Create_Block(self)
        else:
            result=cr.db.select_one_record("block",f"block_id = {self.entry_last_item_created.text()}")
            print(result)
            cols=cr.db.show_columns_name("block")
            print(cols)
            str="block_name"
            flag=None
            name="New Unamed Tab"
            for i in range(len(cols)):
                if cols[i] == str:
                    flag=i
            if flag != None:
                name=result[0][flag]
            x=self.new_tab(parent,name)
        # + Block type param Block()

    def new_Theme(self,parent):
        print("adding a new theme !")
        form = cr.Form_Create_Theme(self)
    """
    def add_list(self):
        #add a list in a new tab to the lister
        pass
    """
    def add_list_item(self):
        if self.entry_item.text() != '':
            item = self.entry_item.text()
            self.manager_list.addItem(item)
            self.entry_item.clear()
    """
app=qtw.QApplication(sys.argv)
mw=MainWindow()
sys.exit(app.exec_())
