cards = input().split()
a_team = []
b_team = []
for every_string in cards:
    if every_string in a_team:
        continue
    if every_string in b_team:
        continue
    if 'A' in every_string:
        a_team.append(every_string)

    elif 'B' in every_string:
        b_team.append(every_string)

print(f'Team A - {11 - len(a_team)}; Team B - {11 - len(b_team)}')

if len(a_team) > 4:
    print(f'Game was terminated')
elif len(b_team) > 4:
    print(f'Game was terminated')