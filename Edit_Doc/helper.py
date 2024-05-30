import PyQt5.QtWidgets as qtw

class Helper(qtw.QWidget):
    def __init__(self):
        super().__init__()
        self.help_layout=qtw.QVBoxLayout()
        self.main_layout=qtw.QHBoxLayout()
        self.help_groupBox=qtw.QGroupBox("Hey i'm the helper")
        self.help_groupBox.setLayout(self.help_layout)
        self.main_layout.addWidget(self.help_groupBox)

        # Tabs
        self.tabwidget=qtw.QTabWidget()
        #Tab 1
        self.tab1=qtw.QWidget()
        self.tabwidget.addTab(self.tab1,"tab1")
        self.tab_hbox1=qtw.QHBoxLayout()
        self.tab1.setLayout(self.tab_hbox1)
        # Widget tab1
        self.btn=qtw.QPushButton("Hi i'm in tab1")
        self.tab_hbox1.addWidget(self.btn)

        #Tab2
        self.tab2=qtw.QWidget()
        self.tab_hbox2=qtw.QHBoxLayout()
        self.tab2.setLayout(self.tab_hbox2)
        self.tabwidget.addTab(self.tab2,"tab2")
        # Widget tab2
        self.label=qtw.QLabel("Hi i'm in tab2")
        self.tab_hbox2.addWidget(self.label)

        #add Tabs to vbox
        self.help_layout.addWidget(self.tabwidget)


        self.setLayout(self.main_layout)
        self.show()

if __name__=="__main__":

    app = qtw.QApplication([])
    hp=Helper()
    app.exec_()
else:
    hp=Helper()
