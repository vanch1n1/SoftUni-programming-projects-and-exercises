century = int(input())
years = 100 * century
days = int(365.2422 * years)
hours = days * 24
minutes = hours * 60
print(f'{century} centuries = {years} years = {days} days = {hours} hours = {minutes} minutes')