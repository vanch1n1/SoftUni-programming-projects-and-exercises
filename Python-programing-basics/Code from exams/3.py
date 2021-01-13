fruit = input()
size_gel = input()
number_gel = int(input())


if fruit == 'Watermelon':
    if size_gel == "big":
        total_price = number_gel * (5 * 28.70)
if fruit == "Watermelon":
    if size_gel == "small":
        total_price = number_gel * (2 * 56)
if fruit == "Mango":
    if size_gel == "big":
        total_price = number_gel * (5 * 19.60)
if fruit == "Mango":
    if size_gel == "small":
        total_price = number_gel * (2 * 36.66)
if fruit == "Pineapple":
    if size_gel == "big":
        total_price = number_gel * (5 * 24.80)
if fruit == "Pineapple":
    if size_gel == "small":
        total_price = number_gel * (2 * 42.10)
if fruit == "Raspberry":
    if size_gel == "big":
        total_price = number_gel * (5 * 15.20)
if fruit == "Raspberry":
    if size_gel == "small":
        total_price = number_gel * (2 * 20)
if 400 <= total_price <= 1000:
    total_price = total_price - (total_price * 0.15)
elif total_price > 1000:
    total_price = total_price - (total_price * 0.50)
elif total_price < 400:
    total_price = total_price
print(f"{total_price:.2f} lv.")