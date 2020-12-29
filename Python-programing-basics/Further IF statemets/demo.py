


money_needed = int(input())
available_money = int(input())
days_passed = 0
spend_counter = 0
while money_needed > available_money:
    save_or_spend = input()
    summ = int(input())
    days_passed += 1
    if save_or_spend == 'spend':
        available_money -= summ
        spend_counter += 1
        if available_money < 0:
            available_money = 0
        if spend_counter == 5:
            print(f"You can't save the money.")
            print(days_passed)
            break
    if save_or_spend == 'save':
        available_money += summ

    if money_needed <= available_money:
        print(f"You saved the money for {days_passed} days.")


