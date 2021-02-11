drink = int(input())
if drink > 21:
    print(f'drink whisky')
if drink <= 21 and drink >= 18:
    print(f'drink beer')
if drink <= 17 and drink >= 14:
    print(f'drink coke ')
if drink < 14:
    print(f'drink toddy')