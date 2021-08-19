class A:
    def display(self):
        print("i am class A")
class B(A):
    def display1(self):
        print("i am class B")
class C(B):
    def display2(self):
        print("i am class C")
class D(C):
    def display3(self):
        super().display()
        super().display1()
        super().display2()
        print("i am class D")
d=D()
d.display3()
