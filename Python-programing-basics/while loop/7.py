import sys

n = int(input())
smallest_number = sys.maxsize
for i in range(n):
    current_number = int(input())
    if current_number < smallest_number:
        smallest_number = current_number
print(f'{smallest_number}')