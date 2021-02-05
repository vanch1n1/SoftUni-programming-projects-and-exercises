first_input = int(input())
second_input = int(input())
result = ''
for every_number in range(first_input, second_input + 1):
    symbol = chr(every_number)
    result += (' '+symbol)
print(result)