text = input()
dictionary = {}
for every_letter in text:
    if every_letter != ' ':
        if not every_letter in dictionary:
            dictionary[every_letter] = 1
        else:
            dictionary[every_letter] += 1

for key, value in dictionary.items():
    print(f"{key} -> {value}")

