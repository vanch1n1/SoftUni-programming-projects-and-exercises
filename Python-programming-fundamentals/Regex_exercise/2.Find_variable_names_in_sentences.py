import re
data = input()
pattern = r"((?<=^_)|(?<=\s_))[A-Za-z0-9]+\b"
hyphens = re.finditer(pattern, data)
hyphens = [i.group()for i in hyphens]
print(','.join(hyphens))
