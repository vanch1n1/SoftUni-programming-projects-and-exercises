import sys

n = int(input())
biggest_number = -sys.maxsize
for i in range(n):
    number = int(input())
    if i == 0:
        biggest_number = number
    else:
        if number > biggest_number:
            biggest_number = number
print(f'{biggest_number}')
