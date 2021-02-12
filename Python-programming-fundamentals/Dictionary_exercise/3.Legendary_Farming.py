elements = input().split()
dictionary = {}
for every_element in range(0, len(elements), 2):
    value = elements[every_element]
    value = int(value)
    key = elements[every_element+1]
    key = key.lower()
    if key in dictionary:
        dictionary[key] += int(value)
    else:
        dictionary[key] = int(value)



if dictionary['motes'] > 250:
    dictionary['motes'] -= 250
    print('Dragonwrath obtained')
if dictionary['fragments'] > 250:
    dictionary['fragments'] -= 250
    print('Valanyr obtained')
if dictionary['shards'] > 250:
    dictionary['shards'] -= 250
    print('Shadowmourne obtained')
sorted_dict = dict(sorted(dict.items(), key=lambda x: x[1]))
print(sorted_dict)