number_of_days = int(input('Брой дни:'))
total_food = float(input('общо храна:'))
bisquits = 0
eaten_food_by_dog = 0
eaten_food_by_cat = 0
total_eaten_food = 0
days_counter = 0
for each_day in range(number_of_days):
    eaten_food_by_dog_for_day = int(input('Храна куче за деня:'))
    eaten_food_by_cat_for_day = int(input('храна за коте'))
    eaten_food_by_cat += eaten_food_by_cat_for_day
    eaten_food_by_dog += eaten_food_by_dog_for_day
    total_eaten_food += eaten_food_by_dog_for_day + eaten_food_by_cat_for_day
    days_counter += 1
    if days_counter == 3:
        bisquits += 0.1 * (eaten_food_by_dog_for_day + eaten_food_by_cat_for_day)
        days_counter = 0
print(f'Total eaten biscuits: {round(bisquits)}gr.')
print(f'{(total_eaten_food/total_food*100):.2f}% of the food has been eaten.')
print(f'{(eaten_food_by_dog/total_eaten_food*100):.2f}% eaten from the dog.')
print(f'{(eaten_food_by_cat/total_eaten_food*100):.2f}% eaten from the cat.')
input()