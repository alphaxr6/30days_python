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
siblings = list(siblings)
parents = ['Papa', 'Maman']
siblings.extend(parents)
siblings = tuple(siblings)
print(siblings)
print(type(siblings))

print('6')
print(len(siblings))
last_index = len(siblings) - 1
before = last_index - 2

parents = siblings[before:last_index]
print(parents)
