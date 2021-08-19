import re
pattern= r"Colour"
if re.match(pattern,"Colour is beautful, i love Colour"):
    print("match")
else:
    print("not match")

if re.search(pattern,"Colour is beautful, i love Colour"):
    print("match")
else:
    print("not match")
pattern2=r"Col"
print(re.findall(pattern2,"Colour is beautful, i love Colour"))