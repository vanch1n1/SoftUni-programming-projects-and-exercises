numbers = input().split()
new_list = []
for every_number in numbers:
    every_number = int(every_number)
    every_number = every_number * -1
    new_list.append(every_number)
print(new_list)