import PyQt5.QtWidgets as qtw
import sys
class Main(qtw.QWidget):
    def __init__(self):
        super().__init__()

        gp1=qtw.QGroupBox()

        vbox1=qtw.QVBoxLayout()
        btn1=qtw.QPushButton("gp1")
        vbox1.addWidget(btn1)
        vbox1.addWidget(gp1)
        #gp1.setLayout(vbox1)
        print("after set gp1")
        gp2=qtw.QGroupBox()
        vbox2=qtw.QVBoxLayout()

        #print(dir(qtw.QGroupBox()))

        btn2=qtw.QPushButton("gp2")
        vbox2.addWidget(btn2)
        gp2.setLayout(vbox2)
        vbox1.addWidget(gp2)
        print("after set gp2")

        self.setLayout(vbox1)
        print("after setLayout")

        self.show()

app=qtw.QApplication([])

mw=Main()

sys.exit(app.exec_())
