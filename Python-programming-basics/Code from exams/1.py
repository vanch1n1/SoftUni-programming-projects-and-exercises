<<<<<<< HEAD
number_of_groups = int(input())
musala_climbers = 0
monblan_climbers = 0
klimanjaro_climbers = 0
k2_climbers = 0
everest_climbers = 0
total_climbers = 0
for each_group in range(number_of_groups):
    number_of_people = int(input())
    if number_of_people < 6:
        musala_climbers += number_of_people
        total_climbers += number_of_people
    elif number_of_people < 13:
        monblan_climbers += number_of_people
        total_climbers += number_of_people
    elif number_of_people < 26:
        klimanjaro_climbers += number_of_people
        total_climbers += number_of_people
    elif number_of_people <= 40:
        k2_climbers += number_of_people
        total_climbers += number_of_people
    elif number_of_people > 40:
        everest_climbers += number_of_people
        total_climbers += number_of_people
print(f'{(musala_climbers/total_climbers*100):.2f}%')
print(f'{(monblan_climbers/total_climbers*100):.2f}%')
print(f'{(klimanjaro_climbers/total_climbers*100):.2f}%')
print(f'{(k2_climbers/total_climbers*100):.2f}%')
print(f'{(everest_climbers/total_climbers*100):.2f}%')
=======
number_of_groups = int(input())
musala_climbers = 0
monblan_climbers = 0
klimanjaro_climbers = 0
k2_climbers = 0
everest_climbers = 0
total_climbers = 0
for each_group in range(number_of_groups):
    number_of_people = int(input())
    if number_of_people < 6:
        musala_climbers += number_of_people
        total_climbers += number_of_people
    elif number_of_people < 13:
        monblan_climbers += number_of_people
        total_climbers += number_of_people
    elif number_of_people < 26:
        klimanjaro_climbers += number_of_people
        total_climbers += number_of_people
    elif number_of_people <= 40:
        k2_climbers += number_of_people
        total_climbers += number_of_people
    elif number_of_people > 40:
        everest_climbers += number_of_people
        total_climbers += number_of_people
print(f'{(musala_climbers/total_climbers*100):.2f}%')
print(f'{(monblan_climbers/total_climbers*100):.2f}%')
print(f'{(klimanjaro_climbers/total_climbers*100):.2f}%')
print(f'{(k2_climbers/total_climbers*100):.2f}%')
print(f'{(everest_climbers/total_climbers*100):.2f}%')
>>>>>>> f5e08af265b4e5302a530dba1d0ac93840d06fcc
