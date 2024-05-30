import PyQt5.QtWidgets as qtw
import mysql.connector as mc

class Connection():
    pass

class Main(qtw.QWidget):
    def __init__(self):
        super().__init__()

        self.show()


class Block():
    id=0
    def __init__(self,parent=None,content=None):
        self.parent=parent
        self.b_id=Block.id
        self.b_name="b"+str(self.b_id)
        if self.parent==None:
            self.content={}
            self.lvl=0
        else :
            self.lvl=self.parent.lvl + 1
            self.content=content
            self.parent.content[self.b_name]=self.content
        Block.id+=1



class Page(Block):
    id=1
    def __init__(self,parent,content={}):
        self.parent=parent
        super().__init__(self.parent)
        self.lvl=self.parent.lvl+1
        self.content=content
        self.p_id=Page.id
        self.p_name="p"+str(self.p_id)
        self.parent.content[self.p_name]=self.content
        Page.id+=1

class Doc(Block):
    id=1
    def __init__(self,parent,content={}):
        self.parent=parent
        super().__init__(self.parent)
        self.lvl=self.parent.lvl+1
        self.content=content
        self.d_id=Page.id
        self.d_name="d"+str(self.d_id)
        self.parent.content[self.d_name]=self.content
        Doc.id+=1

class Line(Block):
    id=1
    def __init__(self,parent,content={}):
        self.parent=parent
        super().__init__(self.parent)
        self.lvl=self.parent.lvl+1
        self.content=content
        self.l_id=Line.id
        self.l_name="l"+str(self.l_id)
        self.parent.content[self.l_name]=self.content
        Line.id+=1

Block1=Block()
Doc1=Doc(Block1)
Page1_d1=Page(Doc1)

#Block1_p1=Block(Page1_d1)
Line1_b1p1=Line(Page1_d1,"ligne 1 du block 1 de la page 1")
Line2_b1p1=Line(Page1_d1,"ligne 2 du block 1 de la page 1")
"""
Block2_p1=Block(Page1_d1)
Line1_b2p1=Line(Block1_p1,"ligne 1 du block 2 de la page 1")
Line2_b2p1=Line(Block1_p1,"ligne 2 du block 2 de la page 1")

Page2_d1=Page(Doc1)

Block1_p2=Block(Page2_d1)
Line1_b1p2=Line(Block1_p2,"ligne 1 du block 1 de la page 2")
Line2_b1p2=Line(Block1_p2,"ligne 2 du block 1 de la page 2")

Block2_p2=Block(Page2_d1)
Line1_b2p2=Line(Block1_p2,"ligne 1 du block 2 de la page 2")
Line2_b2p2=Line(Block1_p2,"ligne 2 du block 2 de la page 2")

Doc2=Doc(Block1)
"""
print(Block1.b_name,"\t",Block1.lvl,"\n\t",Block1.content,"\n")
#print(Doc1.d_name,"\t",Doc1.lvl,"\n\t",Doc1.content,"\n")
print("lvl : ",Line1_b1p1.lvl,"\tcontent : ",Line1_b1p1.content)
app = qtw.QApplication([])
mw=Main()
app.exec_()
