price_ratings = [int(el) for el in input().split()]
entry_point = int(input())
type_of_item = input()
type_price_rating = input()
left_side_item = price_ratings[:entry_point]
right_side_item = price_ratings[entry_point+1:]
sum_left = 0
sum_right = 0

if type_price_rating == 'positive':
    if type_of_item == 'cheap':
        sum_left += sum([num for num in left_side_item if num > 0 and num < price_ratings[entry_point]])
        sum_right += sum([num for num in right_side_item if num > 0 and num < price_ratings[entry_point]])
    else:
        sum_left += sum([num for num in left_side_item if num > 0 and num >= price_ratings[entry_point]])
        sum_right += sum([num for num in right_side_item if num > 0 and num >= price_ratings[entry_point]])
elif type_price_rating == 'negative':
    sum_left += sum([num for num in left_side_item if num < 0])
    sum_right += sum([num for num in right_side_item if num < 0])

else:
    sum_left += sum(left_side_item)
    sum_right += sum(right_side_item)
if sum_left < sum_right:
    print(f'Right - {sum_right}')
else:
    print(f'Left - {sum_left}')
