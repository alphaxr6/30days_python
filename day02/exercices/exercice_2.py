from math import pi

print('Day 2: 30 Days of python programming')

first_name = 'Thomas'
last_name = 'Dupont'
full_name = 'Thomas Dupont'
country = 'Scotland'
city = 'Aberdeen'
age = 29
year = 2023
is_married = False
is_true = True
is_light_on = False

second_name, last_second_name, second_age, second_is_married = 'Jean', 'martin', 19, True

print(first_name, 'is type', type(first_name))
print(last_name, 'is type', type(last_name))
print(full_name, 'is type', type(full_name))
print(country)
print(city)
print(age, 'is type', type(age))
print(year)
print(is_married, 'is type', type(is_married))
print(is_true)
print(is_light_on)
print('')
print(second_name)
print(last_second_name)
print(second_age)
print(second_is_married)
print('')
print(len(first_name))
print(len(first_name), 'and', len(last_name))
print('')

num_one = 5
num_two = 4
summ = [num_one, num_two]

total = sum(summ)
print(total)

diff = num_two - num_one
print(diff)

product = num_one * num_two
print(product)

division = num_one / num_two
print(division)

remainder = num_two % num_one
print(remainder)

exp = num_one ** num_two
print(exp)

floor_division = num_one // num_two
print(floor_division)

print('')
radius_circle = 30
area_of_circle = pi*(radius_circle**2)
print(area_of_circle)

circum_of_circle = 2*pi*radius_circle
print(circum_of_circle)

r = int(input('What is the radius value ? '))

C = 2*pi*r
A = pi*(r**2)

print(C)
print(A)

print('self service id')

personnal_name = str(input('whats your personnale name ? '))
personnal_last_name = str(input('whats your personnal last name ? '))
country = str(input('where do you live ? '))
age = int(input('what is your age ? '))



print(personnal_name, personnal_last_name, country, age)