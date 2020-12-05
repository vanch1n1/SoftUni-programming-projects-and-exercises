
import random

first_day = int(input('enter cases:'))
if not 32 < first_day < 330:
    first_day = int(input('enter realistic number, between 32 and 320:'))
y = [first_day]
x = [0]
days = 0
last_3_days = 0
while days < 30:
    if days > 3:
        last_3rd_day = (y[-3])
        last_2nd_day = (y[-2])
        last_1sth_day = (y[-1])
        last_3_days = last_3rd_day + last_2nd_day + last_1sth_day
        if last_3_days > 450:
            number = random.randint(300, 1000)
            y.append(number)
            days += 1
            x.append(days)   n
        if last_3_days < 150:
            number = random.randint(10, 50)
            y.append(number)
            days += 1
            x.append(days)
        if 150 <last_3_days < 450:
            number = random.randint(32, 300)
            y.append(number)
            days += 1
            x.append(days)
    else:
        number = random.randint(32, 300)
        y.append(number)
        days += 1
        x.append(days)
print(x)
print(y)

