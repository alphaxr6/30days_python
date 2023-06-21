age = int(29)
height = float(1.72)
complex = complex(1j + 3)

base_triangle = input('Enter base: ')
height_triangle = input('Enter height: ')
area_triangle = 0.5 * int(height_triangle) * int(base_triangle)

print('The are of the triangle is :', area_triangle)

side_a = input('Enter side a: ')
side_b = input('Enter side b: ')
side_c = input('Enter side c: ')
perimeter = int(side_a) + int(side_b) + int(side_c)
print('The perimeter is: ', perimeter)

lenght_rectangle = input('Enter Lenght: ')
width_rectable = input('Enter width: ')
print('The area of the rectable is: ', int(lenght_rectangle) * int(width_rectable), 'and the perimeter is: ', 2 * (int(lenght_rectangle) + int(width_rectable)))


radius = input('Enter radius: ')
print('Area is :', 3.14 * float(radius) * float(radius), 'and the circumference: ', 2 * 3.14 * float(radius))

print(len('python'))
print(len('dragon'))

print(len('python') is not len('dragon'))

print('on' in 'python' and 'dragon')

print('jargon' in 'I hope this course is not full of jargon')

print('on' is not 'python' and 'dragon')

python = len(str('python'))
python_float = float(python)
python_string = str(python_float)

hours = input('Enter hours: ')
rate = input('Enter rate: ')
print('Your weekly earning is: ', hours * rate)
