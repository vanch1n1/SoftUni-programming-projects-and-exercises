line = input()
dictionary = {}
while line != 'Lumpawaroo':
    if "->" in line:
        force_user, force_side = line.split(" -> ")
        if force_user not in dictionary.items():
            dictionary[force_side].append(force_user)
        else:
            for key, values in dictionary.items():
                if dictionary[key] == force_user:
                    dictionary[key].remove(force_user)
            dictionary[force_side].append(force_user)

    elif '|' in line:
        force_side, force_user = line.split(" | ")
        if force_side not in dictionary:
            dictionary[force_side] = []
            dictionary[force_side].append(force_user)
        else:
            dictionary[force_side].append(force_user)



    line = input()
print(dictionary)