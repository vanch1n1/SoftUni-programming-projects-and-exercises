banned_words = input().split(', ')
text = input()
for every_word in banned_words:
    if every_word in text:
        text = text.replace(every_word, len(every_word) * '*')
print(text)
