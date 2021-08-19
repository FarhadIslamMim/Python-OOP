class bike:
    def __init__(self,color,name):
        self.color=color
        self.name=name
    def __str__(self):
        print(f"Name:{self.name} Color: {self.color}")
    def print(self):
        print(f"Name:{self.name} Color: {self.color}")
    def __eq__(self, other):
        return self.name==other.name and self.color==other.color
bike1=bike("black","R15",)
bike1.print()
bike2=bike("black","R15")
bike2.print()
print(bike1==bike2)