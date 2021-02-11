elements = input().split(" ")

products = {}
for i in range(0, len(elements), 2):
    key = elements[i]
    values = elements[i + 1]
    products[key] = int(values)
print(products)