n = int(input())
even_list = []
odd_list = []
negative_list = []
postive_list = []

for every_number in range( n):
    every_number = int(input())
    if every_number % 2 == 0:
        even_list.append(every_number)
    if not every_number % 2 == 0:
        odd_list.append(every_number)
    if every_number < 0:
        negative_list.append(every_number)
    if every_number >= 0:
        postive_list.append(every_number)
command = input()
if command == 'positive':
    print(postive_list)
if command == 'negative':
    print(negative_list)
if command == 'even':
    print(even_list)
if command == 'odd':
    print(odd_list)
