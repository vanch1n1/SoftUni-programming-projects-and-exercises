type_flower = input()
number_of_flowers = int(input())
budget = int(input())
price = 0
if type_flower == 'rose':
    if number_of_flowers > 80:
        price = 0.9 * 5 * 80
    else:
        price = 5 * number_of_flowers



if budget >= price:
   print (f'Hey, you have a great garden with {number_of_flowers} {type_flower} and {budget - price} leva left.')
else:
   print(f'Not enough money, you need {price - budget} leva')