challenge = 'Thirty days of python'
print(challenge.capitalize())

print(challenge.count('y'))
print(challenge.count('y', 7, 14))
print(challenge.count('th'))

print(challenge.endswith('on'))
print(challenge.endswith('tion'))

challenge = 'thirty\tdays\tof\tpython'
print(challenge.expandtabs())
print(challenge.expandtabs(10))

print(challenge.find('y'))
print(challenge.find('th'))

print(challenge.rfind('y'))
print(challenge.rfind('th'))

sub_string = 'da'
print(challenge.index(sub_string))
#print(challenge.index(sub_string, 9))

print(challenge.rindex(sub_string))
#print(challenge.rindex(sub_string, 9))

challenger = 'thirtydayspython'
print(challenge.isalnum())
challenge = '30dayspython'
print(challenge.isalnum())
challenge = 'thirty days of python'
print(challenge.isalnum())

print(challenge.isalpha())
challenge = 'thirtydayspython'
print(challenge.isalpha())
challenge = '123'
print(challenge.isalpha())

challenge = 'thirty days of python'
print(challenge.isdecimal())
challenge = '123'
print(challenge.isdecimal())
challenge = '\u00B2'
print(challenge.isdecimal())
challenge = '12 3'
print(challenge.isdecimal())

challenge = 'thirty'
print(challenge.isdigit())
challenge = '30'
print(challenge.isdigit())
challenge = '\u00B2'
print(challenge.isdigit())

challenge = '30DaysofPython'
print(challenge.isidentifier())
challenge = 'thirty_days_of_python'
print(challenge.isidentifier())

challenge = 'thirty days of python'
print(challenge.islower())
challenge = 'Thirty days of python'
print(challenge.islower())

challenge = 'thirty days of python'
print(challenge.isupper())
challenge = 'THIRTY DAYS OF PYTHON'
print(challenge.isupper())

web_tech = ['HTML', 'CSS', 'JavaScript', 'React']
result = ' '.join(web_tech)
print(result)

web_tech = ['HTML', 'CSS', 'JavaScript', 'React']
result = '# '.join(web_tech)
print(result)

challenge = 'thirty days of pythoonnn'
print(challenge.strip('noth'))

challenge = 'thirty days of python'
print(challenge.replace('python', 'coding'))

challenge = 'thirty days of python'
print(challenge.split())
challenge = 'thirty, days, of, python'
print(challenge.split(', '))

challenge = 'thirty days of python'
print(challenge.title())

challenge = 'thirty days of python'
print(challenge.swapcase())
challenge = 'Thirty Days Of Python'
print(challenge.swapcase())

challenge = 'thirty days of python'
print(challenge.startswitch('thirty'))
challnege = '30 days of ptyhon'
print(challenge.startswith('thirty'))