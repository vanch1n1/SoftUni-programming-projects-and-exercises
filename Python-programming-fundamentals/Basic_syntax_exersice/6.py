godina = int(input())


while True:
    godina += 1
    if len(str(godina)) == len(set(str(godina))):
        print(godina)
        break

