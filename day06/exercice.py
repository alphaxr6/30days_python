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
update = list(siblings)
family_members_tmp = siblings.append('Papa', 'Maman')
family_members = tuple(family_members_tmp)
