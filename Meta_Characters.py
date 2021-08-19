import re
pattern=r"colo.r"
if re.match(pattern,"colour"):
    print("match")
else:
    print("not march")
pattern=r"colo...r"
if re.match(pattern,"coloubr"):
    print("match")
else:
    print("not march")


pattern1=r"^colo.r$"
if re.match(pattern1,"colour"):
    print("match")
else:
    print("not march")
pattern1=r"^colo..r$"
if re.match(pattern1,"coloubr"):
    print("match")
else:
    print("not march")



pattern2=r"a*"
if re.match(pattern2,"acolour"):
    print("match")
else:
    print("not march")
pattern2=r"(ab)*"
if re.match(pattern2,"coloubr"):
    print("match")
else:
    print("not march")



pattern12=r"a+"
if re.match(pattern12,"acolour"):
    print("match")

else:
    print("not march")
pattern12=r"a+b"
if re.match(pattern12,"abcoloubr"):
    print("match")
else:
    print("not march")




pattern122=r"ice(-)?cream"
if re.match(pattern122,"ice-cream"):
    print("match")

else:
    print("not march")
pattern122=r"icecream"
if re.match(pattern122,"ice-cream"):
    print("match")
else:
    print("not march")



pattern122=r"a{1,2}$"
if re.match(pattern122,"aa"):
    print("match")

else:
    print("not march")
pattern122=r"a{1,2$}"
if re.match(pattern122,"aaaa"):
    print("match")
else:
    print("not march")