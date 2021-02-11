products = {}
command = input()
while command != 'statistics':
    product, quantity = command.split(": ")
    quantity = int(quantity)
    if product in products:
        products[product] += quantity
    else:
        products[product] = quantity
    command = input()
total_quantity = 0
counter_products = 0
print('Products in stock:')
for every_product in products.items():
    print(f'- {every_product[0]}: {every_product[1]}')
    total_quantity += every_product[1]
    counter_products += 1
print(f'Total Products:{counter_products}')
print(f'Total Quantity: {total_quantity}')
