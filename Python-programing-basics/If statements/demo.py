days = int(input())
room = input()

mark = input()
days = days - 1
price = 0
if room == 'room for one person':

        price = 18

if room == 'apartament':
    if days < 10:
        price = days * 25 * 0.70

    if 10 <= days < 15:
        price = days * 25 * 0.65

    if days >= 15:
        price = days  * 25 * 0.5
if mark == 'positive':
            price = price + price * 0.25
if mark == 'negative':
            price = price - price * 0.1

print(f'{price:.2f}')
