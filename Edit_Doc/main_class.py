


class Main():

    def __init__(self,child_name="osef"):
        self.name=__name__
        self.p1=Process(self)
    class Process():
        def __init__(self,master=None,name="child_of_osef"):
            #master != super !!!!
            self.master=master
            self.name=name

            def fonction_in_init(self,x):
                self.x=x

    Process()
    #ou


Main()
# ou
m1=Main()
print(m1.p1.name," : ",m1.p1)
