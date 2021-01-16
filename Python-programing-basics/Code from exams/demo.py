number_of_groups = int(input)
Musala_counter = 0
Monblan_counter = 0
Kilimanjaro_counter = 0
K2_counter = 0
Everest_counter = 0
musala_climbers = 0
monblan_climbers = 0
klimanjaro_climbers = 0
k2_climbers = 0
everest_climbers = 0
total_climbers = 0
for each_group in range(number_of_groups):
    number_of_people = int(input)
    if number_of_people < 5:
        Musala_counter += 1
        musala_climbers += number_of_people
        total_climbers += number_of_people
    elif number_of_people < 13:
        Monblan_counter += 1
        monblan_climbers += number_of_people
        total_climbers += number_of_people
    elif number_of_people < 26:
        Kilimanjaro_counter += 1
        klimanjaro_climbers += number_of_people
        total_climbers += number_of_people
    elif number_of_people < 41:
        K2_counter += 1
        k2_climbers += number_of_people
        total_climbers += number_of_people
    elif number_of_people > 41:
        Everest_counter += 1
        everest_climbers += number_of_people
        total_climbers += number_of_people
print(f'{musala_climbers/nu}')