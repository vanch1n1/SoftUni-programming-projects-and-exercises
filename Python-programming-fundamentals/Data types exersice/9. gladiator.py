lost_fights = int(input())
price_helmet = float(input())
price_sword = float(input())
price_shield = float(input())
price_armor = float(input())
counter_shield_brakes = 0
total_cost = 0
for every_fight in range(1, lost_fights + 1 ):
    if every_fight % 2 == 0:
        total_cost += price_helmet
    if every_fight % 3 == 0:
        total_cost += price_sword
    if every_fight % 3 == 0 and every_fight % 2 == 0:
        total_cost += price_shield
        counter_shield_brakes += 1
        if counter_shield_brakes % 2== 0:
            total_cost += price_armor



print(f'Gladiator expenses: {total_cost:.2f} aureus')

