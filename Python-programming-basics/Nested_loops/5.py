town = input()

while town != 'End':
    minumum_budget = float(input())
    current_money_saved = 0

    while minumum_budget > current_money_saved:
        money = float(input())
        current_money_saved += money

        if current_money_saved >= minumum_budget:
            print(f'Going to {town}!')

    town = input()