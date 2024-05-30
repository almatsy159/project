import PyQt5.QtWidgets as qtw
import mysql.connector as mc


class Launcher(qtw.QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Edit Doc Laucher")

        launch_layout=qtw.QFormLayout()
        self.setLayout(launch_layout)

        label1=qtw.QLabel("Username :")
        user_entry=qtw.QLineEdit()
        label2=qtw.QLabel("Password :")
        pwd_entry=qtw.QLineEdit()
        commandlinkbtn1=qtw.QCommandLinkButton("advanced option")


        launch_layout.addRow(label1)
        launch_layout.addRow(user_entry)
        launch_layout.addRow(label2)
        launch_layout.addRow(pwd_entry)
        launch_layout.addRow(commandlinkbtn1)
        launch_layout.addRow(qtw.QPushButton("Valid",clicked= lambda: validate()))
        launch_layout.addRow(qtw.QPushButton("New User",clicked= lambda: new_user()))


        self.show()

        def validate():
            print("valid pressed")

        def new_user():
            print("new pressed")




app=qtw.QApplication([])
mw= Launcher()

app.exec_()
