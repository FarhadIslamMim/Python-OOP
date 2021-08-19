class student:
    name=""
    roll = ""
    gpa = ""

    def setValue(self,name,roll,gpa):
        self.name=name
        self.roll=roll
        self.gpa=gpa
    def diaplay(self):
        print(f"Roll:{self.roll} Name:{self.name}  GPA:{self.gpa}")

rahim = student()
rahim.setValue("Rahim",111,5.00)
rahim.diaplay()
#print(f"Rahim->  Roll:{rahim.roll}    GPA:{rahim.gpa}")

Fahim = student()
Fahim.setValue("Fahim",113,4.55)
Fahim.diaplay()

farhad = student()
farhad.setValue("Farhad",115,3.33)
farhad.diaplay()