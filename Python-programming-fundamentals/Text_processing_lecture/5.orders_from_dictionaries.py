class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity
products = []
data = input
while data != 'buy':
    name, price, quantity = data.split()
    if name not in map(lambda x: x.name, products):
        product = Product(name, price, quantity)
        products.append(product)
    else:
        product = filter




class Weapon:
    def __init__(self, bullets):
        self.bullets = bullets
    def shoot(self):
        if self.bullets:
            self.bullets -= 1
            return 'shooting...'
        else:
            return 'no bullets left'
    def __repr__(self):
        return f'Remaining bullets:{self.bullets}'

weapon = Weapon(5)



