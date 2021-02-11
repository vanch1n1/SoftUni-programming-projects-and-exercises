party_size = int(input())
days = int(input())
coins = 0
for each_day in range(1, days + 1):

    if each_day % 10 == 0:
        party_size -= 2
    if each_day % 15 == 0:
        party_size += 5
    coins += 50
    coins -= party_size * 2
    if each_day % 3 == 0:
        coins -= 3 * party_size
    if each_day % 5 == 0:
        coins += 20 * party_size
        if each_day % 3 == 0:
            coins -= party_size * 2
print(f'{party_size} companions received {int(coins/party_size)} coins each.')
