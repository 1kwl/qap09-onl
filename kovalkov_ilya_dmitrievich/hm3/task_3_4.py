#    4. Напишите программу которая удаляет пробел в начале, в конце строки

str = ' PEP 8 – Style Guide for Python Code '

first_space = str.find(' ')
last_space = str.rfind(' ')

print(str[first_space+1:last_space])
