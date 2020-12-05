import random


y = []
x = []
days = 0
while days <= 30:
    number = random.randint(32, 300)
    y.append(number)
    days += 1
    x.append(days)
print(x)
print(y)



