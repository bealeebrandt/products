products = []
while True:
    name = input('Please insert the name of the product: ')
    if name == 'q':
        break
    price = input('please incert the price of the product: ')
    products.append([name, price])
print(products)
