import PyQt5.QtWidgets as qtw
import re
import os

class Terminal(qtw.QWidget):
    def __init__(self,parent):
        self.parent=parent
        super().__init__()

        #self.setWindowTitle("Edit Doc Menu")
        self.main_grid=qtw.QGridLayout()
        self.main_grid.setSpacing(0)
        #self.main_groupBox=qtw.QGroupBox("Main Group Box")
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
    def enter(self):
        #print(dir(qtw.QLineEdit))
        #pattern1=re.compile('^#pr [A-Za-z0-9.-//*&_ ]+ #suf')
        pattern2=re.compile(r"^_pr")
        pattern3=re.compile(r"_suf")
        pattern4=re.compile(r"(_var)")
        chain_to_analyse=f"{self.terminalInput.text()}"
        beg=""
        end=""
        beg_exec=""
        end_exec=""
        chain_to_exec=""
        #re.sub("_var",self.variable_terminal.text(),chain_to_analyse)
        print(chain_to_analyse)
        if self.terminalInput.text() != "" and self.terminalInput.text() != "_pr" and self.terminalInput.text() != "_suf":
            length=len(chain_to_analyse)
            #match1=pattern1.finditer(chain_to_analyse)
            #print(match1)
            if pattern2.match(chain_to_analyse):
                #print("matched first pattern")
                beg_exec=self.prefix_terminal.text()
                chain_to_analyse=chain_to_analyse[3:]
                length=length-2
            #chain += self.terminalInput.text()
            #match2=pattern2.match(self.terminalInput.text())
            #print(match2)

            if pattern3.search(chain_to_analyse):
                #print("matched pattern 2")
                chain_to_analyse=chain_to_analyse[0:length-5]
                end_exec=self.suffix_terminal.text()
            #print("analyser : ",chain_to_analyse)

            if self.parent.tools.terminal_tools.variable_terminal.text() != '':
                while pattern4.search(chain_to_analyse):
                    matched=pattern4.search(chain_to_analyse)
                    #print(matched.groups())
                    start=matched.start()
                    end=matched.end()
                    #print("start,end",start,",",end,";",chain_to_analyse)
                    beg_m=chain_to_analyse[:start]
                    end_m=chain_to_analyse[end:]
                    #chain_to_analyse[start:end]=self.variable_terminal.text()
                    mid=self.variable_terminal.text()
                    #print("mid :",mid)
                    chain_to_analyse=beg_m+mid+end_m
                    print(chain_to_analyse)

            #print(r"analyser : ",chain_to_analyse)
            chain_to_exec=beg_exec+chain_to_analyse+end_exec
            #print(r"executer : ",chain_to_exec)

            x=os.popen(chain_to_exec)
            self.terminalInput.clear()
            #print(x.read())
            #self.terminalOutput.setText(x.read())
            self.terminalOutput.insertPlainText(x.read())
            self.parent.add_item_to_list(self.parent.helper.manager.history.list_command,chain_to_exec)
            event="command executed"
            with open("history_cmd.txt","a") as history_cmd:
                history_cmd.write(chain_to_exec+"\n")
            self.parent.helper.add_item_to_list(self.parent.helper.helpinguin.watcher.app_log,event)

    def clear(self):
        self.terminalOutput.clear()
    
if __name__=="__main__":

    app = qtw.QApplication([])
    hp=Terminal()
    app.exec_()
