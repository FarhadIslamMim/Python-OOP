import re
pattern = r"[aeiou]"
if re.match(pattern, "acolour"):
    print("match")
else:
    print("not march")

pattern = r"[A-Z]"
if re.match(pattern, "acolour"):
    print("match")
elif re.match(pattern, "Scolour"):
    print("match")

else:
    print("not march")

pattern = r"[a-z]"
if re.match(pattern, "acolour"):
    print("match")
else:
    print("not march")

pattern = r"[0-9]"
if re.match(pattern, "acolour"):
    print("match")
elif re.match(pattern, "012"):
    print("match")
else:
    print("not march")


pattern = r"[A-Z][a-z][0-9]"
if re.match(pattern, "Aa9colour"):
    print("match")
elif re.match(pattern, "012"):
    print("match")
else:
    print("not march")