import math

name_of_player = input()
number_of_games = int(input())
total_points = 0
counter_voleyball = 0
counter_tennis = 0
counter_badmington = 0
points_voleyball = 0
points_tennis = 0
points_badmington = 0
for each_game in range(number_of_games):
    game = input()
    if game == 'volleyball':
        points_vol = int(input())
        points_voleyball += points_vol * 1.07
        counter_voleyball += 1
    if game == 'tennis':
        points_ten = int(input())
        points_tennis += points_ten * 1.05
        counter_tennis += 1
    if game == 'badminton':
        points_bad = int(input())
        points_badmington += points_bad * 1.02
        counter_badmington += 1
total_points = points_badmington + points_tennis + points_voleyball
total_points = math.floor(total_points)
average_volleybal = points_voleyball / counter_voleyball
average_tennis = points_tennis / counter_tennis
average_badminton = points_badmington / counter_badmington
if average_volleybal < 75 or average_tennis < 75 or average_badminton < 75:
    print(f'Sorry, {name_of_player}, you lost. Your points are only {total_points}.')
else:
    print(f'Congratulations, {name_of_player}! You won the cruise games with {total_points} points.')

