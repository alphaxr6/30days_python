# Old school style

first_name = "Thomas"
last_name = "Mar"
language = "Python"
formated_string = 'I am %s %s. I learn %s' %(first_name, last_name, language)
print(formated_string)

radius = 10
pi = 3.14
area = pi * radius ** 2
formated_string = 'The area of circle with a radius %d is %.2f.' %(radius, area)

python_libraries = ['Django', 'Flask', 'NumPy', 'Matplotlib', 'Pandas']
formated_string = 'The following are python libraries:%s' %(python_libraries)

#New school style
 
new_formated_string = 'I am {} {}. I learn {}'.format(first_name, last_name, language)
print(new_formated_string)

a = 4
b = 3

print('{} + {} = {}'.format(a, b, a + b))
print('{} - {} = {}'.format(a, b, a - b))
print('{} * {} = {}'.format(a, b, a * b))
print('{} / {} = {:.2f}'.format (a, b, a / b))
print('{} % {} = {}'.format(a, b, a % b))
print('{} // {} = {}'.format(a, b, a // b))
print('{} ** {} = {}'.format(a, b, a ** b))

formated_string = 'The area of the circle with a radius {} is {:.2f}.'.format(radius, area)

#String interpolation

print(f'{a} + {b} = {a + b}')
print(f'{a} - {b} = {a - b}')
print(f'{a} * {b} = {a * b}')
print(f'{a} / {b} = {a / b:.2f}')
print(f'{a} % {b} = {a % b}')
print(f'{a} // {b} = {a // b}')
print(f'{a} ** {b} = {a ** b}')

