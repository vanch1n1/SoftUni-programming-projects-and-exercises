import re
data = input()
pattern = r"(^|(?<=\s))[A-Za-z0-9]+[\,.-]?[A-Za-z0-9]+@[,-.A-Za-z]+\-?[,-.A-Za-z]+\-?[,-.A-Za-z]+"
emails = re.finditer(pattern, data)
for i in emails:
    print(i.group())