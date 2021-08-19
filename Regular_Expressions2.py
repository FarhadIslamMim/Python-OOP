import re
pattern= r"Colour"
text="every man love Colour.Colour is beautful, i love Colour"
match=re.search(pattern,text)
if match:
    print(match.start())
    print(match.end())
    print(match.span())