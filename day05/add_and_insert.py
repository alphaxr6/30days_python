#syntax

lst = list()
lst.append('item')

fruits = ['banana', 'orange', 'mango', 'lemon']
fruits.append('apple')
print(fruits)
fruits.append('lime')
print(fruits)

fruits.insert(2, 'apple')
print(fruits)
fruits.insert(3, 'lime')
print(fruits)

#removing
 #syntax

lst = ['item1', 'item2']
lst.remove('item1')

fruits = ['banana', 'orange', 'mango', 'lemon', 'banana']
fruits.remove('banana')
print(fruits)
fruits.remove('lemon')
print(fruits)

#syntax

lst = ['item1', 'item2']
lst.pop()
lst.pop(1)
fruits = ['banana', 'orange', 'mango', 'lemon']
fruits.pop()
print(fruits)

fruits.pop(0)
print(fruits)

#syntax
lst = ['item1','item2']
del lst[1]
del lst

fruits = ['banana', 'orange', 'mango', 'lemon', 'kiwi', 'lime']
del fruits[0]
print(fruits)
del fruits[1]
print(fruits)
del fruits[1:3]
print(fruits)
del fruits
print(fruits)
