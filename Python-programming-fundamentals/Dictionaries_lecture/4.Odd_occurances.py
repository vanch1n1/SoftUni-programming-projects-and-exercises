words = input().split()
dictionary = {}
words = [w.lower() for w in words]
for word in words:
    dictionary[word] = words.count(word)

for key, value in dictionary.items():
    if not value % 2 == 0:
        print(f"{key}", end=' ')