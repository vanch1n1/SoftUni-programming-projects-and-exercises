water_tank = 255
number_lines = int(input())
total_liters = 0
liters = 0
for i in range(1, number_lines + 1):
    pours = int(input())
    if pours + liters > 255:
        print('Insufficient capacity!')
    if liters + pours <= 255:
        liters += pours


print(f'{liters}')