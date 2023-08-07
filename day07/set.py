#Creating a set
#syntax

st = set()

st = {'item1', 'item2', 'item3', 'item4'}

fruits = {'banana', 'orange', 'mango', 'lemon'}

#Get length

print(len(fruits))

#Chcking an item

print('mango' in fruits)

#Adding item to a set

fruits.add('lime')
print(fruits)

vegetables = ('tomato', 'potato', 'cabbage', 'onion', 'carrot')

fruits.update(vegetables)
print(fruits)

#Removing items from a set

fruits = {'banana', 'orange', 'mango', 'lemon'}
fruits.pop()

removed_item = fruits.pop()
print(removed_item)
print(fruits)

#clearing a set

fruits = {'banana', 'orange', 'mango', 'lemon'}
fruits.clear()
print(fruits)

#Deleting a set

del fruits

#Converting list to set 

fruits = ['banana', 'orange', 'mango', 'lemon', 'orange', 'banana']
fruits = set(fruits)
print(fruits)

#Joining set
fruits = {'banana', 'orange', 'mango', 'lemon'}
vegetables = {'tomato', 'potato', 'cabbage','onion', 'carrot'}

print(fruits.union(vegetables))

fruits = {'banana', 'orange', 'mango', 'lemon'}
vegetables = {'tomato', 'potato', 'cabbage','onion', 'carrot'}

fruits.update(vegetables)
print(fruits)

#Intersection
whole_numbers = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
even_numbers = {0, 2, 4, 6, 8, 10}
whole_numbers.intersection(even_numbers)
print(whole_numbers)

python = {'p', 'y', 't', 'h', 'o','n'}
dragon = {'d', 'r', 'a', 'g', 'o','n'}
python.intersection(dragon)  
print(python)

#subset or super set

whole_numbers = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
even_numbers = {0, 2, 4, 6, 8, 10}
whole_numbers.issubset(even_numbers)
whole_numbers.issuperset(even_numbers)

print(whole_numbers)

#checking difference between 2 sets
whole_numbers = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
even_numbers = {0, 2, 4, 6, 8, 10}
whole_numbers.difference(even_numbers)
print(whole_numbers)

python = {'p', 'y', 't', 'o','n'}
dragon = {'d', 'r', 'a', 'g', 'o','n'}
python.difference(dragon)
print(python)
#Symmetric

whole_numbers = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
some_numbers = {1, 2, 3, 4, 5}
whole_numbers.symmetric_difference(some_numbers)
print(whole_numbers)
python = {'p', 'y', 't', 'h', 'o','n'}
dragon = {'d', 'r', 'a', 'g', 'o','n'}
python.symmetric_difference(dragon)
print(python)

#Join and disjoin

even_numbers = {0,2,4,6,8}
odd_numbers = {1,3,5,7,9}
even_numbers.isdisjoint(odd_numbers)
print(even_numbers)
python = {'p', 'y', 't', 'h', 'o','n'}
dragon = {'d', 'r', 'a', 'g', 'o','n'}
python.isdisjoint(dragon)
print(python)

