number = float(input())

if number < 0 and number > -1:
    print('small negative')
elif number == 0:
    print('zero')
elif number > 0 and number < 1:
    print('small positive')
elif number >= -1:
    print('positive')
elif number > 100000:
    print('large postive')
else:
    print('large negative')
