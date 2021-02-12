line = input()
dictionary = {}
while line != 'End':
    name, emp_id = line.split(' -> ')
    if name not in dictionary:
        dictionary[name] = []
    if emp_id not in dictionary[name]:
        dictionary[name].append(emp_id)

    # else:
    #     dictionary[name].append(id)

    line = input()
for name, emp_id in sorted(dictionary.items(), key=lambda x: x[0]):
    print(name)
    for i in range(len(emp_id)):
        print(f"-- {emp_id[i]}")
