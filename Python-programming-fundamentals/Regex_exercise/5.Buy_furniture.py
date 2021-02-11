import re
data = input()
pattern = r"(^>>)(?P<name>\w+)<<(?P<price>\d+(\.\d+)?)\!(?P<quantity>\d+)($|\s)"
furnitures = []
total_price = 0
while data != 'Purchase':
    match = re.match(pattern, data)
    if match:
        obj = match.groupdict()
        furnitures.append(obj['name'])
        total_price += float(obj['price']) * int(obj['quantity'])
    data = input()
print('Bought furniture:')
for i in furnitures:
    print(i)
print(f'Total money spend: {total_price:.2f}')