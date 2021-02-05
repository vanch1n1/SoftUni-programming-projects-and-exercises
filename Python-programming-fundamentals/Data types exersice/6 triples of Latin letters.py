number = int(input())
output = ''
first_char_in_ascii = ord('a')
for first_char in range(1, number + 1):
    for second_char in range(1, number + 1):
        for third_char in range(1, number + 1):
            print(f'{chr(96 + first_char)}{chr(96 + second_char)}{chr(96 + third_char)}')

