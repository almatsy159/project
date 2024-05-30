class Ref():
    id=0
    def __init__(self,name):
        self.id=Ref.id
        Ref.id+=1
        self.name=name


class Block(Ref):
    def __init__(self,name,type):
        super().__init__(name)
        self.content=None
        self.redirect_type(type)

    def redirect_type(self,my_type):
        print(type(my_type))
        if isinstance(my_type,str):
            if my_type == "list" :
                self.list()

    def list(self):
        item_id=0
        items={}
        x=""
        print("do you know the number of item ?(Y/N)")
        yOrN=input()
        print("you typed {}\n".format(yOrN))
        if yOrN == "N" or yOrN == "n":
            print("to end the list enter \"end\"")
            while x != "end":
                x=input("item {} :".format(item_id))
                if x != "end":
                    items[item_id]=x
                    item_id+=1
        elif yOrN == "Y" or yOrN == "y" :
            compt=0
            y=int(input("input your number of items : "))
            print("\n")
            while compt != y:
                x=input("\titem {} :".format(compt))
                items[item_id]=x
                item_id +=1
                compt +=1
        self.content=items


p1_b1=Block("efficacité","list")
print(p1_b1.content)
