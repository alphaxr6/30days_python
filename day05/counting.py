#Counting

fruits = ['banana', 'orange', 'mango', 'lemon']
print(fruits.count('orange'))
ages = [22, 19, 24, 25, 26, 24, 25, 24]
print(ages.count(24))

# Finding index of an item

fruits = ['banana', 'orange', 'mango', 'lemon']
print(fruits.index('orange'))
ages = [22, 19, 24, 25, 26, 24, 25, 24]
print(ages.index(24))

#Reversing list

fruits = ['banana', 'orange', 'mango', 'lemon']
print(fruits)
fruits.reverse()
print(fruits)
ages = [22, 19, 24, 25, 26, 24, 25, 24]
print(ages)
ages.reverse()
print(ages)

#Sorting list
fruits = ['banana', 'orange', 'mango', 'lemon']
print(fruits)
fruits.sort()
print(fruits)

ages = [22, 19, 24, 25, 26, 24, 25, 24]
print(ages)
ages.sort()
print(ages)

ages.sort(reverse=True)
print(ages)

#Without updating the original list
fruits = ['banana', 'orange', 'mango', 'lemon']
print(sorted(fruits))

fruits = ['banana', 'orange', 'mango', 'lemon']
fruits = print(sorted(fruits, reverse=True))
prints(fruits)