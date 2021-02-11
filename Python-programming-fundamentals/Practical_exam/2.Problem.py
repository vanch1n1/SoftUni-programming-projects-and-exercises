import re
pattern = r'(%|\$)(?P<tag>[A-Z][a-z]{2,})\1:\s+\[(?P<number>[0-9]+)\]\|\[(?P<secondnumber>[0-9]+)\]\|\[(?P<thirdnumber>[0-9]+)\]'
n = int(input())
flag = False
for n in range(n):
    matched_case = None
    message = input()
    decrypted_message = ''
    valid_message = re.finditer(pattern, message)
    for i in valid_message:
        match = i.groupdict()
        for key, value in match.items():
            if key != 'tag':
                number = value
                number = int(number)
                char_from_ascii = chr(number)
                decrypted_message += char_from_ascii
        print(f'{match["tag"]}: {decrypted_message}')
    matched_case = re.match(pattern, message)
    if not matched_case:
        print('Valid message not found!')
