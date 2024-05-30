import PyQt5.QtWidgets as qtw

class EditDoc(qtw.QWidget):
    def __init__(self,parent):
        self.parent = parent
        super().__init__()
        #self.setWindowTitle("Edit Doc Menu")
        self.main_grid=qtw.QGridLayout()
        self.main_grid.setSpacing(0)
            #self.main_groupBox=qtw.QGroupBox("Main Group Box")

        print(__name__)
            #__name__.
        self.doc_tabwidget=qtw.QTabWidget()
        self.doc_tabwidget.currentChanged.connect(self.changingDocTab)
        #Doc items
        self.doc_layout=qtw.QVBoxLayout()
        self.doc_groupBox=qtw.QGroupBox("Doc")
        self.doc_groupBox.setLayout(self.doc_layout)
        self.main_grid.addWidget(self.doc_groupBox)

        self.doc_tabwidget=qtw.QTabWidget()

        #Tab 1
        self.tab1=qtw.QWidget()
        self.doc_tabwidget.addTab(self.tab1,"DU1")
        self.tab_hbox1=qtw.QHBoxLayout()
        self.tab1.setLayout(self.tab_hbox1)
        # Widget tab1

        """
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
        """
        #add Tabs to vbox
        self.doc_layout.addWidget(self.doc_tabwidget)

        self.editDoc=qtw.QTextEdit()
        self.tab_hbox1.addWidget(self.editDoc)


        self.setLayout(self.main_grid)
        self.show()

    def changingDocTab(self):
        print("index of Doc tab changed to :", self.doc_tabwidget.currentIndex())

if __name__ == "__main__":

    app = qtw.QApplication([])
    tree=EditDoc()
    app.exec_()
