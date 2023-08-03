print('1')
first_declaration = list()
print('2')
five_items = ['jhin', 'kindred', 'morgana', 'samira', 'kogmaw', 'tf']
print('3')
print(len(five_items))
print('4')
print(five_items[0])
print(five_items[2:3])
print(five_items[-1])


print('5')
mixed_data_type = ['martin', 29, 172, 'married', 'Bordeaux']

print('6')
it_companies = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']

print('7')
print(it_companies)

print('8')
print(len(it_companies))

print('9')
print(it_companies[0])
print(it_companies[3])
print(it_companies[-1])

print('10')
it_companies[0] = 'Budibase'
print(it_companies)

print('11')
it_companies.append('Samsung')
print(it_companies)

print('12')
it_companies.insert(4, 'MSI')
print(it_companies)

print('13')
it_companies[2] = it_companies[2].toupper()
print(it_companies)

print('14')
it_companies.join('#; ')
print(it_companies)

print('15')
samsung = 'Samsung' in it_companies
print(samsung)
print('Samsung' in it_companies)

print('16')
it_companies.sort()
print(it_companies)

print('17')
it_companies.reverse()
print(it_companies)

print('18')
print(it_companies[0:3])

print('19')
print(it_companies[-1:1])

print('20')
print(it_companies[4])

print('21')
del it_companies[0]
print(it_companies)

print('22')
del it_companies[4]
print(it_companies)

print('23')
del it_companies[-1]
print(it_companies)

print('24')
del it_companies

print('25')
front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node','Express', 'MongoDB']
front_end.extend(back_end)
print(front_end)

print('27')
full_stack = front_end.copy()
print(full_stack)
full_stack.insert(6, 'Python', 'Redux')
print(full_stack)