bought_food = int(input())
bought_food = bought_food * 1000
left_food = 0
command = ''
while command != 'Adopted':
    command = input()
    if command != 'Adopted':
        left_food = bought_food - (int(command))
        bought_food -= int(command)
    else:
        break
if left_food >= 0:
    print(f'Food is enough! Leftovers: {left_food} grams.')
elif left_food < 0:
    print(f'Food is not enough. You need {abs(left_food)} grams more.')
