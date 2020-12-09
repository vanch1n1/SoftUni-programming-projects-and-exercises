

text = input()
text_lenght = len(text)
vowels_sum = 0
for position in range(text_lenght):
    current_chart = text[position]
    if current_chart == 'a':
        vowels_sum += 1
    elif current_chart == "e":
        vowels_sum += 2

ptint(vowels_sum)




