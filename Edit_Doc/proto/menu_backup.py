import PyQt5.QtWidgets as qtw


class Dialog(qtw.QDialog):
    def __init__(self):
        
class MainWindow(qtw.QWidget):
    def __init__(self):
        super().__init__()
        #print(dir(qtw.QWidget))
        #self.main=qtw.QMainWindow(self)

        #print(globals())
        self.setWindowTitle("App : Edit Doc")
        self.setGeometry(100,100,300,300)
        self.layout=qtw.QVBoxLayout()

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
        self.button=qtw.QPushButton("Hi i'm me !",clicked=lambda: self.label.setText("bouton pressed !"))

        self.label=qtw.QLabel("Text by default")
        self.layout.addWidget(self.menu)
        self.layout.addWidget(self.label)
        self.layout.addWidget(self.button)
        self.action1.triggered.connect(lambda: self.label.setText("action1 triggered"))
        self.action2.triggered.connect(lambda: self.label.setText("action2 triggered"))
        self.setLayout(self.layout)
        self.show()

app = qtw.QApplication([])
main=MainWindow()

app.exec_()
