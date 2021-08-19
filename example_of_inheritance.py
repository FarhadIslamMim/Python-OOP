class shape:
    def __init__(self,hight,base):
        self.hight=hight
        self.base=base
    def area(self):
        print("i am area methon of shape class")
class Triangle(shape):
    def area(self):
        area=.5* self.base * self.hight
        print("area of triangle:",area)
class Rectangle(shape):
    def area(self):
        area=self.base * self.hight
        print("area of rectangle:",area)

t=Triangle(20,30)
t.area()
r=Rectangle(20,30)
r.area()