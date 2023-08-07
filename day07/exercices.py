it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]

print('Exercice 1')
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

print('Exercice 2')
print('1')
print(A.update(B))

print('2')
print(A.intersection(B))

print('3')
print(A.issubset(B))

print('4')
print(A.isdisjoint(B))

print('5')
print(A.union(B))
print(B.union(A))

print('6')
print(A.symmetric_difference(B))

print('7')
del A
del B

print('Exercice 3')
print('1')
print(len(age))
print(len(set(age)))