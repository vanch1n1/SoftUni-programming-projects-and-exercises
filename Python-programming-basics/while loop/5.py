transactions_count = int(input())
transactions_made = 0
account_balance = 0
while transactions_made < transactions_count:
    transaction_balance = float(input())
    if transaction_balance < 0:
        print('Invalid operation!')
        break
    account_balance += transaction_balance
    print(f'Increase: {transaction_balance:.2f}')
    transactions_made += 1
print(f'Total: {account_balance:.2f}')