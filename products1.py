products = []
while True:
    name = input('Please insert the name of the product: ')
    if name == 'q':
        break
    price = input('please incert the price of the product: ')
    p = []
    p.append(name)
    p.append(price)
    products.append(p)
print(products)

for p in products:
    print(p[0], 'price is', p[1])
    
