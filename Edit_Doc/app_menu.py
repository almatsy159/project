import PyQt5.QtWidgets as qtw
import create as cr
class Menu(qtw.QWidget):
    def __init__(self,parent):
        self.parent=parent
        super().__init__()
        self.buffer=""
        self.main_grid=qtw.QGridLayout()
        self.main_grid.setSpacing(0)

        print(__name__)
            #__name__.
        self.menu=qtw.QMenuBar()

        self.action1=qtw.QAction("File")
        self.action2=qtw.QAction("In")
        self.action12=qtw.QAction("New Tab")
        self.action3=qtw.QAction("New Block Type")
        self.action4=qtw.QAction("New Block")
        self.action5=qtw.QAction("New Theme")
        # sure ?
        self.action13=qtw.QAction("New Content Type")
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

        # Event
        self.action1.triggered.connect(lambda: self.message_label.setText("action1 triggered"))
        self.action2.triggered.connect(lambda: self.clicker())
        self.action3.triggered.connect(lambda: self.new_BlockType(self.doc_tabwidget))
        self.action4.triggered.connect(lambda: self.new_block_in_new_tab(self.parent.editDoc.doc_tabwidget))
        self.action5.triggered.connect(lambda: self.new_Theme(self.doc_tabwidget))

        self.main_grid.addWidget(self.menu)

        self.setLayout(self.main_grid)

        self.show()

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
                self.parent.editDoc.editDoc.setPlainText(self.buffer)

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

if __name__=="__main__":

    app = qtw.QApplication([])
    hp=Menu()
    app.exec_()
