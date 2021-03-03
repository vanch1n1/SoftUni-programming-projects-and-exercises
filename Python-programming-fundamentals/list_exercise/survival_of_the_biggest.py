numbers = input().split()
n = int(input())
#
# for every_number in range(n):
#     min_number = min(numbers)
#     numbers.remove(min_number)
#
# print(numbers)

numbers.sort()
numbers.reverse()
for every_number in range(n):
    numbers.pop()
print(numbers)