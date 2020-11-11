products = []
with open('products.txt', 'r') as f:
    for line in f:
        if 'Product, Price' in line:
            continue
        name, price = line.strip().split(',')
        products.append([name, price])
print(products)

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

with open('products.txt', 'w') as f:
    f.write('Product, Price\n')
    for p in products:
        f.write(p[0] + ',' + str(p[1]) + '\n')
