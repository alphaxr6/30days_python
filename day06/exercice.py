print('1')
empty_tuple = ()

print('2')
sisters = ('Marie', 'Anne', 'Sarah')
brothers = ('Jean', 'Jacques', 'Mohammed')

print('3')
siblings = sisters + brothers

print('4')
print(len(siblings))

print('5')
print(type(siblings))
siblings = list(siblings)
print(type(siblings))
parents = ['Papa', 'Maman']
siblings.extend(parents)
print(siblings)
print(type(siblings))
siblings = tuple(siblings)
