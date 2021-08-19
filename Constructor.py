class student:
    name=""
    roll = ""
    gpa = ""

    def __init__(self,name,roll,gpa):
        self.name=name
        self.roll=roll
        self.gpa=gpa
    def diaplay(self):
        print(f"Roll:{self.roll} Name:{self.name}  GPA:{self.gpa}")

rahim = student("Rahim",111,5.00)
rahim.diaplay()

Fahim = student("Fahim",113,4.55)
Fahim.diaplay()

farhad = student("Farhad",115,3.33)
farhad.diaplay()