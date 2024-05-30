import PyQt5.QtWidgets as qtw

class Menu(qtw.QWidget):
    def __init__(self):

        super().__init__()
        if __name__=="__main__":
            self.setWindowTitle("Edit Doc Menu")
            self.main_grid=qtw.QGridLayout()
            self.main_grid.setSpacing(0)
            #self.main_groupBox=qtw.QGroupBox("Main Group Box")
        else :
            print(__name__)

        #Terminal items
        self.terminal_layout=qtw.QVBoxLayout()
        self.terminal_groupBox=qtw.QGroupBox("Terminal")
        self.terminal_groupBox.setLayout(self.terminal_layout)
        #self.hbox2.addWidget(self.terminal_groupBox)

        self.terminalOutput=qtw.QTextEdit()
        self.terminalInput=qtw.QLineEdit()
        self.terminalInput.setPlaceholderText("_pr :prefix; then your command; _var : variable ; _suf : suffix")
        self.terminalValid=qtw.QPushButton("Enter",clicked=lambda : self.enter())
        self.terminal_layout.addWidget(self.terminalOutput)
        self.terminal_layout.addWidget(self.terminalInput)
        self.terminal_layout.addWidget(self.terminalValid)


        self.main_grid.addWidget(self.terminal_groupBox)
        #self.main_grid.addWidget(self.main_groupBox)
        #self.main_groupBox.setLayout(self.main_layout)
        self.setLayout(self.main_grid)
        #self.print_name()
        self.show()

if __name__=="__main__":

    app = qtw.QApplication([])
    hp=Menu()
    app.exec_()
else:
    hp=Menu()
