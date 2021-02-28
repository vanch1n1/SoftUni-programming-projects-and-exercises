n = int(input())
list_negative = []
list_postive = []
for iteration in range(n):
    current_num = int(input())
    if current_num >= 0:
        list_postive.append(current_num)
    elif current_num < 0:
        list_negative.append(current_num)
print(list_postive)
print(list_negative)
print(f'Count of positives: {len(list_postive)}. Sum of negatives: {sum(list_negative)}')