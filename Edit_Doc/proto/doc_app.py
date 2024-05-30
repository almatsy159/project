import PyQt5.QtWidgets as qtw
import PyQt5.QtCore as qtc

class Main(qtw.QMainWindow):
    def __init__(self):
        super().__init__()

        #print(dir(qtw.QMenuBar))
        self.setWindowTitle("App : Doc")
        self.centralWidget=qtw.QWidget(self)
        #self.hbox=qtw.QVBoxLayout(self)
        self.setCentralWidget(self.centralWidget)
        #help(qtw.QMenuBar)
        self.menubar=qtw.QMenuBar(self)
        #self.menubar.setGeometry(qtc.QRect(0, 0, 800, 24))

        self.menu_File=qtw.QMenu(self.menubar)
        self.menu_File.setObjectName("File")

        self.action_New=qtw.QAction()
        self.action_New.setObjectName("New")

        self.menu_File.addAction(self.action_New)

        self.menubar.addAction(self.menu_File.menuAction())

        self.setMenuBar(self.menubar)

        self.statusBar= qtw.QStatusBar(self)

        #print(dir(qtw))
        self.show()

app=qtw.QApplication([])
main=Main()
app.exec_()
