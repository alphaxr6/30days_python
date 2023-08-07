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