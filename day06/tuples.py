empty_tuple = ()
empty_typle = tuple()

tpl = ('item1', 'item2', 'item3')

fruits = ('banana', 'orange', 'mango', 'lemon')

len(fruits)

first_fruit = fruits[0]
second_fruit = fruits[1]
last_index = len(fruits) - 1
last_fruit = fruits[last_index]

print(first_fruit)
print(second_fruit)
print(last_index)
print(last_fruit)

first_fruit = fruits[-4]
second_fruit = fruits[-3]
last_fruit = fruits[-1]
print(first_fruit)
print(second_fruit)
print(last_fruit)

all_fruits = fruits[0:4]
all_fruits = fruits[0:]
orange_mango = fruits[1:3]
orange_to_the_rest = fruits[1:]
print(all_fruits)
print(orange_mango)
print(orange_to_the_rest)

all_fruits = fruits[-4:]
orange_mango = fruits[-3:-1]
orange_to_the_rest = fruits[-3:]
print(all_fruits)
print(orange_mango)
print(orange_to_the_rest)

fruits = list(fruits)
fruits[0] = 'apple'
print(fruits)
fruits = tuple(fruits)
print(fruits)
print(type(fruits))


print('orange' in fruits)
print('melon' in fruits)

fruits = ('banana', 'orange', 'mango', 'lemon')
vegetables = ('Tomato', 'Potato', 'Cabbage','Onion', 'Carrot')
fruits_and_vegetables = fruits + vegetables

del fruits