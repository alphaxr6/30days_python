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
family_update = list(siblings)
parents = ['Papa', 'Maman']
family_members = family_update.extend(parents)
print(family_members)
print(type(family_members))
family_members = tuple(family_members)
