import PyQt5.QtWidgets as qtw
class Tree_Tools(qtw.QWidget):
    def __init__(self,parent):

        #Tab Tool tree
        self.parent=parent
        #self.tool_tree=qtw.QWidget()
        super().__init__()

        self.tool_tree_box=qtw.QVBoxLayout()
        self.setLayout(self.tool_tree_box)
        # Widget tab tree

class Global_Tools(qtw.QWidget):
    def __init__(self,parent):
        #Global tools maybe in a status bar ? !!! sure!(not the cbb)
        self.parent=parent
        super().__init__()
        self.target_cbb=qtw.QComboBox()
        self.target_cbb.addItem("Current Doc")
        self.target_cbb.addItem("Terminal")
        self.global_tool_grid=qtw.QGridLayout()
        self.global_tool_gb=qtw.QGroupBox("Global Tools")
        self.global_tool_gb.setLayout(self.global_tool_grid)
        #self.tool_layout.addWidget(self.global_tool_gb)
        self.tool1=qtw.QPushButton("tool1")
        self.tool2=qtw.QPushButton("tool2")
        self.entry_last_item_created=qtw.QLineEdit()
        self.entry_last_item_created.textChanged.connect(lambda: self.last_item_created())
        #Message
        self.message_label=qtw.QLabel()

        self.global_tool_grid.addWidget(self.target_cbb,0,1)
        self.global_tool_grid.addWidget(self.message_label,0,0)
        self.global_tool_grid.addWidget(self.tool1,1,0)
        self.global_tool_grid.addWidget(self.tool2,1,1)
        self.global_tool_grid.addWidget(self.entry_last_item_created)

class EditDoc_Tools(qtw.QWidget):
    def __init__(self,parent):
        #Tab Tool Doc
        self.parent=parent
        super().__init__()
        #self.tool_doc=qtw.QWidget()
        self.tool_doc_box=qtw.QVBoxLayout()
        self.setLayout(self.tool_doc_box)
        # Widget tab doc

class Helper_Tools(qtw.QWidget):
    def __init__(self,parent):
        # Tab tool Helper
        self.parent=parent
        super().__init__()
        #self.tool_helper=qtw.QWidget()
        self.tool_helper_box=qtw.QVBoxLayout()
        self.setLayout(self.tool_helper_box)
        # Widget tab helper
        self.btn_remove_item=qtw.QPushButton("Remove Item")
        self.tool_helper_box.addWidget(self.btn_remove_item)


        #add Tabs to vbox


class Terminal_Tools(qtw.QWidget):
    def __init__(self,parent):
        # Tab tool Terminal
        self.parent=parent
        super().__init__()
        #self.tool_terminal=qtw.QWidget()
        #self.tool_tabwidget.addTab(self.tool_terminal,"Terminal Tools")

        self.tool_terminal_box=qtw.QGridLayout()
        self.setLayout(self.tool_terminal_box)

        # Widget tab tool terminal
        self.terminalClear=qtw.QPushButton("Clear",clicked=lambda : self.clear())
        self.tool_terminal_box.addWidget(self.terminalClear,0,0)
        self.prefix_terminal=qtw.QLineEdit()
        self.prefix_terminal.setPlaceholderText("enter prefix (type : _pr in terminal to use)")
        self.suffix_terminal=qtw.QLineEdit()
        self.suffix_terminal.setPlaceholderText("enter suffix (type : _suf in terminal to use)")
        self.label2=qtw.QLabel("suffix")
        self.variable_terminal=qtw.QLineEdit()
        self.variable_terminal.setPlaceholderText("enter suffix (type : _var in terminal to use)")
        self.label5=qtw.QLabel("variable")
        self.label4=qtw.QLabel("prefix")
        self.tool_terminal_box.addWidget(self.prefix_terminal,1,1)
        self.tool_terminal_box.addWidget(self.suffix_terminal,3,1)
        self.tool_terminal_box.addWidget(self.label2,3,0)
        self.tool_terminal_box.addWidget(self.label4,1,0)
        self.tool_terminal_box.addWidget(self.variable_terminal,2,1)
        self.tool_terminal_box.addWidget(self.label5,2,0)

class Tools(qtw.QWidget):
    def __init__(self,parent):
        self.parent=parent
        super().__init__()
        self.setWindowTitle("Edit Doc Menu")
        self.main_grid=qtw.QGridLayout()
        self.main_grid.setSpacing(0)
        #self.main_groupBox=qtw.QGroupBox("Main Group Box")
        print(__name__)
        #__name__.
        #Tool items
        #self.tool_layout=qtw.QGridLayout()
        self.tool_tabwidget=qtw.QTabWidget()
        #self.global_tools=Global_Tools()
        self.tree_tools=Tree_Tools(self)
        self.tool_tabwidget.addTab(self.tree_tools,"Tree Tools")
        self.editDoc_tools=EditDoc_Tools(self)
        self.tool_tabwidget.addTab(self.editDoc_tools,"Doc Tools")
        self.helper_tools=Helper_Tools(self)
        self.tool_tabwidget.addTab(self.helper_tools,"Helper Tool")
        self.terminal_tools=Terminal_Tools(self)
        self.tool_tabwidget.addTab(self.terminal_tools,"Terminal Tools")

        self.tool_tabwidget.setObjectName("ToolTabWidget")

        self.tool_layout=qtw.QVBoxLayout()
        self.tool_groupBox=qtw.QGroupBox("Tool")
        self.tool_groupBox.setLayout(self.tool_layout)
        #self.main_grid.addWidget(self.tool_groupBox)

        self.main_grid.addWidget(self.tool_tabwidget)

        #self.tool_tabwidget.addWidget(self.global_tools)

        #self.tool_tabwidget.addTab(self.tree_tools)
        #self.tool_tabwidget.addTab(self.editDoc_tools)


        # here current index of each tabs
        # to update (missing tabs )!!!
        self.tool_tabwidget.currentChanged.connect(self.changingToolTab)



        # Event
        #self.action1.triggered.connect(lambda: self.message_label.setText("action1 triggered"))
        #self.action2.triggered.connect(lambda: self.clicker())
        #self.action3.triggered.connect(lambda: self.new_BlockType(self.doc_tabwidget))
        #self.action4.triggered.connect(lambda: self.new_block_in_new_tab(self.doc_tabwidget))
        #self.action5.triggered.connect(lambda: self.new_Theme(self.doc_tabwidget))
        #to layout add group box AND to group box set a layout(child)
        # <LAYOUT>.addWidget(<GroupBox>)
        # <GroupBox>.setLayout(<Child Layout>)
        #self.main_layout.addWidget(self.gp_hbox1)
        #self.main_layout.addWidget(self.gp_hbox2)

        #self.gp_hbox1.setLayout(self.hbox1)
        #self.gp_hbox2.setLayout(self.hbox2)

        #self.main_grid.addWidget(self.main_groupBox)
        #self.main_groupBox.setLayout(self.main_layout)
        self.setLayout(self.main_grid)
        #self.print_name()
        self.show()

    def changingToolTab(self):
        print("index of Tool tab changed to :", self.tool_tabwidget.currentIndex())


if __name__=="__main__":

    app = qtw.QApplication([])
    tools=Tools()
    app.exec_()
