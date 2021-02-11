elements = input().split()
products = {}
for i in range(0, len(elements), 2):
    key = elements[i]
    value = elements[i+1]
    products[key] = int(value)
line_products_to_search = input().split()
for every_product in line_products_to_search:
    if every_product in products:
        print(f'We have {products[every_product]} of {every_product} left')
    else:
        print(f"Sorry, we don't have {every_product}")