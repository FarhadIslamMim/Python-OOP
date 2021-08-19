import re
pattern= r"Colour"
text1="Every man love Colour.Colour is beautful, i love Colour"

text2=re.sub(pattern,"Color",text1,)
print(text2)
text2=re.sub(pattern,"Color",text1,count=1)
print(text2)
text2=re.sub(pattern,"Color",text1,count=2)
print(text2)