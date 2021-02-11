line = input()
while line != 'end':
    reversed_line = ''
    for i in range(len(line) -1, -1, -1):
        a = line[i]
        reversed_line += a
    print(f'{line} = {reversed_line}')

    line = input()