email = input()
line = input()
encrypted_mail = []
while line != 'Complete':
    line = line.split()
    command = line[0]
    if command == 'Make':
        if line[1] == 'Upper':
            email = email.upper()
            print(email)
        elif line[1] == 'Lower':
            email = email.lower()
            print(email)
    if command == 'GetDomain':
        counter = int(line[1])
        # email_first_half = email[:counter]
        # second_half_email =int email[coun]
        print(email[-counter:])
    if command == 'GetUsername':
        if email.find('@') != -1:
            index = email.find("@")
            print(email[:index])
        else:
            print(f"The email {email} doesn't contain the @ symbol.")
    if command == 'Replace':
        char = line[1]
        email = email.replace(char, '-')
        print(email)
    if command == 'Encrypt':
        for i in email:
            acsi_letter = str(ord(i))
            encrypted_mail.append(acsi_letter)
        print(' '.join(el for el in encrypted_mail))
    line = input()