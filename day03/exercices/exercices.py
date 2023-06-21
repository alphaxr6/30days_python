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
perimeter = side_a + side_b + side_c
print('The perimeter is: ', perimeter)

lenght_rectangle = input('Enter Lenght: ')
width_rectable = input('Enter width: ')
print('The area of the rectable is: ', lenght_rectangle * width_rectable, 'and the perimeter is: ', 2 * (lenght_rectangle + width_rectable))
