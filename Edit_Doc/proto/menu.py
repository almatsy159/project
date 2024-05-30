import PyQt5.QtWidgets as qtw



class MainWindow(qtw.QWidget):
    def __init__(self):
        super().__init__()
        print(dir(qtw))
        #self.main=qtw.QMainWindow(self)

        #print(globals())
        self.setWindowTitle("App : Edit Doc")
        self.setGeometry(100,100,300,300)
        self.main_layout=qtw.QGridLayout()
        #self.upper_layout=qtw.QGroupBox()
        #self.lower_layout=qtw.QGroupBox()
        #self.upper_layout.setLayout(self.main_layout)
        #self.lower_layout.setLayout(self.main_layout)
        self.DU_layout=qtw.QVBoxLayout()
        self.Edit_layout=qtw.QVBoxLayout()
        self.List_layout=qtw.QVBoxLayout()
        self.Terminal_layout=qtw.QHBoxLayout()
        self.Tool_layout=qtw.QVBoxLayout()

        #self.main_layout.addWidget(self.upper_layout)

        #self.upper_layout.addWidget(self.Edit_layout)
        #self.upper_layout.addWidget(self.DU_layout)
        #self.upper_layout.addWidget(self.List_layout)

        #self.main_layout.addWidget(self.lower_layout)

        #self.lower_layout.addWidget(self.Terminal_layout)
        #self.lower_layout.addWidget(self.Tool_layout)

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
        #self.menu_file.addMenuItem("Open")
        self.db_print=qtw.QTreeView()
        self.terminal=qtw.QTextEdit()
        self.doc_area=qtw.QTextEdit()
        self.tool_area=qtw.QTextEdit()
        self.entry=qtw.QLineEdit()
        self.button=qtw.QPushButton("Hi i'm me !",clicked=lambda: self.label.setText("bouton pressed !"))

        self.label=qtw.QLabel("Text by default")
        self.main_layout.addWidget(self.menu)
        self.main_layout.addWidget(self.doc_area)
        self.main_layout.addWidget(self.tool_area)
        self.main_layout.addWidget(self.terminal)
        self.main_layout.addWidget(self.entry)
        self.main_layout.addWidget(self.db_print)
        self.main_layout.addWidget(self.label)
        self.main_layout.addWidget(self.button)

        self.action1.triggered.connect(lambda: self.label.setText("action1 triggered"))
        self.action2.triggered.connect(lambda: self.clicker())

        self.setLayout(self.main_layout)
        self.show()

    def clicker(self):
        fname=qtw.QFileDialog.getOpenFileName(self,"Open File","","All Files (*);;TXT Files (*.txt)")
        #C:\\\Users\\gaeta\\OneDrive\\Documents\\prog\\Edit_Doc\\
        print(fname[0])
app = qtw.QApplication([])
main=MainWindow()

app.exec_()
