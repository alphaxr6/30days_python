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
union = A.union(B)
print(union)

print('2')
inter = A.intersection(B)
print(inter)

print('3')
subset = A.issubset(B)
print(subset)

print('4')
disjoin = A.isdisjoint(B)
print(disjoin)

print('5')
A_and_B = A.union(B)
B_and_A = B.union(A)
print(A_and_B)
print(B_and_A)

print('6')
symmetric = A.symmetric_difference(B)
print(symmetric)

print('7')
del A
del B