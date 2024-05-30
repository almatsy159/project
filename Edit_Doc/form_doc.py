import PyQt5.QtWidgets as qtw

class Form_Document(qtw.QWidget):

    def __init__(self):


        self.parent = super().__init__()
        self.init_window()
        self.fill_window()

    def init_window(self):

        self.main_layout = qtw.QGridLayout()
        self.setLayout(self.main_layout)
        self.setTitle("Form Doc")
        self.show()

    def elements(self):
        self.te1=qtw.QTextEdit(self.main_layout)
        self.btn1=qtw.QPushButton("Create",clicked=lambda:self.create)
        self.period_cdd=qtw.QComboBox()

        self.main_layout.addWidget(self.te1)
        self.main_layout.addWidget(self.btn1)
        self.main_layout.addWidget(self.period_cdd)

    def create(self):
        #insert into bd
        pass




"""
class Element():
    def __init__(self,name,type="",exec=""):
        self.script=exec(exec)
        self.name=name
        self.type=type
"""

app = stw.QApplication([])
main=Form_Document()
app.exec_()
