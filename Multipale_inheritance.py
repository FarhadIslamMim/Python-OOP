class A:
    def display(self):
        print("i am class A")
class B:
    def display1(self):
        print("i am class B")
class C:
    def display2(self):
        print("i am class C")
class D(A,B,C):
    def display3(self):
        super().display()
        super().display1()
        super().display2()
        print("i am class D")
d=D()
d.display3()
