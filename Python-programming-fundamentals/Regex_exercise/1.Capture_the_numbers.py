import re
data = input()
numbers = []
pattern = "\\d+"
while data:
    match = re.findall(pattern, data)
    if match:
        numbers.extend(match)
    data = input()
print(*numbers, sep=' ')