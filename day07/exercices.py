it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]

print('1')
print(len(it_companies))

print('2')
it_companies.add('Twitter')
print(it_companies)

print('3')
it_companies.update(['Samsung','MSI', 'Lenovo', 'Alienware', 'Asus'])
print(it_companies)

print('4')
removed_item = it_companies.pop()
print('{} was removed from the list'.format(removed_item))
print(it_companies)

print('5')
it_companies.discard('IBM')
print(it_companies)