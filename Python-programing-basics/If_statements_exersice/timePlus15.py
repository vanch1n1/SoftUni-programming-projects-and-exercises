hours = int(input())
minutes = int(input())
if 15 + minutes > 59:
    minutes = (minutes + 15) - 60
    hours = hours + 1
    if hours == 24:
        hours = 00
        if len(str(minutes)) < 2:
            print(f'{hours}:0{minutes}')
            quit()
    if hours != 24:
        print(f'{hours}:0{minutes}')
        quit()
print(f'{hours}:{minutes + 15}')
