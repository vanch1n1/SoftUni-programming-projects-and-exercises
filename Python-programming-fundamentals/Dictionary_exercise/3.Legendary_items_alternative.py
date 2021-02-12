mapper = {"shards": "Shadowmourne", "fragments": "Valanyr", "motes": "Dragonwrath"}
key_materials = {"shards": 0, "fragments": 0, "motes": 0}
junks = {}
while True:
    data = input().split()
    is_found = False
    for i in range(0, len(data), 2):
        quantity = int(data[i])
        item = data[i+1].lower()
        if item in key_materials:
            key_materials[item] += quantity
        else:
            if item not in junks:
                junks[item] = quantity
            else:
                junks[item] += quantity
        for key, value in key_materials.items():
            if value >= 250:
                print(F'{mapper[key]} obtained!')
                key_materials[key] -= 250
                is_found = True
                break

        if is_found:
            break
    if is_found:
        break
ordered_key_materials = dict(sorted(key_materials.items(), key=lambda x: (-x[1], x[0])))
for key, value in ordered_key_materials.items():
    print(f'{key}: {value}')
ordered_junk_materials = sorted(junks.items(), key=lambda x: x[0])
for key, value in ordered_junk_materials:
    print(f'{key}: {value}')
