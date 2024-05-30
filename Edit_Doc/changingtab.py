import PyQt5.QtWidgets as qtw

class Main(qtw.QWidget):
    def __init__(self):
        super().__init__()
        self.layout=qtw.QHBoxLayout()
        self.tabs=qtw.QTabWidget()
        self.tab1=qtw.QWidget()
        self.tabs.addTab(self.tab1,"tab1")
        self.tab2=qtw.QWidget()
        self.tabs.addTab(self.tab2,"tab2")
        self.layout.addWidget(self.tabs)

        label=qtw.QLabel()
        self.layout.addWidget(label)
        self.setLayout(self.layout)
        self.tabs.currentChanged.connect(self.changingtab)
        self.show()

    def changingtab(self,parent):
        #print("dict : ",self.__dict__)
        #print(dir(self.tabs))
        print("index of tab changed to :", self.tabs.currentIndex())
        #print(parent.currentChanged.connect(self.tabChanged()))
        #print("name of parent : ",self.tabs.objectName)
app = qtw.QApplication([])
x=exec(hex(id(app)))
print(x)
main=Main()
app.exec_()
