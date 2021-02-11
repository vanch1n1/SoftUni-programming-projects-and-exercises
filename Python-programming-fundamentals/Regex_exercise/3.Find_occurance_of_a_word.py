import re
data = input()
searched_word = input()
pattern = f"\\b{searched_word}\\b"
occurances = re.findall(pattern, data, re.IGNORECASE)
print(len(occurances))