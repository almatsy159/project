import PyQt5.QtWidgets as qtw

class Helper(qtw.QWidget):
    def __init__(self,parent):
        
        self.parent=parent
        super().__init__()
        self.help_layout=qtw.QVBoxLayout()
        self.main_layout=qtw.QHBoxLayout()
        self.help_groupBox=qtw.QGroupBox("Hey i'm the helper")
        self.help_groupBox.setLayout(self.help_layout)
        self.main_layout.addWidget(self.help_groupBox)

        # Helper tabs
        self.tabwidget=qtw.QTabWidget()
        # Manager tab
        self.tab1=qtw.QWidget()
        self.tabwidget.addTab(self.tab1,"Manager")
        self.tab_hbox1=qtw.QHBoxLayout()
        self.tab1.setLayout(self.tab_hbox1)

        # Widget ManAger
        self.manager=ManAger(self)
        self.tab_hbox1.addWidget(self.manager)

        # Helpinguin tab
        self.tab2=qtw.QWidget()
        self.tab_hbox2=qtw.QHBoxLayout()
        self.tab2.setLayout(self.tab_hbox2)
        self.tabwidget.addTab(self.tab2,"HelPinguin")
        # Widget helpinguin
        self.helpinguin=HelPinguin(self)
        self.tab_hbox2.addWidget(self.helpinguin)

        #add Tabs to vbox
        self.help_layout.addWidget(self.tabwidget)
        #self.hp_tabwidget.currentChanged.connect(self.changingHelPinguinTab)
        #self.manager_tabwidget.currentChanged.connect(self.changingManagerTab)
        #self.helper_tabwidget.currentChanged.connect(self.changingHelperTab)

        self.setLayout(self.main_layout)
        self.show()

    def addLog(self,event):
        self.helpinguin.watcher.app_log.addItem(event)
        with open("log.txt","a") as log:
            #add time
            str_to_write=event + "\n"
            log.write(str_to_write)

    def add_item_to_list(self,list,toAdd):
        list.addItem(toAdd)
        event="item added to "+list.objectName()
        self.addLog(event)


    def changingHelperTab(self):
        print("index of Helper tab changed to :", self.helper_tabwidget.currentIndex())




class ManAger(qtw.QWidget):
    def __init__(self,parent):
        super().__init__()
        self.parent=parent
        self.manager_tabwidget=qtw.QTabWidget()
        #Lister
        self.lister=Lister()
        self.manager_tabwidget.addTab(self.lister,"Lister")
        #Tab Info (Manager)
        self.info=Info()
        self.manager_tabwidget.addTab(self.info,"Info")
        #Tab Note (Manager)
        self.note=Note()
        self.manager_tabwidget.addTab(self.note,"Note")
        #Tab ShortCut (Manager)
        self.shortcut=ShortCuts()
        self.manager_tabwidget.addTab(self.shortcut,"ShortCut")
        #Tab History (Manager)
        self.history=History()
        self.manager_tabwidget.addTab(self.history,"History")
        #add Manager to hbox
        self.parent.tab_hbox1.addWidget(self.manager_tabwidget)

    def changingManagerTab(self):
        print("index of ManAdagertab changed to :", self.manager_tabwidget.currentIndex())

class Lister(qtw.QWidget):
    def __init__(self):
        super().__init__()
        #self.lister=qtw.QWidget()

        self.m_tab_vbox1=qtw.QVBoxLayout()
        self.setLayout(self.m_tab_vbox1)
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

    def add_item_to_list(self,list,toAdd):
        list.addItem(toAdd)
        event="item added to "+list.objectName()
        self.addLog(event)

    def add_list_item(self):
        if self.entry_item.text() != '':
            item = self.entry_item.text()
            self.manager_list.addItem(item)
            self.entry_item.clear()


class Info(qtw.QWidget):
    def __init__(self):
        super().__init__()
        self.info=qtw.QWidget()
        self.m_tab_vbox2=qtw.QVBoxLayout()
        self.setLayout(self.m_tab_vbox2)

        # Widget Info
        self.editInfo=qtw.QTextEdit()
        self.m_tab_vbox2.addWidget(self.editInfo)
        self.editInfo.setText("Here the info of your system or else (see setup)")

class Note(qtw.QWidget):
    def __init__(self):
        super().__init__()
        self.note=qtw.QWidget()
        self.m_tab_vbox3=qtw.QVBoxLayout()
        self.setLayout(self.m_tab_vbox3)

        # Widget tab2

        self.editNote=qtw.QTextEdit()
        self.m_tab_vbox3.addWidget(self.editNote)
        self.editNote.setText("Here you can take some note")

class ShortCuts(qtw.QWidget):
    def __init__(self):
        super().__init__()
        self.shortcut=qtw.QWidget()
        self.m_tab_vbox4=qtw.QVBoxLayout()
        self.setLayout(self.m_tab_vbox4)

        # Widget shortucut
        self.label=qtw.QLabel("Show the shortCuts \n(maybe in a tree(env,apps...))")
        self.m_tab_vbox4.addWidget(self.label)

class History(qtw.QWidget):
    def __init__(self):
        super().__init__()
        self.history=qtw.QWidget()
        self.m_tab_vbox5=qtw.QVBoxLayout()
        self.setLayout(self.m_tab_vbox5)

        # Widget hystory
        self.label=qtw.QLabel("Show the history of command typpen in the app \n(may be replace by a watch on bash_history?)")
        self.m_tab_vbox5.addWidget(self.label)
        self.list_command=qtw.QListWidget()
        self.list_command.setObjectName("List of command")
        self.m_tab_vbox5.addWidget(self.list_command)

class HelPinguin(qtw.QWidget):
    def __init__(self,parent):
        self.parent=parent
        super().__init__()
        # Helpinguin
        #self.helper_helpin=qtw.QWidget()
        #self.helper_tab_vbox2=qtw.QVBoxLayout()
        #self.helper_helpin.setLayout(self.helper_tab_vbox2)
        #self.helper_tabwidget.addTab(self.helper_helpin,"Hel Pinguin")

        self.hp_tabwidget=qtw.QTabWidget()
        #Tab Error Handler
        #self.hp_tab1=qtw.QWidget()
        self.errHandler=ErrHandler()
        self.hp_tabwidget.addTab(self.errHandler,"Err. Handler")

        #Tab Displayer
        self.displayer=Displayer()

        self.hp_tabwidget.addTab(self.displayer,"Displayer")

        #Tab Watcher
        self.watcher=Watcher()
        self.hp_tabwidget.addTab(self.watcher,"Watcher")


        #Tab Manual
        self.help=Help()
        self.hp_tabwidget.addTab(self.help,"Help")

        #self.helper_tab_vbox2.addWidget(self.hp_tabwidget)
        #Tab Modification
        self.modFollower=ModFollower()
        self.hp_tabwidget.addTab(self.modFollower,"Mod Follower")

        self.parent.tab_hbox2.addWidget(self.hp_tabwidget)

        # Widget helpinguin
        #self.label=qtw.QLabel("Hi i'm in the tab helpinguin")
        #self.helper_tab_hbox2.addWidget(self.label)


    #add Tabs to layout
    #self.help_layout.addWidget(self.helper_tabwidget)

    def changingHelPinguinTab(self):
        print("index of HP tab changed to :", self.hp_tabwidget.currentIndex())

class ErrHandler(qtw.QWidget):
    def __init__(self):
        super().__init__()
        self.hp_tab_vbox1=qtw.QVBoxLayout()
        self.setLayout(self.hp_tab_vbox1)
        # Widget Error Handler
        self.error_list=qtw.QListWidget()
        self.error_list.setObjectName("Error List")
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

class Watcher(qtw.QWidget):
    def __init__(self):
        super().__init__()
        self.hp_tab_vbox3=qtw.QVBoxLayout()
        self.setLayout(self.hp_tab_vbox3)
        # Widget Watcher
        self.label1=qtw.QLabel("Here you can watch file change")
        self.hp_tab_vbox3.addWidget(self.label1)
        # Tabs
        self.watchers=qtw.QTabWidget()
        # Tab App Log
        self.w_tab1=qtw.QWidget()
        self.watchers.addTab(self.w_tab1,"App log")
        self.w_tab_hbox1=qtw.QHBoxLayout()
        self.w_tab1.setLayout(self.w_tab_hbox1)
        # Widget App Log
        self.app_log=qtw.QListWidget()
        self.app_log.setObjectName("app_log")
        self.w_tab_hbox1.addWidget(self.app_log)

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

class Displayer(qtw.QWidget):
    def __init__(self):
        super().__init__()
        self.hp_tab_vbox2=qtw.QVBoxLayout()
        self.setLayout(self.hp_tab_vbox2)
        # Widget Displayer
        self.label=qtw.QLabel("There are displayed possibilities\n(at the moment for Terminal and Doc (by type ?))\n need to know where cursor is!\n add extension system .py = python\n related to bin and var env ")
        self.hp_tab_vbox2.addWidget(self.label)


class Help(qtw.QWidget):
    def __init__(self):
        super().__init__()
        self.hp_tab_vbox4=qtw.QVBoxLayout()
        self.setLayout(self.hp_tab_vbox4)
        # Widget Manual
        self.label3=qtw.QLabel("Here manual is displayed")
        self.hp_tab_vbox4.addWidget(self.label3)


class ModFollower(qtw.QWidget):
    def __init__(self):
        super().__init__()
        self.hp_tab_vbox5=qtw.QVBoxLayout()
        self.setLayout(self.hp_tab_vbox5)
        # Widget Modification
        self.label3=qtw.QLabel("Here the previous state of the current doc are displayed")
        self.hp_tab_vbox5.addWidget(self.label3)


if __name__=="__main__":

    app = qtw.QApplication([])
    hp=Helper()
    app.exec_()
