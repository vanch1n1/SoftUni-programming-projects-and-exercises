strings = input().split()
result = ''
for i in strings:
    length = len(i)
    result += i * length
print(result)