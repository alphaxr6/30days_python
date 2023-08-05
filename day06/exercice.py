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
parents = siblings[-1:-2]
print(parents)

del siblings[-1:-2]
print(siblings)