fruits = ['banana', 'orange', 'mango', 'lemon']
all_fruits = fruits[0:4]
all_fruits_alt = fruits[0:]

print(all_fruits)
print(all_fruits_alt)

orange_and_mango = fruits[1:3]
orange_mango_lemon = fruits[1:]
orange_and_lemon = fruits[::2]

print(orange_and_mango)
print(orange_mango_lemon)
print(orange_and_lemon)

all_fruits = fruits[-4:]
orange_and_mango = fruits[-3:-1]
orange_mango_lemon = fruits[-3:]
reverse_fruits = fruits[::-1]

print(orange_and_mango)
print(orange_mango_lemon)
print(orange_and_lemon)

