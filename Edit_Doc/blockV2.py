

# it's the main entity of the application allowing to divide any element into this relative element
class Block():
    def __init__(self,id,name,lvl,content_id,type_id,theme_id,parent_id="NULL"):
        self.name=name
        self.id=id
        self.lvl=lvl
        self.content_id=content_id
        self.type_id=type_id
        self.parent_id=parent_id
        self.theme_id=theme
        #self.content_type_id=content_type_id

# allow to classify blocks
class Theme():
    def __init__(self,id,name):
        self.id=id
        self.name=name

# define the type of block if it's DU,doc,block,line,list ...
class Type():
    def __init__(self,id,name):
        self.id=id
        self.name=name

# content is blob depending of the type of content
class Content():
    def __init__(self,id,name,content,content_type_id):
        self.id=id
        self.name=name
        self.content=content
        self.content_type_id=content_type_id

# can be image,text,path...
class Content_Type():
    def __init__(self,id,name):
        self.id=id
        self.name=name
