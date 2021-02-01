text = input()
numbers = ''
letters = ''
symbols = ''
for every_symbol in text:
    if every_symbol.isdigit():
        numbers += every_symbol
    elif every_symbol.isalpha():
        letters += every_symbol
    else:
        symbols += every_symbol
print(numbers)
print(letters)
print(symbols)
