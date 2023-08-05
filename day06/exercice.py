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
family_members_tmp = family_update.extend(parents)
family_members = tuple(family_members_tmp)
