<<<<<<< HEAD
quantity = int(input())
days = int(input())
total_money = 0
spirit = 0
for each_day in range(1, days+1):
    if each_day % 11 == 0:
        quantity += 2
    if each_day % 2 == 0:
        total_money += quantity * 2
        spirit += 5
    if each_day % 3 == 0:
        total_money += (quantity * 5 + quantity * 3)
        spirit += 13
    if each_day % 5 == 0:
        total_money += quantity * 15
        spirit += 17
        if each_day % 3 == 0:
            spirit += 30
    if each_day % 10 == 0:
        spirit -= 20
        total_money += 15 + 5 + 3
        if each_day == days:
            spirit -= 30
print(f"Total cost: {total_money}")
print(f"Total spirit: {spirit}")
=======
quantity = int(input())
days = int(input())
total_money = 0
spirit = 0
for each_day in range(1, days+1):
    if each_day % 11 == 0:
        quantity += 2
    if each_day % 2 == 0:
        total_money += quantity * 2
        spirit += 5
    if each_day % 3 == 0:
        total_money += (quantity * 5 + quantity * 3)
        spirit += 13
    if each_day % 5 == 0:
        total_money += quantity * 15
        spirit += 17
        if each_day % 3 == 0:
            spirit += 30
    if each_day % 10 == 0:
        spirit -= 20
        total_money += 15 + 5 + 3
        if each_day == days:
            spirit -= 30
print(f"Total cost: {total_money}")
print(f"Total spirit: {spirit}")
>>>>>>> edae06bf372ceff61595a46bc049a82f253a4728
