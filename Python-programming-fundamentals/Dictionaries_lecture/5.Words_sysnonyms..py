n = int(input())
dictionary = {}
for word in range(n):
    word = input()
    synonym = input()
    if word in dictionary:
        dictionary[word].append(synonym)
    else:
        dictionary[word] = []
        dictionary[word].append(synonym)
for key, value in dictionary.items():
    print(f"{key} - {', '.join(value)}")
