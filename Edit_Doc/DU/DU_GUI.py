import mysql.connector as mc
import PyQt5.QtWidgets as qtw
import sys
#import os

class App(qtw.QWidget):
    id=0
    def __init__(self):
        super().__init__()
        self.obj_dict={}

        self.setWindowTitle("DU-Editor")
        self.setGeometry(300,200,400,500)

        # test layout !!!
        """
        hbox=qtw.QHBoxLayout()
        self.create_layout("gb")
        hbox.addWidget(self.nom_obj)
        self.create_layout("gb")
        hbox.addWidget(self.nom_obj)

        self.setLayout(hbox)

        text1=qtw.QTextEdit()
        #text1.placeholderText("Type here")
        hbox.addWidget(text1)
        b1=qtw.QPushButton("Press me too !",clicked=lambda:self.press_me())
        hbox.addWidget(b1)
        """
        self.setLayout(qtw.QVBoxLayout())
        self.create_GroupBox("ManAger")
        self.create_vlayout("vbox1")

        b1=qtw.QPushButton("Press me too !",clicked=lambda:self.press_me())
        self.vbox1.addWidget(b1)
        self.layout().addWidget(self.ManAger)
        self.setLayout2("vbox1","ManAger")
        b2=qtw.QPushButton("press me =( !")
        self.layout().addWidget(b2)
        # fin test layout
        self.show()

        """
    def create_layout(self,name):
        self.nom_obj=name + str(App.id)
        self.nom_obj=qtw.QGroupBox("I don't know yet")
        # setFont
        hbox1=qtw.QHBoxLayout()
        self.b1=qtw.QPushButton("Press me !",clicked=lambda:self.press_me())
        hbox1.addWidget(self.b1)
        self.nom_obj.setLayout(hbox1)
        """
    def create_vlayout(self,name):
        #name = qtw.QVBoxLayout()
        nom_obj="self."+name+"=qtw.QVBoxLayout()"
        exec(nom_obj)
        #exec("self."+name+".addWidget(parent)")

    def setLayout2(self,name,parent_name):
        exec("self."+parent_name+".setLayout(self."+name+")")

    def create_GroupBox(self,name):
        #name=qtw.QGroupBox(name)
        nom_obj="self."+name+" = qtw.QGroupBox(\""+name+"\")"
        exec(nom_obj)
        #y=eval(equal)
        #x=y
        print(self.__dict__)

    def press_me(self):
        pass

class Input(qtw.QTextEdit):
    pass

class Output(qtw.QTextEdit):
    pass

class Button(qtw.QPushButton):
    pass

class Menu(qtw.QMenuBar):
    pass

class UZ(qtw.QGroupBox):
    def __init__(self):
        self.name="Ui Zard"

class MA(qtw.QGroupBox):
    def __init__(self):
        self.name="Man Ager"

class HP(qtw.QGroupBox):
    def __init__(self):
        self.name="Hel Pinguin"
    pass

app= qtw.QApplication(sys.argv)

if __name__=="__main__":
    #print(locals())
    #print(globals())
    #print(dir(qtw))
    #print(dir(sys))
    #print(dir(os))
    #pass

    win=App()

    app.exec_()
