<<<<<<< HEAD
available_amount = float(input())
gender = input()
age = int(input())
sport = input()

card_price = 0
if sport == "Gym":
    if gender == "m":
        card_price = 42
    elif gender == "f":
        card_price = 35
elif sport == "Boxing":
    if gender == "m":
        card_price = 41
    elif gender == "f":
        card_price = 37
elif sport == "Yoga":
    if gender == "m":
        card_price = 45
    elif gender == "f":
        card_price = 42
elif sport == "Zumba":
    if gender == "m":
        card_price = 34
    elif gender == "f":
        card_price = 31
elif sport == "Dances":
    if gender == "m":
        card_price = 51
    elif gender == "f":
        card_price = 53
elif sport == "Pilates":
    if gender == "m":
        card_price = 39
    elif gender == "f":
        card_price = 37
if age <= 19:
    card_price = card_price - (card_price * 0.20)


money_needed = abs(card_price - available_amount)
if available_amount >= card_price:
    print(f"You purchased a 1 month pass for {sport}.")
else:
=======
available_amount = float(input())
gender = input()
age = int(input())
sport = input()

card_price = 0
if sport == "Gym":
    if gender == "m":
        card_price = 42
    elif gender == "f":
        card_price = 35
elif sport == "Boxing":
    if gender == "m":
        card_price = 41
    elif gender == "f":
        card_price = 37
elif sport == "Yoga":
    if gender == "m":
        card_price = 45
    elif gender == "f":
        card_price = 42
elif sport == "Zumba":
    if gender == "m":
        card_price = 34
    elif gender == "f":
        card_price = 31
elif sport == "Dances":
    if gender == "m":
        card_price = 51
    elif gender == "f":
        card_price = 53
elif sport == "Pilates":
    if gender == "m":
        card_price = 39
    elif gender == "f":
        card_price = 37
if age <= 19:
    card_price = card_price - (card_price * 0.20)


money_needed = abs(card_price - available_amount)
if available_amount >= card_price:
    print(f"You purchased a 1 month pass for {sport}.")
else:
>>>>>>> f5e08af265b4e5302a530dba1d0ac93840d06fcc
    print(f"You don't have enough money! You need ${money_needed:.2f} more.")