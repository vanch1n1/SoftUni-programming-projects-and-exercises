factor = int(input())
count = int(input())
my_list = []
number = 0
for i in range(1, count + 1):
    number = i * factor
    my_list.append(number)
print(my_list)