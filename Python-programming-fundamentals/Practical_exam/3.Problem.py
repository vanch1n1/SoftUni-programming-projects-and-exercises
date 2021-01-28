line = input()
people = {}
while line != 'Results':
    line = line.split(':')
    command = line[0]
    if command == 'Add':
        person = line[1]
        if not person in people:
            health = int(line[2])
            energy = int(line[3])
            people[person] = {'health': health, 'energy': energy}
        else:
            health = int(line[2])
            energy = int(line[3])
            people[person]['health'] += health
            people[person]['energy'] += energy
    elif command == 'Attack':
        attacker = line[1]
        defender = line[2]
        damage = int(line[3])
        if attacker in people and defender in people:
            people[defender]['health'] -= damage
            people[attacker]['energy'] -= 1
            if people[defender]['health'] <= 0:
                people.pop(defender)
                print(f'{defender} was disqualified!')
            if people[attacker]['energy'] <= 0:
                people.pop(attacker)
                print(f'{attacker} was disqualified!')
    if command == 'Delete':
        name = line[1]
        if name == 'All':
            people.clear()
        else:
            people.pop(name)
    line = input()
print(f'People count: {len(people)}')
people = dict(people)
sorted_people = dict(sorted(people.items(), key=lambda x: (-x[1]['health'], x[0])))
for key, value in sorted_people.items():
    print(f'{key} - {value["health"]} - {value["energy"]}')

