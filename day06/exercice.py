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
before = last_index - 1

parents = siblings[before:]
print(parents)


print('7')

fruits = ('banana', 'lemon', 'mango')
vegetables = ('beets', 'asparagus', 'cabbages')
animal_products = ('eggs', 'meats', 'milk')

food_stuff_tp = fruits + vegetables + animal_products

food_stuff_lt = list(food_stuff_tp)
print(type(food_stuff_tp))

print('4')
print(food_stuff_tp[3:5])

print('5')
print(food_stuff_tp[0:3])

print(food_stuff_tp[-4:-1])

del food_stuff_tp