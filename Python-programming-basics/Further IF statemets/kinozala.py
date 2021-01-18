<<<<<<< HEAD
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
=======
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
>>>>>>> f5e08af265b4e5302a530dba1d0ac93840d06fcc
print(f'{output:.2f}')