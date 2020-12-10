first_number = int(input())
second_number = int(input())
magic_number = int(input())
combination = 0
flag = False
for first_loop in range(first_number, second_number + 1):
    for second_loop in range(first_number, second_number + 1):
            combination += 1
            if magic_number == first_loop + second_loop:
               flag = True
               print(f'Combination N:{combination} ({first_loop} + {second_loop} = {magic_number})')
               break
    if flag:
        break
if not flag:
        print(f'{combination} combinations - neither equals {magic_number} ')

