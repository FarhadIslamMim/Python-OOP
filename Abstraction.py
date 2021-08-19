from abc  import  ABC,abstractmethod

class shape(ABC):
    def __init__(self,hight,base):
        self.hight=hight
        self.base=base
    @abstractmethod
    def area(self):
       pass
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