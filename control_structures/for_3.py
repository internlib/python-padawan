product = {'name': 'pen', 'imported': False, 'stock': 100, 'price': 12.00}
print(product)

for p in product.keys():
    print(p)  # key

print('\n')

for p in product.values():
    print(p)  # values

print('\n')

for k, v in product.items():
    print(f'key = {k}, value = {v}')  # key, value
print(k, v)
