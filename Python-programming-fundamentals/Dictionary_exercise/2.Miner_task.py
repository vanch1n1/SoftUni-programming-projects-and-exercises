resource = input()
dictionary = {}
while resource != 'stop':
    quantity = int(input())
    if not resource in dictionary:
        dictionary[resource] = quantity
    else:
        dictionary[resource] += quantity
    resource = input()
for key, value in dictionary.items():
    print(f"{key} -> {value}")

