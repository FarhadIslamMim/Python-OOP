class student:
    roll = ""
    gpa = ""

rahim = student()
#print(isinstance(rahim,student))
rahim.roll = 111
rahim.gpa = 5.00
print(f"Rahim->  Roll:{rahim.roll}    GPA:{rahim.gpa}")

Fahim = student()
#print(isinstance(rahim,student))
Fahim.roll = 113
Fahim.gpa = 4.50
print(f"Fahim->  Roll:{Fahim.roll}    GPA:{Fahim.gpa}")

farhad = student()
#print(isinstance(rahim,student))
farhad.roll = 115
farhad.gpa = 4.00
print(f"Farhad-> Roll:{farhad.roll}    GPA:{farhad.gpa}")