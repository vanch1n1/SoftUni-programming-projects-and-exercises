n = int(input())
result = 0
for every_input in range(1, n + 1):
    letter = input()
    result += ord(letter)
print(f'The sum equals: {result}')
