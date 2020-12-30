budget = float(input())
season = input()
destination = ''
hotel = ''
left_budget = ''
if budget <= 100:
    destination = 'Bulgaria'
    if season == 'summer':
       hotel = 'camp'
    left_budget = budget * 0.7
    if season == 'winter':
       hotel = 'hotel'
    left_budget = budget * 0.3
if budget > 100:
    destination = 'Europe'
    hotel = 'hotel'

print(f'Somewehre in {destination} in {hotel}. Left sum {left_budget}')


