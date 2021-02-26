def calculate_orders(product, quantity):
    if product == "coffee":
        price = 1.50
    elif product == 'water':
        price = 1.00
    elif product == "coke":
        price = 1.40
    elif product == "snacks":
        price = 2.00
    result = price * quantity

    return result
prod = input()
quant = int(input())
print(f'{calculate_orders(prod, quant):.2f}')