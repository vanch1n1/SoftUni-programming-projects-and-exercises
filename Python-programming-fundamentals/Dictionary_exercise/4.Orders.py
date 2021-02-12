product = input()
dictionary = {}
while product != 'buy':
    name, price, quantity = product.split()
    price = float(price)
    quantity = int(quantity)
    if name in dictionary:
        dictionary[name]["price"] = price
        dictionary[name]["quantity"] += quantity

    else:
        dictionary[name] = {'price': price, 'quantity': quantity}
    product = input()

for key, value in dictionary.items():
    total_price = dictionary[key]['price'] * dictionary[key]["quantity"]
    print(f"{key} -> {total_price:.2f}")