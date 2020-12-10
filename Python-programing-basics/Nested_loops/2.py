first_multiplier = 1
second_multiplier = 1
while first_multiplier < 11:
    second_multiplier = 1
    while second_multiplier < 11:
        print(f'{first_multiplier} * {second_multiplier} = {first_multiplier * second_multiplier}')
        second_multiplier += 1
    first_multiplier += 1

