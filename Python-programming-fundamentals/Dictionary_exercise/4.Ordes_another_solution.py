product = input()
product_prices = {}
product_quantities = {}
while product != 'buy':
    name, price, quantity = product.split()
    price = float(price)
    quantity = int(quantity)
    if name not in product_prices and name not in product_quantities:
        product_prices[name] = price
        product_quantities[name] = quantity
    else:
        product_quantities[name] += quantity
        product_prices[name] = price
    product = input()

for key, value in product_prices.items():
    total_price = value * product_quantities[key]
    print(f"{key} -> {total_price:.2f}")