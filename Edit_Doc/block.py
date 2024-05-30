
class Type_of_block():
    pass

class Type_of_doc():
    pass

class Block(Type_of_block):
    pass

class Doc(Block,Type_of_doc):

    def __init__(self):
        Block.__init__()
        Type_of_doc.__init__()

class Line(Block):

class Block_of_word(Block):
    def __init__(self):
        Block.__init__()
"""
class Word(str):
    def __init__(self,parent):
        str.__init__()
"""
