print('welcome to our shop, what do you want?')
items = ['T-shirt','Sweater']
print('R')
print(*items, sep = ",")

items.append('jeans')
print('C')
print(*items, sep= ',')

items.insert(1,'skirt')
items.pop(3)
print('U')
print(*items, sep=',')

items.pop()
print('D')
print(*items, sep=',')


