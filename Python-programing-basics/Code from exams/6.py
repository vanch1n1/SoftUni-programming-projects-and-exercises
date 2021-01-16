days_of_tournement = int(input())
money_raised = 0
counter_days_win = 0
counter_days_lose = 0
command = ''
for each_day in range(days_of_tournement):
    counter_win = 0
    counter_lose = 0
    command = ''
    money_raised_for_the_day = 0
    while command != 'Finish':
        command = input()
        if command == 'Finish':
            break
        outcome = input()
        if outcome == 'win':
            counter_win += 1
            money_raised_for_the_day += 20
            money_raised += 20
        elif outcome == 'lose':
            counter_lose += 1

    if counter_win > counter_lose:
        discount_for_the_day = money_raised_for_the_day * 0.1
        money_raised = money_raised + discount_for_the_day
        counter_days_win += 1
    elif counter_win < counter_lose:
        counter_days_lose += 1
if counter_days_win > counter_days_lose:
    money_raised = money_raised * 1.2
    print(f'You won the tournament! Total raised money: {money_raised:.2f}')
else:
    print(f'You lost the tournament! Total raised money: {money_raised:.2f}')