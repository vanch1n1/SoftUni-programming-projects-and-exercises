trip_price = float(input('Trip price:'))
Puzzle = int(input('Puzzle:'))
Barbie = int(input('Barbie:'))
TeddyBear = int(input('TeddyBear:'))
Minion = int(input('Minion:'))
Thruck = int(input('Thruck:'))

Moneyearned = Puzzle * 2.60 + Barbie * 3 + TeddyBear * 4.10 + Minion * 8.20 + Thruck * 2


totalToys = Puzzle + Barbie + TeddyBear + Minion + Thruck
if totalToys >= 50:
    discount = 0.25
    Moneyearned = Moneyearned - discount
rent = Moneyearned * 0.1
revenue = Moneyearned - rent
if revenue > trip_price:
    outcome = revenue - trip_price
    print(f'Yes! {outcome:.2f} left')
else:
    outcome = trip_price - revenue
    print(f'No, {outcome:.2f} needed. ')





