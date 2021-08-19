class traingle:
    def __init__(self,base,hight):
        self.base=base
        self.hight=hight

    def display(self):
        result=.5*self.base* self.hight
        print(f"Result:",result)

t1=traingle(10,20)
t1.display()
t2=traingle(20,30)
t2.display()