projection = input()
r = int(input())
c = int(input())
output = 0
if projection == 'Premiere':
    output = r * c * 12
elif projection == 'Normal':
    output = r * c * 7.5
elif    projection == 'Discount':
    output  = r * c * 5
print(f'{output:.2f}')